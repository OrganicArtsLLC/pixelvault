// ╔══════════════════════════════════════════════════════════════════╗
// ║  PIXEL VAULT TOUCH LAYER v1.0                                  ║
// ║  Mobile virtual controls — dispatch keyboard events to game.   ║
// ║                                                                ║
// ║  HOW TO ADD TO A NEW GAME:                                     ║
// ║  1. Identify the game's control profile (see PROFILES below)   ║
// ║  2. Append the block between the closing markers at the bottom ║
// ║     of this file to the game, just before </body>              ║
// ║  3. Change the argument on the last line to the profile name   ║
// ║  4. Add mobile_layout field to the game's METADATA comment     ║
// ║                                                                ║
// ║  PROFILES:                                                     ║
// ║    dpad2+fire  — ←→ + fire    (Breakout, Invaders)            ║
// ║    dpad4       — 4-way only   (Pac-Man, Racer)                 ║
// ║    dpad4+hold  — 4-way + hold (Qix)                            ║
// ║    asteroids   — 4-way + fire (Asteroids)                      ║
// ║    defender    — 4-way + fire + bomb (Defender)                ║
// ║    runner      — ←→ + jump   (Runner)                          ║
// ║    joust       — ←→ + flap   (Joust)                           ║
// ║    pong        — bilateral W/S + ↑↓ + serve (Pong)             ║
// ║    tetris      — 4-way + CCW rotate + hard drop (Tetris)       ║
// ║    twin-stick  — WASD move + Arrows shoot (Robotron)           ║
// ║                                                                ║
// ║  KEY DESIGN RULES:                                             ║
// ║  - Fire on document with bubbles:true (covers window listeners)║
// ║  - Set BOTH code AND key (covers Cluster A & Cluster B games)  ║
// ║  - pointer events (not touch) for multitouch + mouse compat    ║
// ║  - Touch layer is invisible on non-touch desktop               ║
// ║  - No game logic is changed — pure input translation           ║
// ╚══════════════════════════════════════════════════════════════════╝

// ── BEGIN TOUCH BLOCK (copy everything from here to END TOUCH BLOCK) ─────────
;(function(P) {
  'use strict';
  if (!('ontouchstart' in window) && navigator.maxTouchPoints < 1) return;

  // ── Styles ──────────────────────────────────────────────────────────────────
  var s = document.createElement('style');
  s.textContent =
    '#pvt{position:fixed;bottom:0;left:0;right:0;display:flex;' +
    'justify-content:space-between;align-items:flex-end;' +
    'padding:10px 14px;pointer-events:none;z-index:9999;' +
    'user-select:none;-webkit-user-select:none;}' +
    '.pvb{width:52px;height:52px;border-radius:50%;' +
    'background:rgba(255,255,255,.13);border:2px solid rgba(255,255,255,.28);' +
    'color:rgba(255,255,255,.8);font-size:19px;' +
    'display:flex;align-items:center;justify-content:center;' +
    'pointer-events:all;touch-action:none;cursor:pointer;' +
    'transition:background .07s,transform .07s;}' +
    '.pvb.on{background:rgba(255,255,255,.32);' +
    'border-color:rgba(255,255,255,.7);transform:scale(.9);}' +
    '.pvb.lg{width:64px;height:64px;font-size:24px;}' +
    '.pvb.red{border-color:rgba(255,80,80,.6);}' +
    '.pvb.grn{border-color:rgba(80,255,80,.6);}' +
    '.pvb.yel{border-color:rgba(255,200,60,.6);}' +
    '.pvd{display:grid;grid-template-columns:repeat(3,52px);' +
    'grid-template-rows:repeat(3,52px);gap:4px;}' +
    '.pvh{display:flex;gap:8px;align-items:flex-end;}' +
    '.pvac{display:flex;flex-direction:column;align-items:center;gap:8px;}' +
    '.pvar{display:flex;gap:8px;}';
  document.head.appendChild(s);

  // ── Overlay ──────────────────────────────────────────────────────────────────
  var ov = document.createElement('div');
  ov.id = 'pvt';
  document.body.appendChild(ov);

  // ── Key dispatch ─────────────────────────────────────────────────────────────
  // Fires on document with bubbles:true so both window (Cluster A) and
  // document (Cluster B) listeners receive the event.
  // Sets code AND key so e.code and e.key games both work correctly.
  function dn(c, k) {
    document.dispatchEvent(
      new KeyboardEvent('keydown', { code: c, key: k, bubbles: true, cancelable: true })
    );
  }
  function up(c, k) {
    document.dispatchEvent(
      new KeyboardEvent('keyup', { code: c, key: k, bubbles: true, cancelable: true })
    );
  }

  // Key pairs: [code, key]
  var K = {
    L:  ['ArrowLeft',  'ArrowLeft'],
    R:  ['ArrowRight', 'ArrowRight'],
    U:  ['ArrowUp',    'ArrowUp'],
    D:  ['ArrowDown',  'ArrowDown'],
    SP: ['Space',      ' '],
    W:  ['KeyW', 'w'],
    A:  ['KeyA', 'a'],
    S:  ['KeyS', 's'],
    D2: ['KeyD', 'd'],
    Z:  ['KeyZ', 'z']
  };

  // ── Button factory ────────────────────────────────────────────────────────────
  // Held button: fires keydown on press, keyup on release.
  // pointer events handle simultaneous touches correctly (multitouch).
  function btn(label, k, cls) {
    var el = document.createElement('div');
    el.className = 'pvb' + (cls ? ' ' + cls : '');
    el.innerHTML = label;
    el.addEventListener('pointerdown', function(e) {
      e.preventDefault();
      el.setPointerCapture(e.pointerId);
      el.classList.add('on');
      dn(k[0], k[1]);
    });
    el.addEventListener('pointerup', function(e) {
      e.preventDefault();
      el.classList.remove('on');
      up(k[0], k[1]);
    });
    el.addEventListener('pointercancel', function() {
      el.classList.remove('on');
      up(k[0], k[1]);
    });
    return el;
  }

  // ── Layout helpers ───────────────────────────────────────────────────────────
  // 4-way arrow d-pad (3×3 grid, corners empty)
  function dp4() {
    var g = document.createElement('div');
    g.className = 'pvd';
    [null, btn('▲',K.U), null,
     btn('◀',K.L), null, btn('▶',K.R),
     null, btn('▼',K.D), null].forEach(function(c) {
      var d = document.createElement('div');
      if (c) d.appendChild(c);
      g.appendChild(d);
    });
    return g;
  }
  // 4-way WASD d-pad (Robotron move stick)
  function dp4w() {
    var g = document.createElement('div');
    g.className = 'pvd';
    [null, btn('▲',K.W), null,
     btn('◀',K.A), null, btn('▶',K.D2),
     null, btn('▼',K.S), null].forEach(function(c) {
      var d = document.createElement('div');
      if (c) d.appendChild(c);
      g.appendChild(d);
    });
    return g;
  }
  // Horizontal pair (←→)
  function dp2h() {
    var g = document.createElement('div');
    g.className = 'pvh';
    g.appendChild(btn('◀',K.L));
    g.appendChild(btn('▶',K.R));
    return g;
  }
  // Vertical pair (↑↓) for custom key pair
  function dp2v(upK, dnK) {
    var g = document.createElement('div');
    g.className = 'pvac';
    g.appendChild(btn('▲',upK));
    g.appendChild(btn('▼',dnK));
    return g;
  }
  // Vertical action group
  function acv(arr) {
    var g = document.createElement('div');
    g.className = 'pvac';
    arr.forEach(function(e) { g.appendChild(e); });
    return g;
  }
  // Horizontal action row (for paired buttons like rotate CW/CCW)
  function acr(arr) {
    var g = document.createElement('div');
    g.className = 'pvar';
    arr.forEach(function(e) { g.appendChild(e); });
    return g;
  }
  // Append to left / right of overlay
  function L(el) { ov.appendChild(el); }
  function R(el) {
    var w = document.createElement('div');
    w.style.cssText = 'display:flex;align-items:flex-end;';
    w.appendChild(el);
    ov.appendChild(w);
  }

  // ── Profiles ─────────────────────────────────────────────────────────────────
  var profiles = {
    // Breakout, Invaders: left + right + fire
    'dpad2+fire': function() {
      L(dp2h());
      R(btn('⊙', K.SP, 'lg red'));
    },

    // Pac-Man, Racer: 4-way navigation, no action button
    'dpad4': function() {
      L(dp4());
    },

    // Qix: 4-way + hold button for fast-draw (Space held = 1.8× speed)
    'dpad4+hold': function() {
      L(dp4());
      R(acv([btn('▶▶', K.SP, 'yel')]));
    },

    // Asteroids: rotate (←→), thrust (↑), brake (↓), shoot (Space)
    // D-pad maps: ↑=thrust, ↓=brake, ←=rotate-left, →=rotate-right
    'asteroids': function() {
      L(dp4());
      R(acv([btn('⊙', K.SP, 'lg red')]));
    },

    // Defender: 4-way flight + shoot (Space) + smart bomb (Z)
    'defender': function() {
      L(dp4());
      R(acv([btn('⊙', K.SP, 'red'), btn('✦', K.Z, 'yel')]));
    },

    // Runner: left + right + variable-height jump (Space/↑ held)
    'runner': function() {
      L(dp2h());
      R(acv([btn('↑', K.SP, 'lg grn')]));
    },

    // Joust: left + right + flap (Space — fires keydown directly, not polled)
    'joust': function() {
      L(dp2h());
      R(acv([btn('▲', K.SP, 'lg')]));
    },

    // Pong: W/S (player 1 left) + ↑↓ (player 2 right) + Space serve (center)
    // Two-thumb layout for single-device two-player
    'pong': function() {
      L(dp2v(K.W, K.S));
      var ctr = document.createElement('div');
      ctr.style.cssText = 'display:flex;align-items:flex-end;padding-bottom:4px;';
      ctr.appendChild(btn('⬤', K.SP, 'grn'));
      ov.appendChild(ctr);
      R(dp2v(K.U, K.D));
    },

    // Tetris: 4-way (↑=rotateCW, ←→=move, ↓=softDrop) + Z=rotateCCW + Space=hardDrop
    'tetris': function() {
      L(dp4());
      R(acv([
        acr([btn('↻', K.U, 'grn'), btn('↺', K.Z, 'grn')]),
        btn('⬇', K.SP, 'lg red')
      ]));
    },

    // Robotron: WASD (move, left stick) + Arrows (shoot, right stick)
    'twin-stick': function() {
      L(dp4w());
      R(dp4());
    }
  };

  var build = profiles[P];
  if (build) build();

// ── Host-page postMessage bridge (v2) ────────────────────────────────────────
// When loaded inside play.html, the host renders controls outside the iframe
// and dispatches PV_KEY messages. This bridge converts those messages to native
// KeyboardEvents so the game code sees them identically to physical keystrokes.
// Also suppresses the in-game touch layer (#pvt) when host controls are active.
window.addEventListener('message', function(e) {
  if (!e.data || typeof e.data !== 'object') return;
  if (e.data.type === 'PV_KEY') {
    var fn = e.data.action === 'keydown' ? dn : up;
    if (e.data.code && e.data.key) {
      fn(e.data.code, e.data.key);
      // Acknowledge to host for latency measurement
      if (e.source) try { e.source.postMessage({ type: 'PV_KEY_ACK' }, '*'); } catch(_) {}
    }
  }
  if (e.data.type === 'PV_HOST_CONTROLS' && e.data.active) {
    var layer = document.getElementById('pvt');
    if (layer) layer.style.display = 'none';
  }
});

// ── END TOUCH BLOCK ──────────────────────────────────────────────────────────
// Change the profile string below to match the game:
})('dpad4');  // <── CHANGE THIS: the profile string for the specific game
