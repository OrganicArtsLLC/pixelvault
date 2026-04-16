"""Batch promote all rating:4 archetype games to the public games/ directory."""
import json
import shutil
import pathlib
import datetime

REPO = pathlib.Path(__file__).parent.parent
GAMES_DIR = REPO / "games"
GAMES_DIR.mkdir(exist_ok=True)

with open(REPO / "manifest.json") as f:
    data = json.load(f)
protos = data if isinstance(data, list) else data.get("prototypes", [])

with open(REPO / "promoted-manifest.json") as f:
    promoted = json.load(f)
promoted_ids = {p["id"] for p in promoted.get("prototypes", [])}

track_filter = "archetype"
candidates = [
    p for p in protos
    if str(p.get("rating", "")) == "4"
    and p.get("track") == track_filter
    and p.get("id") not in promoted_ids
]

success, skipped = [], []

for p in candidates:
    game_id = p["id"]
    src_file = REPO / p["file"]
    dst_file = GAMES_DIR / f"{game_id}.html"

    if not src_file.exists():
        skipped.append((game_id, "source not found"))
        continue

    shutil.copy2(src_file, dst_file)

    entry = dict(p)
    entry["file"] = f"games/{game_id}.html"
    promoted["prototypes"].append(entry)
    promoted_ids.add(game_id)
    success.append(game_id)

promoted["generated"] = datetime.datetime.utcnow().isoformat() + "Z"
promoted["totalGames"] = len(promoted["prototypes"])

with open(REPO / "promoted-manifest.json", "w") as f:
    json.dump(promoted, f, indent=2)

print(f"Promoted: {len(success)}")
print(f"Skipped:  {len(skipped)}")
if skipped:
    for sid, reason in skipped[:20]:
        print(f"  SKIP {sid}: {reason}")
print(f"Total in manifest: {promoted['totalGames']}")
