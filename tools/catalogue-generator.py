#!/usr/bin/env python3
"""
catalogue-generator.py — Scan all prototype HTML files and generate CATALOGUE.md + manifest.json

Reads the metadata comment block from each .html file in prototypes/ and refined/,
then produces a sorted, formatted catalogue document and a JSON manifest for the gallery.

Usage:
    python3 tools/catalogue-generator.py              # Full catalogue (all prototypes)
    python3 tools/catalogue-generator.py --public     # Public catalogue only (visibility: public)
"""
from pathlib import Path
import json
import re
import sys
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROTOTYPES_DIR = PROJECT_ROOT / "prototypes"
AI_ARCHAEOLOGY_DIR = PROJECT_ROOT / "ai-archaeology"
AI_EVOLUTION_DIR = PROJECT_ROOT / "ai-evolution"
REFINED_DIR = PROJECT_ROOT / "refined"
OUTPUT_FILE = PROJECT_ROOT / "CATALOGUE.md"
OUTPUT_PUBLIC = PROJECT_ROOT / "CATALOGUE-PUBLIC.md"
OUTPUT_MANIFEST = PROJECT_ROOT / "manifest.json"

SERIES_NAMES = {
    "adv": "Adventure",
    "anc": "Ancient Games",
    "def": "Deflection / Paddle",
    "fgt": "Fighting / Combat",
    "fix": "Fixed-Position Shooters",
    "hyb": "Cross-Lineage Hybrids",
    "maz": "Maze + Chase",
    "new": "Novel Mechanics",
    "phy": "Physics / Inertia",
    "plt": "Platformer",
    "puz": "Puzzle / Falling Block",
    "rac": "Racing / Driving",
    "rpg": "Role-Playing",
    "scr": "Scrolling / Shmup",
    "sht": "Twin-Stick / Arena Shooter",
    "sim": "Simulation",
    "spt": "Sports",
    "srv": "Service / Dispatch",
    "trp": "Trap / Terrain",
    "wld": "Wild Experiments",
}


def parse_metadata(filepath: Path) -> dict[str, str]:
    """Extract metadata fields from HTML comment block or JS comment block."""
    content = filepath.read_text(errors="replace")
    meta = {}

    # Try HTML comment block: <!-- ... -->
    match = re.search(r"<!--(.*?)-->", content, re.DOTALL)
    if match:
        block = match.group(1)
        for line in block.strip().splitlines():
            line = line.strip()
            if ":" in line:
                key, _, value = line.partition(":")
                key = key.strip().upper()
                value = value.strip()
                if key and value and value != "[" + key.lower() + "]":
                    meta[key] = value

    # Also try JS-style metadata: // @key value
    for match in re.finditer(r"//\s*@(\w+)\s+(.+)", content):
        key = match.group(1).strip().upper()
        value = match.group(2).strip()
        if key and value and key not in meta:
            meta[key] = value

    # Normalize: map both NAME and PROTOTYPE to PROTOTYPE
    if "NAME" in meta and "PROTOTYPE" not in meta:
        meta["PROTOTYPE"] = meta["NAME"]

    # Default visibility to private
    if "VISIBILITY" not in meta:
        meta["VISIBILITY"] = "private"

    return meta


def star_display(rating_str: str) -> str:
    """Convert rating string to star display."""
    try:
        num = int(re.search(r"\d", rating_str).group())
        return "\u2605" * num + "\u2606" * (5 - num)
    except (AttributeError, ValueError):
        return rating_str


def scan_directory(base_dir: Path) -> list[dict]:
    """Scan a directory tree for .html files with metadata."""
    results = []
    if not base_dir.exists():
        return results

    for html_file in sorted(base_dir.rglob("*.html")):
        meta = parse_metadata(html_file)
        if not meta:
            continue

        # Infer series from parent directory name or filename
        series = meta.get("SERIES", html_file.parent.name).lower()
        meta["_file"] = html_file.relative_to(PROJECT_ROOT)
        meta["_series"] = series
        results.append(meta)

    return results


def generate_catalogue(public_only: bool = False) -> str:
    """Generate the full catalogue markdown."""
    archetypes = scan_directory(PROTOTYPES_DIR)
    ai_arch = scan_directory(AI_ARCHAEOLOGY_DIR)
    ai_evo = scan_directory(AI_EVOLUTION_DIR)
    refined = scan_directory(REFINED_DIR)

    # Tag each item with its track
    for item in archetypes:
        item["_track"] = "archetype"
    for item in ai_arch:
        item["_track"] = "ai-archaeology"
    for item in ai_evo:
        item["_track"] = "ai-evolution"
    for item in refined:
        item["_track"] = "refined"

    all_items = archetypes + ai_arch + ai_evo + refined

    # Filter by visibility if generating public catalogue
    if public_only:
        all_items = [
            item for item in all_items
            if item.get("VISIBILITY", "private").lower() == "public"
        ]

    # Count by series
    series_counts: dict[str, int] = {}
    promising: list[dict] = []

    for item in all_items:
        s = item.get("_series", "???")
        series_counts[s] = series_counts.get(s, 0) + 1

        rating_str = item.get("RATING", "")
        if any(c in rating_str for c in ["4", "5", "\u2605\u2605\u2605\u2605"]):
            promising.append(item)

    total = len(all_items)
    counts_str = " ".join(
        f"{k.upper()}({v})" for k, v in sorted(series_counts.items())
    )

    title = "Pixel Vault — Public Catalogue" if public_only else "Pixel Vault Catalogue"

    # Count by track
    n_arch = sum(1 for it in all_items if it.get("_track") == "archetype")
    n_ai_arch = sum(1 for it in all_items if it.get("_track") == "ai-archaeology")
    n_ai_evo = sum(1 for it in all_items if it.get("_track") == "ai-evolution")
    n_refined = sum(1 for it in all_items if it.get("_track") == "refined")

    lines = [
        f"# {title}",
        "",
        f"**Last Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Total Prototypes:** {total}",
        f"**Archetypes:** {n_arch} | **AI Archaeology:** {n_ai_arch} | **AI Evolution:** {n_ai_evo} | **Refined:** {n_refined}",
        f"**By Series:** {counts_str}",
        f"**Promising (4-5 stars):** {len(promising)}",
        "",
    ]

    # --- ARCHETYPES ---
    lines.append("---")
    lines.append("")
    lines.append("## Base Genre Archetypes")
    lines.append("")
    lines.append("Classic genre reconstructions — the human timeline of game evolution.")
    lines.append("")

    def emit_track(track_items: list[dict], header_lines: list[str]) -> None:
        """Emit a grouped-by-series table for a set of items."""
        grouped: dict[str, list[dict]] = {}
        for item in track_items:
            s = item.get("_series", "unknown")
            grouped.setdefault(s, []).append(item)

        for series_code in sorted(grouped.keys()):
            items = grouped[series_code]
            name = SERIES_NAMES.get(series_code, series_code.upper())
            header_lines.append(f"### {series_code.upper()} -- {name}")
            header_lines.append("")
            header_lines.append(
                "| # | Name | Mechanic | Rating | AI Era | AI Insight | Status | Notes |"
            )
            header_lines.append(
                "|---|------|----------|--------|--------|------------|--------|-------|"
            )
            for item in items:
                num = item.get("NUMBER", "?")
                pname = item.get("PROTOTYPE", "untitled")
                mechanic = item.get("MECHANIC", "?")
                rating = star_display(item.get("RATING", "?"))
                ai_era = item.get("AI-ERA", "—")
                ai_insight = item.get("AI-INSIGHT", "—")
                if len(ai_insight) > 80:
                    ai_insight = ai_insight[:77] + "..."
                status = item.get("STATUS", "?")
                notes = item.get("NOTES", "")
                header_lines.append(
                    f"| {num} | {pname} | {mechanic} | {rating} | {ai_era} | {ai_insight} | {status} | {notes} |"
                )
            header_lines.append("")

    # Emit archetypes
    arch_items = [it for it in all_items if it.get("_track") == "archetype"]
    emit_track(arch_items, lines)

    # --- AI ARCHAEOLOGY ---
    ai_arch_items = [it for it in all_items if it.get("_track") == "ai-archaeology"]
    if ai_arch_items:
        lines.append("---")
        lines.append("")
        lines.append("## AI Archaeology")
        lines.append("")
        lines.append("\"What if AI had participated?\" — variants that reimagine classic games through the AI lens.")
        lines.append("")
        emit_track(ai_arch_items, lines)

    # --- AI EVOLUTION ---
    ai_evo_items = [it for it in all_items if it.get("_track") == "ai-evolution"]
    if ai_evo_items:
        lines.append("---")
        lines.append("")
        lines.append("## AI Evolution")
        lines.append("")
        lines.append("How AI would evolve games independently — the machine timeline.")
        lines.append("")
        emit_track(ai_evo_items, lines)

    # --- REFINED ---
    ref_items = [it for it in all_items if it.get("_track") == "refined"]
    if ref_items:
        lines.append("---")
        lines.append("")
        lines.append("## Refined Prototypes")
        lines.append("")
        lines.append("Promoted prototypes receiving polish.")
        lines.append("")
        emit_track(ref_items, lines)

    # Promising prototypes
    if promising:
        lines.append("---")
        lines.append("")
        lines.append("## Promising Prototypes")
        lines.append("")
        lines.append("| Series | # | Name | Rating | Refined? |")
        lines.append("|--------|---|------|--------|----------|")
        for item in promising:
            s = item.get("_series", "?").upper()
            num = item.get("NUMBER", "?")
            pname = item.get("PROTOTYPE", "untitled")
            rating = star_display(item.get("RATING", "?"))
            is_refined = "yes" if str(item.get("_file", "")).startswith("refined") else "no"
            lines.append(f"| {s} | {num} | {pname} | {rating} | {is_refined} |")
        lines.append("")

    # AI Archaeology Summary
    ai_items = [it for it in all_items if it.get("AI-ERA")]
    if ai_items:
        era_groups: dict[str, list[dict]] = {}
        for item in ai_items:
            era_raw = item.get("AI-ERA", "")
            era_key = era_raw.split("(")[0].strip()  # "2" or "3-4"
            era_groups.setdefault(era_key, []).append(item)

        lines.append("---")
        lines.append("")
        lines.append("## AI Archaeology Summary")
        lines.append("")
        lines.append("### Prototypes by AI Era")
        lines.append("")
        for era_key in sorted(era_groups.keys()):
            era_items = era_groups[era_key]
            era_full = era_items[0].get("AI-ERA", era_key)
            lines.append(f"**Era {era_key}** \u2014 {era_full}")
            for it in era_items:
                code = (
                    f"{it.get('_series', '?').upper()}-{it.get('NUMBER', '?')} "
                    f"{it.get('PROTOTYPE', '?')}"
                )
                insight = it.get("AI-INSIGHT", "")
                lines.append(f"- `{code}` \u2014 {insight}")
            lines.append("")

        lines.append("### Game-First AI Discoveries")
        lines.append("")
        lines.append("Games that invented AI concepts before the field formalized them:")
        lines.append("")
        lines.append("| Game | Discovered Concept | Formalized By AI (~Year) |")
        lines.append("|------|--------------------|--------------------------|")
        game_discoveries = [
            ("Pac-Man (1980)", "Multi-agent behavioral policies (ghost personalities)", "MARL theory (~2000)"),
            ("Space Invaders (1978)", "Emergent curriculum learning (speedup-as-fewer-enemies)", "Curriculum Learning (~2015)"),
            ("Defender (1981)", "Partial observability + minimap dimensionality reduction", "Practical POMDPs (~1990s)"),
            ("Pong (1972)", "Specialization over generality (Y-tracker opponent)", "Narrow AI consensus (~1990s)"),
            ("Tetris (1985)", "Real-time NP-hard heuristic spatial reasoning", "Active research area (ongoing)"),
            ("Mario Bros (1985)", "Reward shaping via level design", "Reward shaping in RL (~1999)"),
            ("Asteroids (1979)", "Exploration-exploitation via action consequences", "RL formalization (~1980s-1990s)"),
            ("Qix (1981)", "Territorial control as multi-armed bandit", "Spatial bandit theory (~1985+)"),
        ]
        for game, concept, formalized in game_discoveries:
            lines.append(f"| {game} | {concept} | {formalized} |")
        lines.append("")
        lines.append(f"**Convergence Points Documented:** {len(ai_items)} prototypes")
        lines.append(f"**Game-First Discoveries:** {len(game_discoveries)}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"*Generated by `tools/catalogue-generator.py`*")

    return "\n".join(lines)


def generate_manifest() -> list[dict]:
    """Generate a JSON manifest of all prototypes for the gallery."""
    archetypes = scan_directory(PROTOTYPES_DIR)
    ai_arch = scan_directory(AI_ARCHAEOLOGY_DIR)
    ai_evo = scan_directory(AI_EVOLUTION_DIR)
    refined = scan_directory(REFINED_DIR)

    for item in archetypes:
        item["_track"] = "archetype"
    for item in ai_arch:
        item["_track"] = "ai-archaeology"
    for item in ai_evo:
        item["_track"] = "ai-evolution"
    for item in refined:
        item["_track"] = "refined"

    all_items = archetypes + ai_arch + ai_evo + refined
    manifest = []

    for item in all_items:
        entry = {
            "id": f"{item.get('_series', 'unk')}-{item.get('NUMBER', '000')}-{item.get('PROTOTYPE', 'untitled')}",
            "name": item.get("PROTOTYPE", "untitled"),
            "series": item.get("_series", "unknown"),
            "seriesName": SERIES_NAMES.get(item.get("_series", ""), item.get("_series", "unknown")),
            "number": item.get("NUMBER", "000"),
            "track": item.get("_track", "unknown"),
            "file": str(item.get("_file", "")),
            "date": item.get("DATE", ""),
            "mechanic": item.get("MECHANIC", ""),
            "ancestry": item.get("ANCESTRY", ""),
            "controls": item.get("CONTROLS", ""),
            "status": item.get("STATUS", "sketch"),
            "visibility": item.get("VISIBILITY", "private"),
            "rating": item.get("RATING", ""),
            "aiEra": item.get("AI-ERA", ""),
            "aiInsight": item.get("AI-INSIGHT", ""),
            "notes": item.get("NOTES", ""),
        }
        manifest.append(entry)

    return manifest


def main() -> None:
    """Generate and write the catalogue file and manifest."""
    public_only = "--public" in sys.argv

    catalogue = generate_catalogue(public_only=public_only)
    output = OUTPUT_PUBLIC if public_only else OUTPUT_FILE
    output.write_text(catalogue)

    # Always generate manifest
    manifest = generate_manifest()
    manifest_data = {
        "generated": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "version": "0.5.0",
        "prototypes": manifest,
    }
    OUTPUT_MANIFEST.write_text(json.dumps(manifest_data, indent=2))

    mode = "PUBLIC" if public_only else "FULL"
    print(f"Catalogue ({mode}) written to {output}")
    print(f"Manifest written to {OUTPUT_MANIFEST} ({len(manifest)} prototypes)")
    print(f"  Scanned: {PROTOTYPES_DIR}")
    print(f"  Scanned: {AI_ARCHAEOLOGY_DIR}")
    print(f"  Scanned: {AI_EVOLUTION_DIR}")
    print(f"  Scanned: {REFINED_DIR}")
    if public_only:
        print("  Filtered: visibility=public only")


if __name__ == "__main__":
    main()
