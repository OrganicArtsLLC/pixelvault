#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# promote-games-to-public.sh
#
# Batch-promotes all eligible games (archetype + ai-archaeology) from
# VISIBILITY: private  →  VISIBILITY: public
# Then regenerates manifest.json/CATALOGUE.md via catalogue-generator.py.
#
# Usage:
#   bash scripts/promote-games-to-public.sh              # interactive
#   bash scripts/promote-games-to-public.sh --force      # skip confirmation
#   bash scripts/promote-games-to-public.sh --dry-run    # show what would change
#
# Scope: only prototypes/ and ai-archaeology/ (ai-evolution is always gated)
# Does NOT change STATUS: sketch — that is preserved as-is.
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# ── Args ──
DRY_RUN=0
FORCE=0
for arg in "$@"; do
  [[ "$arg" == "--dry-run" ]] && DRY_RUN=1
  [[ "$arg" == "--force" ]]   && FORCE=1
done

# ── Colors ──
GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'
RED='\033[0;31m'; BOLD='\033[1m'; NC='\033[0m'

echo ""
echo -e "${CYAN}${BOLD}Pixel Vault — Batch Visibility Promotion${NC}"
echo -e "${CYAN}  private → public for archetype + ai-archaeology games${NC}"
[[ $DRY_RUN -eq 1 ]] && echo -e "${YELLOW}  DRY RUN — no files will be modified${NC}"
echo ""

cd "$REPO_ROOT"

# ── Find all eligible game files ──
# (avoid mapfile — macOS ships bash 3.2 which doesn't support it)
GAME_FILES=()
while IFS= read -r line; do
  GAME_FILES+=("$line")
done < <(find prototypes ai-archaeology -name "*.html" | sort)
TOTAL="${#GAME_FILES[@]}"

# ── Count private vs already public ──
PRIVATE_COUNT=0
PUBLIC_COUNT=0
CHANGED_FILES=()

for f in "${GAME_FILES[@]}"; do
  if grep -q "VISIBILITY: private" "$f" 2>/dev/null; then
    PRIVATE_COUNT=$((PRIVATE_COUNT + 1))
    CHANGED_FILES+=("$f")
  elif grep -q "VISIBILITY: public" "$f" 2>/dev/null; then
    PUBLIC_COUNT=$((PUBLIC_COUNT + 1))
  fi
done

echo "  Total eligible game files : ${TOTAL}"
echo "  Currently private         : ${PRIVATE_COUNT}"
echo "  Currently public          : ${PUBLIC_COUNT}"
echo ""

if [[ ${#CHANGED_FILES[@]} -eq 0 ]]; then
  echo -e "${GREEN}✅ All games are already public — nothing to change.${NC}"
  exit 0
fi

if [[ $DRY_RUN -eq 1 ]]; then
  echo -e "${YELLOW}Would promote ${PRIVATE_COUNT} games to public:${NC}"
  for f in "${CHANGED_FILES[@]}"; do
    echo "  ${f}"
  done
  echo ""
  echo -e "${YELLOW}Would then run: python3 tools/catalogue-generator.py${NC}"
  echo -e "${GREEN}✅ Dry run complete — no changes made.${NC}"
  exit 0
fi

if [[ $FORCE -eq 0 ]]; then
  echo -e "${YELLOW}About to change VISIBILITY: private → public in ${PRIVATE_COUNT} files.${NC}"
  read -rp "Proceed? (yes/no): " confirm
  [[ "$confirm" != "yes" ]] && { echo -e "${RED}Cancelled.${NC}"; exit 1; }
fi

# ── Apply changes ──
echo -e "${CYAN}▶ Updating visibility in game files...${NC}"
UPDATED=0

for f in "${CHANGED_FILES[@]}"; do
  # Use sed to replace VISIBILITY: private with VISIBILITY: public in METADATA block
  # The METADATA block is always in the first ~25 lines as an HTML comment
  # Use Python for cross-platform safety (macOS BSD sed -i requires explicit backup arg)
  python3 -c "
import sys
path = sys.argv[1]
with open(path) as f:
    content = f.read()
updated = content.replace('VISIBILITY: private', 'VISIBILITY: public', 1)
with open(path, 'w') as f:
    f.write(updated)
" "$f"
  UPDATED=$((UPDATED + 1))
  [[ $((UPDATED % 50)) -eq 0 ]] && echo "  ...${UPDATED}/${PRIVATE_COUNT} updated"
done

echo -e "  ${GREEN}✓ ${UPDATED} game files updated${NC}"

# ── Regenerate catalogue + manifest ──
echo ""
echo -e "${CYAN}▶ Regenerating manifest.json and CATALOGUE.md...${NC}"
python3 tools/catalogue-generator.py

# ── Verify results ──
NEW_PUBLIC=$(grep -rl "VISIBILITY: public" prototypes ai-archaeology 2>/dev/null | wc -l | tr -d ' ')
NEW_PRIVATE=$(grep -rl "VISIBILITY: private" prototypes ai-archaeology 2>/dev/null | wc -l | tr -d ' ')
echo ""
echo -e "${GREEN}${BOLD}✅ Visibility promotion complete${NC}"
echo ""
echo "  Public games  : ${NEW_PUBLIC}"
echo "  Private games : ${NEW_PRIVATE}"
echo ""
echo "  Next step — git commit and deploy:"
echo ""
echo -e "  ${CYAN}git add prototypes/ ai-archaeology/ manifest.json CATALOGUE.md CATALOGUE-PUBLIC.md${NC}"
echo -e "  ${CYAN}git commit -m 'chore: approve ${UPDATED} games for production visibility'${NC}"
echo -e "  ${CYAN}bash scripts/deploy-play.sh --include-assets${NC}"
echo ""
