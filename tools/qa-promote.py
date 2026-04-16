#!/usr/bin/env python3
"""
qa-promote.py — Promote a QA-certified game to the public gallery.

Usage:
  python3 tools/qa-promote.py <game-id>          # Promote a game
  python3 tools/qa-promote.py --list             # Show all promotable (rating:4) games
  python3 tools/qa-promote.py --promoted         # Show already-promoted games
  python3 tools/qa-promote.py --demote <game-id> # Remove a game from the promoted set

Promotion criteria:
  - manifest.json rating == "4" (QA-certified)
  - Source HTML file exists on disk

Promoted games live in games/<game-id>.html (git-tracked).
The public gallery reads promoted-manifest.json (pushed as manifest.json to public repo).
"""

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).parent.parent
MANIFEST = REPO / "manifest.json"
PROMOTED_MANIFEST = REPO / "promoted-manifest.json"
GAMES_DIR = REPO / "games"
QA_REPORT = REPO / "qa-report.json"


def load_manifest() -> dict:
    m = json.loads(MANIFEST.read_text())
    if "prototypes" not in m:
        print("ERROR: manifest.json has no 'prototypes' array")
        sys.exit(1)
    return m


def load_promoted() -> dict:
    if PROMOTED_MANIFEST.exists():
        return json.loads(PROMOTED_MANIFEST.read_text())
    return {"generated": "", "version": "0.5.0", "totalGames": 0, "prototypes": []}


def load_qa_report() -> dict[str, dict]:
    """Returns dict keyed by file path."""
    if not QA_REPORT.exists():
        return {}
    items = json.loads(QA_REPORT.read_text())
    return {item["file"]: item for item in items}


def save_promoted(promoted: dict) -> None:
    promoted["generated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    promoted["totalGames"] = len(promoted["prototypes"])
    PROMOTED_MANIFEST.write_text(json.dumps(promoted, indent=2, ensure_ascii=False) + "\n")


def find_entry(manifest: dict, game_id: str) -> dict | None:
    for p in manifest["prototypes"]:
        if p["id"] == game_id:
            return p
    return None


def is_promoted(promoted: dict, game_id: str) -> bool:
    return any(p["id"] == game_id for p in promoted["prototypes"])


def cmd_list(manifest: dict, promoted: dict) -> None:
    promoted_ids = {p["id"] for p in promoted["prototypes"]}
    candidates = [p for p in manifest["prototypes"] if p.get("rating") == "4"]
    eligible = [p for p in candidates if p["id"] not in promoted_ids]

    print(f"\n{'='*60}")
    print(f"  QA-Certified games not yet promoted  ({len(eligible)} of {len(candidates)} total)")
    print(f"{'='*60}")
    for p in eligible:
        src = REPO / p["file"]
        exists = "✓" if src.exists() else "✗"
        print(f"  {exists}  {p['id']:<45}  {p.get('track','')}")
    print()
    if promoted_ids:
        print(f"  Already promoted: {len(promoted_ids)} game(s). Run --promoted to see them.")
    print()


def cmd_promoted(promoted: dict) -> None:
    games = promoted["prototypes"]
    print(f"\n{'='*60}")
    print(f"  Promoted games  ({len(games)} total)")
    print(f"{'='*60}")
    for p in games:
        print(f"  {p['id']:<45}  {p['file']}")
    print()


def cmd_promote(game_id: str, manifest: dict, promoted: dict, qa_report: dict) -> int:
    entry = find_entry(manifest, game_id)
    if not entry:
        print(f"ERROR: Game not found in manifest: {game_id}")
        print("       Run --list to see available game IDs.")
        return 1

    if entry.get("rating") != "4":
        rating = entry.get("rating", "unset")
        print(f"ERROR: {game_id} is not certified (rating={rating}, need 4).")
        print("       Open the QA dashboard and rate it Certified (key 4) first.")
        return 1

    src = REPO / entry["file"]
    if not src.exists():
        print(f"ERROR: Source file not found: {entry['file']}")
        return 1

    # Informational QA report check (non-blocking for stale paths)
    qa_file = entry["file"]
    if qa_file in qa_report:
        severity = qa_report[qa_file].get("severity", "UNKNOWN")
        issues = qa_report[qa_file].get("issues", [])
        fatal = [i for i in issues if str(i.get("severity", "")).upper() == "FATAL"]
        if fatal:
            print(f"WARNING: {game_id} has FATAL issues in qa-report:")
            for issue in fatal:
                print(f"         {issue}")
            resp = input("Promote anyway? [y/N] ").strip().lower()
            if resp != "y":
                return 1
    else:
        print(f"  (qa-report has no entry for {qa_file} — skipping automated check)")

    # Copy to games/
    GAMES_DIR.mkdir(exist_ok=True)
    dest_name = f"{game_id}.html"
    dest = GAMES_DIR / dest_name
    shutil.copy2(src, dest)

    # Build public manifest entry (file path points to games/ in the public repo)
    promoted_entry = {**entry, "file": f"games/{dest_name}"}

    if is_promoted(promoted, game_id):
        promoted["prototypes"] = [
            promoted_entry if p["id"] == game_id else p
            for p in promoted["prototypes"]
        ]
        action = "Updated"
    else:
        promoted["prototypes"].append(promoted_entry)
        action = "Added"

    save_promoted(promoted)

    print(f"\n  ✓ {action}: {game_id}")
    print(f"  ✓ Game file:          games/{dest_name}")
    print(f"  ✓ Promoted manifest:  {len(promoted['prototypes'])} game(s) total")
    print(f"\n  Next steps:")
    print(f"    git add games/{dest_name} promoted-manifest.json")
    print(f"    git commit -m 'promote: {game_id}'")
    print(f"    ./publish-public.sh --push --force")
    print()
    return 0


def cmd_demote(game_id: str, promoted: dict) -> int:
    if not is_promoted(promoted, game_id):
        print(f"ERROR: {game_id} is not currently promoted.")
        return 1

    promoted["prototypes"] = [p for p in promoted["prototypes"] if p["id"] != game_id]
    save_promoted(promoted)

    game_file = GAMES_DIR / f"{game_id}.html"
    if game_file.exists():
        game_file.unlink()
        print(f"  ✓ Removed: games/{game_id}.html")

    print(f"  ✓ Demoted: {game_id}")
    print(f"  ✓ Promoted manifest: {len(promoted['prototypes'])} game(s) remaining")
    print(f"\n  Next steps:")
    print(f"    git rm games/{game_id}.html || true")
    print(f"    git add promoted-manifest.json")
    print(f"    git commit -m 'demote: {game_id}'")
    print(f"    ./publish-public.sh --push --force")
    print()
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Promote QA-certified PixelVault games to the public gallery.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--list", action="store_true", help="Show promotable (rating:4) games")
    group.add_argument("--promoted", action="store_true", help="Show already-promoted games")
    group.add_argument("--demote", metavar="GAME_ID", help="Remove a game from promoted set")
    parser.add_argument("game_id", nargs="?", help="Game ID to promote (e.g. scr-007-vanguard-scroll)")

    args = parser.parse_args()

    if not args.list and not args.promoted and not args.demote and not args.game_id:
        parser.print_help()
        return 0

    manifest = load_manifest()
    promoted = load_promoted()
    qa_report = load_qa_report()

    if args.list:
        cmd_list(manifest, promoted)
        return 0
    elif args.promoted:
        cmd_promoted(promoted)
        return 0
    elif args.demote:
        return cmd_demote(args.demote, promoted)
    else:
        return cmd_promote(args.game_id, manifest, promoted, qa_report)


if __name__ == "__main__":
    sys.exit(main())
