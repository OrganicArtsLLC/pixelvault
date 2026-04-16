# DRIFT — Game Design Document

**Version:** 1.0.0
**Date:** 2026-03-21
**Status:** Design Complete, Ready for Implementation

---

## One-Line Description

Leave a glowing trail that destroys enemies. Master momentum. Survive the void.

---

## Game Identity

| Property | Value |
|----------|-------|
| **Title** | DRIFT |
| **Genre** | Single-screen arena shooter |
| **Platform** | Web browser (HTML5 Canvas) |
| **Input** | Keyboard (arrow keys + spacebar) |
| **Resolution** | 800×600 canvas (scales to fit) |
| **Aspect Ratio** | 4:3 (retro CRT homage) |
| **Target FPS** | 60 |
| **Color Palette** | Dark void + neon (cyan, magenta, yellow) |

---

## Controls

| Key | Action |
|-----|--------|
| Arrow Keys / WASD | Thrust in direction |
| Space | Fire projectile |
| P / Escape | Pause |
| M | Toggle sound |
| Enter | Confirm (menus, high score entry) |

### Physics Feel

- **Thrust** accelerates the ship in the pressed direction
- **Momentum persists** when keys are released (ship drifts)
- **Gentle gravity** pulls ship downward (subtle, ~10% of thrust force)
- **Friction** gradually slows the ship (comes to stop over ~3 seconds)
- **Screen wraps** on all 4 edges (exit right, enter left)
- **Max speed** capped to prevent uncontrollable drifting

**Tuning Constants (starting values):**

```
THRUST_FORCE      = 0.15    # Acceleration per frame while key held
FRICTION          = 0.985   # Velocity multiplier per frame (1.0 = no friction)
GRAVITY           = 0.02    # Downward pull per frame
MAX_SPEED         = 4.0     # Maximum velocity magnitude
TRAIL_LIFESPAN    = 180     # Frames (3 seconds at 60fps)
TRAIL_SPAWN_RATE  = 3       # New trail segment every N frames
SHOT_SPEED        = 6.0     # Projectile velocity
SHOT_COOLDOWN     = 30      # Frames between shots (0.5 seconds)
```

---

## Core Mechanics

### 1. The Trail

The primary weapon. The ship continuously emits trail segments behind it as it moves.

**Behavior:**
- Trail segments are small circles (radius: 3-4px) placed at the ship's position
- New segment spawned every 3 frames (20 segments/second)
- Each segment lives for 3 seconds (180 frames)
- Segments fade from full opacity → transparent over their lifespan
- Segments damage and destroy enemies on contact
- Trail does NOT damage the player (safe to cross your own trail)
- Trail does NOT spawn while the ship is stationary (must be moving)

**Visual:**
- Full brightness: first 1 second (solid cyan glow)
- Fading: seconds 1-3 (gradual fade to transparent)
- Subtle bloom/glow effect around fresh trail segments

**Strategy Implications:**
- Moving constantly = maximum trail coverage = maximum killing surface
- Fast movement = wider-spaced trail (gaps enemies can slip through)
- Slow movement = dense trail (solid wall, but less coverage)
- Circling around enemies = encircling trap (satisfying!)

### 2. Shooting

Secondary weapon. Limited resource.

**Behavior:**
- Press Space to fire a projectile in the direction the ship is moving
- If ship is stationary, fires in the last movement direction
- Cooldown: 0.5 seconds between shots
- Projectile travels in straight line at fixed speed
- Projectile wraps with screen edges
- Projectile expires after crossing full screen width (~2 seconds)
- Projectile kills on contact (1 hit)

**Scoring difference:**
- Trail kill: **100 points** × chain multiplier
- Shot kill: **50 points**
- This incentivizes trail use over shooting

### 3. Chain Multiplier

**Behavior:**
- Each trail kill within 2 seconds of the previous trail kill increments the chain
- Chain counter: ×1, ×2, ×3, ×4... (no cap)
- If 2 seconds pass without a trail kill, chain resets to ×1
- Chain multiplier displayed prominently on screen
- Visual escalation: chain ×3+ triggers screen flash, ×5+ triggers screen shake

### 4. Energy Orbs

**Behavior:**
- Small golden orbs spawn at random locations each wave (2-4 per wave)
- Collecting: fly through the orb
- Effect: +25 points, trail lifespan extended by 0.5 seconds for 10 seconds
- Orbs tend to spawn near enemy clusters (risk/reward)
- Uncollected orbs persist across the wave

### 5. Lives System

- Start with 3 lives
- Lose a life when an enemy touches the SHIP (not the trail)
- On death: brief explosion animation, 2-second invincibility on respawn
- Respawn at center of screen
- All momentum zeroed on respawn
- Extra life at 10,000 points (one-time only)
- Game over when lives reach 0

---

## Enemies

### Drifter (Waves 1+)
- **Color:** Red
- **Shape:** Small diamond/square (8×8px)
- **Behavior:** Spawns at random screen edge, drifts in a straight line at constant speed
- **Speed:** Slow (1.0 - 1.5)
- **Bounces** off screen edges (does NOT wrap)
- **HP:** 1 (any hit kills)
- **Points:** 100 (trail) / 50 (shot)
- **Personality:** Mindless. The training dummy.

### Chaser (Waves 4+)
- **Color:** Magenta
- **Shape:** Triangle pointing toward player (10×10px)
- **Behavior:** Accelerates toward player's current position
- **Speed:** Moderate (starts slow, accelerates to 2.5)
- **Does NOT bounce** — wraps screen edges like player
- **HP:** 1
- **Points:** 150 (trail) / 75 (shot)
- **Personality:** Relentless. Forces you to keep moving.

### Splitter (Waves 8+)
- **Color:** Orange
- **Shape:** Large circle (14×14px)
- **Behavior:** Drifts like a Drifter but when killed, splits into 2 Mini-Splitters
- **Speed:** Slow (0.8)
- **HP:** 1 (but splits)
- **Points:** 200 (trail) / 100 (shot), minis are 50/25
- **Mini-Splitters:** Half size, faster (2.0), drift in opposite directions, do NOT split again
- **Personality:** Deceptive. Seems easy, creates chaos.

### Phaser (Waves 12+) [Stretch]
- **Color:** White (blinks)
- **Shape:** Flickering circle (10×10px)
- **Behavior:** Alternates between visible (vulnerable) and invisible (invulnerable) on 2-second cycle
- **Speed:** Moderate (1.5)
- **HP:** 1 (only while visible)
- **Points:** 200 (trail) / 100 (shot)
- **Personality:** Twitchy. Requires timing.

### Eraser (Waves 16+) [Stretch]
- **Color:** Purple with white outline
- **Shape:** X shape (12×12px)
- **Behavior:** Moves toward nearest trail segment and destroys trail on contact (does NOT die)
- **Speed:** Moderate (1.8)
- **HP:** 3 (requires 3 trail contacts OR 3 shots)
- **Points:** 300 (trail) / 150 (shot)
- **Personality:** The anti-trail. Forces aggressive shooting and movement changes.

---

## Wave System

### Wave Structure

Each wave defines:
- Enemy composition (types + counts)
- Spawn pattern (all at once, staggered, from specific edges)
- Clear condition: all enemies destroyed
- Brief "WAVE CLEAR" celebration (1.5 seconds)

### Wave Table (MVP - 15 waves, then loops with scaling)

| Wave | Drifters | Chasers | Splitters | Special | Total Threats |
|------|----------|---------|-----------|---------|---------------|
| 1 | 3 | - | - | - | 3 |
| 2 | 5 | - | - | - | 5 |
| 3 | 7 | - | - | 2 orbs | 7 |
| 4 | 4 | 2 | - | - | 6 |
| 5 | 5 | 3 | - | 3 orbs | 8 |
| 6 | 4 | 4 | - | - | 8 |
| 7 | 6 | 4 | - | 2 orbs | 10 |
| 8 | 3 | 3 | 2 | - | 8 (+4 minis) |
| 9 | 4 | 4 | 2 | 3 orbs | 10 (+4 minis) |
| 10 | 5 | 5 | 3 | - | 13 (+6 minis) |
| 11 | 6 | 5 | 3 | 2 orbs | 14 (+6 minis) |
| 12 | 5 | 6 | 4 | - | 15 (+8 minis) |
| 13 | 6 | 6 | 4 | 3 orbs | 16 (+8 minis) |
| 14 | 7 | 7 | 4 | - | 18 (+8 minis) |
| 15 | 8 | 8 | 5 | 4 orbs | 21 (+10 minis) |

**After wave 15:** Loop back to wave patterns with 1.2× speed multiplier each loop. Endless mode.

### Spawn Patterns

- **Edges:** Enemies spawn just off-screen at random edge positions
- **Staggered:** Not all at once — spawn over 2-3 seconds at wave start
- **Never spawn on player:** Minimum distance of 100px from player at spawn time

---

## Screens & Flow

### 1. Title Screen

```
╔══════════════════════════════════════╗
║                                      ║
║            ▓▓▓▓  ████  ████ █████    ║
║            █   █ █   █  ██  █        ║
║            █   █ ████   ██  ████     ║
║            █   █ █  █   ██  █        ║
║            ▓▓▓▓  █   █ ████ █        ║
║                                      ║
║         ← → ↑ ↓  THRUST             ║
║          SPACE   FIRE                ║
║                                      ║
║       YOUR TRAIL DESTROYS ENEMIES    ║
║                                      ║
║        PRESS ENTER TO START          ║
║                                      ║
║          HIGH SCORES: [S]            ║
╚══════════════════════════════════════╝
```

### 2. Gameplay Screen

```
╔══════════════════════════════════════╗
║ SCORE: 4,250    ×3 CHAIN    WAVE: 5 ║
║ ♥♥♥                                 ║
║                                      ║
║              ◇         ◆            ║
║     ～～～～▶                         ║
║        ～～    ◆                     ║
║    ～～                              ║
║  ～～           ●                    ║
║  ～                                  ║
║                    ▲                 ║
║              ◇                      ║
║                                      ║
║         ◆                ◇          ║
║                                      ║
╚══════════════════════════════════════╝

▶ = Player ship
～ = Trail (fading)
◆ = Drifter
▲ = Chaser
◇ = Energy orb
● = Splitter
```

### 3. Wave Clear Screen (overlay, 1.5 seconds)

```
         WAVE 5 CLEAR!
         BONUS: 2,500
         NO HIT BONUS: ×2
```

### 4. Game Over Screen

```
╔══════════════════════════════════════╗
║                                      ║
║            GAME  OVER                ║
║                                      ║
║         FINAL SCORE: 15,200          ║
║          WAVE REACHED: 12            ║
║         BEST CHAIN: ×7              ║
║                                      ║
║         NEW HIGH SCORE!              ║
║                                      ║
║         ENTER YOUR NAME:             ║
║           [A] S H                    ║
║          ↑↓ to change               ║
║          → next letter               ║
║          ENTER to confirm            ║
║                                      ║
╚══════════════════════════════════════╝
```

### 5. High Score Screen

```
╔══════════════════════════════════════╗
║          HIGH  SCORES                ║
║                                      ║
║    1. ASH .............. 15,200  W12 ║
║    2. JDA .............. 12,800  W10 ║
║    3. AMA ..............  9,450  W09 ║
║    4. BEN ..............  7,200  W08 ║
║    5. TOM ..............  5,800  W07 ║
║    6. LIL ..............  4,100  W06 ║
║    7. LUC ..............  3,600  W05 ║
║    8. JAC ..............  2,900  W04 ║
║    9. AAA ..............  1,500  W03 ║
║   10. ... ..............      0  W00 ║
║                                      ║
║       PRESS ENTER TO PLAY            ║
╚══════════════════════════════════════╝
```

---

## Visual Style

### Color Palette

| Element | Color | Hex |
|---------|-------|-----|
| Background | Near-black | #0a0a0f |
| Stars | Dim white | #333344 |
| Player ship | Bright cyan | #00ffff |
| Trail (fresh) | Cyan | #00ffff at 80% opacity |
| Trail (fading) | Dim cyan | #00ffff → 0% opacity |
| Drifter | Red | #ff3333 |
| Chaser | Magenta | #ff33ff |
| Splitter | Orange | #ff8833 |
| Energy orb | Gold | #ffdd33 |
| Projectile | White | #ffffff |
| Score text | White | #ffffff |
| Chain multiplier | Yellow → Red (escalating) | #ffff33 → #ff3333 |
| Wave text | Green | #33ff33 |
| UI text | Light gray | #aaaaaa |

### Retro Effects

- **CRT scanlines** — Subtle horizontal lines (very low opacity, 5-8%)
- **Pixel grid** — Render at 400×300 then scale up 2× (creates crisp pixel look)
- **Glow/bloom** — Trail and player have subtle additive glow (canvas shadow or post-process)
- **Screen flash** — Brief white flash on chain ×3+
- **Screen shake** — 2-3px shake on enemy kill, larger on death

### Sprite Design (Programmatic)

All sprites drawn with canvas primitives (no image files):

- **Player:** Small arrow/chevron shape, 8×8px logical, rotates to face movement direction
- **Drifter:** Rotating diamond, 6×6px
- **Chaser:** Triangle pointing at player, 8×8px
- **Splitter:** Circle, 10×10px, pulses slightly
- **Mini-Splitter:** Smaller circle, 5×5px
- **Energy orb:** Circle with sparkle, 6×6px, gentle pulse
- **Projectile:** Small bright dot, 3×3px
- **Trail segment:** Circle, 3px radius, with glow

---

## Audio Design (Web Audio API)

All sounds synthesized at runtime. Zero audio files.

### Sound Effects

| Sound | Trigger | Description |
|-------|---------|-------------|
| Thrust | While arrow key held | Low-frequency oscillator, subtle rumble |
| Shot | Fire projectile | Short high-frequency chirp (50ms) |
| Trail kill | Enemy touches trail | Crunchy noise burst + pitch-down (80ms) |
| Shot kill | Projectile hits enemy | Clean pop (60ms) |
| Chain bonus | Chain ×3, ×5, ×7+ | Ascending arpeggio (pitch increases with chain) |
| Orb collect | Player touches orb | Bright ascending tone (100ms) |
| Wave clear | All enemies dead | Three-note ascending chord (500ms) |
| Player death | Enemy touches ship | Descending noise sweep (300ms) |
| Game over | Last life lost | Low drone + descending sweep (1s) |
| Extra life | Score hits 10k | Rising arpeggio (400ms) |
| Menu select | Enter pressed | Click/blip (30ms) |

### Ambient

- **Background drone:** Very subtle low-frequency hum
- **Pitch increases** slightly with each wave (tension building)
- **Volume:** All effects at moderate volume, drone at low volume

---

## State Management

### Game States

```
TITLE → PLAYING → WAVE_CLEAR → PLAYING → ... → GAME_OVER → HIGH_SCORE_ENTRY → HIGH_SCORES → TITLE
                                                     ↑
                                              PAUSED ←→ PLAYING
```

### localStorage Schema

```json
{
  "drift_scores": [
    {"name": "ASH", "score": 15200, "wave": 12, "date": "2026-03-21"},
    {"name": "JDA", "score": 12800, "wave": 10, "date": "2026-03-21"},
    {"name": "AMA", "score": 9450, "wave": 9, "date": "2026-03-21"},
    {"name": "BEN", "score": 7200, "wave": 8, "date": "2026-03-21"},
    {"name": "TOM", "score": 5800, "wave": 7, "date": "2026-03-21"},
    {"name": "LIL", "score": 4100, "wave": 6, "date": "2026-03-21"},
    {"name": "LUC", "score": 3600, "wave": 5, "date": "2026-03-21"},
    {"name": "JAC", "score": 2900, "wave": 4, "date": "2026-03-21"},
    {"name": "AAA", "score": 1500, "wave": 3, "date": "2026-03-21"},
    {"name": "...", "score": 0, "wave": 0, "date": "2026-03-21"}
  ],
  "drift_version": "1.0.0"
}
```

### Default Scores (Pre-seeded)

Board starts full so it always looks populated. Default names use the Ayson family:

1. ASH — 5000 (Joshua's gaming initials from childhood)
2. AMA — 4500 (Amanda)
3. AND — 4000 (Andrew)
4. JAC — 3500 (Jacob)
5. LIL — 3000 (Lilia)
6. LUC — 2500 (Lucas)
7. JDA — 2000 (Jose David — birth father)
8. ANN — 1500 (Anneliese — adopted mom)
9. EDD — 1000 (Eddie — adopted dad)
10. OAL — 500 (OA LLC)

---

## Performance Considerations

- **Object pooling** for trail segments (recycle, don't garbage collect)
- **Spatial hashing** or simple distance checks for collision (no physics engine)
- **Trail limit:** Max 1000 active segments (oldest destroyed first if exceeded)
- **Draw calls:** Batch trail segments into single path operations
- **requestAnimationFrame** for render loop (not setInterval)
- **Delta time** for consistent physics regardless of frame rate

---

## Future Considerations

- **Deployment to joshuaayson.com** — Single HTML file, drop into Astro public folder
- **Blog post** — Write about the design process (arcade analysis → novel concept)
- **Mobile/touch** — Virtual joystick overlay for mobile play (v1.1)
- **Leaderboard API** — Optional: cloud leaderboard via simple API endpoint
- **Co-op mode** — Second player on same keyboard (WASD + left shift)
- **Level editor** — Custom enemy placement patterns

---

**Ready for implementation.**

**Last Updated:** 2026-03-21
**Version:** 1.0.0
