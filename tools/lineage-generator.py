#!/usr/bin/env python3
"""
Lineage Generator — Build ancestry graph from game metadata.

Scans all prototypes and extracts parent→child relationships from
the ANCESTRY field in each game's metadata. Generates:
  1. lineage.json — machine-readable ancestry graph
  2. Updates manifest.json with parentId/childIds fields

Usage:
    python3 tools/lineage-generator.py
"""
import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = PROJECT_ROOT / "manifest.json"
LINEAGE_OUTPUT = PROJECT_ROOT / "lineage.json"


def extract_parent_refs(ancestry: str, game_id: str) -> list[str]:
    """Extract parent game IDs from an ancestry string."""
    parents = []

    # Pattern 1: "ser-NNN (GameName)" — direct reference to another prototype
    # e.g., "adv-003 (Zelda 1986)" or "maz-001 (Pac-Man 1980)"
    refs = re.findall(r'([a-z]{2,4}-\d{3})', ancestry)
    for ref in refs:
        if ref != game_id[:7]:  # Don't self-reference
            parents.append(ref)

    # Pattern 2: "from ser-NNN" — explicit derivation
    from_refs = re.findall(r'from\s+([a-z]{2,4}-\d{3})', ancestry)
    parents.extend(from_refs)

    return list(set(parents))  # dedupe


def find_game_by_prefix(games: list[dict], prefix: str) -> dict | None:
    """Find a game whose ID starts with the given prefix."""
    for g in games:
        gid = g.get('id', '')
        if gid.startswith(prefix) or gid[:7] == prefix[:7]:
            return g
    return None


def build_lineage(manifest_data: dict) -> dict:
    """Build the full lineage graph from manifest data."""
    protos = manifest_data['prototypes']

    # Index games by ID and by series-number prefix
    by_id = {g['id']: g for g in protos}
    by_prefix = {}
    for g in protos:
        prefix = f"{g.get('series','')}-{str(g.get('number','0')).zfill(3)}"
        by_prefix[prefix] = g

    # Build parent-child relationships
    lineage = {
        'nodes': [],
        'edges': [],
        'families': {}  # series → list of games in that series
    }

    for g in protos:
        gid = g['id']
        file = g.get('file', '')
        track = 'ai-archaeology' if 'ai-archaeology' in file else \
                'ai-evolution' if 'ai-evolution' in file else 'archetype'
        series = g.get('series', '?')
        ancestry = g.get('ancestry', '')

        node = {
            'id': gid,
            'series': series,
            'number': g.get('number', '0'),
            'name': g.get('name', gid),
            'track': track,
            'mechanic': g.get('mechanic', '')[:60],
            'parentIds': [],
            'childIds': []
        }

        # Extract parent references from ancestry field
        parent_prefixes = extract_parent_refs(ancestry, gid)
        for pp in parent_prefixes:
            parent = by_prefix.get(pp)
            if parent:
                pid = parent['id']
                node['parentIds'].append(pid)
                # Edge
                lineage['edges'].append({
                    'from': pid,
                    'to': gid,
                    'type': 'ai-overlay' if track == 'ai-archaeology' else
                            'evolution' if track == 'ai-evolution' else 'variant'
                })

        lineage['nodes'].append(node)

        # Build series families
        if series not in lineage['families']:
            lineage['families'][series] = []
        lineage['families'][series].append(gid)

    # Set childIds on parent nodes
    for edge in lineage['edges']:
        for node in lineage['nodes']:
            if node['id'] == edge['from']:
                if edge['to'] not in node['childIds']:
                    node['childIds'].append(edge['to'])

    # Stats
    nodes_with_parents = sum(1 for n in lineage['nodes'] if n['parentIds'])
    nodes_with_children = sum(1 for n in lineage['nodes'] if n['childIds'])
    lineage['stats'] = {
        'totalNodes': len(lineage['nodes']),
        'totalEdges': len(lineage['edges']),
        'nodesWithParents': nodes_with_parents,
        'nodesWithChildren': nodes_with_children,
        'orphans': len(lineage['nodes']) - nodes_with_parents,
        'seriesCount': len(lineage['families'])
    }

    return lineage


def main():
    print("Lineage Generator — Building ancestry graph...")

    manifest = json.load(open(MANIFEST))
    lineage = build_lineage(manifest)

    # Write lineage.json
    with open(LINEAGE_OUTPUT, 'w') as f:
        json.dump(lineage, f, indent=2)

    stats = lineage['stats']
    print(f"  Nodes: {stats['totalNodes']}")
    print(f"  Edges: {stats['totalEdges']}")
    print(f"  With parents: {stats['nodesWithParents']}")
    print(f"  With children: {stats['nodesWithChildren']}")
    print(f"  Orphans (roots): {stats['orphans']}")
    print(f"  Series: {stats['seriesCount']}")
    print(f"  Written to: {LINEAGE_OUTPUT}")

    # Update manifest with parentId/childIds
    by_id = {n['id']: n for n in lineage['nodes']}
    for p in manifest['prototypes']:
        node = by_id.get(p['id'])
        if node:
            p['parentIds'] = node['parentIds']
            p['childIds'] = node['childIds']
            p['track'] = node['track']

    with open(MANIFEST, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"  Updated manifest.json with lineage fields")


if __name__ == '__main__':
    main()
