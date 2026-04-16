#!/usr/bin/env python3
"""
inject-touch-controls.py — Pixel Vault Touch Layer Injector

Injects the mobile touch controls block into every game prototype.
Safe to re-run: detects existing injection and skips or replaces.

Usage:
  python3 tools/inject-touch-controls.py           # inject all known + auto-detect rest
  python3 tools/inject-touch-controls.py --dry-run # preview only
  python3 tools/inject-touch-controls.py --remove  # strip existing touch blocks
  python3 tools/inject-touch-controls.py --verbose # show each file result
"""
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

# ── Default profile for games without an explicit mapping ────────────────────
# 'asteroids' = 4-way d-pad + Space fire button.
# Harmless for games that don't use Space; essential for those that do.
DEFAULT_PROFILE = "asteroids"

# ── Mouse-only keywords — skip injection for these games ─────────────────────
# Games whose primary input is mouse/click get touch-to-mouse synthesis from
# the browser automatically; a d-pad overlay would only confuse things.
MOUSE_ONLY_KEYWORDS = ("mouse", "click", "cursor")
KEYBOARD_KEYWORDS   = ("arrow", "wasd", "←", "→", "left", "right", "space", "jump", "shoot", "fire")

# ── Per-game profile overrides (explicit, hand-tuned) ────────────────────────
# Keys are relative paths from PROJECT_ROOT.
GAME_PROFILES: dict[str, str] = {
    "prototypes/def/def-001-pong.html":      "pong",
    "prototypes/def/def-002-breakout.html":  "dpad2+fire",
    "prototypes/fix/fix-001-invaders.html":  "dpad2+fire",
    "prototypes/phy/phy-001-asteroids.html": "asteroids",
    "prototypes/maz/maz-001-pacman.html":    "dpad4",
    "prototypes/trp/trp-001-qix.html":       "dpad4+hold",
    "prototypes/scr/scr-001-defender.html":  "defender",
    "prototypes/plt/plt-001-runner.html":    "runner",
    "prototypes/fgt/fgt-001-joust.html":     "joust",
    "prototypes/rac/rac-001-racer.html":     "dpad4",
    "prototypes/sht/sht-001-robotron.html":  "twin-stick",
    "prototypes/puz/puz-001-tetris.html":    "tetris",
}

# ── Files that must NOT receive the touch layer (already at/near 50KB limit) ─
# Each ~2.5KB touch block would push these over the hard 50KB constraint.
# Mouse-only games are auto-skipped by detect_profile(); these are skipped
# for size reasons only.
SKIP_FILES: frozenset[str] = frozenset({
    "prototypes/rpg/rpg-001-bards-tale.html",
    "prototypes/rpg/rpg-004-ultima.html",
    "prototypes/rpg/rpg-005-wasteland.html",
    "prototypes/plt/plt-003-castlevania.html",
    "prototypes/plt/plt-007-prince-of-persia.html",
    "prototypes/adv/adv-002-kings-quest.html",
})


def auto_detect_profile(controls: str) -> str | None:
    """
    Auto-detect the best touch profile from a game's CONTROLS metadata string.

    Returns None for mouse-only games (browser handles touch-to-mouse).
    Returns a profile string for keyboard-driven games.
    """
    c = controls.lower() if controls else ""

    has_mouse    = any(k in c for k in MOUSE_ONLY_KEYWORDS)
    has_keyboard = any(k in c for k in KEYBOARD_KEYWORDS)

    # Pure mouse/click games: skip — browser synthesises mouse events from touch
    if has_mouse and not has_keyboard:
        return None

    # Twin-stick: WASD (move) + Arrow keys (aim/fire) — Robotron style
    if "wasd" in c and "arrow" in c:
        return "twin-stick"

    # Tetris family: rotate + hard drop / soft drop
    if "rotat" in c and ("drop" in c or "hard" in c or "soft" in c):
        return "tetris"

    # Joust / flap mechanic
    if "flap" in c:
        return "joust"

    # Runner: lateral movement + jump (no significant up/down other than jump)
    if ("jump" in c) and ("left" in c or "←" in c or "right" in c or "→" in c):
        return "runner"

    # Pong / paddle: W/S bilateral paddles (usually "W/S" in controls)
    if "w/s" in c or ("w —" in c and "s —" in c):
        return "pong"

    # Lateral only + fire (no up/down): Breakout, Invaders, etc.
    lateral = ("left" in c or "←" in c) and ("right" in c or "→" in c)
    has_up   = "up" in c or "↑" in c
    has_down = "down" in c or "↓" in c
    if lateral and not has_up and not has_down and ("space" in c or "fire" in c or "shoot" in c):
        return "dpad2+fire"

    # Pure d-pad navigation: maze, racing with no fire
    if lateral and not ("space" in c or "fire" in c or "shoot" in c or "attack" in c or "jump" in c):
        return "dpad4"

    # Default: 4-way d-pad + Space fire — works for most action/platformer games
    return DEFAULT_PROFILE

# ── Touch block template ──────────────────────────────────────────────────────
# {profile} is replaced with the actual profile string per game.
TOUCH_BLOCK_TEMPLATE = """\
<script>
/* ── Pixel Vault Touch Layer v1.0 — profile: {profile} ── */
;(function(P){{
'use strict';if(!('ontouchstart' in window)&&navigator.maxTouchPoints<1)return;
var s=document.createElement('style');
s.textContent=
  '#pvt{{position:fixed;bottom:0;left:0;right:0;display:flex;'+
  'justify-content:space-between;align-items:flex-end;'+
  'padding:10px 14px;pointer-events:none;z-index:9999;'+
  'user-select:none;-webkit-user-select:none;}}'+
  '.pvb{{width:52px;height:52px;border-radius:50%;'+
  'background:rgba(255,255,255,.13);border:2px solid rgba(255,255,255,.28);'+
  'color:rgba(255,255,255,.8);font-size:19px;'+
  'display:flex;align-items:center;justify-content:center;'+
  'pointer-events:all;touch-action:none;cursor:pointer;'+
  'transition:background .07s,transform .07s;}}'+
  '.pvb.on{{background:rgba(255,255,255,.32);'+
  'border-color:rgba(255,255,255,.7);transform:scale(.9);}}'+
  '.pvb.lg{{width:64px;height:64px;font-size:24px;}}'+
  '.pvb.red{{border-color:rgba(255,80,80,.6);}}'+
  '.pvb.grn{{border-color:rgba(80,255,80,.6);}}'+
  '.pvb.yel{{border-color:rgba(255,200,60,.6);}}'+
  '.pvd{{display:grid;grid-template-columns:repeat(3,52px);'+
  'grid-template-rows:repeat(3,52px);gap:4px;}}'+
  '.pvh{{display:flex;gap:8px;align-items:flex-end;}}'+
  '.pvac{{display:flex;flex-direction:column;align-items:center;gap:8px;}}'+
  '.pvar{{display:flex;gap:8px;}}';
document.head.appendChild(s);
var ov=document.createElement('div');ov.id='pvt';document.body.appendChild(ov);
function dn(c,k){{document.dispatchEvent(new KeyboardEvent('keydown',{{code:c,key:k,bubbles:true,cancelable:true}}));}}
function up(c,k){{document.dispatchEvent(new KeyboardEvent('keyup',  {{code:c,key:k,bubbles:true,cancelable:true}}));}}
var K={{L:['ArrowLeft','ArrowLeft'],R:['ArrowRight','ArrowRight'],
  U:['ArrowUp','ArrowUp'],D:['ArrowDown','ArrowDown'],SP:['Space',' '],
  W:['KeyW','w'],A:['KeyA','a'],S:['KeyS','s'],D2:['KeyD','d'],Z:['KeyZ','z']}};
function btn(lbl,k,cls){{
  var el=document.createElement('div');
  el.className='pvb'+(cls?' '+cls:'');el.innerHTML=lbl;
  el.addEventListener('pointerdown',function(e){{e.preventDefault();el.setPointerCapture(e.pointerId);el.classList.add('on');dn(k[0],k[1]);}});
  el.addEventListener('pointerup',function(e){{e.preventDefault();el.classList.remove('on');up(k[0],k[1]);}});
  el.addEventListener('pointercancel',function(){{el.classList.remove('on');up(k[0],k[1]);}});
  return el;}}
function dp4(){{
  var g=document.createElement('div');g.className='pvd';
  [null,btn('&#9650;',K.U),null,btn('&#9664;',K.L),null,btn('&#9654;',K.R),null,btn('&#9660;',K.D),null].forEach(function(c){{var d=document.createElement('div');if(c)d.appendChild(c);g.appendChild(d);}});
  return g;}}
function dp4w(){{
  var g=document.createElement('div');g.className='pvd';
  [null,btn('&#9650;',K.W),null,btn('&#9664;',K.A),null,btn('&#9654;',K.D2),null,btn('&#9660;',K.S),null].forEach(function(c){{var d=document.createElement('div');if(c)d.appendChild(c);g.appendChild(d);}});
  return g;}}
function dp2h(){{var g=document.createElement('div');g.className='pvh';g.appendChild(btn('&#9664;',K.L));g.appendChild(btn('&#9654;',K.R));return g;}}
function dp2v(u,d){{var g=document.createElement('div');g.className='pvac';g.appendChild(btn('&#9650;',u));g.appendChild(btn('&#9660;',d));return g;}}
function acv(a){{var g=document.createElement('div');g.className='pvac';a.forEach(function(e){{g.appendChild(e);}});return g;}}
function acr(a){{var g=document.createElement('div');g.className='pvar';a.forEach(function(e){{g.appendChild(e);}});return g;}}
function L(el){{ov.appendChild(el);}}
function R(el){{var w=document.createElement('div');w.style.cssText='display:flex;align-items:flex-end;';w.appendChild(el);ov.appendChild(w);}}
var profiles={{
  'dpad2+fire':function(){{L(dp2h());R(btn('&#8857;',K.SP,'lg red'));}},
  'dpad4':function(){{L(dp4());}},
  'dpad4+hold':function(){{L(dp4());R(acv([btn('&#9193;',K.SP,'yel')]));}},
  'asteroids':function(){{L(dp4());R(acv([btn('&#8857;',K.SP,'lg red')]));}},
  'defender':function(){{L(dp4());R(acv([btn('&#8857;',K.SP,'red'),btn('&#10022;',K.Z,'yel')]));}},
  'runner':function(){{L(dp2h());R(acv([btn('&#8679;',K.SP,'lg grn')]));}},
  'joust':function(){{L(dp2h());R(acv([btn('&#9650;',K.SP,'lg')]));}},
  'pong':function(){{
    L(dp2v(K.W,K.S));
    var c=document.createElement('div');c.style.cssText='display:flex;align-items:flex-end;padding-bottom:4px;';c.appendChild(btn('&#9679;',K.SP,'grn'));ov.appendChild(c);
    R(dp2v(K.U,K.D));}},
  'tetris':function(){{
    L(dp4());
    R(acv([acr([btn('&#8635;',K.U,'grn'),btn('&#8634;',K.Z,'grn')]),btn('&#11015;',K.SP,'lg red')]));}},
  'twin-stick':function(){{L(dp4w());R(dp4());}},
}};
var build=profiles[P];if(build)build();
// ── Host-page postMessage bridge (v2) ───────────────────────────────────────
window.addEventListener('message',function(e){{
  if(!e.data||typeof e.data!=='object')return;
  if(e.data.type==='PV_KEY'){{
    var fn=e.data.action==='keydown'?dn:up;
    if(e.data.code&&e.data.key){{
      fn(e.data.code,e.data.key);
      if(e.source)try{{e.source.postMessage({{type:'PV_KEY_ACK'}},'*');}}catch(_){{}}
    }}
  }}
  if(e.data.type==='PV_HOST_CONTROLS'&&e.data.active){{
    var layer=document.getElementById('pvt');
    if(layer)layer.style.display='none';
  }}
}});
}})("{profile}");
</script>"""

# ── Marker for detecting existing injection ───────────────────────────────────
INJECTION_MARKER = "/* ── Pixel Vault Touch Layer v1.0"


def inject_game(path: Path, profile: str, dry_run: bool = False, remove: bool = False) -> str:
    """
    Inject (or remove) the touch block in a game HTML file.

    Args:
        path: Absolute path to game HTML file.
        profile: Touch control profile name.
        dry_run: If True, return what would be written without writing.
        remove: If True, strip existing touch block instead of adding.

    Returns:
        Status string for display.
    """
    content = path.read_text(encoding="utf-8")

    # ── Remove existing block if present ──────────────────────────────────────
    existing_pattern = re.compile(
        r"\n<script>\n/\* ── Pixel Vault Touch Layer v1\.0.*?</script>",
        re.DOTALL,
    )
    had_block = bool(existing_pattern.search(content))
    content_stripped = existing_pattern.sub("", content)

    if remove:
        if had_block:
            if not dry_run:
                path.write_text(content_stripped, encoding="utf-8")
            return f"  REMOVED  {path.name}"
        else:
            return f"  SKIPPED  {path.name} (no block found)"

    # ── Build new touch block ─────────────────────────────────────────────────
    touch_block = TOUCH_BLOCK_TEMPLATE.format(profile=profile)

    # Insert before </body>
    if "</body>" not in content_stripped:
        return f"  ERROR    {path.name} — no </body> tag found"

    new_content = content_stripped.replace("</body>", touch_block + "\n</body>", 1)

    if not dry_run:
        path.write_text(new_content, encoding="utf-8")

    verb = "DRY-RUN" if dry_run else ("UPDATED" if had_block else "INJECTED")
    return f"  {verb}  {path.name}  [{profile}]"


def load_controls_map() -> dict[str, str]:
    """
    Load manifest.json and build a {relative_path: controls_string} map.

    Returns:
        Dict mapping each game's relative file path to its CONTROLS metadata.
    """
    manifest_path = PROJECT_ROOT / "manifest.json"
    if not manifest_path.exists():
        print("  WARNING: manifest.json not found — falling back to default profile for all unlisted games")
        return {}

    with manifest_path.open(encoding="utf-8") as f:
        manifest = json.load(f)

    # manifest entries have a "file" field like "prototypes/maz/maz-001-pacman.html"
    # and a "controls" field with the keyboard instructions string.
    result: dict[str, str] = {}
    for entry in manifest.get("prototypes", manifest if isinstance(manifest, list) else []):
        file_key = entry.get("file", "")
        controls = entry.get("controls", "")
        if file_key:
            result[file_key] = controls
    return result


def collect_game_files() -> list[Path]:
    """
    Collect all .html game files from prototypes/ and ai-archaeology/.

    Note: ai-evolution/ is intentionally excluded — those games are filtered
    from the mobile gallery and don't need the touch layer added in bulk.

    Returns:
        Sorted list of absolute paths.
    """
    dirs = [PROJECT_ROOT / "prototypes", PROJECT_ROOT / "ai-archaeology"]
    files: list[Path] = []
    for d in dirs:
        if d.exists():
            files.extend(sorted(d.rglob("*.html")))
    return files


def main() -> None:
    """Run the injector against all known + auto-detected game files."""
    dry_run  = "--dry-run"  in sys.argv
    remove   = "--remove"   in sys.argv
    verbose  = "--verbose"  in sys.argv

    print("Pixel Vault Touch Layer Injector")
    print(f"Mode: {'DRY RUN' if dry_run else ('REMOVE' if remove else 'INJECT ALL')}")
    print("-" * 60)

    controls_map = load_controls_map()
    all_files    = collect_game_files()

    ok = skipped = errors = 0

    for path in all_files:
        rel = str(path.relative_to(PROJECT_ROOT))

        # ── Skip oversized files that can't fit the touch block ───────────────
        if rel in SKIP_FILES:
            if verbose:
                print(f"  SKIPPED  {path.name}  [size limit — no touch layer]")
            skipped += 1
            continue

        # ── Resolve profile ───────────────────────────────────────────────────
        if rel in GAME_PROFILES:
            profile = GAME_PROFILES[rel]
            source  = "override"
        else:
            controls = controls_map.get(rel, "")
            profile  = auto_detect_profile(controls)
            source   = "auto"

        # None means mouse-only — skip injection
        if profile is None:
            if verbose:
                print(f"  SKIPPED  {path.name}  [mouse-only — browser handles]")
            skipped += 1
            continue

        result = inject_game(path, profile, dry_run=dry_run, remove=remove)

        # Check size after inject
        if not dry_run and not remove and path.exists():
            size = path.stat().st_size
            if size > 51200:
                result += f"  ⚠ SIZE {size:,}B > 50KB"

        if verbose or "ERROR" in result or "MISSING" in result or "⚠" in result:
            tag = f"[{source}]" if verbose else ""
            print(f"{result} {tag}")

        if "ERROR" in result or "MISSING" in result:
            errors += 1
        else:
            ok += 1

    total = len(all_files)
    print("-" * 60)
    print(f"Done. {ok} processed, {skipped} skipped (mouse-only), {errors} errors — {total} total files scanned.")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
