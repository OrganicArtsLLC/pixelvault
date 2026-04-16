#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────
# Pixel Vault — Debug Dev Server
# Usage: ./tools/dev-server.sh [port]
#
# Agent-friendly local development server with:
#   - Pre-flight validation (manifest, catalogue, file sizes, metadata)
#   - Quick health report for all prototypes
#   - HTTP server with auto-open in browser
#   - CORS headers for iframe embedding
#
# Run from project root: bash tools/dev-server.sh
# ─────────────────────────────────────────────────────────────────
set -euo pipefail

PORT="${1:-8080}"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DIR"

# ── Colors ──
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

echo ""
echo -e "${CYAN}${BOLD}╔══════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}${BOLD}║      PIXEL VAULT — DEBUG DEV SERVER          ║${NC}"
echo -e "${CYAN}${BOLD}╚══════════════════════════════════════════════╝${NC}"
echo ""

# ── 1. Pre-flight checks ──
ERRORS=0
WARNINGS=0

echo -e "${BOLD}[1/5] Checking required files...${NC}"

for f in index.html manifest.json CATALOGUE.md; do
  if [[ -f "$f" ]]; then
    echo -e "  ${GREEN}✓${NC} $f"
  else
    echo -e "  ${RED}✗${NC} $f — MISSING"
    ((ERRORS++))
  fi
done

# ── 2. Validate manifest.json ──
echo ""
echo -e "${BOLD}[2/5] Validating manifest.json...${NC}"

if [[ -f manifest.json ]]; then
  PROTO_COUNT=$(python3 -c "import json; print(len(json.load(open('manifest.json'))['prototypes']))" 2>/dev/null || echo "INVALID")
  if [[ "$PROTO_COUNT" == "INVALID" ]]; then
    echo -e "  ${RED}✗${NC} manifest.json is not valid JSON"
    ((ERRORS++))
  else
    echo -e "  ${GREEN}✓${NC} manifest.json — $PROTO_COUNT prototypes indexed"
  fi
fi

# ── 3. Scan all HTML game files ──
echo ""
echo -e "${BOLD}[3/5] Scanning game files...${NC}"

TOTAL_GAMES=0
OVERSIZED=0
MISSING_META=0
TRACK_ARCHETYPE=0
TRACK_ARCHAEOLOGY=0
TRACK_EVOLUTION=0
TRACK_REFINED=0
TRACK_SPARKS=0

declare -a GAME_FILES=()

# Collect all HTML files from game directories
for html_file in \
  prototypes/*/*.html \
  ai-archaeology/*/*.html \
  ai-evolution/*/*.html \
  refined/*/*.html \
  sparks-explorer/*.html; do
  [[ -f "$html_file" ]] || continue
  GAME_FILES+=("$html_file")
done

for html_file in "${GAME_FILES[@]}"; do
  ((TOTAL_GAMES++))

  # Track classification
  case "$html_file" in
    prototypes/*)      ((TRACK_ARCHETYPE++)) ;;
    ai-archaeology/*)  ((TRACK_ARCHAEOLOGY++)) ;;
    ai-evolution/*)    ((TRACK_EVOLUTION++)) ;;
    refined/*)         ((TRACK_REFINED++)) ;;
    sparks-explorer/*) ((TRACK_SPARKS++)) ;;
  esac

  # Size check (50KB = 51200 bytes, but refined/sparks are exempt)
  FILE_SIZE=$(wc -c < "$html_file" | tr -d ' ')
  if [[ "$html_file" != refined/* && "$html_file" != sparks-explorer/* && "$FILE_SIZE" -gt 51200 ]]; then
    SIZE_KB=$((FILE_SIZE / 1024))
    echo -e "  ${RED}✗${NC} OVERSIZED (${SIZE_KB}KB): $html_file"
    ((OVERSIZED++))
  fi

  # Metadata check (first line should start with <!--)
  FIRST_LINE=$(head -1 "$html_file")
  if [[ "$FIRST_LINE" != "<!--"* ]]; then
    echo -e "  ${YELLOW}⚠${NC} No METADATA block: $html_file"
    ((MISSING_META++))
  fi
done

echo -e "  ${GREEN}✓${NC} ${TOTAL_GAMES} game files found"
echo -e "     Archetypes: ${TRACK_ARCHETYPE} | AI-Arch: ${TRACK_ARCHAEOLOGY} | AI-Evo: ${TRACK_EVOLUTION} | Refined: ${TRACK_REFINED} | Sparks: ${TRACK_SPARKS}"

if [[ $OVERSIZED -gt 0 ]]; then
  echo -e "  ${RED}✗${NC} $OVERSIZED files exceed 50KB limit"
  ((WARNINGS+=OVERSIZED))
fi
if [[ $MISSING_META -gt 0 ]]; then
  echo -e "  ${YELLOW}⚠${NC} $MISSING_META files missing METADATA blocks"
  ((WARNINGS+=MISSING_META))
fi

# ── 4. Cross-reference manifest vs actual files ──
echo ""
echo -e "${BOLD}[4/5] Cross-referencing manifest ↔ files...${NC}"

if [[ -f manifest.json ]]; then
  # Files in manifest but missing on disk
  MANIFEST_FILES=$(python3 -c "
import json
with open('manifest.json') as f:
    m = json.load(f)
for p in m['prototypes']:
    print(p['file'])
" 2>/dev/null || true)

  MISSING_ON_DISK=0
  while IFS= read -r mf; do
    if [[ -n "$mf" && ! -f "$mf" ]]; then
      echo -e "  ${RED}✗${NC} In manifest but missing on disk: $mf"
      ((MISSING_ON_DISK++))
    fi
  done <<< "$MANIFEST_FILES"

  if [[ $MISSING_ON_DISK -eq 0 ]]; then
    echo -e "  ${GREEN}✓${NC} All manifest entries have matching files"
  else
    ((ERRORS+=MISSING_ON_DISK))
  fi

  # Files on disk but not in manifest (prototypes/ and ai-archaeology/ only)
  NOT_IN_MANIFEST=0
  for html_file in prototypes/*/*.html ai-archaeology/*/*.html ai-evolution/*/*.html; do
    [[ -f "$html_file" ]] || continue
    if ! echo "$MANIFEST_FILES" | grep -qF "$html_file"; then
      echo -e "  ${YELLOW}⚠${NC} On disk but not in manifest: $html_file"
      echo -e "       Run: ${CYAN}python3 tools/catalogue-generator.py${NC}"
      ((NOT_IN_MANIFEST++))
    fi
  done

  if [[ $NOT_IN_MANIFEST -eq 0 ]]; then
    echo -e "  ${GREEN}✓${NC} All game files are in manifest"
  else
    ((WARNINGS+=NOT_IN_MANIFEST))
  fi
fi

# ── 5. Summary ──
echo ""
echo -e "${BOLD}[5/5] Health summary${NC}"
echo -e "  Total games: ${BOLD}$TOTAL_GAMES${NC}"
echo -e "  Manifest entries: ${BOLD}${PROTO_COUNT:-?}${NC}"

if [[ $ERRORS -gt 0 ]]; then
  echo -e "  ${RED}${BOLD}ERRORS: $ERRORS (must fix before publishing)${NC}"
fi
if [[ $WARNINGS -gt 0 ]]; then
  echo -e "  ${YELLOW}${BOLD}WARNINGS: $WARNINGS (review recommended)${NC}"
fi
if [[ $ERRORS -eq 0 && $WARNINGS -eq 0 ]]; then
  echo -e "  ${GREEN}${BOLD}ALL CLEAR — no issues found${NC}"
fi

# ── Launch server ──
echo ""
echo -e "${CYAN}${BOLD}Starting HTTP server...${NC}"
echo -e "  Gallery:  ${BOLD}http://localhost:${PORT}${NC}"
echo -e "  Games:    ${BOLD}http://localhost:${PORT}/prototypes/${NC}"
echo -e ""
echo -e "  ${CYAN}Tip:${NC} Click any game in the gallery sidebar to play in iframe"
echo -e "  ${CYAN}Tip:${NC} Use ⬈ New Tab button for fullscreen testing"
echo -e "  ${CYAN}Tip:${NC} Press Ctrl+C to stop"
echo ""

# Use Python's http.server with CORS support for iframe embedding
python3 -c "
import http.server
import socketserver

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        # Color-code by response type
        msg = format % args
        if ' 200 ' in msg:
            print(f'\033[0;32m  ▸ {msg}\033[0m')
        elif ' 304 ' in msg:
            print(f'\033[0;36m  ▸ {msg}\033[0m')
        elif ' 404 ' in msg:
            print(f'\033[0;31m  ✗ {msg}\033[0m')
        else:
            print(f'  ▸ {msg}')

with socketserver.TCPServer(('', ${PORT}), CORSHandler) as httpd:
    httpd.serve_forever()
"
