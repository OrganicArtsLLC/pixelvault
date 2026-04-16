# ADR-002: Novel Game Genre Exploration

**Status:** Proposed
**Date:** 2026-03-21
**Author:** Joshua Ayson / OA LLC
**Project:** Pixel Vault
**Supersedes:** ADR-001 (mashup approach rejected — seeking genuinely new genre)

---

## Context

ADR-001 analyzed classic arcade mechanics and proposed mashup combinations. After review, the direction is wrong. We're not looking for "Joust meets Tron" or "Lode Runner meets Asteroids." We're looking for a game that defines its own genre — a core interaction that hasn't been the primary mechanic of any game before.

### What We're After

- A genuinely new core verb — not "shoot," "jump," "steer," or "match"
- Instantly readable on screen — see it, want to play it, understand it in 3 seconds
- Simple to play, hard to master, always fun
- Single-screen, browser-based, retro aesthetic
- The kind of thing that could have appeared on an Apple IIgs and blown minds

### How Genres Are Born

Every game genre is defined by a **core verb** and a **spatial metaphor**:

| Genre | Core Verb | Spatial Metaphor |
|-------|-----------|-----------------|
| Platformer | JUMP | Platforms + gaps |
| Shooter | SHOOT | Field of targets |
| Racer | STEER | Track/path |
| Puzzle | ARRANGE | Grid/board |
| Fighter | STRIKE | Ring/arena |
| Roguelike | EXPLORE | Dungeon/maze |
| Golf/Billiards | AIM + LAUNCH | Trajectory field |
| Tower Defense | PLACE | Path with nodes |
| Rhythm | TIME | Musical track |

The question: **What core verbs haven't been the PRIMARY mechanic of an arcade game?**

Verbs that exist in games as secondary mechanics but have never been the entire point:
- **SPLIT** (becoming multiple entities)
- **ORBIT** (swinging on a tether)
- **ECHO** (spawning time-delayed copies of yourself)
- **PULSE** (expanding/contracting as the primary action)
- **WEAVE** (drawing closed geometry in free space)
- **ERODE** (permanent terrain destruction as attack)

---

## Six Novel Genre Concepts

Each concept proposes a genuinely new primary mechanic that has not been the core of any existing game genre.

---

### Concept 1: ECHO

**Core Verb:** RECORD + REPLAY
**Genre Name:** Shadow Choreography

**The Idea:**
You move through the arena. Every few seconds, the game snapshots your last 5 seconds of movement and spawns a "ghost" — an autonomous copy that replays your recorded path on loop, forever. Ghosts destroy enemies they touch.

You are choreographing an army of shadow copies. After 30 seconds you might have 6 ghosts running independent patterns while you dodge, weave, and create new ones. The game is about designing movement patterns that create overlapping coverage.

**What the screen looks like:**
A bright player surrounded by 4-5 translucent copies, each running a different looping pattern. Glowing paths trace where they'll go. Enemies approach from all sides. It looks like a synchronized dance of light.

**Controls:**
Arrow keys to move. That's it. Movement IS the weapon. Your history IS your army.

**Why it's new:**
No game has made "your past movement becomes autonomous weaponry" the entire mechanic. Games have ghosts (racing games) and time mechanics (Braid), but never as an arena survival loop where you're a movement choreographer.

**The hook:**
You watch your first ghost repeat your panicked zigzag and think: "If I had moved more deliberately, that ghost would be useful." Immediately you start thinking about movement as design. The skill ceiling is infinite — expert players create intricate patrol patterns that lock down the arena while new players survive on chaos.

**Difficulty escalation:**
- Waves 1-3: Slow enemies, learn that ghosts replay your path
- Waves 4-6: Faster enemies, need deliberate ghost placement
- Waves 7+: Ghost-immune enemies (need direct contact kills), plus enemies that chase ghosts (drawing your shadows away)
- Wave 10+: Ghosts have limited lifespan (oldest fades), forcing constant renewal

**Emergent depth:**
- "Sentinel" strategy: move in tight loops to create ghosts that patrol one area
- "Sweeper" strategy: move in long arcs to create ghosts that cover wide ground
- "Trap" strategy: use yourself as bait, lay ghosts in an enemy's predicted path

**Risk/reward:**
Standing still = safe (no new ghost), but your ghost army decays. Moving = vulnerable, but builds your defense. You MUST move to survive long-term.

**Visual magnetism: 9/10** — Multiple glowing copies moving in synchronized patterns is mesmerizing
**Instant legibility: 8/10** — "Oh, those copies are replaying where I was"
**Skill ceiling: 10/10** — Movement pattern design has infinite mastery potential
**Implementation: Medium** — Ghost recording/replay, trail rendering, collision

---

### Concept 2: TETHER

**Core Verb:** ORBIT + SWING
**Genre Name:** Orbital Arena

**The Idea:**
You are a mass on a tether, orbiting a central anchor. You control your orbit radius (extend/retract) and can release + re-latch to different anchor points scattered around the arena. Enemies approach from all directions. You swing through them to destroy them.

The physics: You're always in motion. Extending the tether = wider orbit, slower speed. Retracting = tighter orbit, faster speed. Conservation of angular momentum — retract suddenly and you WHIP around at high speed. Release the tether and you fly in a straight line until you latch onto a new anchor.

**What the screen looks like:**
A bright dot swinging in a wide arc around a central post, trailing light. Enemy clusters approach. The player retracts mid-swing, whipping into a tight fast spiral that shreds through a group of enemies. The player releases, sails across the screen, latches a new post, and swings wide to sweep the other side.

**Controls:**
Up: Retract tether (faster, tighter)
Down: Extend tether (slower, wider)
Space: Release/re-latch

Three inputs. Orbital mechanics does the rest.

**Why it's new:**
Orbital mechanics exist in space games (gravity assists, etc.) but have never been the ENTIRE interface. You don't thrust, steer, or shoot. You swing. The verb is "orbit" and nothing else. Cut the Rope (2010) uses rope physics but as puzzle, not arena combat.

**The hook:**
The first time you retract and feel the speed spike — whipping around the post at 3x speed, tearing through a cluster — you get a visceral rush. It's the slingshot feeling. The physics FEEL incredible because angular momentum is intuitive even if you can't name it.

**Difficulty escalation:**
- Waves 1-3: One central anchor, slow enemies from edges
- Waves 4-6: 3 anchors to choose from, enemies that dodge your orbit
- Waves 7-9: Anchors become temporary (disappear after 15s), forcing releases
- Waves 10+: Enemies with their own orbits (counter-swing), anchor-destroying enemies

**Emergent depth:**
- Tight orbit = safe but small kill zone
- Wide orbit = huge sweep but enemies can approach inside your circle
- Release timing = precision strikes at specific angles
- Anchor selection = positioning strategy (which post gives best coverage?)

**Visual magnetism: 10/10** — A glowing dot swinging in arcs with trailing light is immediately captivating
**Instant legibility: 9/10** — Anyone who has swung a ball on a string understands this instantly
**Skill ceiling: 9/10** — Angular momentum mastery, release timing, anchor switching
**Implementation: Medium** — Orbital physics, tether rendering, multi-anchor system

---

### Concept 3: SPLIT

**Core Verb:** DIVIDE + MERGE
**Genre Name:** Fission Arena

**The Idea:**
You are one entity. Press a button and you split into two halves. Left half: WASD. Right half: Arrow keys. Each half is weaker and smaller. Press the button again and they merge back together (must be adjacent). Merged = strong, slow, big target. Split = weak, fast, covers more ground.

Enemies require different tactics: small enemies die to either half, big enemies need a merged hit, and swarm enemies need both halves working different flanks.

**What the screen looks like:**
A single glowing entity patrols the center. Enemies approach from four sides. The entity splits — two smaller glowing copies, one blue, one orange, sprint in opposite directions. Each half destroys enemies on its side. A large enemy appears in the center. Both halves race back, merge with a flash, and the combined entity slams through the boss.

**Controls:**
WASD: Move (or move left half when split)
Arrow Keys: Move right half (when split), unused when merged
Space: Split / Merge toggle

**Why it's new:**
No arcade game has made the player themselves becoming TWO independently controlled entities the core mechanic. Co-op games have two players. This is one player with two brains. The split second where you're controlling both halves with separate hands — that cognitive challenge is unprecedented.

**The hook:**
Controlling two independent entities with your two hands creates a brain-state that doesn't exist anywhere else in gaming. It's the patting-your-head-while-rubbing-your-stomach of video games. Frustrating for 30 seconds, then it clicks, and you feel superhuman.

**Difficulty escalation:**
- Waves 1-3: Enemies from one direction at a time (don't need to split)
- Waves 4-6: Enemies from two directions simultaneously (MUST split to cover both)
- Waves 7-9: Enemies that are only vulnerable to one color (blue half vs orange half)
- Waves 10+: Merge-only bosses + split-only swarms in the same wave

**Risk/reward:**
Split = amazing coverage but if EITHER half dies, you lose a life. Each half is fragile. You're twice as powerful but twice as vulnerable.

**Visual magnetism: 8/10** — The split/merge animation is cool but the resting state is less dramatic
**Instant legibility: 7/10** — Takes a moment to understand the dual control (but the split animation helps)
**Skill ceiling: 10/10** — Dual independent control is the deepest skill well imaginable
**Implementation: Low-Medium** — Two entities, input splitting, merge detection

---

### Concept 4: THREAD

**Core Verb:** WEAVE + ENCLOSE
**Genre Name:** Geometry Trapper

**The Idea:**
You move freely across the arena trailing a visible line (like string). The line persists. When your line crosses itself — forming any closed shape (triangle, quadrilateral, any polygon) — everything inside that shape is captured: enemies are destroyed, collectibles are scored. The shape flashes, clears, and that segment of line disappears. The rest of your trailing thread remains.

But: enemies can BREAK your thread on contact. A broken thread loses all connection to its start point — you can't close shapes with a severed line. You must weave quickly, close shapes before enemies cut your thread, and choose which enemies to enclose.

**What the screen looks like:**
A player zipping around the arena, trailing a bright cyan line. The screen is criss-crossed with thread. The player banks hard, crosses their own line — a triangle flashes into existence, three enemies inside it evaporate in a burst. Meanwhile another enemy is chewing through a thread line on the other side of the screen.

**Controls:**
Arrow keys: Move freely (8-directional)
Space: Cut your own thread (voluntary sever — useful for removing broken segments)

**Why it's new:**
Qix (1981) had you drawing lines to claim territory, but from the border inward, on a rectangular grid, with strict rules. This is FREEFORM geometry in open space. The shapes are organic, imperfect, hand-drawn. And the thread is vulnerable — it's a racing game against enemies who want to destroy your geometry before you can close it.

**The hook:**
You chase three enemies in a cluster, loop around them, and when the line closes — FLASH — they're gone. Drawing their prison with your movement is deeply satisfying. It's like lassoing, but the lasso is permanent until used. And the bigger the shape, the bigger the score, but the longer the thread = more for enemies to cut.

**Difficulty escalation:**
- Waves 1-3: Slow enemies, learn to enclose basic shapes
- Waves 4-6: Thread-cutting enemies introduced, must close shapes fast
- Waves 7-9: Enemies that dodge (try to avoid enclosure), requiring prediction
- Waves 10+: Minimum shape size required (can't just make tiny triangles), armored enemies need two enclosures

**Emergent depth:**
- Large shapes = more points but higher risk of being cut
- Herding enemies into clusters before enclosing
- Using thread lines as barriers (enemies bounce off intact thread)
- Speed vs precision — zooming creates wide wobbly shapes, slow creates tight ones

**Score system:**
Points = area of closed shape × number of enemies inside × speed bonus (faster closure = higher multiplier)

**Visual magnetism: 9/10** — Geometric lines criss-crossing the screen, shapes flashing as they close — it's like watching art get drawn
**Instant legibility: 8/10** — "Player draws line, line makes shape, shape catches enemies" is intuitive
**Skill ceiling: 9/10** — Freeform geometry creation under pressure, speed vs precision, herding tactics
**Implementation: Medium-High** — Polygon detection from freeform lines, area calculation, thread-enemy interaction

---

### Concept 5: PULSE

**Core Verb:** EXPAND + CONTRACT
**Genre Name:** Waveform Arena

**The Idea:**
You are a circle. You can pulse — expand outward (push everything away) then contract inward (pull everything toward you). The rhythm of your pulsing is your only weapon.

Pulsing creates a visible wave that radiates outward. Enemies hit by the wave are pushed. Push an enemy into the arena wall = destroyed. Push two enemies into each other = both destroyed. Pull an enemy toward you then pulse to push them away = maximum velocity launch.

The twist: each pulse costs energy. Energy regenerates slowly. Holding expanded state drains faster. The dance is managing your expansion/contraction rhythm while positioning to weaponize the physics.

**What the screen looks like:**
A glowing circle pulsates at the center of the screen. Concentric rings ripple outward with each pulse. Enemies float in from the edges. The circle expands — WHOMP — enemies scatter outward like billiard balls. Two smash into the walls and flash out of existence. The circle contracts, and nearby enemies slide inward. Another pulse — WHOMP — they launch backward into an incoming cluster. Chain reaction. Score multiplier climbs.

**Controls:**
Space (hold): Expand
Space (release): Contract
Arrow keys: Move (slowly — you're heavy)

Two interactions. Your body is the weapon.

**Why it's new:**
No game has made pulsation — expand/contract breathing — the entire mechanic. It's almost biological. The rhythm you find is personal. Fast pulsers play differently than slow pulsers. It's an arena game where you can't directly kill anything — you can only create physics interactions that result in kills.

**The hook:**
The moment you pull three enemies toward you, then PULSE right as they arrive, launching all three into the wall simultaneously for a triple kill — that's the "I AM the weapon" feeling. No projectile, no trail, no sword. Just your presence expanding.

**Difficulty escalation:**
- Waves 1-3: Light enemies, easy to push, learn the rhythm
- Waves 4-6: Heavy enemies (multiple pulses to move), requires pull-then-push combos
- Waves 7-9: Enemies that anchor themselves (can't be pushed, must be collided into by other enemies)
- Waves 10+: Enemy pulsars (they push YOU), creating wave interference patterns

**Emergent depth:**
- Pull-push combo: contract to gather, expand to scatter
- Wall-bounce angles: position so pushes send enemies into walls
- Enemy-on-enemy: use heavy enemies as battering rams against light ones
- Rhythm optimization: quick staccato pulses vs long sustained pushes

**Visual magnetism: 9/10** — Concentric rings expanding from a pulsing center is hypnotic and powerful
**Instant legibility: 8/10** — "Big thing pushes small things" is primal, instant understanding
**Skill ceiling: 8/10** — Rhythm mastery, positional play, combo physics
**Implementation: Medium** — Physics with push/pull forces, wave rendering, collision chains

---

### Concept 6: BURROW

**Core Verb:** DIG + SURFACE
**Genre Name:** Subterranean Arena

**The Idea:**
The arena has TWO layers: the surface and the underground. On the surface, you can see everything but enemies can see (and chase) you. Underground, you're invisible and invulnerable — but you're blind (only see a small radius). You choose when to surface and when to burrow.

The mechanic: burrowing leaves a tunnel behind you. You can travel through your old tunnels fast (like pipes). Surface to attack enemies (you're only lethal when you pop UP from underground — the surfacing burst destroys nearby enemies). Then burrow again before they swarm you.

The screen shows the surface arena AND a minimap of your tunnel network below. Over time you build an elaborate subway system under the battlefield, choosing where to surface for ambush attacks.

**What the screen looks like:**
A top-down arena. Enemies patrol the surface. Suddenly the ground cracks and the player ERUPTS upward in a burst, destroying two enemies. They hang on the surface for one second, then dive back under. Underground, a network of tunnels is visible as dotted lines. The player races through a tunnel to the other side, surfaces again behind a cluster — BURST — three more enemies gone. The surface heals behind them.

**Controls:**
Arrow keys: Move (surface or underground)
Space: Toggle burrow/surface (SURFACING is the attack)

**Why it's new:**
Dig Dug (1982) had digging but as a slow tactical puzzle. This is fast, aggressive, and the digging creates INFRASTRUCTURE (reusable tunnels). The dual-layer arena — visible surface vs blind underground — creates a stealth/ambush loop that no arcade game has explored. You're building a transit system under a battlefield.

**The hook:**
Building your tunnel network turns the arena into YOUR territory. By wave 10 you have tunnels everywhere — you can pop up anywhere in 2 seconds. You've turned a chaotic battlefield into a home-field advantage. The surfacing burst feels like a shark surfacing — predatory and satisfying.

**Difficulty escalation:**
- Waves 1-3: Enemies don't know where you are underground, easy ambushes
- Waves 4-6: Enemies that listen (cluster near your last surface point)
- Waves 7-9: Burrowing enemies that enter YOUR tunnels and chase you underground
- Waves 10+: Tunnel collapse events (sections of your network cave in), forcing rebuilding

**Emergent depth:**
- Tunnel planning: create efficient networks for fast traversal
- Surface timing: pop up behind groups, not in front
- Bait-and-switch: surface briefly to draw enemies, burrow, surface elsewhere
- Underground enemy encounters: your tunnels become contested territory

**Visual magnetism: 8/10** — The surfacing burst animation is dramatic, the dual-layer view is intriguing
**Instant legibility: 7/10** — Dual layers take a beat to understand, but the surfacing burst is clear
**Skill ceiling: 9/10** — Tunnel network design, timing, spatial memory
**Implementation: Medium-High** — Dual-layer rendering, tunnel network, minimap, surfacing mechanics

---

## Comparison Matrix

| Criterion | ECHO | TETHER | SPLIT | THREAD | PULSE | BURROW |
|-----------|------|--------|-------|--------|-------|--------|
| **Genre novelty** | 10 | 9 | 9 | 8 | 9 | 8 |
| **"Can't wait to play" visual** | 9 | 10 | 7 | 9 | 9 | 8 |
| **3-second legibility** | 8 | 9 | 7 | 8 | 8 | 7 |
| **Simple to play** | 10 | 8 | 6 | 8 | 9 | 8 |
| **Hard to master** | 10 | 9 | 10 | 9 | 8 | 9 |
| **Always fun (even losing)** | 9 | 10 | 7 | 8 | 9 | 8 |
| **Retro-feasible** | 9 | 9 | 9 | 8 | 9 | 7 |
| **Implementation feasibility** | 7 | 8 | 9 | 6 | 8 | 6 |
| **Sound design potential** | 8 | 9 | 7 | 7 | 10 | 8 |
| **"One more try" factor** | 9 | 9 | 8 | 8 | 9 | 9 |
| **TOTAL** | **89** | **90** | **79** | **79** | **88** | **78** |

---

## Detailed Analysis of Top 3

### TETHER (90 pts) — "Orbital Arena"

**Strongest case for:**
- The swing physics create the most visceral, immediately satisfying game feel
- Three inputs total (extend, retract, release) — simplest control scheme
- The visual of a dot whipping around anchor points is INSTANTLY compelling
- Anyone who has swung a ball on a string already knows the physics intuitively
- The "retract-to-whip" moment — where you pull tight and speed spikes — is a guaranteed rush
- Anchor switching adds strategic depth without complicating controls

**Strongest case against:**
- Player doesn't have true free movement (always orbiting)
- Could feel constraining until mastery of release/re-latch
- Orbital physics tuning is critical — too floaty = frustrating, too tight = boring

---

### ECHO (89 pts) — "Shadow Choreography"

**Strongest case for:**
- The deepest innovation — "your movement history becomes weaponry" is genuinely unprecedented
- The visual of multiple synchronized ghosts is stunning and unique
- Simplest possible controls — just arrow keys, movement IS everything
- Infinite skill ceiling — expert players will choreograph ghost patterns like Bach fugues
- Watching replays of good runs would be mesmerizing (shareability)
- The "aha" moment when you realize deliberate movement > panicked movement is profound

**Strongest case against:**
- Takes slightly longer to "get" than TETHER (the ghost mechanic needs one death to understand)
- Ghost rendering could get visually noisy with many copies
- Recording/replay system is more complex to implement correctly

---

### PULSE (88 pts) — "Waveform Arena"

**Strongest case for:**
- The most primal interaction — expand/contract is almost biological (breathing)
- Indirect kills (physics-based) create the best emergent chain reactions
- Sound design potential is off the charts — each pulse is a WHOMP, rhythm becomes personal
- The expand animation with concentric rings is hypnotic
- Simplest mental model: "I push things. Push things into walls. Things die."

**Strongest case against:**
- Indirect combat can feel disconnected (you never directly kill anything)
- Slower pace than TETHER or ECHO (positioning game vs reaction game)
- Could feel repetitive if push-into-wall is the only kill path (needs enemy variety)

---

## Recommendation

**No recommendation.** This ADR presents the concepts for Joshua's review. The right game is the one that makes Joshua say "I want to play THAT one."

Questions to guide the decision:

1. **Which screen do you picture yourself staring at?** The synchronized ghost dance (ECHO), the whipping orbital arcs (TETHER), or the expanding shockwaves (PULSE)?

2. **Which verb feels most natural to your hands?** Arrow-keys-only choreography (ECHO), extend/retract/release rhythm (TETHER), or hold/release pulsation (PULSE)?

3. **Which game would you play at 11pm when you're tired?** The one that lets you zone out on patterns (ECHO/PULSE) or the one with visceral kinetic energy (TETHER)?

4. **Which game do you want to see on joshuaayson.com?** The abstract art piece (ECHO), the physics toy (TETHER), or the meditative weapon (PULSE)?

Any of the six are buildable. The bottom three (SPLIT, THREAD, BURROW) are strong but trade simplicity for depth. The top three are the sweet spot.

---

## Platform Constraints (Unchanged from ADR-001)

- Single HTML file, Canvas-based, zero dependencies
- localStorage for high scores (3-letter initials, 10 slots)
- Web Audio API for synthesized retro sound
- Under 500KB total
- 60fps on modern browsers
- Keyboard primary, touch as stretch

---

**Last Updated:** 2026-03-21
**Version:** 1.0.0
