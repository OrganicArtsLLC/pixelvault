# ⚠️ games/ — LEGACY FLAT MIRROR — DO NOT EDIT

This directory is a **legacy flat mirror** of `prototypes/{series}/`. It is **not the deploy source** and is **not read by the deploy script**.

## Source of Truth

All game files that appear on play.joshuaayson.com come from:

- `prototypes/{series}/filename.html` — base archetypes
- `ai-archaeology/{series}/filename.html` — AI overlay variants

The deploy script (`scripts/pv-deploy-play.sh`) copies files based on `manifest.json`, where every game's `"file"` field points to `prototypes/series/filename.html`. Files in `games/` are never copied to S3.

## Finding the Correct File to Edit

```bash
# Look up the canonical path for any game by its ID:
python3 -c "import json; m=json.load(open('manifest.json')); \
  game_id='maz-001'; \
  print(next(g['file'] for g in m['prototypes'] if game_id in g['file']))"
```

Or just use the series subdirectory directly:
```
prototypes/maz/maz-001-pacman.html
prototypes/def/def-003-air-puck.html
prototypes/sim/sim-006-lane-battle.html
```

## History

`games/` was originally maintained as a flat working copy (~206 files). All new prototypes are created directly in `prototypes/{series}/` and are NOT reflected here. Do not add new files here; do not rely on this directory for anything.
