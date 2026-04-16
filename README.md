# Pixel Vault

[![License](https://img.shields.io/badge/license-CONTENT--LICENSE-blue)](CONTENT-LICENSE)
[![Author](https://img.shields.io/badge/by-Joshua%20Ayson-black)](https://joshuaayson.com/projects/)

A rapid prototyping system for discovering new game mechanics. 460 single-HTML-file
experiments, organized by genre lineage, catalogued for pattern discovery. Built by
a human and an AI searching together for something neither could find alone.

**The real intent:** Find something the world has never seen or experienced.
Not just something novel — something amazing. A core interaction that doesn't
have a name yet. It will only take time, work, and tokens.

**Constraint:** Every prototype is one HTML file, under 50KB, zero dependencies,
playable in 5 seconds.

## Quick Start

```bash
# Serve locally (required for game loading and QA dashboard)
python3 -m http.server 8080
# Open http://localhost:8080/index.html                 — Museum gallery
# Open http://localhost:8080/play.html?game=maz-001     — Play Engine (full-screen)
# Open http://localhost:8080/tools/qa-dashboard.html    — QA dashboard

# Generate catalogue + JSON manifest
python3 tools/catalogue-generator.py

# Open any prototype directly
open prototypes/def/def-001-pong.html
```

## Current Status

| Track | Count | Description |
|-------|-------|-------------|
| Base Archetypes | 241 | Classic genre reconstructions (~2600 BCE – 2020s) |
| AI Archaeology | 76 | "What if AI had participated?" — AI concept overlays |
| AI Evolution | 143 | AI as sole designer, evolving from first principles |
| **Total** | **460** | Across 20 series |

**Version:** 1.0.0
**Live:** https://play.joshuaayson.com

---

## QA Workflow

The project uses a systematic QA pipeline to get all 209 games working and polished.

### QA Dashboard

```bash
python3 -m http.server 8080
open http://localhost:8080/tools/qa-dashboard.html
```

The dashboard is the central QA tool. It loads all 209 games and lets you rate each one.

**Status tiers:**

| Key | Status | Meaning | Action Required |
|-----|--------|---------|-----------------|
| `4` | **Certified** | Fully QA'd, approved, production-ready | None — locked in, persists across resets |
| `1` | **OK** | Works correctly, quick check passed | None for now — may need deeper testing later |
| `2` | **Playable** | Functional but has minor issues (speed, balance, boring) | No rush — second-pass polish candidate |
| `3` | **Broken** | Won't start, major bugs, unplayable | Fix needed — export report and send to Claude |

**Keyboard shortcuts (in fullscreen):**
- `4` Certify, `1` OK, `2` Playable, `3` Broken
- `←` `→` Navigate between games
- `Esc` Close fullscreen

**Features:**
- Ratings and notes persist in browser localStorage
- Certified status survives storage resets — never overwritten
- Click stat badges in header to filter by status
- "Re-check" badge appears on games updated since last rating
- Export JSON report for bug-fix handoff

### The Fix Cycle

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  You: Test   │────▶│ You: Export   │────▶│ Claude: Fix  │
│  & Rate      │     │ QA Report    │     │ Broken Games │
└─────────────┘     └──────────────┘     └──────┬──────┘
       ▲                                         │
       │            ┌──────────────┐              │
       └────────────│ Claude: Run  │◀─────────────┘
                    │ gen-timestamps│
                    └──────────────┘
```

1. **You test** — Open dashboard, play games, rate them, add notes
2. **You export** — Click "Export Report", share the JSON file path
3. **Claude fixes** — Reads report, fixes all Broken games in a batch PR
4. **Claude updates timestamps** — `bash tools/gen-timestamps.sh`
5. **You re-check** — Dashboard shows orange "UPDATED" badges on fixed games
6. **Filter to "Re-check"** to see only games that were updated since your last rating
7. **Re-rate** — The badge clears once you re-rate the game

### Resuming a QA Session

Your progress is saved automatically. To resume:

1. Start the server: `python3 -m http.server 8080`
2. Open: `http://localhost:8080/tools/qa-dashboard.html`
3. Your ratings, notes, and certified games are all still there
4. Filter to "Untested" to continue where you left off
5. Filter to "Re-check" to review games fixed since your last session

### QA Reports

Exported reports are JSON with this structure:
```json
{
  "generated": "2026-03-24T...",
  "summary": { "total": 209, "certified": 5, "ok": 30, "playable": 10, "broken": 3, "untested": 161 },
  "games": [
    { "id": "...", "file": "...", "status": "broken", "notes": "blank screen", "certifiedAt": null }
  ]
}
```

---

## Automated Quality Gates

### CI Pipeline (GitHub Actions)

Every push and PR runs:

| Job | What | Blocks PR? |
|-----|------|-----------|
| Structural + Size + Metadata | `test-games.sh`, 50KB limit, metadata blocks | Yes |
| QA + Security Scanners | JS health scan, security patterns | Yes |
| Catalogue Sync | manifest.json freshness | Yes |
| Secret Scanning | Gitleaks | Yes |
| SAST (Semgrep) | OWASP, XSS, injection | Advisory |

### Local QA Tools

```bash
# Pass 1: Automated game health scan
node tools/qa-pass1.js              # Full scan (FATAL/ERROR/WARNING/OK)
node tools/qa-pass1.js --fatal-only # Quick check for showstoppers
node tools/qa-pass1.js --json       # Output qa-report.json

# Security audit
node tools/qa-security.js           # Scan for vulnerabilities
node tools/qa-security.js --fix     # With fix suggestions

# Game test suite (structure, metadata, size)
bash tools/test-games.sh
bash tools/test-games.sh --file=prototypes/maz/maz-001-pacman.html

# Catalogue regeneration
python3 tools/catalogue-generator.py

# Timestamp generation (run after fixing games)
bash tools/gen-timestamps.sh

# Batch UI polish (disclaimers, font smoothing, text contrast)
python3 tools/batch-ui-polish.py
python3 tools/batch-canvas-text.py
```

---

## Three Development Tracks

### Track 1: Base Genre Archetypes (`prototypes/`)

241 classic genre reconstructions across 20 series. Each prototype rebuilds a
foundational mechanic from scratch.

**Series:** ADV (7), ANC (6), DEF (3), FGT (6), FIX (5), HYB (3), MAZ (9),
PHY (7), PLT (11), PUZ (12), RAC (4), RPG (8), SCR (10), SHT (6), SIM (10),
SPT (8), SRV (5), TRP (2)

### Track 2: AI Archaeology (`ai-archaeology/`)

76 experiments asking "What if AI had participated?" Each takes a base archetype
and adds an AI concept visualization overlay. Press `H` to toggle the overlay.

Examples:
- **Ghost Mind** (Pac-Man) — ghost targeting tiles and decision state
- **Block Planner** (Tetris) — heuristic placement scores per position
- **Probe Field** (Minesweeper) — mine probability per cell
- **Deep Think** (Chess) — minimax search tree visualization
- **Flow State** (DDR) — adaptive difficulty with flow channel chart

### Track 3: AI Evolution (`ai-evolution/`)

143 AI-originated experiments where AI is the sole designer. No human ancestor
required: pure AI-first mechanics exploring novel verbs and interactions.
- `new/` series: core mechanic experiments (thread, echo, pulse, fold, swarm...)
- `wld/` and `srv/` variants: interdisciplinary and service-domain concepts

### Info Panel System

Every prototype has a `?` key overlay containing:
- **How to Play** — Controls and tips
- **History & Lineage** — Ancestry chain and creator attribution
- **AI Archaeology** — AI concept connection
- **Educational Notice** — Disclaimer for games based on real titles
- **Classification** — Series, mechanic, what the prototype tests
- **Prototype Notes** — Implementation observations

Press `?` to open, `Escape` to close. Game pauses while open.

---

## Project Structure

```
index.html              # Museum gallery — browse and launch all prototypes
play.html               # Play Engine — full-screen game stage (play.html?game=<id>)
compendium.html         # Historical compendium browser view
manifest.json           # Auto-generated JSON manifest
CATALOGUE.md            # Full catalogue (auto-generated)
qa-report.json          # Latest automated QA scan results

docs/
  COMPENDIUM.md         # Historical research, 70+ creators, 7 AI eras
  DESIGN-CONTRACT.md    # Agent governance constraints
  GAME-DESIGN.md        # DRIFT game design document
  IP-WATCHLIST.md       # Protected IP tracker
  ADR-001 to ADR-012    # Architecture decision records (see Design Documents below)

scripts/
  pv-deploy-play.sh        # Deploy to play.joshuaayson.com (canonical production)
  pv-deploy-staging.sh     # Deploy to staging.joshuaayson.com/pixel-vault/
  pv-deploy-production.sh  # Deploy to joshuaayson.com/pixel-vault/ (legacy path)
  publish.sh            # Alias/helper for production publish
  promote-games-to-public.sh  # Bulk-approve games in manifest.json
  setup-play-infra.sh   # One-time AWS infra setup for play.joshuaayson.com
  publish-config.json   # Local CloudFront distribution IDs (gitignored template)

prototypes/             # Track 1: 241 base genre archetypes
  adv/ anc/ def/ fgt/ fix/ hyb/ maz/ phy/ plt/ puz/
  rac/ rpg/ scr/ sht/ sim/ spt/ srv/ trp/

ai-archaeology/         # Track 2: 76 AI concept overlays
  adv/ anc/ def/ fgt/ hyb/ maz/ phy/ plt/ puz/
  rac/ rpg/ scr/ sht/ sim/ spt/

ai-evolution/           # Track 3: 143 AI-originated experiments (staging only)
  new/ srv/ wld/

tools/
  qa-dashboard.html       # Visual QA testing dashboard
  qa-pass1.js             # Automated game health scanner
  qa-security.js          # Security vulnerability scanner
  qa-timestamps.json      # File modification timestamps for re-check detection
  gen-timestamps.sh       # Regenerate timestamps after fixes
  test-games.sh           # Structural test suite
  catalogue-generator.py  # Manifest + catalogue generator
  batch-ui-polish.py      # Batch disclaimer + CSS + font updates
  batch-canvas-text.py    # Batch canvas text contrast helper
  inject-touch-controls.py     # Touch control layer injection
  touch-controls-template.js   # Reference source for all 10 touch profiles + postMessage bridge

infra/                  # AWS SAM template for leaderboard Lambda functions
```

## Game Development Workflow

### Adding a New Game

```bash
git checkout main && git pull
git checkout -b game/{series}-{number}-{name}

# Create the game file
# Metadata comment block MUST be first line (before <!DOCTYPE>)
# Must be under 50KB, zero external dependencies
# 800x600 canvas, requestAnimationFrame loop
# Info panel with ? key, `if (infoOpen) return;` guard

# Test
bash tools/test-games.sh --file=prototypes/{series}/{series}-{number}-{name}.html

# Commit, push, PR
git add prototypes/{series}/{series}-{number}-{name}.html
git commit -m "feat: add {SERIES}-{NUMBER} {Name} — {mechanic description}"
git push -u origin game/{series}-{number}-{name}
gh pr create --title "feat: {SERIES}-{NUMBER} {Name}"

# After merge: regenerate catalogue
python3 tools/catalogue-generator.py
```

### Naming Convention

`{series}-{number}-{name}.html` — e.g. `def-003-air-puck.html`

Series codes: adv, anc, def, fgt, fix, hyb, maz, new, phy, plt, puz,
rac, rpg, scr, sht, sim, spt, srv, trp, wld

### Metadata Block

Every game file starts with (before `<!DOCTYPE>`):
```html
<!--
PROTOTYPE: name
SERIES: xxx
NUMBER: 000
DATE: YYYY-MM-DD
MECHANIC: one-line description
ANCESTRY: lineage references
CONTROLS: key bindings
STATUS: sketch
VISIBILITY: private
RATING: 1-5
AI-ERA: 0-7 (Era Name)
AI-INSIGHT: AI connection
NOTES: design context
-->
```

---

## Play Engine

**`play.html`** is the dedicated full-screen game stage. All game launches from the gallery route through it.

```
http://localhost:8080/play.html?game=maz-001-pacman   # by game id
http://localhost:8080/play.html?game=maz-001-pacman&diag=1  # with diagnostics overlay
```

**What it does:**
- Pre-play interstitial showing game title, series, controls diagram, ancestry
- Full-viewport game iframe (800×600, integer-scaled to fill the screen)
- Auto-hiding HUD — fades after 3 seconds of play, reappears on tap/mouse-move
- Host-side `#touch-strip` rendered **outside** the game iframe (never scaled with the game)
- `postMessage` bridge dispatches `PV_KEY` events to the game iframe — games don't need to know they're in play.html
- `sessionStorage` key `pv-gallery-state` saves gallery scroll position for the Back button
- Double-Esc (desktop) confirms exit; single tap on touch

**Navigation behavior:**
- Desktop: gallery card click → same-tab navigation to play.html, Back returns to gallery
- Mobile: gallery card click → new tab (preserves gallery state on the parent tab)

**Diagnostics:** `?diag=1` shows frame timing, jank count, and scale factor overlay.

### Mobile Architecture

**The problem (old behavior):** Games opened inside a CSS-scaled modal iframe at ~48% of their natural 800px width on a 390px phone. Touch controls injected inside the iframe were equally scaled — tiny tap targets overlapping gameplay. Browser chrome (address bar + toolbar) stole another ~100px.

**The solution (play.html):** play.html owns the full viewport. The `#touch-strip` D-pad/buttons live in the host page, outside the iframe, and are never scaled. `postMessage({type:'PV_KEY', key:' '})` delivers key events into the game. The game iframe does not know it is on mobile.

```
┌─ play.html (full viewport) ─────────────────────────────────────────┐
│  ┌─ #game-stage (full width, integer-scaled canvas) ─────────────┐ │
│  │  game iframe loads here                                        │ │
│  └────────────────────────────────────────────────────────────────┘ │
│  ┌─ #touch-strip (host-side, outside iframe) ─────────────────────┐ │
│  │  [← ↑ ↓ →]    [A] [B]    full-size tap targets               │ │
│  └────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘
```

See [ADR-012](docs/ADR-012-gameplay-experience-engine.md) for the full specification.

---

## Touch Controls

10 control profiles are injected into game HTML files via `tools/inject-touch-controls.py`. The template source is `tools/touch-controls-template.js`.

**Profiles:** d4 (4-direction), d8 (8-direction), dpad-ab (movement + action), fire (shoot), jump, rotate-thrust, paddle, paddle-2p, mouse-target, swipe.

**postMessage bridge** (added in Play Engine phase): when a game is loaded inside play.html, the host page sends `{type:'PV_KEY', key:'ArrowLeft'}` messages. The injected template listens for these and fires the same synthetic key events. If the host is providing its own touch controls, it also sends `{type:'PV_HOST_CONTROLS', active:true}` to hide the in-game touch layer.

**Re-injection workflow** (after changing `touch-controls-template.js`):
```bash
python3 tools/inject-touch-controls.py   # re-injects all eligible games
bash tools/gen-timestamps.sh              # mark all updated for QA re-check
```

---

## Deployment

Pixel Vault is a fully self-contained repo. Deployment is independent — the deploy scripts, S3 buckets, and CloudFront distributions are owned entirely by this project.

### Three deploy targets

| Script | Target URL | Audience | ai-evolution |
|--------|-----------|----------|-------------|
| `scripts/pv-deploy-play.sh` | `play.joshuaayson.com` | Public internet | ✗ gated |
| `scripts/pv-deploy-production.sh` | `joshuaayson.com/pixel-vault/` | Public internet (legacy) | ✗ gated |
| `scripts/pv-deploy-staging.sh` | `staging.joshuaayson.com/pixel-vault/` | Password-protected preview | ✓ included |

### Standard deploy workflow

```bash
# 1. Regenerate manifest after adding/changing games
python3 tools/catalogue-generator.py

# 2. Test structural + CI checks locally
bash tools/test-games.sh

# 3. Deploy to staging first (always test before production)
bash scripts/pv-deploy-staging.sh
# Staging password: set STAGING_PASSWORD env var
# Preview at: https://staging.joshuaayson.com/pixel-vault/

# 4. Deploy to canonical production (requires typing YES)
bash scripts/pv-deploy-play.sh
# Live at: https://play.joshuaayson.com
```

### Per-game approval gate

Games ship to production only if all three conditions are met:
1. `track` is `archetype` or `ai-archaeology` (ai-evolution never ships)
2. `visibility: public` in `manifest.json`
3. `status` is not `broken`

```bash
# Quick-approve all non-broken archetypes and ai-archaeology games
python3 tools/promote-games-to-public.py

# Or manually edit manifest.json and set "visibility": "public" per game
```

### Environment variables

| Variable | Used in | Description |
|----------|---------|-------------|
| `PV_PLAY_CF_DISTRIBUTION` | `pv-deploy-play.sh` | CloudFront distribution ID for play.joshuaayson.com |
| `STAGING_PASSWORD` | `pv-deploy-staging.sh` | Password injected into staging gate |

Set IDs in `scripts/publish-config.json` (copy from `scripts/publish-config.example.json`).

---

## Design Documents

- [COMPENDIUM.md](docs/COMPENDIUM.md) — Historical research: 70+ creators, genre lineage, AI convergence
- [DESIGN-CONTRACT.md](docs/DESIGN-CONTRACT.md) — Agent constraints and governance
- [GAME-DESIGN.md](docs/GAME-DESIGN.md) — DRIFT full game design spec
- [ADR-001](docs/ADR-001-game-concept.md) — Classic arcade mechanics, DRIFT concept
- [ADR-002](docs/ADR-002-novel-genre-exploration.md) — Novel genre verbs
- [ADR-003](docs/ADR-003-game-archaeology-and-rapid-prototyping.md) — Game archaeology, rapid prototyping
- [ADR-004](docs/ADR-004-ai-archaeology-layer.md) — AI archaeology layer, H-key overlay system
- [ADR-005](docs/ADR-005-mobile-support-strategy.md) — Mobile support strategy, touch control profiles
- [ADR-006](docs/ADR-006-leaderboard-security-ops.md) — Leaderboard security and ops
- [ADR-007](docs/ADR-007-srv-service-dispatch.md) — SRV service/dispatch series
- [ADR-008](docs/ADR-008-monetization-implementation.md) — Monetization strategy
- [ADR-009](docs/ADR-009-community-publishing-pipeline.md) — Community publishing pipeline
- [ADR-010](docs/ADR-010-ip-legal-code-sharing.md) — IP, legal, and code sharing
- [ADR-011](docs/ADR-011-public-site-architecture.md) — Public site architecture, play.joshuaayson.com, deployment pipeline
- [ADR-012](docs/ADR-012-gameplay-experience-engine.md) — Gameplay Experience Engine: play.html, mobile-first full-screen play, postMessage touch bridge

## Tech

Single HTML files. Vanilla JavaScript. HTML5 Canvas. Web Audio API. Zero dependencies.
Every game must be under 50KB and playable in 5 seconds.

---

**Project:** Pixel Vault
**Author:** Joshua Ayson / OA LLC
**Version:** 1.0.0

---

## License

Dual-licensed:

- **Engine** (`templates/`, `tools/`) — [GPL-3.0-or-later](LICENSE)
- **Game content** (`prototypes/`, `ai-archaeology/`, `ai-evolution/`) — [CC BY-NC-SA 4.0](CONTENT-LICENSE)

See [LICENSE](LICENSE) and [CONTENT-LICENSE](CONTENT-LICENSE) for details.
