#!/usr/bin/env python3
"""
Compendium Generator — Mine all 460 game files to build comprehensive
creator index, timeline, genre lineage, and collection statistics.

Extracts from both metadata blocks AND info panel HTML content.

Usage:
    python3 tools/compendium-generator.py              # Generate report
    python3 tools/compendium-generator.py --markdown    # Output as markdown sections
"""
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MARKDOWN_MODE = '--markdown' in sys.argv


def parse_html_file(filepath):
    """Extract metadata and info panel content from a game HTML file."""
    content = filepath.read_text(errors='replace')
    result = {
        'file': str(filepath.relative_to(PROJECT_ROOT)),
        'metadata': {},
        'history': '',
        'creators_mentioned': [],
        'years_mentioned': [],
    }

    # Parse metadata block
    meta_match = re.search(r'<!--(.*?)-->', content, re.DOTALL)
    if meta_match:
        for line in meta_match.group(1).strip().splitlines():
            line = line.strip()
            if ':' in line:
                key, _, value = line.partition(':')
                key = key.strip().upper()
                value = value.strip()
                if key and value:
                    result['metadata'][key] = value

    # Extract History & Lineage section
    history_match = re.search(
        r'<h2>History.*?</h2>(.*?)(?:<h2>|</div>)',
        content, re.DOTALL | re.IGNORECASE
    )
    if history_match:
        result['history'] = re.sub(r'<[^>]+>', ' ', history_match.group(1)).strip()

    # Extract years
    ancestry = result['metadata'].get('ANCESTRY', '')
    full_text = ancestry + ' ' + result['history']
    years = re.findall(r'\b(1[0-9]{3}|20[0-2][0-9])\b', full_text)
    result['years_mentioned'] = sorted(set(int(y) for y in years))

    # Extract creator names from history (bolded text that looks like names)
    bold_texts = re.findall(r'<strong>([^<]{3,50})</strong>', content)
    for bt in bold_texts:
        # Filter to likely human names (First Last pattern)
        if re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+', bt) and \
           not bt.startswith(('AI Era', 'How to', 'Core ', 'The ', 'No ')):
            result['creators_mentioned'].append(bt)

    # Also check for creator patterns in ancestry
    creator_patterns = re.findall(
        r'(?:by |created by |creator |designed by )([A-Z][a-z]+ [A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)',
        full_text
    )
    result['creators_mentioned'].extend(creator_patterns)
    result['creators_mentioned'] = list(set(result['creators_mentioned']))

    return result


def scan_all_games():
    """Scan all game files and extract data."""
    games = []
    dirs = ['prototypes', 'ai-archaeology', 'ai-evolution']
    for d in dirs:
        dirpath = PROJECT_ROOT / d
        if not dirpath.exists():
            continue
        for html_file in sorted(dirpath.rglob('*.html')):
            data = parse_html_file(html_file)
            games.append(data)
    return games


def build_creator_index(games):
    """Build comprehensive creator index from all games."""
    creators = defaultdict(lambda: {'games': [], 'years': set(), 'org': set()})

    for g in games:
        for creator in g['creators_mentioned']:
            gid = g['metadata'].get('PROTOTYPE', os.path.basename(g['file']))
            creators[creator]['games'].append(gid)
            for y in g['years_mentioned']:
                creators[creator]['years'].add(y)

    return dict(sorted(creators.items()))


def build_timeline(games):
    """Build chronological timeline of all games."""
    timeline = []
    for g in games:
        ancestry = g['metadata'].get('ANCESTRY', '')
        prototype = g['metadata'].get('PROTOTYPE', '')
        series = g['metadata'].get('SERIES', '')
        number = g['metadata'].get('NUMBER', '')
        mechanic = g['metadata'].get('MECHANIC', '')

        # Get the primary year (earliest in ancestry)
        years = g['years_mentioned']
        if years:
            primary_year = min(years)
            timeline.append({
                'year': primary_year,
                'game': f'{series}-{number}-{prototype}' if series else prototype,
                'mechanic': mechanic[:60] if mechanic else '',
                'ancestry': ancestry[:80] if ancestry else '',
                'track': 'AI Arch' if 'ai-archaeology' in g['file'] else
                         'AI Evo' if 'ai-evolution' in g['file'] else 'Archetype'
            })

    return sorted(timeline, key=lambda x: x['year'])


def build_series_summary(games):
    """Build per-series game count and description."""
    series_data = defaultdict(lambda: {'proto': 0, 'ai_arch': 0, 'ai_evo': 0, 'games': []})

    for g in games:
        s = g['metadata'].get('SERIES', '?')
        f = g['file']
        gid = g['metadata'].get('PROTOTYPE', '')

        if 'ai-archaeology' in f:
            series_data[s]['ai_arch'] += 1
        elif 'ai-evolution' in f:
            series_data[s]['ai_evo'] += 1
        else:
            series_data[s]['proto'] += 1

        series_data[s]['games'].append(gid)

    return dict(sorted(series_data.items()))


def main():
    print("Compendium Generator — Mining 460 game files...")
    games = scan_all_games()
    print(f"  Scanned: {len(games)} files")

    creators = build_creator_index(games)
    timeline = build_timeline(games)
    series = build_series_summary(games)

    print(f"  Creators found: {len(creators)}")
    print(f"  Timeline entries: {len(timeline)}")
    print(f"  Series: {len(series)}")

    if MARKDOWN_MODE:
        # Output markdown sections for insertion into COMPENDIUM.md
        print("\n\n### === CREATOR INDEX (extracted from info panels) ===\n")
        print("| Creator | Games | Era |")
        print("|---------|-------|-----|")
        for name, data in creators.items():
            game_list = ', '.join(data['games'][:3])
            if len(data['games']) > 3:
                game_list += f' +{len(data["games"])-3} more'
            years = sorted(data['years'])
            year_range = f"{min(years)}-{max(years)}" if years else "?"
            print(f"| {name} | {game_list} | {year_range} |")

        print("\n\n### === COLLECTION STATISTICS ===\n")
        total_proto = sum(s['proto'] for s in series.values())
        total_arch = sum(s['ai_arch'] for s in series.values())
        total_evo = sum(s['ai_evo'] for s in series.values())
        print(f"| Track | Count |")
        print(f"|-------|-------|")
        print(f"| Archetypes | {total_proto} |")
        print(f"| AI Archaeology | {total_arch} |")
        print(f"| AI Evolution | {total_evo} |")
        print(f"| **Total** | **{total_proto + total_arch + total_evo}** |")
        print()
        print("| Series | Code | Archetypes | AI Arch | AI Evo | Total |")
        print("|--------|------|-----------|---------|--------|-------|")
        for s, data in sorted(series.items()):
            total = data['proto'] + data['ai_arch'] + data['ai_evo']
            print(f"| {s.upper()} | `{s}` | {data['proto']} | {data['ai_arch']} | {data['ai_evo']} | {total} |")

        # Timeline by decade
        print("\n\n### === TIMELINE BY DECADE ===\n")
        decades = defaultdict(list)
        for t in timeline:
            decade = (t['year'] // 10) * 10
            decades[decade].append(t)

        for decade in sorted(decades):
            entries = decades[decade]
            label = f"{decade}s" if decade >= 1900 else f"~{decade} CE" if decade > 0 else "Ancient"
            print(f"\n**{label}** ({len(entries)} games)")
            for t in entries[:10]:
                print(f"- {t['year']}: {t['game']} — {t['mechanic']}")
            if len(entries) > 10:
                print(f"- ... and {len(entries)-10} more")
    else:
        # Summary mode
        print("\n=== Top Creators ===")
        for name, data in list(creators.items())[:20]:
            print(f"  {name}: {len(data['games'])} games")

        print(f"\n=== Timeline Span ===")
        if timeline:
            print(f"  Earliest: {timeline[0]['year']} ({timeline[0]['game']})")
            print(f"  Latest: {timeline[-1]['year']} ({timeline[-1]['game']})")

        print(f"\n=== Series Breakdown ===")
        for s, data in sorted(series.items(), key=lambda x: -(x[1]['proto']+x[1]['ai_arch']+x[1]['ai_evo'])):
            total = data['proto'] + data['ai_arch'] + data['ai_evo']
            print(f"  {s.upper():5} {data['proto']:3} proto + {data['ai_arch']:2} arch + {data['ai_evo']:3} evo = {total:3} total")


if __name__ == '__main__':
    main()
