#!/usr/bin/env python3
"""
Batch rename trademarked game names in Pixel Vault prototypes.

Renames filenames, updates METADATA PROTOTYPE fields, <title> tags, and <h1> tags.
Preserves ANCESTRY, AI-INSIGHT, and educational prose — those reference original
games for historical/educational purposes.

Usage:
    python3 tools/trademark-cleanup.py              # Dry run (default)
    python3 tools/trademark-cleanup.py --apply      # Apply renames
    python3 tools/trademark-cleanup.py --scan       # Scan for unlisted trademarks
    python3 tools/trademark-cleanup.py --stats      # Show statistics only

After applying, regenerate catalogue:
    python3 tools/catalogue-generator.py
    bash tools/gen-timestamps.sh

Created: April 2026 — Pre-publication trademark cleanup
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path

# ── Project root ─────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
SEARCH_DIRS = [
    PROJECT_ROOT / "prototypes",
    PROJECT_ROOT / "ai-archaeology",
    PROJECT_ROOT / "ai-evolution",
]

# ── Complete rename mapping ──────────────────────────────────────────────────
# Format: "old-suffix" → "new-suffix"
# The suffix is the part after {series}-{number}- in the filename.
# Organized by risk tier for auditability.

RENAMES: dict[str, str] = {
    # ═══════════════════════════════════════════════════════════════════════
    # HIGH RISK — Active trademark enforcement, major publishers
    # ═══════════════════════════════════════════════════════════════════════

    # --- prototypes/ ---
    "pacman": "pellet-chase",                   # Bandai Namco
    "tetris": "falling-blocks",                 # The Tetris Company
    "zelda": "quest-explorer",                  # Nintendo
    "donkey-kong": "barrel-climb",              # Nintendo
    "metroid": "bounty-explorer",               # Nintendo
    "castlevania": "whip-climb",                # Konami
    "contra": "run-and-gun",                    # Konami
    "diablo": "dungeon-loot",                   # Blizzard/Activision
    "carmen-sandiego": "globe-detective",        # HMH/Broderbund
    "mortal-kombat": "arena-fighter",           # WB Games
    "doom": "corridor-shooter",                 # id/Bethesda/Microsoft
    "civilization": "empire-builder",           # 2K/Firaxis
    "scrabble": "word-grid",                    # Hasbro/Mattel
    "wordle": "word-guess",                     # NYT
    "prince-of-persia": "palace-runner",        # Ubisoft
    "clashroyale": "lane-battle",               # Supercell
    "clashofclans": "village-raid",             # Supercell
    "punchout": "boxing-ring",                  # Nintendo
    "kid-icarus": "sky-archer",                 # Nintendo
    "bubble-bobble": "bubble-trap",             # Taito
    "cuttherope": "rope-physics",               # ZeptoLab
    "cookierun": "endless-dash",                # Devsisters
    "kingdomrush": "tower-defense",             # Ironhide
    "bloons": "pop-defense",                    # Ninja Kiwi
    "deathloop": "time-loop",                   # Arkane/Bethesda

    # --- ai-archaeology/ (compound names) ---
    "carmen-deduction": "globe-deduction",       # HMH
    "mk-combos": "arena-combos",                # WB Games (MK abbreviation)
    "metroidmap": "bounty-map",                 # Nintendo
    "dk-barrels": "barrel-dodge",               # Nintendo (DK abbreviation)
    "castlevania-fsm": "whip-fsm",              # Konami
    "wordle-entropy": "word-entropy",            # NYT
    "diablo-loot": "dungeon-loot-ai",           # Blizzard
    "contra-predict": "run-predict",             # Konami
    "doom-spatial": "corridor-spatial",          # id/Bethesda

    # --- ai-evolution/ ---
    "gravitypong": "gravity-paddle",             # Atari (Pong)

    # ═══════════════════════════════════════════════════════════════════════
    # MEDIUM RISK — Classic arcade/game names, some actively defended
    # ═══════════════════════════════════════════════════════════════════════

    # --- prototypes/ ---
    "pong": "paddle-volley",                    # Atari
    "breakout": "brick-break",                  # Atari
    "frogger": "road-crossing",                 # Konami
    "qbert": "pyramid-hop",                     # Sony (via Gonzo Games)
    "dig-dug": "tunnel-digger",                 # Bandai Namco
    "tron": "light-trail",                      # Disney
    "katamari": "roll-collect",                 # Bandai Namco
    "lemmings": "march-rescue",                 # Sony (via Psygnosis)
    "wing-commander": "space-dogfight",         # EA (Origin Systems)
    "gauntlet": "dungeon-crawl",                # WB (Midway/Atari)
    "ultima": "open-rpg",                       # EA (Origin Systems)
    "worms": "artillery-duel",                  # Team17
    "populous": "god-sim",                      # EA (Bullfrog)
    "kings-quest": "crown-adventure",           # Activision (Sierra)
    "maniac-mansion": "haunted-puzzle",         # LucasArts/Disney
    "dragons-lair": "animated-quest",           # Digital Leisure
    "burgertime": "food-stack",                 # G-Mode (Data East)
    "battleship": "naval-grid",                 # Hasbro
    "outrun": "coast-racer",                    # Sega
    "zaxxon": "iso-shooter",                    # Sega
    "pengo": "ice-slide",                       # Sega
    "agario": "cell-absorb",                    # Miniclip
    "gunbound": "arc-artillery",                # Softnyx
    "doodlejump": "platform-hop",              # Lima Sky
    "bards-tale": "party-rpg",                  # inXile
    "wasteland": "post-apoc-rpg",               # inXile
    "skifree": "slope-run",                     # Microsoft
    "rampage": "monster-smash",                 # WB (Midway)
    "joust": "flap-duel",                       # WB (Midway)
    "asteroids": "space-rocks",                 # Atari
    "centipede": "bug-shoot",                   # Atari
    "missile-command": "sky-defense",           # Atari
    "tempest": "tube-shooter",                  # Atari
    "marble-madness": "marble-roll",            # EA (Atari)
    "oregon-trail": "frontier-trek",            # HMH (MECC)
    "paperboy": "delivery-run",                 # WB (Midway)
    "tapper": "bar-serve",                      # WB (Midway)
    "papersplease": "border-check",             # 3909 LLC
    "karateka": "martial-run",                  # Jordan Mechner
    "berzerk": "room-escape",                   # Stern
    "robotron": "swarm-rescue",                 # WB (Midway)
    "1942": "warbird-scroll",                   # Capcom
    "paneldepon": "swap-match",                 # Nintendo
    "kururin": "spin-navigate",                 # Nintendo
    "molemania": "burrow-puzzle",               # Nintendo
    "bump-n-jump": "leap-racer",                # Mattel/Data East
    "stratego": "rank-battle",                  # Jumbo/Konami
    "mastermind": "code-crack",                 # Hasbro

    # --- ai-archaeology/ (compound names) ---
    "tron-territory": "light-territory",         # Disney
    "digdug-tunnel": "tunnel-ai",               # Bandai Namco
    "asteroids-predict": "space-rocks-predict",  # Atari
    "katamari-growth": "roll-growth",           # Bandai Namco
    "lemmingbrain": "march-brain",              # Sony
    "battleship-bayes": "naval-bayes",          # Hasbro
    "missile-intercept": "sky-intercept",        # Atari
    "mastermind-knuth": "codebreak-knuth",      # Hasbro
    "paneldepon-chain": "swap-chain",            # Nintendo
    "1942-formations": "warbird-formations",     # Capcom
    "oregon-survival": "frontier-survival",      # HMH
    "taipan-trade": "merchant-trade",            # (see lower risk)
    "dicewars-prob": "territory-dice-prob",      # (see lower risk)

    # ═══════════════════════════════════════════════════════════════════════
    # LOWER RISK — Indie/niche/older titles, less enforcement but still TM
    # ═══════════════════════════════════════════════════════════════════════

    # --- prototypes/ ---
    "zork": "text-adventure",                   # Activision (via Infocom)
    "pitfall": "jungle-swing",                  # Activision
    "canabalt": "roof-sprint",                  # Semi Secret Software
    "lode-runner": "dig-and-run",               # Tozai Games
    "anotherworld": "cinematic-escape",         # Eric Chahi
    "downwell": "vertical-descent",             # Devolver
    "sokoban": "box-push",                      # Thinking Rabbit
    "nethack": "ascii-dungeon",                 # NetHack DevTeam (open src)
    "dungeon-master": "party-crawler",          # FTL Games
    "taipan": "trade-voyage",                   # (public domain concept)
    "motherload": "drill-mine",                 # XGen Studios
    "unpacking": "unbox-sort",                  # Witch Beam
    "dicewars": "territory-dice",               # (Flash game)
    "cristales": "time-crystal-rpg",            # Modus Games
    "astonishia": "turnbased-rpg",              # Sonnori
    "chipschallenge": "tile-puzzle",            # (mixed ownership)
    "colorlines": "color-match",                # (generic concept)
    "cameltry": "ball-maze",                    # Taito
    "puzzloop": "ring-shooter",                 # Mitchell
    "bakubaku": "feed-match",                   # Sega
    "quinty": "grid-whack",                     # Namco
    "magicaldrop": "drop-match",                # G-Mode (Data East)
    "penguinland": "egg-roll",                  # Sega
    "hoshisaga": "star-click",                  # (Flash game)
    "puchicarat": "gem-aim",                    # Taito
    "perestroika": "reform-platform",           # (Russian, niche)
    "semblance": "morph-platform",              # Nyamakop
    "umihara": "elastic-swing",                 # Success
    "liquidkids": "water-blast",                # Taito
    "gimmick": "bounce-throw",                  # Sunsoft
    "moastray": "hex-strategy",                 # (Korean, niche)
    "dungreed": "rogue-dungeon",                # Team Horay
    "pangya": "golf-aim",                       # Ntreev Soft
    "audition": "rhythm-dance",                 # T3 Entertainment
    "pumpit": "dance-arrows",                   # Andamiro
    "djmax": "rhythm-keys",                     # Neowiz
    "qwop": "ragdoll-run",                      # Bennett Foddy
    "qix": "area-claim",                        # Taito
    "jezzball": "split-bounce",                 # Microsoft
    "snake": "snake",                           # (generic, no rename needed)
    "vanguard": "vanguard-scroll",              # SNK (borderline generic)

    # --- ai-archaeology/ (compound names for lower-risk games) ---
    "pitfall-danger": "jungle-danger",          # Activision
    "canabalt-timing": "sprint-timing",         # Semi Secret
    "snake-optimal": "snake-optimal",           # (generic, keep)
    "chips-route": "tile-route",                # (Chip's Challenge)
    "nightstalker-prox": "stalker-prox",        # (Intellivision, niche)
    "crazyarcade-blast": "bomb-blast",          # Nexon
    "mole-path": "burrow-path",                 # Nintendo
    "puzzloop-chain": "ring-chain",             # Mitchell
    "sokoban-deadlock": "boxpush-deadlock",     # Thinking Rabbit
    "cameltry-path": "ballmaze-path",           # Taito
    "grow-optimal": "grow-optimal",             # (Eyezmaze, keep — generic verb)
    "colorlines-path": "colormatch-path",       # (generic)
    "bakubaku-feed": "feedmatch-feed",          # Sega
    "magicaldrop-opt": "dropmatch-opt",         # G-Mode
    "vanguard-threat": "scroll-threat",         # SNK

    # --- additional adventure games (indie / niche) ---
    "adarkroom": "survival-text",               # Doublespeak Games
    "coffeetalk": "cafe-chat",                  # Toge Productions
    "minit": "one-minute-quest",                # Devolver
    "chuchel": "fuzzy-quest",                   # Amanita Design
    "detention": "haunted-school",              # Red Candle Games
    "yumenikki": "dream-walk",                  # Kikiyama
    "replica": "phone-spy",                     # Somi
    "iljimae": "folk-thief",                    # (Korean drama, niche)
    "crazyarcade": "bomb-battle",               # Nexon
    "kingdomwinds": "kingdom-winds",            # (keep — not trademarked)
}

# Files that should NOT be renamed (generic terms, no trademark issue)
SKIP_FILES = {
    "snake",            # Generic term
    "snake-optimal",    # Compound with generic
    "grow-optimal",     # "Grow" is a generic verb
    "kingdomwinds",     # Not a trademarked name
    "chess", "solitaire", "mahjong", "mancala", "ur", "go",
    "backgammon", "checkers", "dominoes", "blackjack", "reversi",
    "fanorona", "surakarta",  # Ancient/generic game names
}


# ── Helpers ──────────────────────────────────────────────────────────────────

def parse_filename(filename: str) -> tuple[str, str, str] | None:
    """Extract (series, number, name) from filename like 'maz-001-pacman.html'."""
    m = re.match(r'^([a-z]+)-(\d{3})-(.+)\.html$', filename)
    if m:
        return m.group(1), m.group(2), m.group(3)
    return None


def make_display_name(name_suffix: str) -> str:
    """Convert suffix like 'pellet-chase' to display 'PELLET CHASE'."""
    return name_suffix.replace("-", " ").upper()


def update_file_content(
    content: str,
    old_suffix: str,
    new_suffix: str,
    series: str,
    number: str,
) -> str:
    """Update PROTOTYPE, <title>, and <h1> in file content."""
    series_upper = series.upper()
    new_display = make_display_name(new_suffix)
    code = f"{series_upper}-{number}"

    # 1. Update PROTOTYPE: line
    content = re.sub(
        r'^(PROTOTYPE:\s*).*$',
        f'\\1{new_suffix}',
        content,
        count=1,
        flags=re.MULTILINE,
    )

    # 2. Update <title> — preserve any trailing [?] or whitespace
    content = re.sub(
        rf'(<title>\s*{re.escape(code)}\s*·\s*)([^<]*?)((?:\s*\[.\])?\s*</title>)',
        rf'\g<1>{new_display}\g<3>',
        content,
        count=1,
        flags=re.IGNORECASE,
    )

    # 3. Update <h1> — preserve surrounding tags
    content = re.sub(
        rf'(<h1[^>]*>\s*{re.escape(code)}\s*·\s*)([^<]*?)(</h1>)',
        rf'\g<1>{new_display}\g<3>',
        content,
        count=1,
        flags=re.IGNORECASE,
    )

    return content


def find_all_games() -> list[tuple[Path, str, str, str]]:
    """Find all game HTML files and parse their components.

    Returns list of (filepath, series, number, name_suffix).
    """
    games = []
    for search_dir in SEARCH_DIRS:
        if not search_dir.exists():
            continue
        for html_file in search_dir.rglob("*.html"):
            parsed = parse_filename(html_file.name)
            if parsed:
                series, number, name = parsed
                games.append((html_file, series, number, name))
    return sorted(games, key=lambda g: g[0].name)


# ── Main actions ─────────────────────────────────────────────────────────────

def dry_run() -> list[tuple[Path, str, str]]:
    """Show what would be renamed without making changes."""
    games = find_all_games()
    renames = []

    for filepath, series, number, name in games:
        if name in SKIP_FILES:
            continue
        if name in RENAMES:
            new_name = RENAMES[name]
            if new_name == name:
                continue
            new_filename = f"{series}-{number}-{new_name}.html"
            renames.append((filepath, name, new_name))

    return renames


def apply_renames() -> list[tuple[Path, Path]]:
    """Apply all renames, updating file content and filenames."""
    games = find_all_games()
    applied = []

    for filepath, series, number, name in games:
        if name in SKIP_FILES:
            continue
        if name not in RENAMES:
            continue
        new_name = RENAMES[name]
        if new_name == name:
            continue

        # Read and update content
        content = filepath.read_text(encoding="utf-8")
        updated = update_file_content(content, name, new_name, series, number)

        # Write updated content
        filepath.write_text(updated, encoding="utf-8")

        # Rename file
        new_filename = f"{series}-{number}-{new_name}.html"
        new_path = filepath.parent / new_filename
        filepath.rename(new_path)
        applied.append((filepath, new_path))

    return applied


def scan_unlisted() -> list[tuple[Path, str]]:
    """Find game files whose names are NOT in the rename mapping.

    Helps identify files that might need trademark review.
    """
    games = find_all_games()
    unlisted = []

    known_names = set(RENAMES.keys()) | SKIP_FILES
    # Also add the new names so already-renamed files aren't flagged
    known_names |= set(RENAMES.values())

    for filepath, series, number, name in games:
        if name not in known_names:
            unlisted.append((filepath, name))

    return unlisted


def show_stats():
    """Show summary statistics."""
    games = find_all_games()
    total = len(games)
    to_rename = 0
    skipped = 0
    clean = 0

    known_targets = set(RENAMES.values())

    for _, _, _, name in games:
        if name in SKIP_FILES:
            skipped += 1
        elif name in RENAMES and RENAMES[name] != name:
            to_rename += 1
        elif name in known_targets:
            clean += 1  # Already renamed
        else:
            clean += 1

    print(f"\n  Pixel Vault Trademark Cleanup — Statistics")
    print(f"  {'─' * 45}")
    print(f"  Total game files:     {total}")
    print(f"  Need renaming:        {to_rename}")
    print(f"  Skipped (generic):    {skipped}")
    print(f"  Clean / already done: {clean}")
    print()


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Batch rename trademarked game names in Pixel Vault."
    )
    parser.add_argument(
        "--apply", action="store_true",
        help="Apply renames (default is dry run).",
    )
    parser.add_argument(
        "--scan", action="store_true",
        help="Scan for files NOT in the rename mapping.",
    )
    parser.add_argument(
        "--stats", action="store_true",
        help="Show statistics only.",
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output rename mapping as JSON (for migration tools).",
    )
    args = parser.parse_args()

    if args.stats:
        show_stats()
        return

    if args.json:
        renames = dry_run()
        mapping = {}
        for filepath, old_name, new_name in renames:
            series, number, _ = parse_filename(filepath.name)
            old_id = f"{series}-{number}-{old_name}"
            new_id = f"{series}-{number}-{new_name}"
            mapping[old_id] = new_id
        print(json.dumps(mapping, indent=2))
        return

    if args.scan:
        unlisted = scan_unlisted()
        if not unlisted:
            print("\n  ✓ All game files are accounted for in the rename mapping.")
        else:
            print(f"\n  Files NOT in rename mapping ({len(unlisted)}):")
            print(f"  {'─' * 60}")
            for filepath, name in unlisted:
                rel = filepath.relative_to(PROJECT_ROOT)
                print(f"    {rel}")
            print(f"\n  Review these files — if trademarked, add to RENAMES dict.")
        return

    if args.apply:
        print("\n  ▶ Applying trademark renames...")
        applied = apply_renames()
        if not applied:
            print("  No files to rename.")
        else:
            print(f"\n  ✓ Renamed {len(applied)} files:")
            print(f"  {'─' * 60}")
            for old_path, new_path in applied:
                old_rel = old_path.relative_to(PROJECT_ROOT)
                new_name = new_path.name
                print(f"    {old_rel} → {new_name}")
            print(f"\n  Next steps:")
            print(f"    python3 tools/catalogue-generator.py   # Regenerate catalogue")
            print(f"    bash tools/gen-timestamps.sh            # Update timestamps")
            print(f"    git add -A && git commit -m 'chore: batch trademark cleanup'")
        return

    # Default: dry run
    renames = dry_run()
    if not renames:
        print("\n  ✓ No files need renaming.")
    else:
        print(f"\n  Dry Run — {len(renames)} files would be renamed:")
        print(f"  {'─' * 70}")

        # Group by risk tier
        high_risk = []
        medium_risk = []
        lower_risk = []

        # Simple heuristic: check position in mapping
        high_keys = {
            "pacman", "tetris", "zelda", "donkey-kong", "metroid", "castlevania",
            "contra", "diablo", "carmen-sandiego", "mortal-kombat", "doom",
            "civilization", "scrabble", "wordle", "prince-of-persia", "clashroyale",
            "clashofclans", "punchout", "kid-icarus", "bubble-bobble", "cuttherope",
            "cookierun", "kingdomrush", "bloons", "deathloop",
            "carmen-deduction", "mk-combos", "metroidmap", "dk-barrels",
            "castlevania-fsm", "wordle-entropy", "diablo-loot", "contra-predict",
            "doom-spatial", "gravitypong",
        }

        for filepath, old_name, new_name in renames:
            rel = filepath.relative_to(PROJECT_ROOT)
            entry = f"    {rel} → {filepath.parent.name}/{filepath.name.replace(old_name, new_name)}"
            if old_name in high_keys:
                high_risk.append(entry)
            elif old_name in {
                "pong", "breakout", "frogger", "qbert", "dig-dug", "tron",
                "katamari", "lemmings", "wing-commander", "gauntlet", "ultima",
                "worms", "populous", "kings-quest", "maniac-mansion", "dragons-lair",
                "burgertime", "battleship", "outrun", "zaxxon", "pengo", "agario",
                "gunbound", "doodlejump", "bards-tale", "wasteland", "skifree",
                "rampage", "joust", "asteroids", "centipede", "missile-command",
                "tempest", "marble-madness", "oregon-trail", "paperboy", "tapper",
                "papersplease", "karateka", "berzerk", "robotron", "1942",
                "paneldepon", "kururin", "molemania", "bump-n-jump", "stratego",
                "mastermind",
                "tron-territory", "digdug-tunnel", "asteroids-predict",
                "katamari-growth", "lemmingbrain", "battleship-bayes",
                "missile-intercept", "mastermind-knuth", "paneldepon-chain",
                "1942-formations", "oregon-survival", "taipan-trade", "dicewars-prob",
            }:
                medium_risk.append(entry)
            else:
                lower_risk.append(entry)

        if high_risk:
            print(f"\n    HIGH RISK ({len(high_risk)}):")
            for e in high_risk:
                print(e)
        if medium_risk:
            print(f"\n    MEDIUM RISK ({len(medium_risk)}):")
            for e in medium_risk:
                print(e)
        if lower_risk:
            print(f"\n    LOWER RISK ({len(lower_risk)}):")
            for e in lower_risk:
                print(e)

        print(f"\n  To apply: python3 tools/trademark-cleanup.py --apply")


if __name__ == "__main__":
    main()
