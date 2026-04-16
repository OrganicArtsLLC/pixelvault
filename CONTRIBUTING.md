# Contributing to Pixel Vault

Thank you for your interest in contributing to Pixel Vault.

**Organization:** OA LLC  
**License:** See [LICENSE](LICENSE) (GPL-3.0) and [CONTENT-LICENSE](CONTENT-LICENSE) (CC BY-NC-SA 4.0)

---

## Hard Requirements (Never Break)

- **Single file** — every game is ONE `.html` file, no external assets
- **50KB limit** — `wc -c <file>` must be ≤ 51,200 bytes
- **Zero dependencies** — no CDN links, no external scripts
- **Canvas-based** — 800×600 on `<canvas>`, 60fps via `requestAnimationFrame`
- **Metadata block** — must be the first thing in the file, before `<!DOCTYPE html>`

## Quick Start

```bash
# Local dev server (required for gallery)
python3 -m http.server 8080

# Test all games (CI gate)
bash tools/test-games.sh

# Regenerate catalogue (run after any game change)
python3 tools/catalogue-generator.py
```

## Naming Convention

`{series}-{number}-{name}.html` — e.g. `maz-001-pacman.html`

See [docs/DESIGN-CONTRACT.md](docs/DESIGN-CONTRACT.md) for the full series registry.

## Pre-commit Hook

```bash
git config core.hooksPath .githooks
```

## Commit Format

```
<type>: <subject>
```

Types: `feat:` (new game), `fix:`, `docs:`, `ci:`, `chore:`

## Security

Report security issues privately via GitHub Security Advisories — do **not** open a public issue.
