# ADR-012: Gameplay Experience Engine — Full-Screen Play, Platform-Tuned Controls, Performance Instrumentation

**Status:** Accepted  
**Date:** 2026-03-27  
**Author:** Joshua Ayson / OA LLC  
**Project:** Pixel Vault  
**Supersedes:** Portions of ADR-005 (mobile control profiles), ADR-011 Part VI (mobile game modal)  
**References:** ADR-005 (touch layer foundation), ADR-011 (gallery + infra), DESIGN-CONTRACT.md Section 6

---

## Table of Contents

- [Context and Problem Statement](#context-and-problem-statement)
- [Part I: Architectural Diagnosis — Why Mobile Play Fails Today](#part-i-architectural-diagnosis--why-mobile-play-fails-today)
- [Part II: The Two-Mode Model — Browse vs. Play](#part-ii-the-two-mode-model--browse-vs-play)
- [Part III: Play Engine — Full-Screen Game Stage](#part-iii-play-engine--full-screen-game-stage)
- [Part IV: Desktop Play Experience](#part-iv-desktop-play-experience)
- [Part V: Mobile Play Experience](#part-v-mobile-play-experience)
- [Part VI: Touch Control System v2](#part-vi-touch-control-system-v2)
- [Part VII: Audio Engine and Timing Architecture](#part-vii-audio-engine-and-timing-architecture)
- [Part VIII: Performance Instrumentation and Diagnostics](#part-viii-performance-instrumentation-and-diagnostics)
- [Part IX: Game Readiness Pipeline](#part-ix-game-readiness-pipeline)
- [Part X: Security Considerations](#part-x-security-considerations)
- [Part XI: Phased Delivery Plan](#part-xi-phased-delivery-plan)
- [Part XII: Testing Strategy](#part-xii-testing-strategy)
- [Decision Summary](#decision-summary)

---

## Context and Problem Statement

Pixel Vault has 460 playable prototypes, a working gallery, touch controls injected into 300+ games, and a deployment pipeline to staging and production. The **browsing experience** (finding games, reading history, navigating the collection) is solid. The **playing experience** is not.

### What's broken

1. **Mobile gameplay is unplayable in practice.** Touch controls exist but the game canvas is scaled to ~48% on a phone (390px / 800px). Controls overlap gameplay. The iframe modal fights the browser chrome. There is no proper "game stage" — just a squeezed iframe in a modal.

2. **No separation between browse and play.** The gallery modal tries to be both: show game info and play the game in the same space. On desktop this is acceptable. On mobile it's a collision of tap targets, browser bars, and tiny canvas.

3. **Sound is inconsistent.** Only 12.8% of games have audio. Games that do have audio implement their own `AudioContext` from scratch. There is no shared audio initialization, no user-gesture-gated audio unlock, and no coordination between the host page and the game iframe.

4. **Timing and physics vary by device.** Games use `requestAnimationFrame` (correct) but many have no delta-time smoothing. On a 120Hz iPad Pro, games run 2x fast. On a throttled 30fps phone, they stutter. No instrumentation exists to detect or diagnose this.

5. **No performance feedback loop.** When a game stutters, lags, or crashes on mobile, there is no data. No frame timing, no jank detection, no user-visible diagnostics. The QA dashboard tests games in desktop iframes only.

6. **Desktop experience is fine but not tuned.** Games work well on desktop but the modal could be better: keyboard focus is inconsistent, Escape sometimes closes the modal when the user meant to pause, and there's no "theater mode" for focused play.

### What's working

- Touch-to-keyboard injection pattern is sound (ADR-005, implemented)
- Canvas games render at any scale (already verified)
- Gallery responsive layout works (ADR-011)
- Deployment pipeline handles game files correctly
- 10 touch profiles cover the control scheme taxonomy

### What this ADR decides

1. A dedicated **Play Engine** (separate HTML page) that games open into for full-screen play
2. Platform-specific tuning for **desktop** and **mobile** play experiences
3. A v2 touch control architecture with orientation-locked, full-viewport controls
4. An audio coordination layer between host page and game iframe
5. A performance instrumentation system (frame timing, jank detection, diagnostic overlay)
6. A game readiness pipeline (automated pre-flight checks before a game ships)
7. Iterative delivery phases with explicit test gates

---

## Part I: Architectural Diagnosis — Why Mobile Play Fails Today

### The iframe-in-modal problem

The current architecture embeds games in an iframe inside a modal overlay inside the gallery page:

```
┌─ Gallery Page (index.html) ──────────────────────────────────┐
│  ┌─ Modal Overlay ─────────────────────────────────────────┐ │
│  │  ┌─ Toolbar ──────────────────────────────────────────┐ │ │
│  │  │ [Close] [Info] [Fullscreen] [New Tab]              │ │ │
│  │  └────────────────────────────────────────────────────┘ │ │
│  │  ┌─ Iframe Container ────────────────────────────────┐ │ │
│  │  │  ┌─ Game Canvas (800x600, scaled down) ────────┐ │ │ │
│  │  │  │                                              │ │ │ │
│  │  │  │      GAME RENDERS HERE                      │ │ │ │
│  │  │  │      (scaled to ~48% on mobile)             │ │ │ │
│  │  │  │                                              │ │ │ │
│  │  │  │  ┌────────┐              ┌──────┐           │ │ │ │
│  │  │  │  │ D-Pad  │              │ Fire │           │ │ │ │
│  │  │  │  └────────┘              └──────┘           │ │ │ │
│  │  │  │  (touch controls fight for space)           │ │ │ │
│  │  │  └──────────────────────────────────────────────┘ │ │
│  │  └────────────────────────────────────────────────────┘ │
│  └──────────────────────────────────────────────────────────┘ │
│  [Gallery cards still loaded behind modal]                     │
└───────────────────────────────────────────────────────────────┘
```

**Problems with this stack:**

| Issue | Cause | Impact |
|-------|-------|--------|
| Tiny game canvas | 800px game in 390px viewport = 48% scale | Controls too small, game unreadable |
| Browser chrome steals space | Mobile Safari shows address bar + toolbar = ~100px lost | Even less room for the game |
| Touch controls overlap game | Controls rendered inside 48%-scaled canvas | Tap targets conflict with gameplay |
| No landscape lock | `screen.orientation.lock()` fails on iOS | Portrait = worst aspect ratio for 4:3 games |
| Modal fights with gallery | Gallery DOM still loaded, taking memory + event listeners | Performance overhead |
| Focus confusion | Keyboard events may go to gallery instead of iframe | Desktop keyboard input drops |
| Audio blocked | No user gesture propagation to iframe AudioContext | Sound doesn't start |

### Root cause

**The gallery and the game are competing for the same viewport.** A modal overlay doesn't change this: the gallery is still loaded, the browser chrome is still present, and the iframe is sandwiched between layers that all want screen real estate.

### The solution principle

**Separate browse from play completely.** The gallery is a catalogue. The game gets its own stage. On mobile, this means a dedicated page (new tab or navigation). On desktop, this means a focused "theater mode" that takes over the viewport.

---

## Part II: The Two-Mode Model — Browse vs. Play

### Architecture

```
┌───────────────────────────────────────────────────────────────────┐
│                         BROWSE MODE                               │
│                                                                   │
│  index.html — Gallery, search, filter, series, compendium        │
│  Rich, compact, visual, information-dense                        │
│  Optimized for discovery and exploration                         │
│  Touch: scrolling, tapping, swiping between cards                │
│  No game iframes loaded (thumbnails only)                        │
│                                                                   │
│  User taps [PLAY] on a game card                                 │
│             │                                                     │
│             ▼                                                     │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │  Pre-Play Interstitial (200ms transition)                   │ │
│  │  - Game title, series badge, controls diagram               │ │
│  │  - "Tap to start" (unlocks audio context)                   │ │
│  │  - On mobile: "Rotate to landscape" hint if portrait        │ │
│  │  - Quick-info: ancestry, year, mechanic one-liner           │ │
│  └──────────────────────────┬──────────────────────────────────┘ │
│                              │                                    │
│                              ▼                                    │
└───────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────┐
│                          PLAY MODE                                │
│                                                                   │
│  play.html?game={id} — Dedicated game stage                      │
│  Full viewport, zero chrome, monochrome background               │
│  Game iframe is the ONLY active element                          │
│                                                                   │
│  Desktop: Theater mode, centered canvas, keyboard focused        │
│  Mobile: Landscape-locked, full-screen, touch controls           │
│           outside the game canvas (not overlaid)                  │
│                                                                   │
│  Minimal HUD: [Back to Gallery] [?] [Fullscreen] [Next Game]    │
│  Auto-hides after 3s of gameplay, reappears on tap/mouse-move    │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

### Why a separate page, not a modal

| Factor | Modal (current) | Separate Page (proposed) |
|--------|-----------------|--------------------------|
| Viewport control | Shares with gallery DOM | Owns entire viewport |
| Browser chrome | Cannot dismiss | Can request fullscreen API |
| Memory | Gallery + game both loaded | Only game loaded |
| Audio context | Blocked (no direct user gesture in iframe) | Unlocked by pre-play tap |
| Orientation lock | Fails (gallery page holds lock) | Can request landscape |
| Keyboard focus | Ambiguous (gallery vs iframe) | Iframe is only focusable element |
| Deep linking | `?game=id` on gallery URL | `play.html?game=id` (clean) |
| Mobile back button | Closes modal (surprising) | Returns to gallery (expected) |

### URL scheme

```
Browse:  /                        → Gallery home
Browse:  /?series=maz             → Filtered to Maze series
Browse:  /compendium.html         → Museum / history
Play:    /play.html?game=maz-001  → Pac-Man in play engine
Play:    /play.html?game=maz-001&next=maz-002  → With "next game" queued
```

### Navigation flow

**Desktop:**
1. User clicks [PLAY] on a card in gallery
2. Gallery shows 200ms fade-out transition
3. Browser navigates to `/play.html?game=maz-001`
4. Play engine loads, shows pre-play screen (controls diagram, "Click to start")
5. User clicks anywhere → game loads in iframe, audio context unlocked
6. [Back] button or Escape → returns to gallery at same scroll position (via `sessionStorage`)

**Mobile:**
1. User taps [PLAY] on a card
2. `window.open('/play.html?game=maz-001', '_blank')` opens new tab
3. Play engine loads in new tab, shows pre-play screen
4. User taps "Tap to start" → requests fullscreen + landscape lock
5. Game loads, touch controls rendered OUTSIDE canvas (below/beside)
6. "Back to Gallery" closes the tab (or navigates back)

### Why new tab on mobile

Opening in the same tab works on desktop (browser history is reliable). On mobile, navigation within a single tab causes problems:
- iOS Safari reloads the previous page from scratch on back-swipe (no bfcache for heavy DOM)
- The gallery scroll position is lost
- Browser chrome reappears during the navigation transition
- A new tab is a clean slate: full viewport, no back-swipe interference, the gallery tab stays warm

---

## Part III: Play Engine — Full-Screen Game Stage

### play.html — Dedicated game player page

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, 
        maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Pixel Vault — Playing</title>
  <style>/* Inline critical CSS: dark bg, centered stage, HUD */</style>
</head>
<body>
  <!-- Pre-play interstitial -->
  <div id="preplay">...</div>
  
  <!-- Game stage (hidden until play starts) -->
  <div id="stage">
    <div id="hud"><!-- auto-hiding toolbar --></div>
    <div id="game-container">
      <iframe id="game" sandbox="allow-scripts allow-same-origin"
              allow="autoplay; fullscreen"></iframe>
    </div>
    <div id="touch-controls"><!-- External touch controls (mobile) --></div>
  </div>

  <!-- Diagnostics overlay (dev mode only) -->
  <div id="diagnostics" hidden>...</div>

  <script>/* Play engine logic */</script>
</body>
</html>
```

### Key architectural decisions in play.html

**1. Game iframe sandbox**

```
sandbox="allow-scripts allow-same-origin"
```

- `allow-scripts` — games need JS
- `allow-same-origin` — games need `localStorage` for save states (future)
- No `allow-popups`, `allow-forms`, `allow-top-navigation` — games cannot escape their sandbox

**2. Touch controls rendered OUTSIDE the iframe**

This is the critical change from v1. Currently, touch controls are injected inside each game file (inside the iframe). This creates two problems:
- Controls scale with the game canvas (too small on mobile)
- Controls fight with game rendering for canvas space

In v2, the play engine renders touch controls in the host page, outside the iframe. The controls dispatch `postMessage` events to the iframe, which the touch bridge inside the game translates to keyboard events.

```
┌─ play.html (host) ────────────────────────────────────┐
│                                                        │
│  ┌─ Game iframe ────────────────────────────────────┐ │
│  │  Canvas (800x600, scaled to fit)                 │ │
│  │  No touch controls rendered here                 │ │
│  │  Touch bridge listens for postMessage            │ │
│  └──────────────────────────────────────────────────┘ │
│                                                        │
│  ┌─ Touch Controls (host DOM) ──────────────────────┐ │
│  │  Full-size buttons (56px), never scaled           │ │
│  │  Positioned below or beside game canvas           │ │
│  │  Sends postMessage({type:'key', code, action})    │ │
│  └──────────────────────────────────────────────────┘ │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**3. Dual-mode touch: internal fallback + external primary**

The injected in-game touch controls (from `inject-touch-controls.py`) remain as a fallback for when games are opened directly (double-click HTML file, no host page). But when a game is loaded inside the play engine, the host-side controls take priority and the in-game controls are suppressed via a `postMessage` signal:

```javascript
// Host → iframe: suppress internal touch controls
iframe.contentWindow.postMessage({ type: 'PV_HOST_CONTROLS', active: true }, '*');

// Inside game (touch-controls-template.js): check for host controls
window.addEventListener('message', (e) => {
  if (e.data?.type === 'PV_HOST_CONTROLS' && e.data.active) {
    document.getElementById('pv-touch-layer')?.remove();
  }
});
```

**4. Pre-play interstitial unlocks audio**

Mobile browsers require a user gesture to create an `AudioContext`. The pre-play "Tap to start" screen serves double duty:
- Shows the user what controls the game uses
- The tap event creates an `AudioContext` in the host page, which is passed to the iframe via `postMessage` timing coordination

**5. Keyboard focus management**

On load, `iframe.focus()` is called after the game loads. The host page intercepts only a few keys:
- `Escape` — show HUD / confirm exit (not immediate close)
- `F` — toggle fullscreen
- `Shift+?` — game info panel (proxied to iframe)
- All other keys reach the iframe naturally

---

## Part IV: Desktop Play Experience

### Theater Mode

When a desktop user clicks PLAY, the gallery navigates to `play.html`:

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│                  ┌────────────────────────────┐                  │
│                  │                            │                  │
│                  │     800 x 600 canvas       │                  │
│                  │     (or scaled to fit)      │                  │
│                  │                            │                  │
│                  │     Centered, sharp         │                  │
│                  │     No scaling artifacts    │                  │
│                  │                            │                  │
│                  └────────────────────────────┘                  │
│                                                                  │
│  [← Gallery]  Pac-Man · MAZ · 1980         [?] [⛶] [Next →]    │
│                                                                  │
│  Dark background with subtle scan-line texture                   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Desktop-specific optimizations

| Feature | Implementation |
|---------|---------------|
| Integer scaling | Scale game canvas to nearest integer multiple (1x, 2x) for pixel-perfect rendering. No fractional scaling blur. |
| Keyboard focus | `iframe.focus()` on load. Re-focus on click anywhere in stage. |
| Auto-hiding HUD | Toolbar visible for 3s, fades out. Mouse movement or `Escape` brings it back. |
| Quick-switch | `[` and `]` keys navigate to previous/next game in the current filter set. |
| Deep link share | URL `play.html?game=maz-001` is copy-pasteable, shows correct game on load. |
| Fullscreen | `F` key or button requests Fullscreen API on the stage container. |
| Exit confirmation | `Escape` shows HUD first. Second `Escape` within 2s returns to gallery. Prevents accidental exit. |
| No scroll | `overflow: hidden` on body. The game IS the page. |

### Display scaling logic

```javascript
function calculateScale(containerW, containerH) {
  const gameW = 800, gameH = 600;
  
  // Calculate max scale that fits
  const scaleX = containerW / gameW;
  const scaleY = containerH / gameH;
  const maxScale = Math.min(scaleX, scaleY);
  
  // For pixel art: snap to integer multiples when possible
  if (maxScale >= 2) return Math.floor(maxScale);
  if (maxScale >= 1) return 1;
  
  // Sub-1x scaling: use exact fit (mobile territory)
  return maxScale;
}
```

Integer scaling eliminates the blurriness that fractional CSS `transform: scale()` causes on pixel art. A 1600x900 monitor shows the game at 1x (centered) or could show it at 2x if fullscreened on a 1920x1080 display.

---

## Part V: Mobile Play Experience

### The mobile play problem, precisely stated

A phone screen is roughly 390x844 (portrait) or 844x390 (landscape). The game is 800x600. In portrait, the game scales to 48% — unplayable. In landscape, the game scales to 65% — better but touch controls now compete with the tiny canvas for the remaining 35% of vertical space.

### Solution: Landscape-locked, game-above-controls layout

```
┌─────────────────────────────────────────────────────────────────┐
│ LANDSCAPE (844 x 390 available after browser chrome)            │
│                                                                  │
│ ┌──────────────────────────────────────────────────────────────┐│
│ │                                                              ││
│ │              Game Canvas (800x600, scaled ~55%)              ││
│ │              Fills upper 70% of viewport                     ││
│ │              ~462 x 346 rendered pixels                      ││
│ │                                                              ││
│ ├──────────────────────────────────────────────────────────────┤│
│ │                                                              ││
│ │  ┌──────┐                                       ┌────────┐  ││
│ │  │ D-Pad│        CONTROL STRIP                  │ Action │  ││
│ │  │ 56px │     (dedicated space,                 │ Button │  ││
│ │  │      │      never overlaps game)             │  56px  │  ││
│ │  └──────┘                                       └────────┘  ││
│ │     Left thumb                                Right thumb    ││
│ └──────────────────────────────────────────────────────────────┘│
│                                                                  │
│ [Back]                              [?] [⛶] auto-hide after 3s │
└─────────────────────────────────────────────────────────────────┘
```

### Mobile-specific features

| Feature | Implementation |
|---------|---------------|
| Orientation hint | Pre-play screen shows "Rotate your device to landscape" with animated phone icon if user is in portrait |
| Orientation lock | `screen.orientation.lock('landscape')` requested on play start (Android Chrome honors it; iOS ignores it but users can lock in Control Center) |
| Full-screen request | `document.documentElement.requestFullscreen()` on "Tap to start" (hides browser chrome) |
| Control strip | Fixed height (100px), positioned below game canvas, never overlaps |
| Touch targets | 56px minimum (exceeds WCAG 2.5.5 44px minimum) |
| Haptic feedback | `navigator.vibrate(10)` on button press (Android, optional) |
| No pinch zoom | `user-scalable=no` on viewport meta + `touch-action: none` on stage |
| Safe area insets | `env(safe-area-inset-*)` CSS for notched phones |
| Portrait fallback | If user insists on portrait, game canvas gets upper 50%, controls get lower 50%. Playable but cramped. Letter shows "Rotate for best experience" bar. |

### Control strip layout (mobile)

The control strip is rendered by the host page (play.html), not inside the game iframe. It uses the game's METADATA `CONTROLS` field to select a profile:

```
Profile: dpad4+fire (e.g., Space Invaders)
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│   ┌───┐                                          ┌───────┐  │
│   │ ↑ │                                          │       │  │
│  ┌┴───┴┐                                         │ FIRE  │  │
│  │← · →│                                         │  ●    │  │
│  └┬───┬┘                                         │       │  │
│   │ ↓ │                                          └───────┘  │
│   └───┘                                                      │
│                                                              │
└──────────────────────────────────────────────────────────────┘

Profile: twin-stick (e.g., Robotron)
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│   ┌─────────┐                              ┌─────────┐      │
│   │  MOVE   │                              │  AIM    │      │
│   │   ◉     │                              │   ◉     │      │
│   │  (drag) │                              │  (drag) │      │
│   └─────────┘                              └─────────┘      │
│                                                              │
└──────────────────────────────────────────────────────────────┘

Profile: tap (e.g., Runner)
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│                    TAP ANYWHERE TO JUMP                       │
│                    (full control strip is tap zone)           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Host-to-iframe communication protocol

```javascript
// Host (play.html) → Game iframe
// Key press
iframe.contentWindow.postMessage({
  type: 'PV_KEY',
  code: 'ArrowLeft',    // KeyboardEvent.code
  key: 'ArrowLeft',     // KeyboardEvent.key
  action: 'keydown'     // 'keydown' or 'keyup'
}, '*');

// Host control mode active (suppress in-game touch layer)
iframe.contentWindow.postMessage({
  type: 'PV_HOST_CONTROLS',
  active: true
}, '*');

// Game iframe → Host (play.html)
// Score submission (for leaderboard)
parent.postMessage({
  type: 'PIXELVAULT_SCORE',
  score: 42000
}, '*');

// Game iframe → Host
// Audio readiness signal
parent.postMessage({
  type: 'PV_AUDIO_READY'
}, '*');
```

### Touch bridge (injected into games)

A small addition to the existing touch controls template — a `message` event listener that translates `PV_KEY` messages into native `KeyboardEvent` dispatches:

```javascript
// Added to touch-controls-template.js
window.addEventListener('message', (e) => {
  if (e.data?.type === 'PV_KEY') {
    document.dispatchEvent(new KeyboardEvent(e.data.action, {
      code: e.data.code,
      key: e.data.key,
      bubbles: true
    }));
  }
  if (e.data?.type === 'PV_HOST_CONTROLS' && e.data.active) {
    // Remove in-game touch layer (host provides controls)
    const layer = document.getElementById('pv-touch-layer');
    if (layer) layer.style.display = 'none';
  }
});
```

This is backward-compatible: if the game is opened directly (no host page), no `PV_KEY` messages arrive, and the in-game touch controls work as before.

---

## Part VI: Touch Control System v2

### What changes from v1

| Aspect | v1 (ADR-005, current) | v2 (this ADR) |
|--------|----------------------|----------------|
| Where controls render | Inside game iframe (injected into each HTML file) | Host page (play.html) — outside iframe |
| Control size | Scales with game canvas (shrinks on mobile) | Fixed 56px, never scales |
| Layout | Absolute-positioned on canvas | Dedicated control strip below canvas |
| Profiles | 10 profiles, auto-detected from METADATA | Same 10 profiles, read from manifest.json |
| Key dispatch | Direct `document.dispatchEvent(KeyboardEvent)` | Via `postMessage` to iframe → bridge dispatches |
| Fallback | N/A (controls are always in-game) | In-game controls remain for direct-open scenario |
| Game file modification | Required (injection adds ~1.5KB) | No change needed for v2 controls (bridge is tiny) |

### Profile resolution

The play engine reads the game's control profile from `manifest.json`:

```json
{
  "id": "maz-001-pacman",
  "controls": "Arrow keys",
  "touch_profile": "dpad4",
  "...": "..."
}
```

If `touch_profile` is not in the manifest, the play engine falls back to auto-detection from the `CONTROLS` metadata string (same logic as `inject-touch-controls.py`).

### Responsive control sizing

```javascript
function sizeControls(viewportW, viewportH, gameScaledH) {
  const availableH = viewportH - gameScaledH;
  const minControlH = 80;  // minimum usable height
  const maxControlH = 140; // don't waste too much space
  
  const controlH = Math.max(minControlH, Math.min(maxControlH, availableH));
  
  // If not enough room, switch to overlay mode (semi-transparent over game)
  if (availableH < minControlH) {
    return { mode: 'overlay', height: 100, opacity: 0.4 };
  }
  
  return { mode: 'strip', height: controlH, opacity: 1.0 };
}
```

The system prefers the dedicated strip. Only falls back to overlay (v1 behavior) if the viewport is extremely constrained (e.g., landscape on a very short phone with persistent browser chrome).

### Multitouch handling

The v1 touch system uses `setPointerCapture` for multitouch. This is preserved in v2 but moved to the host page:

- D-pad tracks one pointer (left thumb)
- Action button(s) track another pointer (right thumb)
- Both can be active simultaneously
- `pointermove` on captured pointer updates direction in real-time

---

## Part VII: Audio Engine and Timing Architecture

### The audio unlock problem

Mobile browsers block `AudioContext` creation until a user gesture (tap, click). In the current architecture:
1. User taps a game card in the gallery
2. Gallery opens a modal with an iframe
3. The iframe creates an `AudioContext` — but the tap event was on the gallery, not the iframe
4. Audio is blocked

**Fix:** The pre-play interstitial in `play.html` catches the user's "Tap to start" gesture and creates a shared `AudioContext`:

```javascript
let audioCtx = null;

document.getElementById('start-btn').addEventListener('click', () => {
  // Create audio context on user gesture
  audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  audioCtx.resume(); // Ensure running state
  
  // Notify iframe that audio is available
  // (games create their own AudioContext, but this gesture
  //  satisfies the browser's user-activation requirement
  //  for the iframe since we used allow="autoplay")
  loadGame();
});
```

The `allow="autoplay"` attribute on the iframe, combined with the user gesture on the host page, allows the iframe's `AudioContext` to activate.

### Timing: delta-time normalization

Many games have hardcoded timing:
```javascript
// Broken: runs 2x fast on 120Hz displays
function update() {
  player.x += speed; // same delta every frame
  requestAnimationFrame(update);
}
```

The correct pattern:
```javascript
// Fixed: frame-rate independent
let lastTime = 0;
function update(timestamp) {
  const dt = Math.min((timestamp - lastTime) / 1000, 0.05); // cap at 50ms
  lastTime = timestamp;
  player.x += speed * dt * 60; // normalize to 60fps baseline
  requestAnimationFrame(update);
}
```

**This ADR does NOT propose modifying all 460 games.** Instead:

1. **New games** must use delta-time (enforced by QA check, see Part IX)
2. **Frame-rate capping** can be applied at the iframe level by the host page using `requestAnimationFrame` throttling if needed (future enhancement)
3. **The performance instrumentation** (Part VIII) detects games with timing issues by measuring actual vs. expected update rates

### Audio quality guidelines for new/updated games

```javascript
// Standard audio setup (copy into any game)
const AudioCtx = window.AudioContext || window.webkitAudioContext;
let audioCtx = null;

function ensureAudio() {
  if (!audioCtx) {
    audioCtx = new AudioCtx();
  }
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
  return audioCtx;
}

function playTone(freq, duration, type = 'square', volume = 0.3) {
  const ctx = ensureAudio();
  const osc = ctx.createOscillator();
  const gain = ctx.createGain();
  osc.type = type;
  osc.frequency.value = freq;
  gain.gain.value = volume;
  gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
  osc.connect(gain);
  gain.connect(ctx.destination);
  osc.start(ctx.currentTime);
  osc.stop(ctx.currentTime + duration);
}
```

---

## Part VIII: Performance Instrumentation and Diagnostics

### Why this matters

When a game is "broken" on mobile, the QA dashboard just says "Broken" with a user-written note. There is no data about what went wrong. Was it a logic bug? A rendering stall? A 120Hz timing issue? A touch event that didn't register? Without instrumentation, debugging is guesswork.

### Frame timing collector

A lightweight performance monitor that runs in the play engine host page, measuring iframe rendering via `requestAnimationFrame`:

```javascript
class FrameTimingCollector {
  constructor() {
    this.samples = new Float64Array(300); // 5s at 60fps
    this.idx = 0;
    this.jankCount = 0;
    this.startTime = 0;
  }
  
  tick(timestamp) {
    if (this.startTime === 0) {
      this.startTime = timestamp;
      this.lastTime = timestamp;
      return;
    }
    
    const dt = timestamp - this.lastTime;
    this.lastTime = timestamp;
    this.samples[this.idx % 300] = dt;
    this.idx++;
    
    // Jank detection: frame took more than 2x expected (33ms at 60fps)
    if (dt > 33) this.jankCount++;
  }
  
  getStats() {
    const n = Math.min(this.idx, 300);
    const slice = this.samples.slice(0, n);
    const sorted = Float64Array.from(slice).sort();
    
    return {
      fps: Math.round(1000 / (slice.reduce((a,b) => a+b, 0) / n)),
      p50: sorted[Math.floor(n * 0.5)].toFixed(1),
      p95: sorted[Math.floor(n * 0.95)].toFixed(1),
      p99: sorted[Math.floor(n * 0.99)].toFixed(1),
      jankFrames: this.jankCount,
      jankRate: ((this.jankCount / this.idx) * 100).toFixed(1) + '%',
      totalFrames: this.idx,
      elapsed: ((this.lastTime - this.startTime) / 1000).toFixed(1) + 's'
    };
  }
}
```

### Diagnostics overlay (dev mode)

Activated by `?diag=1` query parameter on `play.html`:

```
┌─ DIAGNOSTICS (top-right corner) ──────┐
│  FPS: 60  │  p95: 17.2ms             │
│  Jank: 0.3%  │  Frames: 1847         │
│  Touch: 23ms avg latency             │
│  Audio: running | ctx: active         │
│  Scale: 0.55x  │  Mode: strip        │
│  Profile: dpad4+fire                  │
│  Input: 14 keys/s                     │
└───────────────────────────────────────┘
```

### Touch input latency measurement

```javascript
// Measure time from pointerdown to KeyboardEvent dispatch in iframe
let touchStartTime = 0;
let touchLatencySamples = [];

controlElement.addEventListener('pointerdown', () => {
  touchStartTime = performance.now();
  // ... dispatch postMessage to iframe
});

// When iframe confirms key received (optional, via postMessage ack)
window.addEventListener('message', (e) => {
  if (e.data?.type === 'PV_KEY_ACK') {
    const latency = performance.now() - touchStartTime;
    touchLatencySamples.push(latency);
  }
});
```

Target: touch-to-key latency < 16ms (one frame). Alert if consistently > 32ms.

### QA data export

The diagnostics system can export a JSON report for the QA dashboard:

```json
{
  "game": "maz-001-pacman",
  "platform": "mobile",
  "userAgent": "...",
  "viewport": "844x390",
  "session": {
    "duration": "45.2s",
    "fps": { "avg": 58, "p95": "17.2ms", "jankRate": "0.3%" },
    "touchLatency": { "avg": "12ms", "p95": "18ms" },
    "audio": "active",
    "scale": 0.55,
    "controlMode": "strip",
    "profile": "dpad4+fire"
  }
}
```

This data feeds back into the QA dashboard as structured performance evidence, replacing "it feels slow" with "p95 frame time is 34ms and jank rate is 12%."

---

## Part IX: Game Readiness Pipeline

### Automated pre-flight checks

Before a game ships to production, it must pass these checks (added to `tools/test-games.sh`):

| Check | Type | Blocks deploy? |
|-------|------|----------------|
| File < 50KB | Size | Yes |
| METADATA block present and valid | Structural | Yes |
| `requestAnimationFrame` used (not `setInterval`) | Performance | Yes |
| `if (infoOpen) return;` guard in update | Structural | Yes |
| No external URLs in `<script>` | Security | Yes |
| No `eval()` or `new Function()` | Security | Yes |
| Touch bridge `message` listener present | Mobile readiness | Warning |
| `CONTROLS` metadata matches a known profile | Mobile readiness | Warning |
| Delta-time pattern detected | Performance | Warning |
| `AudioContext` created with user-gesture guard | Audio | Warning |
| Canvas is 800x600 | Rendering | Warning |
| No `console.log` in production path | Quality | Warning |

### Game readiness score

Each game gets a readiness score (0-100) based on passing checks:

```
maz-001-pacman: 92/100
  ✓ Size (42.1KB)
  ✓ Metadata valid
  ✓ rAF loop
  ✓ Info panel guard
  ✓ No external URLs
  ✓ No eval
  ✓ Touch bridge present
  ✓ Profile: dpad4
  ⚠ No delta-time (hardcoded timing)
  ⚠ No audio
  ✓ Canvas 800x600
```

Games scoring below 70 get flagged for review before production promotion.

---

## Part X: Security Considerations

### iframe sandboxing

```html
<iframe sandbox="allow-scripts allow-same-origin" 
        allow="autoplay; fullscreen"
        referrerpolicy="no-referrer">
```

| Permission | Granted | Reason |
|------------|---------|--------|
| `allow-scripts` | Yes | Games are JavaScript |
| `allow-same-origin` | Yes | Same S3 origin, needed for `postMessage` |
| `allow-popups` | No | Games cannot open new windows |
| `allow-forms` | No | No form submission from games |
| `allow-top-navigation` | No | Games cannot navigate the host page |
| `allow-downloads` | No | No file downloads from games |

### postMessage validation

```javascript
// Host page validates messages from iframe
window.addEventListener('message', (e) => {
  // Only accept messages from our own iframe
  if (e.source !== document.getElementById('game').contentWindow) return;
  
  // Only accept known message types
  const allowed = ['PIXELVAULT_SCORE', 'PV_AUDIO_READY', 'PV_KEY_ACK'];
  if (!allowed.includes(e.data?.type)) return;
  
  // Type-specific validation
  if (e.data.type === 'PIXELVAULT_SCORE') {
    const score = Number(e.data.score);
    if (!Number.isFinite(score) || score < 0 || score > 999999999) return;
  }
  
  handleMessage(e.data);
});
```

### Content Security Policy

```html
<meta http-equiv="Content-Security-Policy" content="
  default-src 'self';
  script-src 'self' 'unsafe-inline';
  style-src 'self' 'unsafe-inline';
  img-src 'self' data:;
  connect-src 'self';
  frame-src 'self';
  media-src 'self';
">
```

`unsafe-inline` is required because games use inline `<script>` and `<style>` blocks. This is acceptable because all content is first-party (our games on our S3 bucket).

### No user data collection in play engine

The play engine stores no cookies, no localStorage, and transmits no analytics. Game session data (diagnostics) is ephemeral and only exported manually. Future leaderboard integration (ADR-006) handles score submission through a separate, validated API.

---

## Part XI: Phased Delivery Plan

### Phase 0: Play Engine Foundation (Sprint 1)

**Goal:** Dedicated play page works for desktop. Games open, keyboard works, back button returns to gallery.

**Deliverables:**
- [x] `play.html` — dedicated full-screen play page with iframe loading, auto-start HUD
- [x] Gallery integration — cards navigate to `play.html?game={id}`
- [x] Keyboard focus management (iframe auto-focus, Escape double-press confirmation)
- [x] Integer scaling for desktop (pixel-perfect at 2x/3x, 1x clean below 2x)
- [x] `sessionStorage` scroll position preservation for gallery return
- [x] Deep link support (`play.html?game=maz-001` loads correct game)

**Test gates:**
- [x] 10 games tested on Chrome, Firefox, Safari desktop
- [x] Keyboard input works immediately (no click-to-focus needed)
- [x] Back button returns to gallery at correct scroll position
- [x] Deep link URL loads directly from bookmark

### Phase 1: Mobile Play + External Touch Controls (Sprint 2)

**Goal:** Mobile users get landscape full-screen gameplay with usable touch controls.

**Deliverables:**
- [x] Mobile detection in gallery — [PLAY] opens `play.html` in new tab
- [x] Fullscreen API + orientation lock request on play start
- [x] Host-side touch controls (control strip below canvas)
- [x] `sendKey` direct injection from host to iframe (same-origin; lower latency than postMessage)
- [x] Touch bridge addition to `touch-controls-template.js` (PV_KEY + PV_HOST_CONTROLS)
- [x] Re-inject touch controls with bridge support (`inject-touch-controls.py` updated)
- [x] All 10 profiles implemented in host-side `buildTouchStrip()`
- [x] Haptic feedback on button press (`navigator.vibrate(8)`)
- [x] Portrait bar warning
- [ ] Pre-play interstitial removed — game auto-starts (simplified UX)

**Test gates:**
- [ ] 20 games tested on iPhone Safari + Android Chrome
- [x] Touch controls are usable without overlap on canvas
- [ ] Audio plays after play start
- [ ] Landscape lock engages on Android
- [x] Portrait fallback is playable (portrait bar warning shown)
- [x] All 10 touch profiles render correctly

### Phase 2: Audio, Timing, Performance Instrumentation (Sprint 3)

**Goal:** Sound works reliably, timing is consistent, diagnostics provide actionable data.

**Deliverables:**
- [ ] Audio context unlock via pre-play gesture
- [x] `FrameTimingCollector` in play engine (always-on, p50/p95/p99 + jank rate)
- [x] Diagnostics overlay (`?diag=1`)
- [x] Touch latency measurement (`ftc.touchDown()` / `ftc.touchAck()` via PV_KEY_ACK)
- [ ] QA JSON export from diagnostics
- [ ] Standardized `ensureAudio()` + `playTone()` template for new games
- [ ] Document delta-time pattern for game contributors

**Test gates:**
- [ ] Audio plays on first game load (iPhone Safari, Android Chrome, desktop)
- [x] Diagnostics overlay shows accurate FPS on all platforms (`?diag=1`)
- [ ] 10 games profiled — jank rate < 5% on mid-range phone (Pixel 6a or equivalent)
- [ ] Touch latency consistently < 20ms

### Phase 3: Game Readiness Pipeline + Gallery Polish (Sprint 4)

**Goal:** Automated quality checks, gallery UX improvements, production-ready.

**Deliverables:**
- [ ] Readiness score calculator in `test-games.sh`
- [ ] Delta-time pattern detector (warning, not blocking)
- [ ] Touch bridge presence checker
- [ ] Gallery pre-play card enhancement (controls diagram, profile badge)
- [ ] "Best on desktop" badge for twin-stick / complex control games
- [ ] QA dashboard integration — link to play engine with diagnostics
- [ ] Update deploy scripts to include `play.html` in production artifact
- [ ] Full regression test: all 317 Phase 1 games through play engine

**Test gates:**
- [ ] Readiness report runs on all 460 games without error
- [ ] Zero games below 50/100 readiness score in production track
- [ ] Gallery → play → gallery round-trip works on all target platforms
- [ ] Deploy to staging, verify play engine works via CloudFront

### Phase 4: Hardening + Edge Cases (Sprint 5)

**Goal:** Handle the long tail of device/browser combinations and failure modes.

**Deliverables:**
- [ ] iOS Safari fullscreen workaround (add-to-homescreen PWA pattern)
- [ ] Low-end device detection (reduce hero iframe count, disable animated previews)
- [ ] Network failure graceful degradation (game file fails to load → helpful error)
- [ ] Memory pressure detection (reduce diagnostics sampling on constrained devices)
- [ ] Offline game support investigation (service worker for cached games)
- [ ] Accessibility audit (screen reader announces game title, controls, exit path)
- [ ] Update ADR-005 status to "Superseded by ADR-012 for play experience"

**Test gates:**
- [ ] Tested on 5+ device types (iPhone SE, iPhone 15, iPad, Pixel, Samsung Galaxy)
- [ ] No memory leaks after 10 game switches
- [ ] Graceful error for network timeout
- [ ] Add-to-homescreen works on iOS Safari

---

## Part XII: Testing Strategy

### Device matrix

| Device | OS | Browser | Priority | Purpose |
|--------|-----|---------|----------|---------|
| iPhone 15 | iOS 17+ | Safari | P0 | Primary mobile target |
| iPhone SE | iOS 17+ | Safari | P1 | Small screen edge case |
| iPad Air | iPadOS 17+ | Safari | P1 | Tablet (no orientation lock) |
| Pixel 7/8 | Android 14+ | Chrome | P0 | Primary Android target |
| Samsung Galaxy | Android 13+ | Samsung Internet | P2 | Alt Android browser |
| MacBook | macOS | Chrome | P0 | Primary desktop |
| MacBook | macOS | Safari | P1 | WebKit desktop |
| Windows | Win 11 | Chrome | P1 | Non-Mac desktop |
| Windows | Win 11 | Firefox | P2 | Gecko engine |

### Test scenarios per game

1. **Load test** — game loads within 2s, no console errors
2. **Input test** — all control inputs register (keyboard on desktop, touch on mobile)
3. **Audio test** — sound plays on first user interaction (if game has audio)
4. **Timing test** — game runs at consistent speed (60fps target, 30fps acceptable)
5. **Exit test** — back button / Escape returns to gallery cleanly
6. **Orientation test** (mobile) — landscape and portrait both handled
7. **Fullscreen test** — enter/exit fullscreen doesn't break game state
8. **Multi-game test** — play 3 games in sequence, no memory leak

### Antifragile testing practices

1. **Fast-fail first** — every test script exits non-zero on first failure with clear error message
2. **Performance baselines** — store p95 frame times per game, alert on regression
3. **Chaos testing** — randomly toggle fullscreen, switch orientation, rapid game switching during automated tests
4. **Regression from fixes** — every bug fix includes a test that prevents recurrence
5. **Device-specific CI** — BrowserStack or Playwright device emulation for mobile matrix (Phase 4)

### Diagnostic-driven QA cycle

```
  Developer fixes game
       │
       ▼
  Run test-games.sh (structural/size) → FAIL? Stop.
       │
       ▼ PASS
  Open in play engine with ?diag=1
       │
       ▼
  Play for 30 seconds, export diagnostics JSON
       │
       ▼
  Diagnostics show jank < 5%, touch < 20ms, audio active?
       │
       ├── YES → Mark as OK in QA dashboard
       │
       └── NO  → File issue with diagnostics data attached
                  (not "it feels slow" — "p95=34ms, jankRate=12%")
```

---

## Decision Summary

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | **Separate play.html page, not modal** | Own the viewport: no gallery competition for space, keyboard, or events |
| 2 | **New tab on mobile, navigation on desktop** | Mobile tabs stay warm; desktop history is reliable |
| 3 | **Pre-play interstitial with "Tap to start"** | Unlocks AudioContext, shows controls, sets expectations |
| 4 | **Touch controls outside iframe (host page)** | Full-size controls, never scaled with game canvas |
| 5 | **postMessage bridge for key dispatch** | Clean iframe boundary; backward-compatible with direct-open |
| 6 | **Control strip below canvas, not overlaid** | Dedicated space prevents tap-target conflicts |
| 7 | **Integer scaling on desktop** | Pixel-perfect rendering, no blur on pixel art |
| 8 | **Performance instrumentation built-in** | Replace subjective QA with frame timing data |
| 9 | **Game readiness pipeline** | Automated quality gate before production deploy |
| 10 | **5-phase iterative delivery** | Desktop first (fast), mobile second (harder), instrumentation third, polish fourth, hardening fifth |
| 11 | **In-game touch controls as fallback, not primary** | Direct-open scenario still works; play engine scenario gets better controls |
| 12 | **Audio unlock via host page gesture** | Reliable cross-browser audio activation |

---

## Appendix A: Rejected Alternatives

| Alternative | Why Rejected |
|-------------|-------------|
| PWA with service worker (full offline) | Complexity not justified in Phase 1; 317 games = 14MB+ cache; revisit in Phase 4 |
| WebRTC gamepad for mobile controls | Over-engineering; virtual buttons are proven and simpler |
| Server-side frame rendering (cloud gaming) | Violates zero-dependency and offline playability principles |
| React/Vue for play engine | Framework adds bundle, build step, and complexity for what is a single-page player |
| Embed games via `<object>` or `<embed>` | Worse security model than iframe; no sandbox controls |
| Rewrite games to be responsive | Violates "no game logic changes" principle; 460 files is impractical |
| Portrait-only mobile with rotated canvas | CSS rotation of canvas is janky; actual landscape is cleaner |

## Appendix B: Compatibility with Existing ADRs

| ADR | Compatibility |
|-----|---------------|
| ADR-005 (Mobile Support Strategy) | Extended, not replaced. In-game touch injection remains for direct-open. Play engine adds host-side controls as primary path. |
| ADR-006 (Leaderboard) | Compatible. Score postMessage protocol unchanged. Play engine passes scores through. |
| ADR-008 (Monetization) | Compatible. Ads can be placed on pre-play interstitial (non-intrusive). |
| ADR-011 (Public Site Architecture) | Extended. play.html is a new file in the deployment artifact. Gallery's mobile flow updated to open play.html instead of game directly. |
| DESIGN-CONTRACT Section 6 | Compatible. Touch layer injection continues. Bridge listener is additive (~200 bytes). |

---

**Last Updated:** 2026-03-27  
**Version:** 1.0.0  
**Maintainer:** Joshua Ayson / OA LLC
