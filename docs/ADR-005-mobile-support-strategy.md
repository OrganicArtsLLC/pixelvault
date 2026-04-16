# ADR-005: Mobile Support Strategy

**Status:** Proposed
**Date:** 2026-03-22
**Author:** Joshua Ayson / OA LLC
**Project:** Pixel Vault

---

## Context

The project is being prepared for public hosting where the primary audience is
8-14 year olds. This audience overwhelmingly uses phones and tablets as their
primary device. If the games don't work on mobile, they don't work for this
audience.

### Current State

| Aspect | Status | Notes |
|--------|--------|-------|
| Viewport meta tags | ✅ Ready | All 20 prototypes have proper viewport config |
| Canvas scaling | ✅ Ready | All games resize with `window.resize` events |
| Gallery responsive CSS | ✅ Ready | 800px breakpoint switches sidebar → stacked |
| Touch input | ❌ Missing | Zero `touchstart`/`touchmove`/`touchend` events |
| Mouse input for gameplay | ❌ Missing | All games are keyboard-only |
| Pointer events | ❌ Missing | No unified pointer event handling |

**Single blocking issue:** every prototype uses keyboard-only input. Layout
and rendering are already mobile-ready.

### Control Schemes by Prototype

| Game | Controls | Mobile Complexity |
|------|----------|------------------|
| Pong | W/S + ↑/↓, Space | **Low** — vertical touch zones |
| Breakout | ←/→, Space | **Low** — touch-drag paddle |
| Invaders | ←/→, Space | **Low** — d-pad + fire |
| Pac-Man | ←/→/↑/↓ | **Medium** — 4-way d-pad or swipe |
| Tetris | ←/→/↑/↓, Z, Space | **Medium** — swipe + tap-rotate |
| Runner | ←/→, Space (variable) | **Low** — tap-to-jump |
| Joust | ←/→, Space (flap) | **Low** — d-pad + flap button |
| Racer | ←/→/↑/↓ | **Medium** — tilt or d-pad |
| Asteroids | ←/→ rotate, ↑ thrust, Space | **Medium** — 3 buttons + fire |
| Qix | ←/→/↑/↓, Space (hold) | **Medium** — swipe + hold button |
| Defender | ←/→/↑/↓, Space, Z | **High** — d-pad + 2 buttons |
| Robotron | WASD + Arrows (8-way each) | **Highest** — twin virtual sticks |

---

## Decision

**Built-in touch layer per game. Not a separate mobile version.**

### Rationale

1. **One codebase, one file per game** — The project's core constraint is
   single-HTML-file prototypes. Maintaining separate mobile versions doubles
   the file count and guarantees drift.

2. **Layout is already done** — Canvas scaling and gallery responsiveness work
   today. Only the input layer needs work. This is additive, not a rewrite.

3. **Touch doesn't break keyboard** — Adding `touchstart`/`touchmove` handlers
   alongside existing `keydown`/`keyup` handlers has zero conflict. Both can
   coexist in the same file.

4. **Progressive enhancement** — Detect touch support at runtime, show virtual
   controls only when needed. Desktop users see nothing different.

5. **Complexity is bounded** — Even Robotron (hardest case) is solvable with
   twin virtual joysticks. Every other game is simpler.

### Rejected Alternatives

| Alternative | Why Rejected |
|-------------|-------------|
| Separate mobile HTML files | Violates single-file constraint, doubles maintenance |
| Responsive framework (Phaser, etc.) | Adds dependencies, violates zero-dependency constraint |
| Mobile-only simplified versions | Fragments the experience, kids on desktop see different game |
| "Desktop only" with warning | Loses the primary audience entirely |

---

## Implementation Plan

### Phase 1: Touch Input Module (Template)

Create a reusable touch control pattern that each game inlines. Not external
JS — a copyable block that goes in the `<script>` section of each game.

```
┌─────────────────────────────────┐
│   Canvas (game renders here)    │
│                                 │
│  ┌─────┐            ┌───────┐  │
│  │D-Pad│            │ Fire  │  │
│  │     │            │ Jump  │  │
│  └─────┘            └───────┘  │
│   (left thumb)    (right thumb) │
└─────────────────────────────────┘
```

**Components:**
- **Virtual D-Pad** — Semi-transparent overlay, 4-way or 8-way
- **Action Buttons** — 1-3 buttons (fire, jump, special)
- **Twin Sticks** — For Robotron-class games only
- **Touch-to-key bridge** — Touch events dispatch the same key events the game
  already listens for, so zero game logic changes

**Key technique — keyboard event injection:**
```javascript
// Touch fires the same events the game already handles
function injectKey(code, type) {
  document.dispatchEvent(new KeyboardEvent(type, { code }));
}

// D-pad touch → arrow keys
dpad.addEventListener('touchstart', (e) => {
  const dir = getDpadDirection(e);
  injectKey(dir, 'keydown');
});
```

This means **game code doesn't change at all**. The touch layer sits on top
and translates touches into the keyboard events the game already processes.

### Phase 2: Control Profiles

Each game declares a control profile in its metadata comment block:

```html
<!-- METADATA
controls: dpad+fire
mobile_layout: standard
-->
```

**Profiles:**
| Profile | Layout | Games |
|---------|--------|-------|
| `dpad+fire` | D-pad left, fire button right | Invaders, Joust, Defender |
| `horizontal+fire` | Left/right buttons, fire right | Breakout (drag alt), Qix |
| `drag` | Touch-drag on game element | Pong (paddle), Breakout (paddle) |
| `dpad` | D-pad only, no fire button | Pac-Man, Racer |
| `tap` | Tap anywhere = action | Runner (jump) |
| `dpad+multi` | D-pad + 2-3 buttons | Asteroids, Tetris, Defender |
| `twin-stick` | Two virtual joysticks | Robotron |
| `swipe` | Swipe gestures for direction | Tetris (alt), Pac-Man (alt) |

### Phase 3: Gallery Touch Enhancement

- Tap game card → load game (already works via click)
- Touch-friendly filter buttons (already sized OK)
- Fullscreen button for immersive mobile play
- Orientation lock hint (landscape recommended for most games)

### Phase 4: Per-Game Rollout

Build touch support incrementally, easiest first:

**Wave 1 (Low complexity):**
- Runner (tap-to-jump — simplest possible)
- Pong (touch-drag paddles)
- Breakout (touch-drag paddle)
- Joust (d-pad + flap)

**Wave 2 (Medium complexity):**
- Invaders (d-pad + fire)
- Pac-Man (d-pad or swipe)
- Tetris (swipe + tap)
- Racer (d-pad or tilt)

**Wave 3 (Higher complexity):**
- Asteroids (d-pad + thrust + fire)
- Qix (d-pad + hold button)
- Defender (d-pad + fire + bomb)

**Wave 4 (Twin-stick):**
- Robotron (twin virtual joysticks — hardest case)

---

## Design Constraints

1. **No game logic changes** — Touch layer injects keyboard events. The game
   code that processes `keydown`/`keyup` stays exactly as-is.

2. **No external files** — Touch controls are inlined in each game's HTML.
   No shared .js imports (violates single-file constraint).

3. **Invisible on desktop** — Virtual controls only render when touch is
   detected (`'ontouchstart' in window`).

4. **Semi-transparent** — Controls overlay the canvas at ~30% opacity so
   they don't obscure gameplay.

5. **Thumb-friendly zones** — Controls placed in bottom corners, sized for
   thumb reach (44px minimum touch targets per WCAG).

6. **No impact on file size** — Touch layer adds ~2-3KB per game. Well
   within the 50KB single-file constraint.

---

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Twin-stick feels bad on mobile | Medium | Robotron gets extra tuning; consider simplified "auto-aim" mode |
| Touch zones conflict with gameplay | Low | Controls in dead zones (bottom corners), semi-transparent |
| Performance on older phones | Low | Canvas games are trivial for modern mobile GPUs |
| Copy-paste touch code diverges | Medium | Template block in `templates/`, lint check could verify |
| Some games genuinely bad on mobile | Low | Gallery can flag "best on desktop" without blocking play |

---

## Success Criteria

- All 12 archetypes playable on iPhone/iPad Safari and Android Chrome
- No game logic changes required
- Virtual controls invisible on desktop
- File size increase < 3KB per game
- Gallery usable on phone without horizontal scrolling
- Kids can pick up and play without reading instructions

---

## Sizing Estimate

| Component | Scope |
|-----------|-------|
| Touch template pattern | One reusable block per profile type |
| Wave 1 (4 games) | First pass, validate the pattern works |
| Wave 2 (4 games) | Expand to medium complexity |
| Wave 3-4 (4 games) | Complex controls, twin-stick |
| Gallery tweaks | Fullscreen button, orientation hint |

---

## Conclusion

Mobile support is achievable **without a separate design** because:

1. Canvas rendering already scales to any screen
2. Gallery layout already responds to small screens
3. Touch-to-keyboard injection means zero game logic changes
4. The touch layer is additive — it can be built incrementally
5. Even the hardest case (Robotron twin-stick) has a known solution

The only work is building virtual control overlays and injecting keyboard
events from touch. This is a well-understood pattern used by countless
browser-based retro game emulators.

**Recommendation:** Approve and begin with Wave 1 (Runner, Pong, Breakout,
Joust) to validate the pattern before rolling out to all games.
