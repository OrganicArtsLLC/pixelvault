#!/usr/bin/env python3
"""
Batch UI Polish — Apply across all game HTML files:
1. Add educational disclaimer to info panels (games based on real titles)
2. Modernize text rendering: anti-aliased fonts, contrast shadows, clean HUD
3. Add CSS font-smoothing and improved typography

Usage:
    python3 tools/batch-ui-polish.py          # Apply to all games
    python3 tools/batch-ui-polish.py --dry    # Preview changes without writing
"""
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DRY_RUN = '--dry' in sys.argv

# Directories to process
DIRS = ['prototypes', 'ai-archaeology', 'ai-evolution']

# AI-originated games (no disclaimer needed — not based on real titles)
AI_ORIGINAL_PREFIXES = {'new-'}  # NEW series games are AI-originated

DISCLAIMER_HTML = """
    <h2>Educational Notice</h2>
    <p>This prototype is an educational reconstruction of a classic game mechanic, created for research and historical study as part of the Pixel Vault project. It is not affiliated with, endorsed by, or connected to the original game's creators or rights holders. All original games referenced belong to their respective owners.</p>
"""

# CSS improvements for modern text rendering
CSS_ADDITIONS = """
html { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; }
"""

# JS text rendering improvements — add shadow for contrast on canvas text
JS_HUD_IMPROVEMENT = """
// ── UI Polish: crisp text with contrast shadows ──
const _origFillText = CanvasRenderingContext2D.prototype.fillText;
const _origStrokeText = CanvasRenderingContext2D.prototype.strokeText;
CanvasRenderingContext2D.prototype.fillText = function(text, x, y, maxWidth) {
  if (!this._noShadow) {
    const prevShadow = this.shadowColor;
    const prevBlur = this.shadowBlur;
    if (!this.shadowBlur || this.shadowBlur < 1) {
      this.shadowColor = 'rgba(0,0,0,0.7)';
      this.shadowBlur = 2;
    }
    _origFillText.apply(this, arguments);
    this.shadowColor = prevShadow;
    this.shadowBlur = prevBlur;
  } else {
    _origFillText.apply(this, arguments);
  }
};
"""


def find_game_files():
    files = []
    for d in DIRS:
        dirpath = PROJECT_ROOT / d
        if dirpath.exists():
            for f in dirpath.rglob('*.html'):
                files.append(f)
    return sorted(files)


def needs_disclaimer(filepath):
    """Games based on real titles need disclaimer. AI-originated (new-*) don't."""
    name = filepath.name
    for prefix in AI_ORIGINAL_PREFIXES:
        if name.startswith(prefix):
            return False
    # WLD series in ai-evolution are also AI-originated
    rel = filepath.relative_to(PROJECT_ROOT)
    if 'ai-evolution' in str(rel):
        return False
    return True


def add_disclaimer(content, filepath):
    """Add educational disclaimer to the info panel if not already present."""
    if 'Educational Notice' in content:
        return content, False

    # Find the closing </div> of the info panel inner div
    # Pattern: look for the Prototype Notes section end, then insert before closing </div>
    # The info panel structure is: <div id="info-panel"><div class="inner">...sections...</div></div>

    # Find the last </div> before </div> of info-panel
    # Better: find "Prototype Notes" section and insert after it
    marker = '<h2>Prototype Notes</h2>'
    if marker not in content:
        # Try alternate markers
        for m in ['Prototype Notes', 'Classification', 'AI Archaeology']:
            pattern = f'<h2>{m}</h2>'
            if pattern in content:
                marker = pattern
                break

    # Insert before the closing </div></div> of the info panel
    # Find the pattern: </div>\n</div> that closes the inner and info-panel divs
    panel_close = re.search(r'(  </div>\s*</div>\s*<script>)', content)
    if panel_close:
        insert_pos = panel_close.start()
        new_content = content[:insert_pos] + DISCLAIMER_HTML + '\n' + content[insert_pos:]
        return new_content, True

    # Fallback: find </div>\n</div> near info-panel
    panel_close2 = re.search(r'(</div>\s*</div>\s*\n\s*<script>)', content)
    if panel_close2:
        insert_pos = panel_close2.start()
        new_content = content[:insert_pos] + DISCLAIMER_HTML + '\n' + content[insert_pos:]
        return new_content, True

    return content, False


def improve_css(content):
    """Add font-smoothing and modern text rendering CSS."""
    if '-webkit-font-smoothing' in content:
        return content, False

    # Insert after the opening <style> block's first line
    # Find: * { margin: 0; ... }
    insert_after = 'box-sizing: border-box; }'
    if insert_after in content:
        idx = content.index(insert_after) + len(insert_after)
        new_content = content[:idx] + '\n' + CSS_ADDITIONS + content[idx:]
        return new_content, True

    return content, False


def improve_fonts(content):
    """Replace pixelated monospace with clean monospace stack for readability."""
    changed = False

    # Improve info panel font stack for readability
    old_font = "font-family: monospace;"
    new_font = "font-family: 'SF Mono', 'Cascadia Code', 'Fira Code', 'Consolas', monospace;"
    if old_font in content and new_font not in content:
        # Only replace the body-level font, not canvas font strings
        # The body font affects the info panel
        content = content.replace(
            'font-family: monospace; }',
            "font-family: 'SF Mono', 'Cascadia Code', 'Consolas', monospace; }",
            1  # Only first occurrence (body style)
        )
        changed = True

    return content, changed


def process_file(filepath):
    content = filepath.read_text(errors='replace')
    changes = []

    # 1. Add disclaimer (if based on real game)
    if needs_disclaimer(filepath):
        content, added = add_disclaimer(content, filepath)
        if added:
            changes.append('disclaimer')

    # 2. Improve CSS
    content, added = improve_css(content)
    if added:
        changes.append('css-smoothing')

    # 3. Improve fonts
    content, added = improve_fonts(content)
    if added:
        changes.append('font-stack')

    if changes and not DRY_RUN:
        filepath.write_text(content)

    return changes


def main():
    files = find_game_files()
    print(f'Processing {len(files)} game files...')
    if DRY_RUN:
        print('(DRY RUN — no files will be modified)\n')

    stats = {'disclaimer': 0, 'css-smoothing': 0, 'font-stack': 0, 'skipped': 0}
    for f in files:
        rel = f.relative_to(PROJECT_ROOT)
        changes = process_file(f)
        if changes:
            print(f'  ✓ {rel}: {", ".join(changes)}')
            for c in changes:
                stats[c] = stats.get(c, 0) + 1
        else:
            stats['skipped'] += 1

    print(f'\n{"DRY RUN " if DRY_RUN else ""}Summary:')
    print(f'  Disclaimers added:  {stats["disclaimer"]}')
    print(f'  CSS smoothing:      {stats["css-smoothing"]}')
    print(f'  Font stack updated: {stats["font-stack"]}')
    print(f'  Skipped (no change):{stats["skipped"]}')


if __name__ == '__main__':
    main()
