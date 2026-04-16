#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────
# Pixel Vault — Game Test Runner
# Usage: bash tools/test-games.sh [--verbose] [--file path/to/game.html]
#
# Agent-friendly test suite: no server required, exit code 0 = pass.
#
# Tests each game file for:
#   [FAIL] Missing DOCTYPE
#   [FAIL] No <canvas> element
#   [FAIL] No <script> block
#   [FAIL] No requestAnimationFrame (game loop)
#   [FAIL] External CDN/script dependency (zero-dep contract)
#   [FAIL] Oversized > 50KB (prototypes/ai-* tracks only)
#   [FAIL] Missing METADATA block (first line must be <!--)
#   [FAIL] eval() or new Function() usage (code injection)
#   [FAIL] External fetch()/XHR to remote URLs (data leak / zero-dep)
#   [WARN] Uses setInterval for animation (bad practice)
#   [WARN] Missing required METADATA fields
#   [WARN] No 800px canvas width reference
#   [WARN] No input handling detected
#   [WARN] JS keyword 'var' used (prefer let/const)
#   [WARN] document.write() usage (XSS-prone)
#   [WARN] innerHTML assigned from variable (potential XSS)
#   [WARN] localStorage/sessionStorage usage
# ─────────────────────────────────────────────────────────────────
set -uo pipefail

DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DIR"

# ── Args ──
VERBOSE=0
SINGLE_FILE=""
for arg in "$@"; do
  case "$arg" in
    --verbose|-v) VERBOSE=1 ;;
    --file=*)     SINGLE_FILE="${arg#--file=}" ;;
    --file)       shift; SINGLE_FILE="${1:-}" ;;
  esac
done

# ── Colors ──
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
DIM='\033[2m'
NC='\033[0m'

# ── Counters ──
TOTAL=0
PASS=0
FAIL=0
WARN_TOTAL=0
declare -a FAILED_FILES=()

echo ""
echo -e "${CYAN}${BOLD}╔══════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}${BOLD}║      PIXEL VAULT — GAME TEST RUNNER          ║${NC}"
echo -e "${CYAN}${BOLD}╚══════════════════════════════════════════════╝${NC}"
echo ""

# ─────────────────────────────────────────────────────────────────
# TEST FUNCTION
# Returns: sets GAME_FAILED=0|1, GAME_WARNS+=issues, GAME_ERRORS+=issues
# ─────────────────────────────────────────────────────────────────
test_game() {
  local file="$1"
  local track="$2"  # prototype|archaeology|evolution|refined|sparks
  GAME_FAILED=0
  GAME_WARNS=()
  GAME_ERRORS=()

  # ── File size (macOS stat; fallback to xargs-trimmed wc) ──
  local size
  size=$(stat -f%z "$file" 2>/dev/null || wc -c < "$file" | xargs | awk '{print $1}')

  # ── [FAIL] DOCTYPE ──
  if ! grep -q '<!DOCTYPE html' "$file"; then
    GAME_ERRORS+=("NO DOCTYPE (<!DOCTYPE html missing)")
    GAME_FAILED=1
  fi

  # ── [FAIL] Canvas element ──
  if ! grep -qi '<canvas' "$file"; then
    GAME_ERRORS+=("NO CANVAS ELEMENT (<canvas> not found)")
    GAME_FAILED=1
  fi

  # ── [FAIL] Script block ──
  if ! grep -qi '<script' "$file"; then
    GAME_ERRORS+=("NO SCRIPT BLOCK (<script> not found)")
    GAME_FAILED=1
  fi

  # ── [FAIL] requestAnimationFrame ──
  if ! grep -q 'requestAnimationFrame' "$file"; then
    GAME_ERRORS+=("NO requestAnimationFrame (game loop missing)")
    GAME_FAILED=1
  fi

  # ── [FAIL/WARN] External script dependencies (CDN / remote scripts) ──
  if grep -qiE '<script[^>]+src="https?://' "$file"; then
    if [[ "$track" == "sparks" ]]; then
      # sparks-explorer is exempt from series rules but should still be flagged
      GAME_WARNS+=("EXTERNAL SCRIPT DEPENDENCY (sparks-explorer exception — violates zero-dep contract)")
    else
      GAME_ERRORS+=("EXTERNAL SCRIPT DEPENDENCY (src=https://...)")
      GAME_FAILED=1
    fi
  fi

  # ── [FAIL] Size > 50KB for prototype/archaeology/evolution ──
  if [[ "$track" == "prototype" || "$track" == "archaeology" || "$track" == "evolution" ]]; then
    if [[ $size -gt 51200 ]]; then
      local kb=$(( size / 1024 ))
      GAME_ERRORS+=("OVERSIZED: ${kb}KB exceeds 50KB limit")
      GAME_FAILED=1
    fi
  fi

  # ── METADATA block (first line = <!--) ──
  local first_line
  first_line=$(head -1 "$file")
  if [[ "$first_line" != "<!--"* ]]; then
    if [[ "$track" == "prototype" || "$track" == "archaeology" || "$track" == "evolution" ]]; then
      # Prototypes MUST have metadata
      GAME_ERRORS+=("MISSING METADATA BLOCK (first line must be <!--)")
      GAME_FAILED=1
    else
      # Refined/sparks: metadata strongly recommended
      GAME_WARNS+=("MISSING METADATA BLOCK (first line should be <!--)")
    fi
  else
    # ── [WARN] Required metadata fields (case-insensitive, old and new format) ──
    # Check key fields: mechanic, series/prototype, controls, status
    for field in mechanic controls status; do
      if ! head -30 "$file" | grep -qi "${field}:"; then
        GAME_WARNS+=("METADATA missing field: ${field}")
      fi
    done
    # Series check: either SERIES: or PROTOTYPE: should be present
    if ! head -30 "$file" | grep -qiE "^(series|prototype):"; then
      GAME_WARNS+=("METADATA missing field: series/prototype")
    fi
  fi

  # ── [WARN] setInterval for animation ──
  if grep -q 'setInterval' "$file"; then
    GAME_WARNS+=("USES setInterval (prefer requestAnimationFrame)")
  fi

  # ── [WARN] 800px canvas width — check any explicit canvas dimension assignment (prototype/archaeology only) ──
  if [[ "$track" == "prototype" || "$track" == "archaeology" ]]; then
    if ! grep -qE 'canvas\.width\s*=|W\s*=\s*[0-9]' "$file"; then
      GAME_WARNS+=("CANVAS WIDTH NOT EXPLICITLY SET (expected canvas.width = N or W = N)")
    fi
  fi

  # ── [WARN] Input handling ──
  if ! grep -qiE 'addEventListener|onkeydown|onkeyup|onmousemove|onmousedown|onclick' "$file"; then
    GAME_WARNS+=("NO INPUT HANDLING DETECTED")
  fi

  # ── [WARN] var usage (style) — avoid || echo 0 bug (grep exits 1 for no-matches) ──
  local var_count=0
  var_count=$(grep -cE '(^|[^a-z])var [a-zA-Z]' "$file" 2>/dev/null) || var_count=0
  if [[ $var_count -gt 5 ]]; then
    GAME_WARNS+=("USES 'var' in JS (${var_count} occurrences — prefer let/const)")
  fi

  # ─────────────────────────────────────────────────────
  # SECURITY CHECKS
  # ─────────────────────────────────────────────────────

  # ── [FAIL] eval() — arbitrary code execution risk ──
  if grep -qE '(^|[^a-zA-Z.])eval\(' "$file"; then
    GAME_ERRORS+=("[SECURITY] eval() usage — code injection risk")
    GAME_FAILED=1
  fi

  # ── [FAIL] new Function() — equivalent to eval ──
  if grep -q 'new Function(' "$file"; then
    GAME_ERRORS+=("[SECURITY] new Function() — equivalent to eval()")
    GAME_FAILED=1
  fi

  # ── [FAIL] External fetch() to remote URLs ──
  if grep -qiE "fetch\([[:space:]]*['\"]https?://" "$file"; then
    GAME_ERRORS+=("[SECURITY] fetch() to external URL — violates zero-dep contract, potential data leak")
    GAME_FAILED=1
  fi

  # ── [FAIL] External XMLHttpRequest to remote URLs ──
  if grep -qiE "\.open\(['\"][A-Z]+['\"],\s*['\"]https?://" "$file"; then
    GAME_ERRORS+=("[SECURITY] XMLHttpRequest to external URL — violates zero-dep contract")
    GAME_FAILED=1
  fi

  # ── [WARN] document.write() — deprecated, XSS-prone ──
  if grep -q 'document.write(' "$file"; then
    GAME_WARNS+=("[SECURITY] document.write() is deprecated and XSS-prone")
  fi

  # ── [WARN] innerHTML with non-literal (potential XSS) ──
  # Flag innerHTML assigned to a variable or expression (not a plain string literal)
  if grep -qE 'innerHTML\s*\+?=' "$file" && grep -qE 'innerHTML\s*\+?=\s*[a-zA-Z_$`]' "$file"; then
    GAME_WARNS+=("[SECURITY] innerHTML assigned from variable/expression — verify no user data reaches this")
  fi

  # ── [WARN] localStorage/sessionStorage usage ──
  if grep -qE 'localStorage|sessionStorage' "$file"; then
    GAME_WARNS+=("[SECURITY] localStorage/sessionStorage used — ensure no sensitive data stored")
  fi
}

# ─────────────────────────────────────────────────────────────────
# COLLECT FILES
# ─────────────────────────────────────────────────────────────────
declare -a ALL_FILES=()
declare -a ALL_TRACKS=()

if [[ -n "$SINGLE_FILE" ]]; then
  if [[ -f "$SINGLE_FILE" ]]; then
    ALL_FILES+=("$SINGLE_FILE")
    ALL_TRACKS+=("prototype")
  else
    echo -e "${RED}File not found: $SINGLE_FILE${NC}"
    exit 1
  fi
else
  # Collect all game HTML files
  for f in prototypes/*/*.html; do
    [[ -f "$f" ]] && ALL_FILES+=("$f") && ALL_TRACKS+=("prototype")
  done
  for f in ai-archaeology/*/*.html; do
    [[ -f "$f" ]] && ALL_FILES+=("$f") && ALL_TRACKS+=("archaeology")
  done
  for f in ai-evolution/*/*.html; do
    [[ -f "$f" ]] && ALL_FILES+=("$f") && ALL_TRACKS+=("evolution")
  done
  for f in refined/*/*.html; do
    [[ -f "$f" ]] && ALL_FILES+=("$f") && ALL_TRACKS+=("refined")
  done
  for f in sparks-explorer/*.html; do
    [[ -f "$f" ]] && ALL_FILES+=("$f") && ALL_TRACKS+=("sparks")
  done
fi

# ─────────────────────────────────────────────────────────────────
# RUN TESTS
# ─────────────────────────────────────────────────────────────────
echo -e "${BOLD}Testing ${#ALL_FILES[@]} game files...${NC}"
echo ""

for i in "${!ALL_FILES[@]}"; do
  file="${ALL_FILES[$i]}"
  track="${ALL_TRACKS[$i]}"
  ((TOTAL++))

  test_game "$file" "$track"

  GAME_WARNS_COUNT=${#GAME_WARNS[@]}
  WARN_TOTAL=$(( WARN_TOTAL + GAME_WARNS_COUNT ))

  if [[ $GAME_FAILED -eq 0 && $GAME_WARNS_COUNT -eq 0 ]]; then
    ((PASS++))
    if [[ $VERBOSE -eq 1 ]]; then
      echo -e "${GREEN}  ✓ PASS${NC}  $file"
    fi
  elif [[ $GAME_FAILED -eq 1 ]]; then
    ((FAIL++))
    FAILED_FILES+=("$file")
    echo -e "${RED}  ✗ FAIL${NC}  $file"
    for err in "${GAME_ERRORS[@]}"; do
      echo -e "         ${RED}[FAIL]${NC} $err"
    done
    for warn in "${GAME_WARNS[@]}"; do
      echo -e "         ${YELLOW}[WARN]${NC} $warn"
    done
  else
    # Warnings only
    ((PASS++))
    echo -e "${YELLOW}  ⚠ WARN${NC}  $file"
    for warn in "${GAME_WARNS[@]}"; do
      echo -e "         ${YELLOW}[WARN]${NC} $warn"
    done
  fi
done

# ─────────────────────────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BOLD}RESULTS${NC}"
echo -e "${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "  Total tested:  ${BOLD}$TOTAL${NC}"
echo -e "  ${GREEN}Passed:${NC}        ${BOLD}$PASS${NC}"
echo -e "  ${RED}Failed:${NC}        ${BOLD}$FAIL${NC}"
echo -e "  ${YELLOW}Warnings:${NC}      ${BOLD}$WARN_TOTAL${NC}"

if [[ $FAIL -gt 0 ]]; then
  echo ""
  echo -e "${RED}${BOLD}FAILED FILES:${NC}"
  for f in "${FAILED_FILES[@]}"; do
    echo -e "  ${RED}✗${NC} $f"
  done
fi

echo ""
if [[ $FAIL -eq 0 ]]; then
  echo -e "${GREEN}${BOLD}✓ ALL TESTS PASSED${NC}"
  exit 0
else
  echo -e "${RED}${BOLD}✗ $FAIL TEST(S) FAILED — fix before shipping${NC}"
  exit 1
fi
