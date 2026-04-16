# ADR-013: Public Release Architecture — Default-Private Game Model

**Status:** Accepted  
**Date:** 2026-04-12  
**Author:** Joshua Ayson / OA LLC

---

## Context

Pixel Vault contains two classes of content:

1. **Public content** — the museum infrastructure (gallery, play engine, QA tooling, CI/CD pipeline, series registry, metadata system), all documentation, templates, and the conceptual framework. This infrastructure is the genuine contribution of the project.

2. **Private content** — the 460 playable game prototypes themselves (HTML files), the IP watchlist, and internal agent operation documents. Game files may contain implementation patterns derived from specific trademarked games. The IP watchlist is a private legal reference. Agent instructions are operational tooling not meant for public consumption.

The decision made in ADR-010 established that games default to private until individually cleared. This ADR documents the technical implementation of that decision via history-clean and layered protection.

---

## Decision

Adopt a **three-layer privacy architecture** and perform a one-time history clean. This makes the museum infrastructure public while all game files default to private pending individual IP clearance.

### Layer 1: Working-Tree Privacy (`.gitignore`)

All game prototype directories are gitignored:

```
prototypes/
ai-archaeology/
ai-evolution/
```

Additionally:
- `CLAUDE.md` — agent-private instructions 
- `.github/copilot-instructions.md` — agent-private instructions
- `IP-WATCHLIST.md` (root) — private legal reference

Files in these paths exist on disk for local play/development but **never enter git**.

### Layer 2: History Clean (`git filter-repo`)

On 2026-04-12, `git filter-repo --invert-paths` was run against 641 private paths using `--path-glob` for the three game directories plus 3 specific file paths. This rewrote 986 commits down to **85 commits** in ~5 seconds.

**The original commit hash before filter-repo:** `882b900`  
**Post-filter HEAD:** `53d2f99` (after two-pass: IP-WATCHLIST.md required a second pass)

**To re-run history clean if needed:**
```bash
git filter-repo --invert-paths \
  --path-glob 'prototypes/*' \
  --path-glob 'ai-archaeology/*' \
  --path-glob 'ai-evolution/*' \
  --path 'CLAUDE.md' \
  --path '.github/copilot-instructions.md' \
  --path 'IP-WATCHLIST.md' \
  --force
```

### Layer 3: Pre-Commit Hook (`.git/hooks/pre-commit`)

A pre-commit hook blocks any staged commit that includes private paths. It immediately exits 1 if any game directory files are staged.

The hook was installed 2026-04-12 and is the **last line of defense** against accidental 460-game exposure.

---

## What Is Public (Museum Infrastructure)

| Category | Public |
|----------|--------|
| `index.html` — museum gallery | ✅ |
| `play.html` — Play Engine (full-screen stage) | ✅ |
| `dev.html` — developer hub | ✅ |
| `compendium.html` — historical compendium browser | ✅ |
| `manifest.json` — prototype index | ✅ |
| `CATALOGUE.md`, `CATALOGUE-PUBLIC.md` | ✅ |
| `tools/` — all QA/build tools | ✅ |
| `templates/` — 5 base starter templates | ✅ |
| `infra/` — AWS SAM backend | ✅ |
| `scripts/` — deploy scripts | ✅ |
| `docs/ADR-001` through `ADR-012`, `ADR-013` | ✅ |
| `package.json`, `README.md`, `lineage.json` | ✅ |
| `.github/workflows/` — CI/CD | ✅ |

---

## What Remains Private (On-Disk Only)

| Path | Why Private |
|------|-------------|
| `prototypes/` (241 games) | Pending individual IP clearance per ADR-010 |
| `ai-archaeology/` (76 games) | Pending individual IP clearance |
| `ai-evolution/` (143 games) | Pending individual IP clearance |
| `IP-WATCHLIST.md` | Private legal reference document |
| `CLAUDE.md` | Agent operation guide |
| `.github/copilot-instructions.md` | Agent operation guide |

---

## On-Demand Game Publishing

Individual games can be published via `tools/publish-game.sh` (create as needed):

1. Check game against `IP-WATCHLIST.md` (private reference) — confirm no protected IP
2. Verify trademark-removed per ADR-019 conventions
3. `tools/publish-game.sh prototypes/maz/maz-001-pacman.html`
4. Script copies to published game registry, removes from `.gitignore` for that file, commits

The expected long-term flow: curated game releases over time as each file is individually IP-cleared.

---

## Why Not Just Delete the Games

Deleting them would lose local development utility. The `.gitignore` approach keeps them accessible locally for development, QA testing, and maintenance — just never exposed to the public repo. This is the correct balance between open-source infrastructure and IP-cautious game content.

---

## Consequences

- Pixel Vault is now a public, forkable repository on GitHub
- The museum engine, QA tooling, gallery, play engine, and CI/CD are visible open source
- All 460 game prototypes remain local-only (default private)
- 986 → 85 commits: public history is clean and focused on infrastructure
- Pre-commit hook prevents any future accidental game file exposure
- History has been rewritten; any collaborators need fresh clones

---

## Related

- `ADR-010`: IP and legal framework for code sharing
- `ADR-011`: Public site architecture
- `ADR-012`: Gameplay experience engine (play.html)
- Filter-repo two-pass note: `IP-WATCHLIST.md` was at root (not `docs/`), required second filter-repo invocation
