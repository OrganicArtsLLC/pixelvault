# ADR-001: Retro Arcade Game Concept Selection

**Status:** Proposed
**Date:** 2026-03-21
**Author:** Joshua Ayson / OA LLC
**Project:** Pixel Vault
**Deployment Target:** joshuaayson.com (single-page, static hosting)

---

## Context

Design a novel single-screen retro arcade game for web deployment. The game should feel authentic to the golden age of arcade gaming (1978-1986) while introducing a genuinely new mechanic born from analyzing what made the classics great.

### Inspiration Sources (Joshua's Gaming DNA)

| Game | Year | Core Mechanic | Why It Worked |
|------|------|--------------|---------------|
| Space Invaders | 1978 | Fixed shooter, marching enemies | Escalating tempo creates psychological pressure |
| Defender | 1981 | Side-scroll rescue shooter | Purpose beyond shooting (save humans) |
| Joust | 1982 | Flap-to-fly, height-wins combat | Satisfying physics, skill-based movement |
| Moon Patrol | 1982 | Auto-scroll, jump + multi-shoot | Multi-axis threat management |
| Centipede | 1980 | Trackball shooter, mushroom field | Player actions reshape the battlefield |
| Lode Runner | 1983 | Dig traps, collect gold, no jump | Trap mechanic + puzzle + emergent AI |
| Mario Bros | 1983 | Bump-from-below, kick, pipes | Two-phase enemy defeat, co-op potential |
| Ikari Warriors | 1986 | Top-down run-and-gun | Rotational aiming, vehicles |
| Astrosmash | 1981 | Fixed shooter, falling debris | Score can go negative (Intellivision classic) |

### Platform Constraints

- **Single HTML page** - Canvas-based rendering, no server required
- **Static hosting** - S3 + CloudFront via joshuaayson.com
- **Local storage** - High scores persist in browser localStorage
- **Input** - Keyboard primary (arrow keys + 1-2 buttons), touch as stretch goal
- **Performance** - 60fps on modern browsers, minimal assets
- **Size** - Under 500KB total (no heavy frameworks)

---

## Analysis: What Makes Arcade Games Timeless

After studying the mechanical DNA of 15+ golden-age games, ten design patterns emerge that separate "played once" from "played forever":

### The Ten Arcade Commandments

1. **Escalating Tension** - Every great arcade game gets harder. Space Invaders speeds up as you kill. Centipede gets denser. The player must constantly adapt.

2. **Player Actions Reshape the Battlefield** - In Centipede, every shot creates a mushroom obstacle. In Lode Runner, you dig the terrain. The arena is never the same twice.

3. **Multi-Threat Management** - Moon Patrol has ground hazards AND aerial enemies. Defender has abductors AND landers AND bombers. The brain must split focus.

4. **Satisfying Physics** - Joust's flap-and-drift. Asteroids' momentum. The way a Centipede segment splits. The game FEELS good in your hands before you understand the rules.

5. **Risk/Reward Tension** - Top rows in Space Invaders score higher but are harder to hit. Joust eggs must be collected before they hatch. Greed kills, but restraint bores.

6. **One More Try Factor** - Death is quick. Restart is instant. The player always feels like they were ONE decision away from surviving. This is the addiction loop.

7. **Emergent Complexity** - Simple rules create surprising situations. Two enemies colliding. Chain reactions. A trap catching three enemies instead of one. The player discovers tactics the designer didn't plan.

8. **Audio as Game State** - Space Invaders' heartbeat IS the tempo. Pac-Man's siren means ghosts are dangerous. Sound communicates what your eyes can't see. Great arcade sound design is informational, not decorative.

9. **Immediate Legibility** - You understand the game in 5 seconds of watching someone else play. No tutorial. No text. The visual language teaches.

10. **Simple Input, Complex Output** - Two buttons and a stick create infinite tactical situations. The constraint IS the design space.

---

## Three Candidate Concepts

Each concept synthesizes specific classic mechanics into a novel combination. All are single-screen, simple-control, retro-aesthetic games.

---

### Concept A: "DRIFT" (Recommended)

**Elevator Pitch:** You leave a temporary glowing trail behind you. The trail destroys enemies. Lay traps, lure enemies through your wake, survive the void.

**Mechanical DNA:**
- **Joust** → Momentum-based physics with gravity (flap/thrust feel)
- **Tron Light Cycles** → Trail concept (but temporary, not fatal to self)
- **Lode Runner** → Trap mechanic (trail IS the trap)
- **Asteroids** → Screen wrap, inertia, spatial awareness
- **Space Invaders** → Wave escalation

**Controls:**
- Arrow keys (or WASD): Thrust in 4 directions
- Space: Fire projectile (limited, recharges)
- Movement is momentum-based (drift after releasing keys)

**Core Loop:**
1. Move through the arena, leaving a glowing trail (2-3 second lifespan)
2. Enemies that touch your trail are destroyed
3. Direct shots also kill but are limited
4. Survive each wave — enemies escalate in speed, count, behavior
5. Collect energy orbs for bonus score + trail length extension
6. Every 5 waves: a boss pattern (large enemy, unique behavior)

**Why It's Novel:**
- "Trail as weapon" has never been the PRIMARY mechanic in an arcade game
- Tron's light cycles were obstacles, not weapons. This inverts that.
- Players must think about WHERE they've been, not just where they're going
- Creates beautiful visual patterns (glowing trails in dark void)
- Emergent trap-setting: circle an enemy to box them in with trail

**Enemy Types (escalating introduction):**
| Wave | Enemy | Behavior |
|------|-------|----------|
| 1-3 | Drifter | Floats in straight lines, bounces off walls |
| 4-6 | Chaser | Follows player at moderate speed |
| 7-9 | Phaser | Blinks in/out of existence (immune while invisible) |
| 10+ | Splitter | Splits into 2 smaller enemies when hit by trail |
| 15+ | Eraser | Destroys your trail on contact instead of dying |
| Boss | Void Worm | Snakes around screen, must be encircled by trail |

**Risk/Reward:**
- Longer trails = more killing surface but also more screen commitment
- Moving fast = longer trail but harder to control (momentum)
- Staying still = safe but trail vanishes, leaving you exposed
- Collecting orbs extends trail but orbs spawn near enemy clusters

**Visual Identity:**
- Black void with subtle star field
- Player ship: bright cyan/white, pixel-art style
- Trail: fading gradient (bright → dim → gone)
- Enemies: warm colors (red, orange, magenta)
- Explosions: pixel-burst particles
- CRT scanline overlay for authenticity

**Audio Design:**
- Ambient low hum (increases pitch with wave number)
- Trail: subtle synthesized "whoosh" while moving
- Enemy destruction: classic arcade pop/crunch
- Shot fired: tight laser chirp
- Wave clear: ascending arpeggio
- All synthesized at runtime (Web Audio API, zero file overhead)

**Difficulty Curve:**
- Waves 1-3: Learn movement, trail, 3-5 slow drifters
- Waves 4-6: Chasers introduced, 6-8 enemies mixed
- Waves 7-9: Phasers, first real difficulty spike, 8-12 enemies
- Waves 10+: Splitters multiply the threat count
- Waves 15+: Erasers force you to keep moving (can't rely on trail walls)
- Every 5th wave: Boss encounter

**Score System:**
- Trail kill: 100 pts × chain multiplier (consecutive kills without pause)
- Shot kill: 50 pts (deliberate incentive to use trail over shooting)
- Orb collect: 25 pts
- Wave clear bonus: 500 × wave number
- No-hit wave bonus: 2x multiplier on wave clear

---

### Concept B: "RICOCHET"

**Elevator Pitch:** Your shots bounce off walls. Each bounce makes them stronger. Master the geometry of the arena to chain ricochets through enemy formations.

**Mechanical DNA:**
- **Space Invaders** → Fixed(ish) shooter format, wave-based enemies
- **Breakout/Arkanoid** → Ball-bounce angle physics
- **Billiards** → Geometry, angles, planning shots
- **Centipede** → Destructible mid-field obstacles that redirect shots

**Controls:**
- Left/Right: Move along bottom of screen
- Up/Down: Adjust shot angle (displayed as aim line)
- Space: Fire

**Core Loop:**
1. Enemies descend/patrol in the upper 2/3 of the screen
2. Aim your shot angle and fire
3. Shots ricochet off left/right walls (and later, off placed barriers)
4. Each wall bounce: damage × 2 (direct = 1x, 1 bounce = 2x, 2 bounces = 4x)
5. Some enemies require ricochet hits (shielded on front, vulnerable on back)
6. Destructible barriers in mid-screen deflect shots at angles
7. Enemy shots ALSO ricochet (later waves)

**Why It's Novel:**
- Geometry-as-gameplay in a shooter is underexplored
- The "bouncing buff" mechanic rewards skill and planning
- Turns a simple shooter into a spatial reasoning puzzle
- Enemy ricochets in later waves create beautiful chaos

**Strengths:** Immediately understandable, clean arcade format, great skill ceiling
**Weaknesses:** Less movement freedom (bottom-of-screen), may feel static at lower skill levels

---

### Concept C: "WARDEN"

**Elevator Pitch:** You guard a space prison. Inmates escape upward. Alien ships try to extract them. Zap platforms to create traps. If an inmate escapes, they return armed.

**Mechanical DNA:**
- **Joust** → Flap-to-fly physics, platform arena, wrap-around screen
- **Lode Runner** → Dig/trap mechanic (zap platforms to create gaps)
- **Defender** → Rescue/abduction mechanic (prevent extraction)
- **Mario Bros** → Pipes, platform layout, bump-from-below feel
- **Space Invaders** → Wave escalation, increasing tempo

**Controls:**
- Left/Right: Move horizontally
- Up (tap repeatedly): Flap upward (Joust physics)
- Space: Fire weapon
- Down: Zap platform below you (creates temporary gap/trap)

**Core Loop:**
1. Inmates climb upward through platforms toward the top
2. Alien extraction ships hover at the top waiting for inmates
3. Fly around, shoot extraction ships before they grab inmates
4. Zap platforms under inmates to trap them (they fall back down)
5. If an inmate reaches an extraction ship: they leave and RETURN as an armed enemy
6. Clear all inmates to advance to next wave
7. Escalation: more inmates, faster movement, armed returnees from previous waves

**Why It's Novel:**
- Combines five distinct classic mechanics into one coherent system
- The "consequences compound" design: each failure makes future waves harder
- Trap placement creates a Lode Runner-style tactical layer
- Emotional stakes: every extraction is YOUR failure coming back to haunt you

**Strengths:** Deepest gameplay, strongest narrative frame, most mechanical variety
**Weaknesses:** Most complex to balance, Joust physics are hard to get right, steepest learning curve

---

## Decision Matrix

| Criterion | DRIFT | RICOCHET | WARDEN |
|-----------|-------|----------|--------|
| **Novelty** | 9/10 | 7/10 | 8/10 |
| **Simple to learn** | 8/10 | 9/10 | 5/10 |
| **Depth of mastery** | 8/10 | 7/10 | 9/10 |
| **Visual appeal** | 10/10 | 6/10 | 7/10 |
| **Implementation complexity** | Medium | Low | High |
| **Retro feel** | High | High | High |
| **"One more try" factor** | 9/10 | 7/10 | 8/10 |
| **Sound design potential** | 9/10 | 6/10 | 7/10 |
| **Web performance** | Excellent | Excellent | Good |
| **Touch-friendly (mobile)** | Good | Good | Poor |
| **TOTAL** | **80** | **64** | **66** |

---

## Decision

### **Selected: Concept A — "DRIFT"**

**Rationale:**

1. **Most novel mechanic** — "Trail as weapon" doesn't exist in the arcade canon. It's genuinely new while feeling instantly intuitive.

2. **Strongest visual identity** — Glowing trails against a dark void creates a look that's both retro AND modern. Think Geometry Wars meets Tron meets Asteroids. This will look stunning in screenshots (important for joshuaayson.com).

3. **Best physics feel** — Momentum-based movement has the same satisfying drift as Joust and Asteroids. The player fights gravity AND inertia, making every movement feel meaningful.

4. **Deepest emergent gameplay** — Players will discover tactics on their own: circling enemies to pen them in, speed-running for maximum trail length, threading between enemy clusters to lay traps. The system encourages creativity.

5. **Perfect web fit** — Canvas rendering, Web Audio API synthesis, localStorage for scores. No dependencies. Under 500KB. Runs at 60fps.

6. **Best "one more try"** — You can always see HOW you could have survived. The trail shows your path — you can visually trace your mistake.

7. **Scalable complexity** — MVP can ship with 3 enemy types and 10 waves. Version 2 adds bosses, power-ups, new enemies. The core loop is complete at minimum scope.

---

## Implementation Plan

### Tech Stack

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Rendering | HTML5 Canvas | Native, fast, no dependencies |
| Audio | Web Audio API | Synthesized retro sounds, zero file size |
| Game loop | requestAnimationFrame | Smooth 60fps, battery-friendly |
| State | Plain JS objects | No framework overhead |
| Scores | localStorage | Persists per-browser, no server needed |
| Language | Vanilla JavaScript (ES6+) | Zero build step, works everywhere |
| Styling | Inline CSS | Single file deployment possible |

### File Structure

```
simple-new-game/
├── ADR-001-game-concept.md          # This document
├── GAME-DESIGN.md                    # Detailed design specification
├── index.html                        # The game (single file for easy deploy)
├── README.md                         # Overview + how to play
└── assets/                           # Optional: extracted assets if needed
```

### MVP Scope (v1.0)

- [ ] Core movement physics (thrust, drift, gravity)
- [ ] Trail rendering and lifecycle (spawn, fade, despawn)
- [ ] Trail-enemy collision detection
- [ ] 3 enemy types (Drifter, Chaser, Splitter)
- [ ] 10-wave progression with escalation
- [ ] Projectile firing (limited ammo, recharge)
- [ ] Energy orb collection (score + trail extension)
- [ ] Score display (current + multiplier)
- [ ] Lives system (3 lives)
- [ ] Death/respawn animation
- [ ] Wave clear screen
- [ ] Game over screen
- [ ] High score table (3-letter initials, 10 slots, localStorage)
- [ ] Synthesized audio (movement, kills, shots, wave clear, death)
- [ ] CRT/retro visual filter (scanlines, slight glow)
- [ ] Title screen with instructions
- [ ] Pause functionality (P key or Escape)

### Stretch Goals (v1.1+)

- [ ] Additional enemy types (Phaser, Eraser)
- [ ] Boss encounters (every 5th wave)
- [ ] Power-ups (speed, spread shot, trail width, shield)
- [ ] Screen shake on explosions
- [ ] Particle effects on enemy death
- [ ] Touch controls for mobile
- [ ] Gamepad support
- [ ] Screenshot/share functionality
- [ ] Sound toggle (M key)

---

## High Score System Design

### Classic Arcade Implementation

```
╔══════════════════════════╗
║     HIGH  SCORES         ║
║                          ║
║  1. ASH ........  15,200 ║
║  2. JDA ........  12,800 ║
║  3. AMA ........   9,450 ║
║  4. BEN ........   7,200 ║
║  5. TOM ........   5,800 ║
║  6. LIL ........   4,100 ║
║  7. LUC ........   3,600 ║
║  8. JAC ........   2,900 ║
║  9. AAA ........   1,500 ║
║ 10. ... ........       0 ║
║                          ║
║  PRESS START TO PLAY     ║
╚══════════════════════════╝
```

- **10 slots** displayed at all times
- **3-letter initials** — classic arcade entry (A-Z, arrow keys to scroll through letters)
- **Stored in localStorage** as JSON array
- **Pre-seeded** with default scores to fill the board on first play
- **Entry trigger:** Score qualifies for top 10 → initial entry screen after Game Over
- **Visual:** Blinking cursor on current letter, arcade font, color-coded ranks (gold/silver/bronze for top 3)

### localStorage Schema

```json
{
  "drift_highscores": [
    {"name": "ASH", "score": 15200, "wave": 12, "date": "2026-03-21"},
    {"name": "JDA", "score": 12800, "wave": 10, "date": "2026-03-21"}
  ],
  "drift_version": "1.0.0"
}
```

---

## Consequences

### Positive
- Novel mechanic differentiates from generic retro clones
- Single-file deployment to joshuaayson.com is trivial
- Zero dependencies, zero build step, zero server requirements
- Satisfying physics and visual identity create strong first impression
- High score system encourages repeat play and household competition
- Project demonstrates game design thinking on the blog

### Negative
- Momentum physics require careful tuning (can feel floaty or heavy)
- Trail rendering needs optimization for performance (many particles)
- Balance tuning will require extensive playtesting
- No multiplayer in v1 (could be added as co-op in future)

### Risks
- Trail mechanic might feel passive if not tuned well → mitigate with limited ammo encouraging trail use
- Difficulty curve might spike too fast → mitigate with playtesting and tunable constants
- Touch controls for mobile need careful UX → defer to v1.1

---

## References

- [Joust (1982)](https://en.wikipedia.org/wiki/Joust_(video_game)) — Flap physics, platform arena
- [Asteroids (1979)](https://en.wikipedia.org/wiki/Asteroids_(video_game)) — Momentum, screen wrap
- [Lode Runner (1983)](https://en.wikipedia.org/wiki/Lode_Runner) — Trap mechanic
- [Space Invaders (1978)](https://en.wikipedia.org/wiki/Space_Invaders) — Wave escalation
- [Centipede (1980)](https://en.wikipedia.org/wiki/Centipede_(video_game)) — Battlefield reshaping
- [Geometry Wars (2003)](https://en.wikipedia.org/wiki/Geometry_Wars) — Modern twin-stick with retro DNA (visual reference)

---

**Last Updated:** 2026-03-21
**Version:** 1.0.0
