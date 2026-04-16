#!/usr/bin/env bash
# ============================================================
# Pixel Vault — Game Publisher
# ============================================================
# Force-track a game file into the public repo despite the
# default-private .gitignore rules for game directories.
#
# Usage:
#   tools/publish-game.sh prototypes/maz/maz-001-pacman.html
#   tools/publish-game.sh ai-archaeology/fix/fix-001-galaxian.html
#
# All game directories (prototypes/, ai-archaeology/, ai-evolution/)
# are gitignored by default. Use this script to publish specific games.
# After running, review the staged change and commit.
#
# ⚠️  WARNING: Once published, a file is visible in the public repo.
#     Review the game for IP issues before publishing.
#     See docs/IP-WATCHLIST.md for known protected IP.
# ============================================================

set -euo pipefail

if [[ $# -eq 0 ]]; then
    echo "Usage: tools/publish-game.sh <game-file-path>"
    echo "Examples:"
    echo "  tools/publish-game.sh prototypes/maz/maz-001-pacman.html"
    echo "  tools/publish-game.sh ai-archaeology/fix/fix-001-galaxian.html"
    exit 1
fi

GAME_FILE="$1"

if [[ ! -f "$GAME_FILE" ]]; then
    echo "Error: File not found: $GAME_FILE"
    exit 1
fi

# Verify it's a game file (HTML in a game directory)
if [[ "$GAME_FILE" != prototypes/* ]] && [[ "$GAME_FILE" != ai-archaeology/* ]] && [[ "$GAME_FILE" != ai-evolution/* ]]; then
    echo "Error: Not a game file path. Expected prototypes/, ai-archaeology/, or ai-evolution/."
    exit 1
fi

echo "=================================="
echo "⚠️  PUBLISHING GAME TO PUBLIC REPO"
echo "=================================="
echo ""
echo "  File: $GAME_FILE"
echo ""
echo "  This file will be visible in the PUBLIC repository."
echo "  Please verify:"
echo "  [ ] No copyrighted characters, logos, or music references"
echo "  [ ] No IP-WATCHLIST.md protected material"
echo "  [ ] METADATA block is accurate"
echo "  [ ] Game plays correctly"
echo ""
read -rp "Confirm publish? (yes/N): " CONFIRM

if [[ "$CONFIRM" != "yes" ]]; then
    echo "Aborted."
    exit 0
fi

# Force-add despite .gitignore
git add -f "$GAME_FILE"

echo ""
echo "✓ Staged for commit: $GAME_FILE"
echo ""
echo "Next steps:"
echo "  git status                    # review staged change"
echo "  git commit -m 'feat: publish <game-id> <name>'"
echo ""
echo "After committing, regenerate the catalogue:"
echo "  python3 tools/catalogue-generator.py"
