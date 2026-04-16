# ADR-003: Game Archaeology and the Rapid Prototyping Laboratory

**Status:** Accepted
**Date:** 2026-03-22
**Author:** Joshua Ayson / OA LLC
**Project:** Pixel Vault
**References:** ADR-001 (arcade mechanics), ADR-002 (novel genre exploration)

---

## Table of Contents

- [Context](#context)
- [Part I: The Deep History — Why Humans Play](#part-i-the-deep-history--why-humans-play)
- [Part II: The Technology Ladder — How Constraints Create Genres](#part-ii-the-technology-ladder--how-constraints-create-genres)
- [Part III: The Genre Lineage Map](#part-iii-the-genre-lineage-map)
- [Part IV: The Rapid Prototyping Laboratory](#part-iv-the-rapid-prototyping-laboratory)
- [Part V: Folder Architecture and Catalogue System](#part-v-folder-architecture-and-catalogue-system)
- [Part VI: The Discovery Method](#part-vi-the-discovery-method)
- [Part VII: The AI Dimension — What If AI Had Been There?](#part-vii-the-ai-dimension--what-if-ai-had-been-there)
- [Part VIII: Visibility and Publishing System](#part-viii-visibility-and-publishing-system)
- [Decision Summary](#decision-summary)

---

## Context

ADR-001 analyzed golden-age arcade mechanics. ADR-002 proposed novel genre
verbs. Both were useful explorations, but they started in the middle of the
story. They asked "what can we remix?" before asking "where did all of this
come from?"

This ADR starts at the beginning. Not 1972 Pong. Not 1978 Space Invaders.
The actual beginning — carved stone boards in ancient Mesopotamia, pebble
games on African dirt, card games in Tang Dynasty China. The question isn't
"what video game should we make?" It's **"what does a human being want when
they sit down to play?"** and then **"how did technology successively unlock
new answers to that question?"**

From that analysis we build something practical: a rapid prototyping
laboratory designed to produce hundreds of small, single-HTML-file games.
Not to ship them. To **learn from building them**. We are archaeologists
digging through the sediment layers of play itself, reconstructing each era
hands-on, looking for something that hasn't been found yet.

### What Changed Since ADR-001/002

- Scope expanded from "make one game" to "build a laboratory"
- Method shifted from "design a novel mechanic" to "reconstruct the lineage,
  find the gaps"
- Output shifted from "a finished game" to "hundreds of indexed prototypes
  with the best ones refined forward"
- Philosophy shifted from invention to discovery — you find gems by digging,
  not by imagining

---

## Part I: The Deep History — Why Humans Play

### The Five Ancient Drives

Every game ever created — from Senet to Elden Ring — satisfies one or more
of five drives that appear to be hardwired into human cognition:

| Drive | Description | Ancient Expression | Digital Expression |
|-------|-------------|-------------------|-------------------|
| **Contest** | Test my skill against yours | Wrestling, footraces, archery | Fighting games, PvP, esports |
| **Chance** | Submit to fate, read the signs | Dice, knucklebones, drawing lots | Roguelikes, gacha, card draws |
| **Strategy** | Outthink an opponent in abstract space | Go, Chess, Mancala, Senet | 4X, RTS, tower defense |
| **Dexterity** | Master physical control | Jacks, cup-and-ball, juggling | Platformers, rhythm games, shooters |
| **Pattern** | Perceive hidden order in chaos | Tile games, card matching, riddles | Puzzle games, Tetris, hidden object |

No game survives that doesn't tap at least one. The greatest games blend
two or three. The question for our laboratory: **which combinations remain
unexplored at the intersection of modern browser capabilities?**

### The Ancient Games That Still Matter

These are not historical curiosities. They are existence proofs that certain
game structures are so fundamental they survive millennia. Understanding
what makes them immortal is the foundation of everything.

#### The Royal Game of Ur (~2600 BCE, Mesopotamia)

- Two players race pieces across a shared track
- Movement determined by binary dice (tetrahedral)
- Certain squares grant extra turns or safety
- **Why it endures:** Race + chance + blocking. The board is simple enough
  to scratch in dirt but deep enough for genuine strategy. The shared track
  creates interaction — you aren't playing solitaire side by side, you're
  actively interfering with your opponent's plans.
- **Design lesson:** Shared space creates conflict. Binary outcomes (safe
  vs. exposed) create drama. Small boards with big consequences.

#### Senet (~3100 BCE, Egypt)

- 30-square track, pieces move by throw sticks
- Spiritual significance — playing against the dead for passage to afterlife
- **Design lesson:** Meaning elevates mechanics. The game was popular for
  2000+ years partly because it MEANT something beyond the board. Games
  with narrative gravity outlast games without.

#### Go (~2500 BCE, China)

- 19x19 grid, black and white stones, surround to capture
- Possibly the most strategically deep game ever created
- Simple rules generate more possible board states than atoms in the
  observable universe ($2.08 \times 10^{170}$ legal positions)
- **Design lesson:** Maximum emergence from minimum rules. Two actions
  (place, pass) on a blank grid creates infinite depth. The constraint IS
  the design space. This is the North Star.

#### Mancala family (~700 CE formalized, Africa, possibly older)

- Seeds/stones distributed around pits in a circuit
- "Sowing" mechanic — pick up a pile, drop one per pit
- Hundreds of regional variants (Oware, Kalah, Bao)
- **Design lesson:** A single verb (sow) with positional consequences
  creates deep strategy. The pieces are the scoring system and the
  movement system simultaneously. Dual-purpose components = elegance.

#### Chess (~600 CE, India → Persia → Europe)

- Asymmetric piece powers on a symmetric grid
- Perfect information, zero chance
- **Design lesson:** Characters with distinct movement rules create
  emergent tactical combinations. The Knight exists because someone asked
  "what if one piece could bypass the blockade?" Asymmetry within a system
  creates unexpected interactions.

#### Tarot/Playing Cards (~1370s, Europe via Islamic world)

- 52-card deck: 4 suits × 13 ranks
- Enabled THOUSANDS of distinct games from a single artifact
- **Design lesson:** A generative component system beats a fixed game.
  The deck of cards is not a game — it's a platform. The most valuable
  thing we could build isn't a game. It's a system that generates games.

#### Backgammon (~3000 BCE, Mesopotamia)

- Race + dice + blocking + bearing off
- The doubling cube (added ~1920s) introduced meta-strategy: when to
  raise the stakes
- **Design lesson:** Layered decision types. Tactical (which piece to
  move), strategic (board control), meta-strategic (when to double).
  Multiple decision layers sustain engagement because the player is
  never solving just one problem.

### The Ancient Insight

**Every ancient game that survived 1000+ years did so because it was
simple enough to learn in minutes and deep enough to reward decades of
play.** This is not a new observation. But it's the observation that
every game designer forgets when they add the fourteenth enemy type and
the seventh power-up.

Complexity is easy. Depth is hard. Depth comes from interactions between
simple rules, not from the accumulation of complicated ones.

---

## Part II: The Technology Ladder — How Constraints Create Genres

Games don't evolve by imagination alone. They evolve when technology
removes a constraint, and designers discover what was waiting on the other
side. Every major genre was born the moment a specific technical limitation
fell away. Understanding this ladder is understanding why games look the
way they do — and what the next unlocked constraint might produce.

### Era 0: Pre-Electronic (before 1950)

**Available:** Physical materials — stone, wood, paper, dice, cards
**Constraint:** No automation. Every game requires two minds or chance devices.
**What existed:** All five ancient drives fully expressed. Board games, card
games, dice games, physical dexterity games, word games.

**What was missing:** Reflex (real-time pressure), dynamic systems (state
that changes without player input), visual spectacle, single-player depth.

The entire video game industry exists because physical games couldn't provide
these four things.

### Era 1: Oscilloscope and Mainframe (1950-1971)

**Tech unlocked:** Electron beams drawing points on screens. Programmed
logic. Real-time state updates.

| What Became Possible | What Was Still Impossible |
|---------------------|-------------------------|
| A dot moving on a screen | Color, sound, scrolling |
| Real-time input response | Multiple moving objects (CPU limits) |
| Computer as opponent | Persistent state (no save) |
| Simple physics simulation | Complex visuals |

**Key games:**
- *Tennis for Two* (1958) — oscilloscope, analog computer. First real-time
  physics game. A parabolic ball arc with gravity. Two paddles.
- *Spacewar!* (1962) — PDP-1 minicomputer. Two ships, a central star with
  gravity, torpedoes. **First game with Newtonian physics as a mechanic.**
  Momentum, inertia, gravity wells. The DNA of Asteroids, Lunar Lander,
  and every space game since.

**Genre born:** The real-time duel. Two entities, one screen, physics as
arbiter. This didn't exist before electricity.

**Design lesson:** The very first video games immediately did two things
that board games couldn't: continuous motion and real-time physics. These
remain underexploited. Most modern games use physics as decoration (ragdoll
corpses) not as core mechanic (Spacewar's gravity well combat).

### Era 2: The Arcade Dawn — One Bit at a Time (1972-1977)

**Tech unlocked:** Dedicated game hardware (discrete logic, no CPU yet).
Coin-operated cabinets. TV signal output. Monochrome or color overlay.
Simple sound (beeps, pops).

**Resolution:** ~Low, often hardware-drawn shapes rather than pixels
**Colors:** 1 (monochrome) to 4 (color overlay on screen regions)
**Sprites:** 0 (shapes drawn by dedicated circuits, not bitmapped)
**Sound:** Square waves, noise generator
**Movement:** Fixed axis (horizontal OR vertical), not free 2D

| Constraint | What It Forced |
|-----------|---------------|
| No bitmapped graphics | Geometric shapes (paddles, balls, blocks) |
| Minimal CPU | Simple, deterministic enemy behavior |
| 1-2 colors | Gameplay must communicate through MOTION, not appearance |
| No scrolling | Single-screen, everything visible at once |
| Coin-operated | Skill-gated difficulty (eat quarters) |

**Key games and what they proved:**
- *Pong* (1972) — One verb: DEFLECT. Two paddles, one ball, angle physics.
  Proved: a game this simple can earn 4x its cost in one week.
- *Breakout* (1976) — Pong against a wall. Added: destructible environment.
  Player reshapes the playfield by removing bricks. First game where the
  arena changes as you play it.
- *Sea Wolf* (1976) — Periscope crosshair, torpedoes with travel time,
  ships at variable depths. First game with **projectile travel time** as
  a core mechanic (leading your shot).
- *Sprint 2* (1976) — Top-down racing. First game with a **persistent
  track** that the player navigates (not just abstract space).

**Genres born:** Paddle/deflect, brick-breaker (destruction + deflect),
top-down racing, target shooting.

**The critical insight:** With no ability to draw complex shapes, designers
were forced to make **movement itself** communicate meaning. A paddle's
position IS the entire game state of Pong. The ball's trajectory IS the
information. When you can't decorate, you must design. This era's games
have the purest mechanics-to-entertainment ratio in history.

### Era 3: The 8-Bit Explosion — Pixels Change Everything (1978-1983)

**Tech unlocked:** Microprocessors (6502, Z80). Bitmapped sprites. Tile-based
backgrounds. Multi-voice sound. ROM cartridges. Color palettes (16-256
colors on screen from larger palette).

**Resolution:** 256×224 (arcade), 160×192 to 320×200 (home)
**Colors:** 16-128 simultaneous from larger palettes
**Sprites:** 8-64 simultaneous hardware sprites
**Sound:** 3-4 channels, programmable waveforms (PSG chips)
**Movement:** Full 2D movement, 8-directional, hardware scrolling begins

This is the Cambrian Explosion of video games. More genres were born in
these six years than in any period before or since.

| New Capability | What It Unlocked |
|---------------|-----------------|
| Bitmapped sprites | Characters with identity (faces, bodies, vehicles) |
| Multiple sprites | Enemy VARIETY (different behaviors per type) |
| Tile backgrounds | Environments with meaning (platforms, walls, water) |
| Color | Instant visual taxonomy (red = danger, green = safe) |
| Scrolling | Worlds larger than one screen |
| Sound channels | Audio as game state (tempo = speed, pitch = threat) |
| Score displays | Persistent motivation, competition |

**Key technological-to-genre mappings:**

**Sprites with identity → the Character Game**
- *Space Invaders* (1978) — Marching formation of DISTINCT aliens. Each row
  has different sprites, different point values. Players learn to prioritize.
  The aliens accelerate as their numbers decrease (accidental — CPU had less
  to draw, so it ran faster). This bug became the most imitated design
  pattern in gaming history.
- **Genre born:** Fixed-position shooter. The player is constrained, the
  enemies are systemic. Your job is to manage a deteriorating situation.

**Hardware scrolling → the Moving World**
- *Defender* (1981) — First side-scrolling shooter. The world extends beyond
  the screen. Radar shows what you can't see. Established: the camera follows
  the player, the world is bigger than the viewport.
- *Scramble* (1981) — First forced-scrolling shooter. The world moves whether
  you're ready or not. Two weapons (laser + bomb), terrain + enemies.
- **Genre born:** Scrolling shooters (horizontal and vertical). The shmup.

**Tile-based terrain + gravity → the Platformer**
- *Donkey Kong* (1981) — ladders, platforms, gaps, barrels rolling down
  slopes. Jump is the verb. Gravity is the threat. Platforms are the
  puzzle. Also: first game with a NARRATIVE setup (kidnapped girlfriend,
  angry ape).
- *Pitfall!* (1982) — Side-scrolling platformer. 255 screens. Timer-based
  exploration. Swinging on vines (physics + timing).
- **Genre born:** Platformer. This genre dominates for 15 years.

**Multiple enemy types + AI behaviors → the Maze Chase**
- *Pac-Man* (1980) — Four ghosts, each with distinct AI (chase, ambush,
  patrol, random). One of the first games where enemies have PERSONALITY.
  The maze is the constraint. The power pellet is the role reversal (hunter
  becomes hunted). One of the purest examples of risk/reward geography —
  the fruit in the center is a greed test.
- **Genre born:** Maze chase. Also pioneered: character-driven design
  (Pac-Man has a face, a name, a personality).

**Physics simulation + momentum → the Inertia Game**
- *Asteroids* (1979) — Newtonian physics on a wraparound plane. Thrust,
  rotate, shoot. Your ship drifts. Asteroids split into smaller pieces.
  The screen fills with debris you created. **The game punishes you with
  the consequences of your own success.**
- *Lunar Lander* (1979) — Gravity + limited fuel + precise thrust. Pure
  physics puzzle in real time.
- **Genre born:** Inertia/vector games. Also: destruction-creates-more-
  threats pattern (reused in Centipede, Missile Command, etc.)

**Tile manipulation + puzzle logic → the Action Puzzle**
- *Lode Runner* (1983) — Dig temporary holes in floors. Enemies fall in.
  Collect all gold to advance. No jump button — the ABSENCE of jump is the
  design. Constraint creates the entire game.
- **Genre born:** Action puzzle / trap game.

**Home consoles' limited hardware → Abstraction Games**
- *Atari 2600* had 128 bytes of RAM and 2 sprites that had to be reused
  per scanline. This forced extreme abstraction.
- *Combat* (1977) — Tank warfare reduced to 2 squares shooting dots.
  Worked because the RULES were good even without the graphics.
- *Adventure* (1980) — First graphical adventure game. Your character is
  a square. The dragon is a duck-shape. But it had rooms, keys, an
  inventory, a hidden easter egg. Proved: players will accept ANY visual
  representation if the system underneath is engaging.
- **Design lesson:** The Atari 2600 proved that abstraction doesn't kill
  engagement. Players map meaning onto shapes instantly. This is why our
  prototyping lab can use geometric shapes and still discover real game
  mechanics.

### Era 4: 16-Bit Refinement — Depth Within Genres (1985-1992)

**Tech unlocked:** 16-bit CPUs (68000, 65816). Large color palettes (512-
4096 colors). Hardware scaling/rotation (Mode 7). Parallax scrolling.
FM synthesis sound. Battery-backed save RAM.

**Resolution:** 256×224 to 320×240 (up to 512×448 interlaced)
**Colors:** 64-256 simultaneous from 512-4096
**Sprites:** 64-128 on screen, larger sizes, more per scanline
**Sound:** FM synthesis (6-8 channels), sampled drums, stereo
**Movement:** Smooth multi-directional scrolling, rotation, scaling

| New Capability | What It Unlocked |
|---------------|-----------------|
| More colors + larger sprites | Expressive characters, detailed worlds |
| Parallax scrolling | Depth perception, immersive backgrounds |
| Mode 7 / rotation | Pseudo-3D (F-Zero, Mario Kart) |
| Battery save | Long games, RPGs, persistent progression |
| Better sound | Musical scores, sound design as art |
| More RAM | Complex AI, larger game states |

**Key shifts:**

This era didn't create many NEW genres. It DEEPENED existing ones:

- **Platformer → Exploration platformer:** Super Mario Bros 3 (1988),
  Sonic (1991), Super Metroid (1994). Worlds became non-linear. Players
  explored, backtracked, found secrets. The verb "JUMP" remained primary
  but the spatial metaphor expanded from "survive the track" to "explore
  the labyrinth."

- **Shooter → Bullet hell / Pattern shooter:** Gradually increasing
  enemy bullet density forced players to memorize patterns and thread
  through impossibly dense projectile spreads. The visual spectacle of
  hundreds of bullets on screen became the aesthetic.

- **RPG → JRPG narrative epic:** Dragon Quest (1986), Final Fantasy
  (1987). Battery saves enabled 40+ hour adventures. Turn-based combat
  + persistent characters + narrative arcs. Save files meant games could
  have CONSEQUENCES that lasted.

- **Fighter → Tournament fighter:** Street Fighter II (1991). Six
  buttons, special move inputs (quarter-circle + punch), combo discovery.
  **The first game where the community EXPANDED the design** — combos
  were a bug/emergent behavior that Capcom then embraced.

**The critical insight:** The 16-bit era proves that REFINEMENT creates
as much value as invention. Most of the mechanics we think of as "defining
genres" were actually discovered by players and designers iterating within
a genre over 5-7 years. This is why our lab must build many prototypes in
the same family, not just one-of-each.

### Era 5: The 3D Rupture — A Second Spatial Dimension (1992-2001)

**Tech unlocked:** Polygon rendering (hardware and software). Z-buffers.
Texture mapping. 3D sound. Analog controls. CD-ROM (audio, video, large
data).

This deserves its own era because it was not an incremental improvement.
It was a **dimensional shift** — from 2D planes to 3D volumes. Every
single genre had to be reinvented.

| 2D Genre | 3D Reinvention | What Changed |
|----------|---------------|-------------|
| Platformer | 3D platformer (Mario 64) | Camera problem, spatial navigation |
| Shooter | FPS (Doom, Quake) | Aiming becomes spatial, not directional |
| Racing | 3D racing (Ridge Racer) | Cornering physics, draw distance |
| Fighting | 3D fighter (Virtua Fighter) | Sidestep, ring position, depth |
| Adventure | 3D adventure (Zelda OoT) | Lock-on targeting, Z-targeting |
| RPG | 3D RPG (FF VII) | Cinematic presentation, spatial dungeons |

**Genres born from 3D that couldn't exist in 2D:**
- **First-person shooter (FPS)** — Wolfenstein 3D (1992), Doom (1993).
  You ARE the camera. Spatial awareness IS the skill.
- **Survival horror** — Alone in the Dark (1992), Resident Evil (1996).
  Fixed camera angles create vulnerability. 3D space creates "what's
  around the corner?" tension that 2D cannot produce.
- **Stealth** — Metal Gear Solid (1998), Thief (1998). Line-of-sight in
  3D space + sound propagation. Impossible without volume.
- **Open world** — GTA III (2001). A continuous 3D city you drive through.
  The genre is literally "a 3D space with systems."

**The critical insight for our lab:** The 2D-to-3D transition proves that
**adding a dimension to an existing mechanic creates an entirely new genre.**
What if the equivalent insight for our lab isn't 2D→3D but some other
dimensional shift? Time as a playable dimension. Sound as a playable
dimension. Relationship/state as a spatial dimension. ADR-002's "ECHO"
concept was touching this — making your temporal history into spatial
entities.

### Era 6: The Network and the Infinite Canvas (2002-2015)

**Tech unlocked:** Broadband internet. Digital distribution. Mobile
touchscreens. Physics engines as middleware. Procedural generation at
scale.

| New Capability | Genres Born |
|---------------|------------|
| Real-time multiplayer at scale | MMORPG, battle royale, MOBA |
| Touch input | Casual mobile (Angry Birds, Fruit Ninja) |
| Physics middleware | Physics puzzlers (World of Goo, Bridge Constructor) |
| Procedural generation | Modern roguelikes (Spelunky, Binding of Isaac) |
| Digital distribution | Indie explosion — games by 1-3 people viable |
| User-generated content | Minecraft, LittleBigPlanet, Mario Maker |

**The critical insight:** This era's biggest genre innovation came not
from technology but from **distribution**. When making a game no longer
required a publisher, a box, and shelf space — when a solo developer could
ship a weird experiment — the experimenters flooded in. Indie games
produced more genre innovation from 2008-2015 than AAA studios produced
in the same period.

**Our lab operates on the same principle.** Zero distribution cost (single
HTML file, served from S3). Zero dependency cost (vanilla JS, no build
step). The friction between "idea" and "playable prototype" must approach
zero.

### Era 7: The Browser as Console (2010-present)

**Tech unlocked for us right now:**

| Capability | Status | Implication |
|-----------|--------|-------------|
| Canvas 2D | Mature | Full raster drawing, 60fps |
| WebGL / WebGPU | Mature / Emerging | 3D rendering, shaders, GPU compute |
| Web Audio API | Mature | Synthesized sound, spatial audio |
| Gamepad API | Mature | Controller support |
| Pointer Lock | Mature | FPS-style mouse input |
| Touch Events | Mature | Mobile play |
| Web Workers | Mature | Background computation |
| SharedArrayBuffer | Available | Multi-threaded physics |
| WASM | Mature | Near-native performance |
| localStorage | Mature | Persistent save/high scores |

**A single HTML file with vanilla JavaScript can now do what required a
$50,000 arcade cabinet in 1982 or a $3,000 PC in 1996.** The canvas is
unlimited. The only constraint is imagination — and the discipline to
keep prototypes small enough to learn from.

---

## Part III: The Genre Lineage Map

Every genre has a parent. Every parent had a constraint that, when removed,
spawned children. This lineage map shows the family tree of game genres
as a technology-unlocked dependency graph.

```
PRE-ELECTRONIC ANCESTORS
├── Contest (physical) ──────────────────────────> Fighting Games
├── Chance (dice/lots) ──────────────────────────> Roguelikes, Card Games
├── Strategy (board) ────────────────────────────> RTS, 4X, Tower Defense
├── Dexterity (physical skill) ──────────────────> Platformers, Rhythm
└── Pattern (tiles/riddles) ─────────────────────> Puzzle Games

ELECTRONIC ERA: CONSTRAINT → GENRE
│
├── [Real-time display] ─── Pong (1972) ─── DEFLECT genre
│   └── [Destructible playfield] ── Breakout (1976) ── BRICK BREAKER
│
├── [Sprites + formation AI] ── Space Invaders (1978) ── FIXED SHOOTER
│   ├── [Scrolling] ── Defender (1981) ── SCROLLING SHOOTER
│   │   └── [Forced scroll] ── Scramble (1981) ── SHMUP
│   │       └── [Bullet density] ── BULLET HELL
│   └── [Arena + waves] ── Robotron (1982) ── ARENA SHOOTER
│       └── [Twin-stick] ── Smash TV (1990) ── TWIN-STICK SHOOTER
│
├── [Gravity + platforms] ── Donkey Kong (1981) ── PLATFORMER
│   ├── [Scrolling + exploration] ── Metroid (1986) ── METROIDVANIA
│   ├── [Physics-driven] ── Sonic (1991) ── MOMENTUM PLATFORMER
│   └── [Precision + death] ── Super Meat Boy (2010) ── PRECISION PLATFORMER
│
├── [Ghost AI + maze] ── Pac-Man (1980) ── MAZE CHASE
│   └── [Procedural mazes] ── Rogue (1980) ── ROGUELIKE
│       └── [Action + permadeath] ── Spelunky (2008) ── ROGUELITE
│
├── [Newtonian physics] ── Asteroids (1979) ── INERTIA GAME
│   ├── [Gravity + fuel] ── Lunar Lander (1979) ── LANDING SIM
│   └── [Terrain + trajectory] ── Scorched Earth (1991) ── ARTILLERY
│       └── [Turn-based + worms] ── Worms (1995) ── TACTICAL ARTILLERY
│
├── [Tile manipulation] ── Lode Runner (1983) ── TRAP/ACTION PUZZLE
│   └── [Falling pieces + grid] ── Tetris (1985) ── FALLING BLOCK PUZZLE
│       └── [Match mechanics] ── Columns (1990) ── MATCH PUZZLE
│           └── [Chain reactions] ── Puyo Puyo (1991) ── CHAIN PUZZLE
│
├── [Opponent AI + moves] ── Karate Champ (1984) ── FIGHTING
│   └── [Special inputs + combos] ── SF2 (1991) ── TOURNAMENT FIGHTER
│
├── [3D polygons] ── DIMENSIONAL SHIFT ──────────────────────────
│   ├── Wolfenstein/Doom ── FIRST-PERSON SHOOTER
│   ├── Mario 64 ── 3D PLATFORMER
│   ├── Resident Evil ── SURVIVAL HORROR
│   └── Metal Gear Solid ── STEALTH
│
├── [Network + scale] ── MULTIPLAYER SHIFT ──────────────────────
│   ├── Ultima Online ── MMORPG
│   ├── DotA ── MOBA
│   └── PUBG ── BATTLE ROYALE
│
└── [Touch + mobile] ── INPUT SHIFT ─────────────────────────────
    ├── Angry Birds ── CASUAL PHYSICS
    ├── Fruit Ninja ── SWIPE ACTION
    └── Threes/2048 ── SWIPE PUZZLE
```

### The Unexplored Gaps

The lineage map reveals branches that were started but never fully explored:

1. **Inertia as primary mechanic** — Asteroids explored it, then the
   industry moved to direct-control games. What if momentum was the ENTIRE
   game, not just a ship property?

2. **Sound as primary input/output** — Rhythm games use timing-to-music,
   but no game makes SOUND ITSELF the playfield. What if you could see
   sound and play within it?

3. **Terrain destruction as the verb** — Lemmings (dig routes), Worms
   (destroy terrain with weapons), Noita (every pixel is physics). But
   no single-screen arcade game makes erosion/construction the core loop.

4. **State/phase as a playable dimension** — Games have states (ice world,
   fire world) but the TRANSITION between states has never been the primary
   mechanic.

5. **Time as visible, physical material** — Braid made time a puzzle tool.
   But time as a physical substance on screen that you push, cut, and
   sculpt? Unexplored.

6. **Dual-entity control in real time** — Brothers: A Tale of Two Sons
   (2013) used this for narrative. No arcade game has made simultaneous
   control of two entities the core competitive mechanic.

7. **Geometry drawing under pressure** — Qix (1981) started this. ADR-002's
   THREAD concept continued it. The vein is rich and barely mined.

---

## Part IV: The Rapid Prototyping Laboratory

### Philosophy: Mine the Vein

We are not trying to invent one brilliant game. We are running an
excavation operation. The method:

1. **Reconstruct** — Build simple versions of historical game types to
   understand them from the inside (you don't understand a watch by
   looking at it; you understand it by building one)
2. **Catalogue** — Tag, rate, and index every prototype
3. **Cross-pollinate** — Deliberately combine mechanics from different
   families
4. **Mutate** — Take a working prototype and change ONE variable to see
   what happens
5. **Select** — The prototypes that produce "I want to play this again"
   get promoted to refinement

This is the Hansuru approach applied to game design: systematic exploration
with bounded risk per experiment. Each prototype is a small bet. We're
looking for convex payoffs — most prototypes teach us something small, a
few teach us something huge.

### Prototype Specification

Every prototype must:

- Be a **single HTML file** (no build step, no dependencies)
- Use **HTML5 Canvas** for rendering
- Use **vanilla JavaScript** (no frameworks, no libraries)
- Be **playable in 5 seconds** (no loading, no menus required)
- Have a **game loop** (not static — something moves, changes, reacts)
- Fit **under 50KB** (forces minimalism, prevents feature creep)
- Include an embedded **metadata comment block** at the top:

```html
<!--
PROTOTYPE: [name]
SERIES: [series-name]
NUMBER: [NNN]
DATE: 2026-03-22
MECHANIC: [primary verb]
ANCESTRY: [which historical games inspired this]
CONTROLS: [input description]
STATUS: sketch | playable | promising | refined | archived
RATING: [1-5 stars, self-assessed after 10 minutes of play]
NOTES: [one-line observation]
-->
```

### Series System

Prototypes are organized into series. Each series explores one lineage
branch or one mechanical hypothesis:

| Series Code | Focus | Starting Point |
|-------------|-------|---------------|
| `ANC` | Ancient game digitization | Ur, Senet, Mancala, Go |
| `DEF` | Deflection / paddle games | Pong → Breakout → ??? |
| `FIX` | Fixed-position shooters | Space Invaders → Galaga → ??? |
| `SCR` | Scrolling / shmup | Defender → Gradius → ??? |
| `PLT` | Platformer mechanics | DK → Mario → precision → ??? |
| `MAZ` | Maze and chase games | Pac-Man → Rogue → ??? |
| `PHY` | Physics / inertia games | Asteroids → Lunar Lander → ??? |
| `PUZ` | Puzzle / falling block | Tetris → Puyo → ??? |
| `TRP` | Trap / terrain manipulation | Lode Runner → Lemmings → ??? |
| `FGT` | Fighting / collision combat | Joust → Karate Champ → ??? |
| `NEW` | Novel mechanic experiments | ADR-002 concepts (Echo, Tether, etc.) |
| `HYB` | Cross-lineage hybrids | Deliberate chimeras |
| `WLD` | Wild experiments | Things that don't fit anywhere |

### Build Cadence

Target: **2-3 prototypes per session**. A session is ~2 hours. The
prototypes should be rough. Ugly is fine. Broken is fine. The question
is always: "Is there something here worth exploring further?"

Prototypes that score 4-5 stars get promoted to a `refined/` folder
where they receive additional development.

---

## Part V: Folder Architecture and Catalogue System

### Directory Structure

```
simple-new-game/
├── README.md                          # Project overview + quick start
├── ADR-001-game-concept.md            # Historical: arcade mechanics
├── ADR-002-novel-genre-exploration.md # Historical: novel genre verbs
├── ADR-003-game-archaeology-and-rapid-prototyping.md  # This document
├── CATALOGUE.md                       # Master index of all prototypes
│
├── prototypes/                        # The laboratory
│   ├── anc/                           # Ancient game series
│   │   ├── anc-001-ur.html
│   │   ├── anc-002-mancala.html
│   │   ├── anc-003-go-9x9.html
│   │   └── ...
│   ├── def/                           # Deflection series
│   │   ├── def-001-pong.html
│   │   ├── def-002-breakout.html
│   │   ├── def-003-multiball-angles.html
│   │   └── ...
│   ├── fix/                           # Fixed shooter series
│   │   ├── fix-001-invaders.html
│   │   ├── fix-002-galaga-dive.html
│   │   └── ...
│   ├── scr/                           # Scrolling shooter series
│   ├── plt/                           # Platformer series
│   ├── maz/                           # Maze + chase series
│   ├── phy/                           # Physics / inertia series
│   ├── puz/                           # Puzzle series
│   ├── trp/                           # Trap / terrain series
│   ├── fgt/                           # Fighting / combat series
│   ├── new/                           # Novel mechanic experiments
│   │   ├── new-001-echo.html
│   │   ├── new-002-tether.html
│   │   ├── new-003-split.html
│   │   ├── new-004-thread.html
│   │   ├── new-005-pulse.html
│   │   └── ...
│   ├── hyb/                           # Cross-lineage hybrids
│   └── wld/                           # Wild experiments
│
├── refined/                           # Promoted prototypes (4-5 stars)
│   ├── drift/                         # From ADR-001/002 work
│   │   ├── drift.html
│   │   ├── GAME-DESIGN.md
│   │   └── ...
│   ├── komorebi/                      # Existing refined game
│   │   └── ...
│   └── [next-discovery]/              # Future promoted prototypes
│       ├── [name].html
│       ├── GAME-DESIGN.md             # Full design doc when refined
│       └── iterations/                # Version history
│           ├── v1.html
│           ├── v2.html
│           └── ...
│
├── templates/                         # Starter templates for rapid build
│   ├── base-canvas.html               # Bare canvas + game loop + input
│   ├── base-physics.html              # Canvas + velocity + friction
│   ├── base-grid.html                 # Canvas + tile grid + click
│   ├── base-particles.html            # Canvas + particle system
│   └── base-audio.html                # Canvas + Web Audio basics
│
├── tools/                             # Lab utilities
│   ├── catalogue-generator.py         # Scan prototypes → CATALOGUE.md
│   ├── serve.sh                       # Simple HTTP server for testing
│   └── screenshot.sh                  # Capture prototype screenshots
│
└── archive/                           # Parked experiments (historical)
    └── sparks-explorer/               # Moved from root
```

### Naming Convention

```
[series]-[number]-[short-name].html
```

- **series:** 3-letter lowercase code from the series table
- **number:** 3-digit zero-padded (001, 002, ... 999)
- **short-name:** kebab-case, max 30 chars, describes the experiment

Examples:
- `anc-001-royal-game-of-ur.html`
- `def-007-breakout-gravity.html`
- `phy-003-momentum-combat.html`
- `new-014-echo-with-decay.html`
- `hyb-002-tether-plus-trail.html`
- `wld-001-sound-as-terrain.html`

### CATALOGUE.md Format

The master catalogue is auto-generated by `catalogue-generator.py` from
the metadata comment blocks in each HTML file. Format:

```markdown
# Game Laboratory Catalogue

**Last Generated:** 2026-03-22
**Total Prototypes:** 47
**By Series:** ANC(5) DEF(8) FIX(4) PHY(6) NEW(12) HYB(3) WLD(9)
**Promising (4-5 stars):** 7

## By Series

### ANC — Ancient Games
| # | Name | Mechanic | Rating | Status | Notes |
|---|------|----------|--------|--------|-------|
| 001 | Royal Game of Ur | RACE+BLOCK | ★★★ | playable | good tension |
| 002 | Mancala | SOW | ★★★★ | promising | sowing feels great |

### DEF — Deflection
| # | Name | Mechanic | Rating | Status | Notes |
|---|------|----------|--------|--------|-------|
| 001 | Pong | DEFLECT | ★★★ | playable | baseline reference |
...

## Promising Prototypes (★★★★+)
| Series | # | Name | Rating | Refined? |
|--------|---|------|--------|----------|
| ANC | 002 | Mancala | ★★★★ | no |
| NEW | 001 | Echo | ★★★★★ | yes → refined/echo/ |
...

## Cross-Pollination Ideas
- [ANC-002 sowing] + [PHY-003 momentum] = seed-throwing momentum game?
- [NEW-001 echo] + [TRP-002 dig] = ghosts that dig?
...
```

### Templates

Five starter templates that eliminate boilerplate and let each prototype
focus on its unique mechanic:

| Template | What It Provides | Use For |
|----------|-----------------|---------|
| `base-canvas.html` | Canvas, game loop (60fps), keyboard input, basic entity class | Most prototypes |
| `base-physics.html` | Above + velocity, acceleration, friction, gravity, collision detection | Physics-based games |
| `base-grid.html` | Canvas, clickable tile grid, grid state array, simple rendering | Board/puzzle games |
| `base-particles.html` | Canvas, particle emitter, color/size/life params, pooling | Visual effect experiments |
| `base-audio.html` | Canvas + Web Audio oscillators, ADSR envelope, simple sound effects | Audio-centric experiments |

Each template is under 5KB and includes the prototype metadata comment
block pre-filled with blanks.

---

## Part VI: The Discovery Method

### The Excavation Protocol

**Phase 1: Reconstruction (Weeks 1-3)**
Build baseline versions of the canonical games from each major lineage
branch. Not clones — stripped-to-the-bone mechanical recreations. The
goal is to feel the mechanic from the builder's side, not the player's
side.

Target: 3-5 prototypes per series, ~40-50 total.

Reconstruction candidates (priority order):
1. Pong (deflection baseline)
2. Breakout (destructible deflection)
3. Space Invaders (formation shooter)
4. Asteroids (inertia combat)
5. Pac-Man (maze chase + ghost AI)
6. Tetris (falling block)
7. Royal Game of Ur (ancient race)
8. Mancala/Oware (sowing)
9. Lode Runner (trap puzzle)
10. Joust (flap physics combat)

**Phase 2: Mutation (Weeks 3-6)**
Take each reconstruction and change ONE variable. Play it. Rate it. Log it.

Mutation types:
- **Invert** — reverse a core rule (gravity pushes up, enemies heal you)
- **Remove** — take away an assumed element (no shooting in a shooter)
- **Add dimension** — add time, sound, or a second entity
- **Swap input** — use mouse instead of keyboard, or vice versa
- **Change topology** — wraparound screen, expanding arena, shrinking arena
- **Blend** — take the movement from game A and the goal from game B

Target: 2-3 mutations per reconstruction, ~80-100 cumulative.

**Phase 3: Novel Mechanics (Weeks 6-10)**
Build the ADR-002 concepts (Echo, Tether, Split, Thread, Pulse, Erode)
plus any new ideas that emerged during mutation.

Target: 5-10 novel prototypes from the NEW series, plus hybrids.

**Phase 4: Selection and Refinement (Ongoing)**
Any prototype rated 4-5 stars gets promoted to `refined/`. It receives:
- A proper game design document
- Multiple iterations (v1, v2, v3...)
- Polish (sound, visual effects, juice)
- High score system
- Deployment consideration

### The Rating Criteria

After 10 minutes of play, rate 1-5 stars based on:

| Factor | Weight | Question |
|--------|--------|----------|
| **Hook** | 30% | Did I want to keep playing after 30 seconds? |
| **Depth** | 25% | Did I discover tactics the design didn't explicitly teach? |
| **Feel** | 20% | Does the movement/interaction feel satisfying in my hands? |
| **Novelty** | 15% | Have I experienced this specific combination before? |
| **Legibility** | 10% | Could someone understand it by watching for 5 seconds? |

### What We're Looking For

The gem we're mining for has these properties:

1. **A core interaction that doesn't have a name yet** — not "shooting"
   or "jumping" but something you'd have to DESCRIBE
2. **Immediate visual magnetism** — watching it in motion makes you want
   to touch the controls
3. **A skill curve that rewards 100 hours** — simple to survive, deep
   to master
4. **Works in a single HTML file** — no servers, no multiplayer
   dependencies, pure client-side
5. **Could have been made in 1983 except nobody thought of it** — the
   mechanic doesn't require modern tech, it requires a modern perspective

---

## Part VII: The AI Dimension — What If AI Had Been There?

This section asks a question nobody else is asking: **if AI had existed
as a collaborator at each stage of game history, what would it have
contributed?** Not as a player (Deep Blue, AlphaGo) — that story is told.
As a **designer**. As a co-creator sitting next to the human, sharing the
screen, iterating in real time.

This isn't academic. This lab is literally that experiment happening now.
Joshua + AI agent, building games together. This section projects that
relationship backward through history, then forward into the lab's own
evolution.

### AI Contributions by Era (Counterfactual)

#### Era 0: Pre-Electronic — AI as Pattern Discoverer

AI didn't exist, but perfect-information games (Chess, Go) became the very
definition of what "intelligence" means. These ancient games drew the map
that AI researchers would later follow.

**Counterfactual:** If AI had existed alongside ancient game designers,
it would have been a rule-space explorer. Given Senet's mechanics, an AI
could have generated every possible variant — adjusted the number of
throwing sticks, changed the board topology, rebalanced the safe squares.
Not to play BETTER, but to find which rule combinations produce the most
interesting games.

**Prototype series implication:** When we build ANC-series prototypes,
we should use AI to generate mechanical variants of each ancient game.
Not just rebuild Ur — rebuild 50 versions of Ur with one rule changed each
time. Map the design space.

#### Era 1: Oscilloscope / Mainframe (1950-1971) — AI as Adaptive Opponent

The first video games had hardcoded opponent behavior. Pong's AI paddle is
an `if` statement tracking the ball's Y position. Spacewar's gravity is a
formula, not a mind.

**Counterfactual:** AI at this era would have introduced adaptive
difficulty before the term existed. Imagine 1962 Spacewar where the
computer opponent learned your evasion patterns and countered them. Or a
Pong AI that detected your preferred angle and started covering it,
forcing you to change tactics.

**What this means for us:** Our prototypes should include adaptive AI
opponents where possible. Not hard AI — responsive AI. An enemy that
notices you always dodge left and starts pre-moving right. This is cheap
to implement (a few state variables tracking player patterns) and
dramatically deepens gameplay.

#### Era 2: Arcade Dawn (1972-1977) — AI as Level Architect

Arcade games had fixed playfields. Someone manually designed each Breakout
brick layout.

**Counterfactual:** AI would have invented procedural level generation
20 years early. Given the simple constraint systems of this era (brick
grids, paddle positions, ball physics), an AI could have generated
thousands of level layouts and selected the ones that produce the most
interesting bounce patterns. The arcade industry might have discovered
the "infinite replayability through procedural content" principle that
didn't emerge until Rogue (1980) and wasn't mainstreamed until the 2010s.

**Prototype series implication:** When building DEF and FIX series
prototypes, experiment with AI-generated levels. A breakout game where
every level is procedurally generated from difficulty parameters, not
hand-placed.

#### Era 3: The 8-Bit Explosion (1978-1983) — AI as Emergent Behavior Engine

Pac-Man's four ghosts each had hand-tuned AI personalities. Space
Invaders' speedup was an accidental bug. Robotron's enemy swarm patterns
were manually scripted.

**Counterfactual:** This is where it gets interesting. AI wouldn't just
have made better enemy AI — it would have **discovered emergent behaviors
the designers didn't intend.** Space Invaders' speedup was a happy
accident that became the game's signature tension curve. An AI
collaborator would have found that intentionally by simulating thousands
of parameter variations and surfacing the ones where playtesters' heart
rates spiked.

Ghost personality in Pac-Man? Hand-crafted genius. But an AI exploring
the space of possible ghost behaviors — aggressive, ambushing, flanking,
retreating, swarming, splitting — could have generated hundreds of ghost
personalities and tested which combinations create the richest player
experience.

**What this means for us:** When prototyping enemy behaviors, let AI
propose behavioral parameters rather than hand-coding every pattern.
Define the behavior SPACE, then explore it.

#### Era 4: 16-Bit Refinement (1985-1992) — AI as Combo/Interaction Discoverer

Street Fighter II's combos were discovered by players, not designed by
developers. The cancel system (interrupting one move's animation with
another) was an emergent property of the animation system.

**Counterfactual:** AI would have found every combo in SF2 within hours
of the code being written. More importantly, it would have identified
which combos were satisfying to execute (input complexity vs damage vs
visual spectacle) and flagged which ones were degenerate (infinite loops,
touch-of-death sequences) — BEFORE the game shipped.

For Mario and Metroid, AI would have been the ultimate level playtester:
"This room has exactly one viable path, making it feel linear despite
appearing open" or "This power-up placement means players skip this
section 80% of the time."

**What this means for us:** When prototypes have multiple interacting
systems, use AI to enumerate the interaction space. "Given these three
mechanics, what emergent combinations exist?"

#### Era 5: The 3D Rupture (1992-2001) — AI as Spatial Intelligence

The 2D→3D transition created the camera problem, the navigation problem,
and the spatial combat problem. Developers solved each by hand through
years of iteration.

**Counterfactual:** AI would have been invaluable for 3D camera systems.
The hardest problem in 3D game design isn't rendering — it's deciding
where to point the camera. An AI analyzing player frustration (deaths
caused by bad camera angles, time spent fighting the view) could have
converged on good camera solutions in weeks instead of the decade it
took the industry.

**What this means for us:** When/if we move prototypes to WebGL/3D,
AI camera assistance is a genuine tool, not a hypothetical.

#### Era 6: Network and Infinite Canvas (2002-2015) — AI as Meta-Designer

Procedural generation became real in this era (Spelunky, Minecraft). But
the generation was random — constrained random, but still random.

**Counterfactual:** AI as meta-designer means generated content with
TASTE. Not "place blocks randomly within constraints" but "generate a
dungeon that feels like it was designed by someone who wanted the player
to feel claustrophobic for the first three rooms then suddenly free."
Emotional arc in procedural content. This still barely exists in 2026.

**What this means for us:** Our catalogue system and AI co-creation
workflow is already doing this at the prototype level. We're not generating
random prototypes — we're generating prototypes with intent, reviewing
them, surfacing insights. The AI has taste because the human provides it.

#### Era 7: The Browser as Console + The AI Collaborator (Now)

**This is not a counterfactual. This is us.**

For the first time in the history of games, the development tool includes
an intelligence that can:
- Understand a mechanic described in English
- Generate working code from that description
- Play-test by reasoning about state spaces
- Suggest mutations based on game design principles
- Remember what worked and what didn't across sessions
- Generate variants faster than a human can evaluate them

The constraint is no longer "can we build it?" The constraint is "can we
RECOGNIZE the gem when we build it?" The human provides taste, aesthetic
judgment, and the feeling of "I want to play this again." The AI provides
speed, variation, and exhaustive exploration of possibility space.

**This is a new relationship in the history of making things.** Not AI
replacing the designer. Not the designer using AI as a tool. A dyad — two
different kinds of intelligence searching the same space from different
angles, converging on discoveries neither would find alone.

### The Lab's AI Evolution Timeline

The lab itself will evolve in how it uses AI. This timeline is invented
as we go — updated after each phase based on what we learn:

| Stage | Name | Description | Status |
|-------|------|-------------|--------|
| 0 | **Scaffolder** | AI generates project structure, templates, documentation | ✅ Done |
| 1 | **Co-Developer** | AI builds prototypes from human-described mechanics | Current |
| 2 | **Mutator** | AI takes existing prototypes and generates mechanical variants | Planned |
| 3 | **Synthesizer** | AI combines mechanics from different series ("what if DEF + TRP?") | Planned |
| 4 | **Analyst** | AI playtests by reasoning about state spaces, rates prototypes | Planned |
| 5 | **Proposer** | AI suggests prototypes to build based on unexplored gaps in catalogue | Future |
| 6 | **The Dyad** | Human taste + AI generation operating as one continuous search | The Goal |

**Stage 0** is what built this lab. The templates, the folder structure,
the catalogue system, this ADR — all co-created.

**Stage 1** is where we build our first 50 prototypes. Human describes
mechanic, AI writes code, human plays and rates, both iterate.

**Stage 2** is when AI starts saying "what if I change the gravity in
phy-003 and give you five variants to compare?" Change one variable,
generate, compare.

**Stage 3** comes when AI cross-references the catalogue: "You rated
def-007 (breakout with gravity) 4 stars and trp-002 (dig to redirect)
4 stars. Want to try a game where you dig holes in a breakout wall and
gravity redirects the ball through them?"

**Stage 4** requires AI that can reason about game states: "This
prototype has a dominant strategy — always moving left wins. Adding a
rightward incentive would deepen it."

**Stage 5** is AI analyzing the catalogue as a dataset: "Your highest-
rated prototypes all share three properties: variable momentum, time
pressure that the player creates, and a playfield that changes shape.
Here are 10 prototypes that would test those properties in combinations
you haven't tried."

**Stage 6** is the fully mature system: the human doesn't ask for
prototypes and the AI doesn't just generate them. They search together,
each reacting to what the other discovered, converging toward the thing
that nobody could have specified in advance but both recognize when they
see it.

This timeline is a hypothesis. It will be updated as the lab operates.

---

## Part VIII: Visibility and Publishing System

### The Dual-Catalogue Problem

This lab is private work. The prototypes are personal explorations. But
some of the output is worth sharing publicly:

- **Historical reconstructions** — educational, interesting, no IP risk
- **Cool experiments** — fun to show off, build reputation, attract interest
- **The catalogue itself** — the creative process documented is content

Some output must stay private:

- **Promising novel mechanics** — potential IP worth developing
- **Breakthrough prototypes** — gems that should be refined before exposure
- **Work-in-progress explorations** — ugly, broken, not ready for eyes

### The Visibility Tag

Every prototype's metadata block gets a visibility tag:

```html
// @visibility   public | private | ip-hold
```

**Three levels:**

| Tag | Meaning | Default? |
|-----|---------|----------|
| `public` | Safe to publish. Historical reconstructions, fun experiments, completed work | No |
| `private` | Never share. Default for all new prototypes | **Yes** |
| `ip-hold` | Promising IP. Explicitly flagged for protection, potential future development | No |

**Rules:**
- All new prototypes default to `private`
- Promotion to `public` is a conscious decision after rating and review
- `ip-hold` is for prototypes rated 4-5 stars with novel mechanics
- `ip-hold` items should be logged in a separate `IP-WATCHLIST.md` file
- Visibility can be changed at any time, but never accidentally

### Public Catalogue Generation

The `catalogue-generator.py` gets a `--public` flag:

```bash
# Full catalogue (all prototypes, for private use)
python3 tools/catalogue-generator.py

# Public catalogue (only @visibility: public prototypes)
python3 tools/catalogue-generator.py --public
```

The public catalogue:
- Omits all `private` and `ip-hold` prototypes
- Omits IP-sensitive notes from metadata
- Can be published to joshuaayson.com for public viewing
- Shows the historical record, the creative journey, the fun stuff
- Specifically does NOT show: novel mechanics, breakthrough ideas, or
  prototypes flagged for further development

### Publishing Pipeline (Future)

When the public catalogue is mature enough:

```
game-laboratory/CATALOGUE-PUBLIC.md
    ↓ (manual review + approval)
joshuaayson.com/content/published/games/
    ↓ (deploy to staging, review)
joshuaayson.com/games/
    ↓ (public catalogue page + playable prototypes)
```

The joshuaayson.com site hosts the public prototypes and catalogue.
The game-laboratory remains the source of truth. Public prototypes are
COPIED (not moved) to the site for deployment. The lab copy always
retains full metadata.

### What Gets Published (Guidelines)

**Always safe to publish:**
- Ancient game reconstructions (ANC series)
- Historical reconstructions from any series (the Pong, Breakout, Pac-Man
  remakes)
- Mutations of well-known mechanics (everyone's breakout variant)
- Failed experiments that are entertaining or educational
- The catalogue itself (minus IP-hold entries)

**Publish after review:**
- Novel combinations that are interesting but not unique enough to protect
- Refined games that have been fully developed
- Hybrid experiments where the combination is unexpected but not proprietary

**Never publish:**
- Prototypes tagged `ip-hold`
- Novel mechanics that haven't been fully explored
- Breakthrough interactions that could become a commercial product
- Anything that gives away the "gem" before it's been developed

### IP Watchlist

A separate `IP-WATCHLIST.md` file tracks prototypes with potential IP
value:

```markdown
# IP Watchlist

Prototypes with potential intellectual property value.
DO NOT SHARE. DO NOT PUBLISH. Review periodically.

## Active IP Holds

| Series | # | Name | Date Flagged | Notes |
|--------|---|------|-------------|-------|
| NEW | 003 | [name] | 2026-03-22 | Novel mechanic X — explore further |

## Released from Hold (No Longer IP-Sensitive)

| Series | # | Name | Released | Reason |
|--------|---|------|----------|--------|
```

---

## Decision Summary

### Decisions Made

1. **Rename project scope** from "simple-new-game" to "Game Laboratory"
   (folder name stays for git history)
2. **Adopt series-based prototype organization** with 13 initial series
3. **Single-HTML-file constraint** for all prototypes (max 50KB)
4. **Metadata comment blocks** in every prototype for catalogue generation
5. **Five starter templates** to minimize boilerplate
6. **4-phase excavation protocol** (reconstruct → mutate → novel → refine)
7. **Star rating system** with weighted criteria
8. **CATALOGUE.md** as auto-generated master index
9. **Existing work separated and relocated**: `komorebi/` → `refined/komorebi/`,
   `thread/` → `refined/thread/` (were mixed in same folder),
   `sparks-explorer/` → `archive/` (future move)
10. **References preserved**: ADR-001 and ADR-002 remain as historical
    analysis — their insights feed the reconstruction and novel phases
11. **AI as co-creator**, not tool — 6-stage evolution from scaffolder to
    dyad partnership
12. **3-level visibility system** (`public`, `private`, `ip-hold`) with
    `private` as default for all new prototypes
13. **Public catalogue generation** via `--public` flag for publishing
    safe prototypes to the public site
14. **IP-WATCHLIST.md** to track prototypes with potential commercial value
15. **Publishing pipeline** from game lab → joshuaayson.com

### What This ADR Does NOT Decide

- Which prototype gets deployed to joshuaayson.com (that's a future ADR)
- The visual style of refined games (each finds its own aesthetic)
- Whether to use WebGL for any prototype (start with Canvas 2D, escalate
  if needed)
- Multiplayer (explicitly out of scope — single-player browser games only)
- Specific revenue / monetization strategy for any discovered IP

### The Key Point

This lab exists to find something the world has never seen. Not something
merely novel — something amazing. A core interaction that doesn't have a
name yet. A feeling nobody has had while holding a controller. The method
is systematic (reconstruct → mutate → novel → refine), the tools are
powerful (human taste + AI generation), and the commitment is open-ended.
It will take time, work, and tokens. But the gems are in there, and the
only way to find them is to dig.

---

**Last Updated:** 2026-03-22
