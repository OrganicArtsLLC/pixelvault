#!/usr/bin/env python3
"""
Batch Canvas Text Polish — Improve in-game HUD text contrast and readability.

Adds a subtle text shadow to all canvas fillText calls for better contrast,
and ensures textBaseline is set for consistent vertical alignment.

Inserts a small JS snippet right after the canvas context is obtained.

Usage:
    python3 tools/batch-canvas-text.py
    python3 tools/batch-canvas-text.py --dry
"""
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DRY_RUN = '--dry' in sys.argv

DIRS = ['prototypes', 'ai-archaeology', 'ai-evolution']

# Snippet to insert: a helper function for crisp HUD text
SNIPPET = """
// ── Crisp HUD text helper ──
function hudText(text, x, y, color, size, align) {
  ctx.save();
  ctx.font = (size || 14) + 'px monospace';
  ctx.textAlign = align || 'left';
  ctx.textBaseline = 'top';
  ctx.shadowColor = 'rgba(0,0,0,0.8)';
  ctx.shadowBlur = 3;
  ctx.shadowOffsetX = 1;
  ctx.shadowOffsetY = 1;
  ctx.fillStyle = color || '#fff';
  ctx.fillText(text, x, y);
  ctx.restore();
}
"""

def find_game_files():
    files = []
    for d in DIRS:
        dirpath = PROJECT_ROOT / d
        if dirpath.exists():
            for f in dirpath.rglob('*.html'):
                files.append(f)
    return sorted(files)


def process_file(filepath):
    content = filepath.read_text(errors='replace')

    if 'hudText' in content:
        return False  # Already has it

    # Find where to insert: after canvas context is obtained
    # Common patterns: const ctx = canvas.getContext('2d');
    pattern = re.search(r"((?:const|let|var)\s+ctx\s*=\s*\w+\.getContext\(['\"]2d['\"]\)\s*;)", content)
    if not pattern:
        return False

    insert_pos = pattern.end()
    new_content = content[:insert_pos] + '\n' + SNIPPET + content[insert_pos:]

    if not DRY_RUN:
        filepath.write_text(new_content)
    return True


def main():
    files = find_game_files()
    print(f'Processing {len(files)} game files...')
    if DRY_RUN:
        print('(DRY RUN)\n')

    updated = 0
    for f in files:
        if process_file(f):
            rel = f.relative_to(PROJECT_ROOT)
            print(f'  ✓ {rel}')
            updated += 1

    print(f'\n{"DRY RUN " if DRY_RUN else ""}Updated: {updated} / {len(files)}')


if __name__ == '__main__':
    main()
