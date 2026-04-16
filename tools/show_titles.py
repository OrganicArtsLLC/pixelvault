#!/usr/bin/env python3
"""Show all rendered game titles - document.title and canvas text."""
import glob, re, os

title_re = re.compile(r"document\.title\s*=\s*['\"]([^'\"]+)['\"]", re.I)
hud_re = re.compile(r"hudText\(['\"]([^'\"]+)['\"]|fillText\(['\"]([^'\"]+)['\"]", re.I)

for f in sorted(glob.glob('prototypes/**/*.html', recursive=True)):
    try:
        c = open(f, encoding='utf-8', errors='ignore').read()
    except:
        continue
    gid = os.path.basename(f).replace('.html', '')
    t = title_re.search(c)
    dt = t.group(1) if t else ''
    huds = [m.group(1) or m.group(2) for m in hud_re.finditer(c)]
    print(f"{gid} | {dt} | {' / '.join(huds[:4])}")
