# Pixel Vault — Design Contract

**Authoritative agent guidance, architecture rules, and creative governance for the Pixel Vault project.**

> This document is the single source of truth for how Pixel Vault is built, extended, and maintained. An AI agent should read this file before taking any action on the project. Every rule here represents a deliberate decision, not a default. If the rule is wrong, change it here first, then propagate.

---

**Version:** 1.0.0
**Last Updated:** 2026-03-22
**Project Path:** `pixelvault/`
**Status:** Active

---

## Table of Contents

1. [Project Identity](#1-project-identity)
2. [File Architecture Rules](#2-file-architecture-rules)
3. [Prototype Conventions](#3-prototype-conventions)
4. [Series Registry](#4-series-registry)
5. [METADATA Block Specification](#5-metadata-block-specification)
6. [Mobile Touch Layer](#6-mobile-touch-layer)
7. [Gallery and Manifest Rules](#7-gallery-and-manifest-rules)
8. [Creative Evaluation Framework](#8-creative-evaluation-framework)
9. [Track Definitions](#9-track-definitions)
10. [Toolchain](#10-toolchain)
11. [Versioning and Changelog Protocol](#11-versioning-and-changelog-protocol)
12. [Agent Decision Rules](#12-agent-decision-rules)
13. [Roadmap and Phase Status](#13-roadmap-and-phase-status)

---

## 1. Project Identity

| Field | Value |
|---|---|
| **Name** | Pixel Vault |
| **Tagline** | Every mechanic. One file. No dependencies. |
| **Mission** | Systematically prototype and preserve every fundamental game mechanic in its smallest possible form. |
| **Audience** | Children aged 8–14 (primary), parents, students, retro gaming enthusiasts |
| **Format** | Single HTML files — open in a browser, play immediately, no install |
| **Origin** | Archival and design research project, started 2026 |

### What Pixel Vault Is

Pixel Vault is a **mechanic museum and rapid prototyping system**. Each prototype isolates one game mechanic, traces its lineage, and provides a playable implementation under 50KB. The collection is organized by genre series (like taxonomy) and displayed through a self-contained browser gallery.

The museum aspect is as important as the game aspect. Every prototype has documented ancestry (real arcade titles), an AI-era designation, and a design insight. Pixel Vault is not just games — it is annotated game history in runnable form.

### What Pixel Vault Is Not

- Not a game engine or framework
- Not a commercial product (currently private/educational)
- Not a place for full-featured games
- Not a JavaScript library

---

## 2. File Architecture Rules

These rules are **hard constraints**. Violating them breaks the museum model.

### Hard Rules (Never Break)

| Rule | Constraint |
|---|---|
| **Single-file** | Every prototype must be one `.html` file. No external JS, CSS, or asset files. |
| **Size limit** | Each prototype must stay under **50KB** (51,200 bytes). Current max is ~27KB — there is headroom. |
| **Zero dependencies** | No CDN links, no `<script src="">` to external resources, no npm. |
| **Self-contained** | The file must be playable by double-clicking it in a file manager with no internet. |
| **Canvas-based** | All games use `<canvas>`. No DOM-manipulation games. |
| **Target resolution** | 800×600 logical pixels (enforced in CSS, not just JS). |
| **60fps target** | All games use `requestAnimationFrame` loop. No `setInterval` animation. |

### File Structure Within Each HTML File

```html
<!-- HTML comment METADATA block (always first, lines 1-15 approx) -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Game Name]</title>
  <style>
    /* Reset + canvas centering */
    /* Game-specific styles */
    /* Touch button styles (injected by tool) */
  </style>
</head>
<body>
  <canvas id="c"></canvas>
  <script>
    /* All game logic */
    loop();
  </script>
  <script>
    /* ── Pixel Vault Touch Layer v1.0 — profile: [name] ── */
    /* (injected by tools/inject-touch-controls.py) */
  </script>
</body>
</html>
```

### Directory Structure

```
pixelvault/
├── docs/                       ← documentation (ADRs, design docs, research)
│   ├── DESIGN-CONTRACT.md      ← this file
│   ├── ADR-001 through ADR-005 ← architecture decision records
│   ├── COMPENDIUM.md           ← historical research document
│   ├── GAME-DESIGN.md          ← game design document (DRIFT)
│   └── IP-WATCHLIST.md         ← IP tracking (private)
├── README.md                   ← human overview (version-tracked)
├── CATALOGUE.md                ← auto-generated, don't edit by hand
├── CATALOGUE-PUBLIC.md         ← public-safe version (no private entries)
├── manifest.json               ← auto-generated, read by index.html
├── index.html                  ← gallery/museum viewer
├── prototypes/                 ← all archetype and working prototypes
│   ├── [series-code]/
│   │   ├── README.md           ← series description
│   │   └── [ser-###-name].html
├── ai-archaeology/             ← AI-enhanced variants (do not mix with prototypes/)
│   └── [series-code]/
│       └── [ser-###-name].html
├── ai-evolution/               ← emerging AI-first experiments
└── tools/
    ├── catalogue-generator.py
    ├── dev-server.sh           ← local dev server with pre-flight validation
    ├── inject-touch-controls.py
    ├── test-games.sh           ← structural + security test runner
    └── touch-controls-template.js
```

---

## 3. Prototype Conventions

### File Naming

Format: `[series-code]-[number]-[name].html`

- `series-code` — 3-letter lowercase abbreviation (see Section 4)
- `number` — zero-padded 3-digit integer: `001`, `002`, etc.
- `name` — lowercase, letters only, slug form (no hyphens in name part)

Examples: `def-001-pong.html`, `fix-001-invaders.html`, `puz-001-tetris.html`

### Series Directory

Each series lives in `prototypes/[series-code]/`. New series requires:
1. Create directory
2. Create `README.md` in that directory (one paragraph describing the series)
3. Register in Section 4 of this document
4. Add an entry in `ADR-00X` if the series represents a new architectural direction

### Number Gap Policy

Number gaps are **allowed**. If `def-001` and `def-003` exist with no `def-002`, that's fine — it means a prototype was retired. Do not renumber existing prototypes to close gaps.

---

## 4. Series Registry

All active series codes. A series is a genre lineage — all prototypes in a series share a fundamental mechanic ancestry.

| Code | Full Name | Mechanic Archetype | Status |
|------|-----------|-------------------|--------|
| `def` | Deflection | Ball bounced by paddle or surface | Active — 2 prototypes |
| `fgt` | Fighter | Two entities in direct combat | Active — 1 prototype |
| `fix` | Fixed Shooter | Stationary base shoots ascending threats | Active — 1 prototype |
| `maz` | Maze | Navigate a closed grid or tunnel system | Active — 1 prototype |
| `phy` | Physics | Newtonian simulation, inertia-based control | Active — 1 prototype |
| `plt` | Platform | Gravity + lateral movement, avoid falls | Active — 1 prototype |
| `puz` | Puzzle | Placement, pattern, spatial logic | Active — 1 prototype |
| `rac` | Racing | Forward movement, path selection, speed | Active — 1 prototype |
| `scr` | Scroller | Forward-scrolling environment with threats | Active — 1 prototype |
| `sht` | Shooter | Omnidirectional fire, free movement | Active — 1 prototype |
| `trp` | Trapper | Territory capture, line drawing, area control | Active — 1 prototype |
| `adv` | Adventure | Room exploration, puzzles, inventory management | Active — 0 prototypes |
| `rpg` | Role-Playing | Stats, combat, progression, exploration | Active — 0 prototypes |
| `spt` | Sports | Athletic mechanics, physics-based competition | Active — 0 prototypes |
| `sim` | Simulation | Economy, trading, resource management | Active — 0 prototypes |
| `anc` | Ancestor | Pre-Pong era mechanics (experimental) | Reserved — no prototypes yet |
| `hyb` | Hybrid | Deliberate mechanic crossbreeding | Reserved — no prototypes yet |
| `new` | New Concept | Mechanics without historical arcade precedent | Reserved — no prototypes yet |
| `srv` | Service / Dispatch | Multi-lane timing delivery and return acknowledgement | Active — 3 prototypes (SRV-001, SRV-002, SRV-003) |
| `wld` | World / Sim | Simulation, ecosystem, emergent systems | Reserved — no prototypes yet |

### Adding a New Series

1. Confirm it doesn't fit any existing series (discuss with agent first)
2. Create `prototypes/[code]/README.md`
3. Add row to table above
4. Commit: `docs: register [code] series in DESIGN-CONTRACT`

---

## 5. METADATA Block Specification

Every prototype file **must** begin with an HTML comment containing structured metadata. This block is parsed by `catalogue-generator.py`.

### Format

```html
<!--
PROTOTYPE: [name]          — slug, lowercase, matches filename name segment
SERIES: [code]             — 3-letter code from Series Registry
NUMBER: [###]              — zero-padded integer
DATE: [YYYY-MM-DD]         — date first created

MECHANIC: [verb phrase]    — core mechanic in 8 words or fewer
ANCESTRY: [title (year), title (year)]  — 2-4 real arcade/console titles this descends from
STATUS: [sketch|refine|archive]         — sketch=first pass, refine=polished, archive=retired
VISIBILITY: [private|public]            — private=internal only, public=shareable
RATING: [1-5]              — 1=barely works, 3=fun, 5=exemplary mechanic capture

AI-ERA: [1-7]              — era number from Compendium AI timeline (see below)
AI-INSIGHT: [1 sentence]   — what this prototype reveals about AI history

NOTES: [free text]         — 1-3 sentences, design observations, not instructions
-->
```

### AI Era Reference

| Era | Name | Dates |
|-----|------|-------|
| 1 | Symbolic AI | 1950–1965 |
| 2 | Expert Systems | 1965–1980 |
| 3 | Knowledge Explosion | 1980–1997 |
| 4 | Statistical Learning | 1997–2012 |
| 5 | Deep Learning | 2012–2020 |
| 6 | Transformer Era | 2020–2024 |
| 7 | Agentic AI | 2024–present |

### Rules

- All fields except `NOTES` are required
- `ANCESTRY` must reference **real historical titles**, not fictional ones
- `MECHANIC` should be a verb phrase: "deflect ball", "suppress advancing formation", not a noun
- This block must be the **first thing in the file** before `<!DOCTYPE html>`
- Do not add fields not in this specification without updating this contract

---

## 6. Mobile Touch Layer

### Strategy

Touch controls are **built into each game file**, not served as a separate system. The touch layer is injected before `</body>` via `tools/inject-touch-controls.py`. The layer uses a touch-to-keyboard translation pattern: finger gestures dispatch synthetic `KeyboardEvent`s that the existing game logic handles natively.

This approach means:
- Zero changes to game logic when adding touch
- Touch controls are invisible on desktop
- Every game remains a single self-contained file

### How It Works

```
Touch press → TouchEvent → handler → document.dispatchEvent(KeyboardEvent)
                                          ↓
                              Game's existing keydown listener fires
                              (game is unmodified)
```

The dispatched event sets BOTH `code` AND `key` properties and uses `bubbles: true`, which covers:
- **Cluster A games** (e.code + window listener): pong, breakout, invaders, asteroids, pacman, qix, defender, runner, tetris
- **Cluster B games** (e.key + document listener): joust, racer, robotron

### Control Profiles

Each game is assigned one profile. The profile defines which touch buttons appear and what keys they fire.

| Profile | Left Side | Right Side | Games |
|---------|-----------|-----------|-------|
| `dpad2+fire` | ← → | ⊙ Space | breakout, invaders |
| `dpad4` | 4-way arrows | — | pacman, racer |
| `dpad4+hold` | 4-way arrows | ▶▶ Space (hold) | qix |
| `asteroids` | 4-way arrows (↑=thrust) | ⊙ Space | asteroids |
| `defender` | 4-way arrows | ⊙ Space + ✦ Z | defender |
| `runner` | ← → | ↑ Space (held) | runner |
| `joust` | ← → | ▲ Space | joust |
| `pong` | W/S (P1) | ↑↓ (P2) + Space serve | pong |
| `tetris` | 4-way arrows | ↻ ↑  ↺ Z  ⬇ Space | tetris |
| `twin-stick` | WASD move | ↑↓←→ aim | robotron |

### Visual Specification

- Button size: 52px minimum (WCAG 2.5.5 touch target)
- Overlay position: fixed, bottom of viewport, split left/right
- Background: `rgba(255,255,255,0.13)` — semi-transparent, low distraction
- Press feedback: `scale(0.9)` + brighter background on `pointerdown`
- Container: `pointer-events: none`, individual buttons: `pointer-events: all`
- `setPointerCapture` used for multitouch (enables twin-stick on robotron)

### Adding Touch to a New Game

1. Determine which profile fits the game's controls (see table above, or create a new profile)
2. If creating a new profile:
   - Add the profile to `tools/touch-controls-template.js` (canonical reference)
   - Add the profile to `tools/inject-touch-controls.py` `PROFILES` dict
   - Document it in this table
3. Add the game to `GAME_PROFILES` in `tools/inject-touch-controls.py`
4. Run: `python3 tools/inject-touch-controls.py`

The injector is **idempotent** — safe to re-run. It strips and re-injects, never double-injects.

### Modifying the Touch Block

Do not edit the touch `<script>` block inside an HTML file directly. Always:
1. Edit `tools/touch-controls-template.js` (the readable canonical source)
2. Update the minified `TOUCH_BLOCK_TEMPLATE` in `inject-touch-controls.py`
3. Re-run the injector across all games

---

## 7. Gallery and Manifest Rules

### manifest.json

Auto-generated by `tools/catalogue-generator.py`. **Never edit by hand.** Always regenerate after adding, moving, or renaming prototypes.

```bash
python3 tools/catalogue-generator.py
```

### Required Fields Per Prototype Entry

```json
{
  "id": "def-001-pong",
  "title": "Pong",
  "series": "def",
  "number": "001",
  "path": "prototypes/def/def-001-pong.html",
  "track": "archetypes",
  "mechanic": "deflect — ball bounces between two paddles",
  "ancestry": "Tennis for Two (1958), Atari Pong (1972)",
  "rating": 4,
  "aiEra": 2,
  "aiInsight": "...",
  "status": "sketch",
  "visibility": "private",
  "notes": "..."
}
```

Fields are parsed directly from the METADATA block in each HTML file. If a field is missing or malformed, the generator will log a warning. Fix the METADATA block, then regenerate.

### gallery (index.html) Rules

- Reads `manifest.json` at load time via `fetch('./manifest.json')`
- Renders prototypes in an iframe on the right panel
- Filter buttons correspond to `series` and `track` fields
- Do not hardcode prototype entries in `index.html` — they all come from the manifest
- The dark sidebar, filter bar, and iframe player are the canonical gallery chrome — change aesthetics cautiously, change function never

### CATALOGUE.md

Auto-generated. Used as human-readable index. Never edit by hand.

### CATALOGUE-PUBLIC.md

Auto-generated with `--public` flag. Omits any prototype where `VISIBILITY: private`. Run:

```bash
python3 tools/catalogue-generator.py --public
```

---

## 8. Creative Evaluation Framework

Every prototype is judged by these criteria before being considered complete. This is also the framework for deciding whether to invest in a refinement pass.

### The Five Questions

1. **Mechanic purity** — Does this prototype isolate exactly one mechanic? Or did scope creep bleed in a second mechanic?
2. **Playable in 5 seconds** — Can someone open the file, understand what to do, and be engaged within 5 seconds with zero instructions?
3. **Ancestry honest** — Does the ANCESTRY field reference the real games this mechanic descends from, not the most famous game in the genre?
4. **AI insight earned** — Does the AI-INSIGHT field reveal something genuinely interesting about how game AI relates to AI research history? Or is it generic?
5. **Size discipline** — Is the prototype under 50KB? Does it feel tight — no unnecessary enemies, effects, or text?

### Rating Scale Guidance

| Rating | Meaning |
|--------|---------|
| ⭐ (1) | Mechanic barely functional; needs complete rebuild |
| ⭐⭐ (2) | Mechanic works but not fun; physics or feel is off |
| ⭐⭐⭐ (3) | Plays well; acceptable as a museum piece |
| ⭐⭐⭐⭐ (4) | Strong feel; teaches the mechanic clearly |
| ⭐⭐⭐⭐⭐ (5) | Exemplary; could not be purer or more instructive |

Target: Keep the collection average above ⭐⭐⭐⭐ (4.0). Retire or archive prototypes rated 2 or below.

### When to Refine vs. Archive

| Condition | Action |
|-----------|--------|
| Mechanic works, feel is off | Refine — bump `STATUS` to `refine` |
| Mechanic is correct, rating ≥ 4 | Ship as-is — don't over-polish |
| Mechanic is wrong (picked wrong ANCESTRY) | Rebuild or archive |
| Rating ≤ 2 and no clear fix | Move to `archive/` folder, mark `STATUS: archive` |
| Duplicate mechanic of existing ⭐⭐⭐⭐+ entry | Do not add — merge insight into existing prototype's NOTES |

---

## 9. Track Definitions

Pixel Vault has three tracks. Every prototype belongs to exactly one track.

### Track: Archetypes (`prototypes/`)

**Purpose:** The canonical mechanic library. One prototype per significant mechanic variation. This is the museum's permanent collection.

**Rules:**
- Each game must represent a **distinct** mechanic (not a reskin)
- Must have complete METADATA block
- Must pass the Five Questions (Section 8)
- Rating targets ≥ 3 before committing

**Current count:** 84 archetypes across 19 series

### Track: AI Archaeology (`ai-archaeology/`)

**Purpose:** Variants of archetype games where AI behavior is enhanced, annotated, or historically informed. Exists to demonstrate what AI layers look like on top of the baseline mechanic.

**Rules:**
- Every entry in ai-archaeology must reference an archetype in `prototypes/`
- The variant must **visibly demonstrate** an AI technique, not just describe it in comments
- File naming convention: same as archetypes

**Current count:** 6 variants (fix×1, phy×1, srv×1, trp×1, wld×2)

### Track: AI Evolution (`ai-evolution/`)

**Purpose:** Experimental games where the AI is the design lead — mechanics emerging from AI suggestions, not historical research.

**Rules:**
- No required ancestry (these are forward-facing, not backward-facing)
- Must still be single-file, ≤50KB, zero dependencies
- Must still have METADATA block, but `ANCESTRY` may read "No arcade precedent — AI-originated"

**Current count:** 43 (new×41, srv×1, wld×1)

---

## 10. Toolchain

All tools live in `tools/`. Do not move them. Do not add tools to the project root.

### `tools/catalogue-generator.py`

Scans all three tracks, reads METADATA blocks, generates:
- `CATALOGUE.md` — full internal catalogue
- `CATALOGUE-PUBLIC.md` (with `--public`) — visibility-filtered version
- `manifest.json` — machine-readable, consumed by `index.html`

**Run after:** any prototype is added, renamed, moved, or has METADATA changed.

```bash
python3 tools/catalogue-generator.py
python3 tools/catalogue-generator.py --public
```

### `tools/inject-touch-controls.py`

Injects the touch layer `<script>` block into each game HTML file. Idempotent — strips and re-injects. Never double-injects.

**Run after:** any new prototype is added, or the touch template is modified.

```bash
python3 tools/inject-touch-controls.py             # inject all
python3 tools/inject-touch-controls.py --dry-run   # preview only
python3 tools/inject-touch-controls.py --remove    # strip touch blocks
```

### `tools/touch-controls-template.js`

Canonical readable source for the touch layer implementation. **Not executed directly.** Read this to understand the pattern, copy relevant sections when creating a new game manually, or use it as the source of truth when modifying the minified block inside `inject-touch-controls.py`.

### `tools/dev-server.sh`

Starts a local HTTP server for developing and testing the gallery. Runs a 5-stage pre-flight validation (manifest present, file count, Python available, port free, gallery reachable) before serving.

```bash
bash tools/dev-server.sh
# Opens http://localhost:8080 after pre-flight checks
```

### `tools/test-games.sh`

Agent-friendly structural and security test runner. Validates every game file in `prototypes/`, `ai-archaeology/`, `ai-evolution/`, and `refined/`. Exits 0 only if zero FAIL results. Run after any prototype change.

```bash
bash tools/test-games.sh
bash tools/test-games.sh --verbose    # show all results including PASS
```

**Checks performed (FAIL = blocks CI):**
- METADATA block present and complete
- Canvas element present
- requestAnimationFrame used (not setInterval)
- 800×600 resolution declared
- File size < 50KB
- No `eval()` usage
- No `new Function()` usage
- No external `fetch()` to remote URLs
- No external XMLHttpRequest to remote URLs

**Checks performed (WARN = advisory):**
- `document.write()` presence
- `innerHTML` assigned from a variable
- `localStorage` / `sessionStorage` usage

---

## 11. Versioning and Changelog Protocol

### Prototype Versioning Policy

Pixel Vault uses a **2-default, 3-when-earned** model.

For historical mechanics, maintain two versions by default:

1. Archetype (`prototypes/`) — canonical reconstruction
2. AI Archaeology (`ai-archaeology/`) — AI-informed variant of that archetype

AI Evolution is selective, not required per mechanic:

3. AI Evolution (`ai-evolution/`) — only when a prototype is genuinely novel

Do not create a forced third copy for every archetype. Add AI Evolution entries only when at
least one of the following holds:

- A new core interaction verb appears
- The prototype no longer has meaningful arcade ancestry
- The play feel is clearly distinct within ~10 seconds

`refined/` is a promotion stage for proven winners, not a mandatory fourth version.

### Version Number (`README.md`)

Format: `v[MAJOR].[MINOR].[PATCH]`

| Increment | When |
|-----------|------|
| MAJOR | Architecture change (new track, gallery overhaul, file format breaking change) |
| MINOR | New prototype(s) added, new tool added, new feature in gallery |
| PATCH | Metadata fixes, NOTES edits, catalogue regeneration, bug fixes |

### After Any Change, Run Checklist

- [ ] METADATA block updated in affected HTML files
- [ ] `python3 tools/catalogue-generator.py` run (regenerate CATALOGUE.md + manifest.json)
- [ ] `python3 tools/catalogue-generator.py --public` run if public catalogue is used
- [ ] `python3 tools/inject-touch-controls.py` run if new game added or touch template changed
- [ ] `README.md` version bumped if MINOR or MAJOR change
- [ ] DESIGN-CONTRACT.md updated if any rule changed (Series Registry, Profile table, etc.)
- [ ] Commit with appropriate prefix (see below)

### Commit Message Prefixes

| Prefix | Use |
|--------|-----|
| `feat:` | New prototype, new track, new gallery feature |
| `fix:` | Bug fix in a prototype, tool fix |
| `docs:` | README, COMPENDIUM, ADR, or this contract |
| `meta:` | METADATA block corrections |
| `touch:` | Touch layer changes (template, injector, profiles) |
| `tools:` | Changes to `tools/` scripts |
| `catalogue:` | Regenerated CATALOGUE.md / manifest.json only |
| `refactor:` | Restructuring with no behavior change |

---

## 12. Agent Decision Rules

These rules are explicit YES / NO / ASK classifications. An agent should apply these before taking action.

### ALWAYS DO (No Confirmation Needed)

- Fix a bug in a prototype that breaks gameplay
- Update a METADATA block to correct a factual error
- Re-run `catalogue-generator.py` after any file change
- Re-run `inject-touch-controls.py` after any new prototype is added
- Bump PATCH version in README.md after a fix
- Fix a typo in DESIGN-CONTRACT.md, README.md, COMPENDIUM.md
- Add a new series `README.md` file when registering a new series

### DO WITH BRIEF CONFIRMATION (1 Sentence to User Before Proceeding)

- Add a new prototype to an existing series
- Modify the touch template (affects all 12 games on next inject)
- Change the gallery's visual design (index.html CSS/layout)
- Add a new control profile to the touch system
- Retire a prototype (move to archive)
- Bump MINOR version in README.md

### ASK BEFORE DOING (Full Discussion)

- Create a new series (code, directory, registry entry)
- Add a new track (changes fundamental project structure)
- Change the METADATA block specification (breaks catalogue parser for existing files)
- Delete any file permanently (use `archive/` instead)
- Change the 50KB size limit
- Change the zero-dependency rule
- Publish or share any prototype marked `VISIBILITY: private`
- Change the gallery's filter logic or manifest schema
- Modify any ADR (Architecture Decision Record)

### NEVER DO

- Edit `CATALOGUE.md`, `CATALOGUE-PUBLIC.md`, or `manifest.json` by hand — always regenerate
- Edit the touch `<script>` block inside individual HTML files directly — always use injector
- Add external file dependencies to any prototype (CDN links, external images, etc.)
- Create a prototype over 50KB without explicit approval and contract update
- Renumber existing prototypes to close number gaps
- Add a prototype with a fabricated ANCESTRY (real historical titles only)
- Commit with vague messages like "update files" or "fix stuff"

---

## 13. Roadmap and Phase Status

### Completed Phases

| Phase | Description | Status |
|-------|-------------|--------|
| 1–4 | Initial scaffold, ADRs 001–004, 13 series directories | ✅ Complete |
| 5–6 | 9 base + 5 AI-native prototypes | ✅ Complete |
| 7 | Speed/feel pass across all 14 prototypes | ✅ Complete |
| 8 | Three-track folder architecture, git mv to ai-archaeology/ | ✅ Complete |
| 9a | 3 new archetypes (joust, racer, robotron) | ✅ Complete |
| 9b | README v0.4.0, CATALOGUE.md with 20 entries | ✅ Complete |
| 10a | Museum gallery (index.html, manifest.json, iframe player) | ✅ Complete |
| 10b | COMPENDIUM.md historical research document | ✅ Complete |
| 10c | README v0.5.0 | ✅ Complete |
| 11a | Project renamed to Pixel Vault, all files updated | ✅ Complete |
| 11b | ADR-005 mobile support strategy | ✅ Complete |
| 11c | Touch layer: keyboard audit, template, injector | ✅ Complete |
| 11d | Touch layer injected into all 12 archeype games | ✅ Complete |
| 11e | DESIGN-CONTRACT.md v1.0.0 | ✅ Complete (this file) |
| 12a | Security pipeline: CI/CD workflows, test-games.sh security checks, .gitignore | ✅ Complete |
| 12b | AWS backend: SAM stack (Lambda + DynamoDB x3 + WAF + API Gateway) | ✅ Complete |
| 12c | Publish system: scripts/publish.sh + publish-config.example.json | ✅ Complete |
| 12d | Gallery v2: leaderboard drawer, score modal, postMessage, session tracking | ✅ Complete |
| 12e | ADR-006: Leaderboard, security, publish operations | ✅ Complete |

### Active / Upcoming Work

| Phase | Description | Priority |
|-------|-------------|----------|
| 12 | Mobile QA — test touch layer on real device or DevTools mobile sim | High |
| 13 | README update — document new tools (injector, template) in quick-start | Medium |
| 14 | First AI Evolution prototype — mechanic originated by AI, not history | Medium |
| 15 | Public-ready package — review VISIBILITY fields, generate CATALOGUE-PUBLIC.md, consider gh-pages deployment | Low |
| 16 | Founder variant prototypes — add parent or sibling mechanics (e.g., `def-003-arkanoid` as brick-layout variant) | Low |

### Reserved Series (Next Candidates)

- `wld-001` — ecosystem or cellular automata prototype (wld series)
- `anc-001` — pre-Pong era game (Tennis for Two, OXO, or Nim)
- `hyb-001` — deliberate mechanic crossbreed (e.g., maze + shooter)

---

## 14. Publish Pipeline

### Overview

Pixel Vault is published to `https://joshuaayson.com/pixel-vault/`. Only a curated subset of games is deployed to production.

### Release Branch Strategy

1. Cut a branch named `release/vX.Y.Z` from `main`
2. GitHub Actions `release.yml` workflow triggers automatically
3. CI gate runs (all `ci.yml` jobs must pass)
4. `scripts/publish.sh` deploys the curated game set to S3
5. CloudFront invalidation runs to clear cache

```bash
# Cut a release branch
git checkout -b release/v0.6.0
git push origin release/v0.6.0
# → GitHub Actions takes over from here
```

### Publish Configuration

`publish-config.json` is **gitignored** — never commit it. Use `publish-config.example.json` as a template.

**Required fields:**
```json
{
  "destination": "s3://your-bucket/pixel-vault",
  "apiUrl": "/pixel-vault/api",
  "version": "0.6.0",
  "leaderboardTopN": 10,
  "publishedGames": ["def-001-pong", "maz-001-pacman", ...]
}
```

For GitHub Actions, the full JSON is stored in repository secret `PUBLISH_CONFIG`.

### What Gets Deployed

`scripts/publish.sh` builds the publish artifact by:
1. Filtering `manifest.json` to only `publishedGames` entries
2. Excluding any entry with `visibility: private`
3. Stripping `visibility` and `notes` fields from the public manifest
4. Generating `config.json` with `apiUrl` and `leaderboardEnabled`
5. Syncing to S3 with appropriate cache headers

### Required GitHub Secrets

| Secret | Purpose |
|--------|---------|
| `PUBLISH_CONFIG` | Full `publish-config.json` JSON blob |
| `AWS_DEPLOY_ROLE_ARN` | OIDC role for keyless deploy (preferred) |
| `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` | Fallback key-based auth |
| `CLOUDFRONT_DISTRIBUTION_ID` | For cache invalidation after deploy |

### Backend Deployment (One-Time Setup)

The AWS backend (API Gateway + Lambda + DynamoDB + WAF) is deployed separately via AWS SAM:

```bash
cd infra
sam build
sam deploy --guided   # First time — creates samconfig.toml (gitignored)
sam deploy            # Subsequent deploys
```

See `infra/README.md` for full setup instructions.

---

*End of Design Contract. Update this document whenever the project advances. The contract serves the project — if a rule stops serving, change the rule.*

---

**Maintained by:** Joshua Ayson / OA LLC
**Project:** Pixel Vault (`pixelvault/`)
**Version:** 1.1.0 (updated 2026-03-22)
