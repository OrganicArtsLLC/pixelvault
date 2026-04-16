# ADR-004: The AI Archaeology Layer — Parallel Evolution as a Lens

**Status:** Accepted
**Date:** 2026-03-22
**Author:** Joshua Ayson / OA LLC
**Project:** Pixel Vault
**References:** ADR-003 Part VII (The AI Dimension), ADR-003 Part II (Technology Ladder)

---

## Table of Contents

- [Context](#context)
- [Part I: The Thesis — Two Timelines, One Story](#part-i-the-thesis--two-timelines-one-story)
- [Part II: The AI Timeline — Seven Eras of Machine Intelligence](#part-ii-the-ai-timeline--seven-eras-of-machine-intelligence)
- [Part III: The Convergence Map — Where AI Meets Games](#part-iii-the-convergence-map--where-ai-meets-games)
- [Part IV: AI as Participant in Each Game Category](#part-iv-ai-as-participant-in-each-game-category)
- [Part V: The Dual-Lens System — Implementation](#part-v-the-dual-lens-system--implementation)
- [Part VI: The Info Panel AI Layer](#part-vi-the-info-panel-ai-layer)
- [Part VII: The AI Archaeology Catalogue Extension](#part-vii-the-ai-archaeology-catalogue-extension)
- [Part VIII: Future Prototypes — AI-Native Experiments](#part-viii-future-prototypes--ai-native-experiments)
- [Decision Summary](#decision-summary)

---

## Context

ADR-003 Part VII asked: "What if AI had been there?" — a counterfactual
analysis of what AI would have contributed as a co-designer at each stage
of game history. That section established the premise. This ADR expands it
into something much larger: **a complete parallel timeline where AI evolution
is placed alongside game evolution as a dual-channel view of how intelligence
— human and machine — has changed what it means to create, play, and
discover.**

The insight that makes this more than academic: **game evolution and AI
evolution are not separate stories.** They are two expressions of the same
underlying question — *what happens when you give an intelligence a
constrained space and ask it to find optimal behavior?* Games constrain
human intelligence. AI research constrains machine intelligence. The
constraints shaped both. The resulting behaviors mirror each other in ways
nobody has mapped.

This ADR provides three things:

1. **The AI Timeline** — A standalone history of AI evolution structured
   to parallel the game technology ladder from ADR-003 Part II
2. **The Convergence Map** — Where the two timelines touch, influence,
   and mirror each other
3. **The Implementation Plan** — How to embed this dual-lens into every
   prototype, info panel, and catalogue entry in the laboratory

This is not a bolt-on feature. It is a new way of seeing the entire
project. Every prototype we build sits at a specific intersection of two
evolutionary lines. Understanding that intersection deepens the archaeology
and opens new categories of experiment.

### Why This Matters Beyond the Lab

The game industry tells one story: human designers inventing genres over
50 years. The AI industry tells another: researchers building increasingly
capable systems over 70 years. Nobody has laid these side by side and
asked: **where do the patterns rhyme?** Where did a breakthrough in one
domain foreshadow or enable a breakthrough in the other? Where did they
solve the same problem independently? Where did they miss each other
entirely?

That mapping is original. It doesn't exist. We are going to create it, and
the laboratory prototypes are the medium through which it becomes tangible
— not a paper, not a lecture, but playable artifacts that sit at the
intersection of both timelines.

---

## Part I: The Thesis — Two Timelines, One Story

### The Parallel Structure

Game evolution is driven by **technology removing constraints**. When
hardware could draw a dot on a screen, Tennis for Two was born. When
hardware could render sprites, Space Invaders was born. When hardware
could scroll the world, Defender was born. Each constraint that fell
opened a new possibility space, and human designers rushed to fill it.

AI evolution follows the same pattern, driven by different constraints:
**compute power, data availability, and algorithmic insight.** When
compute could handle search trees, chess programs appeared. When neural
networks could learn from data, image recognition emerged. When
transformers could process sequences, language models arrived. Each
constraint that fell opened a new capability space.

The parallel is structural, not metaphorical:

| Dimension | Game Evolution | AI Evolution |
|-----------|---------------|-------------|
| **Driver** | Hardware constraints falling | Compute/algorithm constraints falling |
| **Unit of progress** | New genre discovered | New capability demonstrated |
| **Explosion moment** | 8-bit era (1978-1983) — Cambrian explosion of genres | Deep learning era (2012-2020) — Cambrian explosion of applications |
| **The big rupture** | 2D → 3D (1992) — spatial dimension added | Narrow → General (2020s) — reasoning dimension added |
| **Refinement pattern** | 16-bit era deepened genres without inventing new ones | Scaling laws improve models without new architectures |
| **Emergent behavior** | SF2 combos (unintended), Invaders speedup (bug) | GPT emergent abilities (chain-of-thought, in-context learning) |
| **What the community adds** | Players discover depth designers didn't intend | Users discover prompting techniques researchers didn't anticipate |
| **The meta question** | What is a game? (still debated) | What is intelligence? (still debated) |

The two timelines don't just rhyme — they interrogate each other. The
history of games asks questions about intelligence that AI hasn't answered.
The history of AI asks questions about play that games haven't explored.

### The Three Relationships

When you lay both timelines on the same axis, three types of relationship
emerge:

**1. Convergence** — AI and games solving the same problem simultaneously
or in sequence. Example: pathfinding. Pac-Man ghosts (1980) used simple
A*-like chase algorithms. Academic AI was developing A* (formally published
1968) for exactly this kind of spatial reasoning. The game needed it for
fun; the researchers needed it for robots. Same problem, different stakes.

**2. Divergence** — AI and games splitting from a shared root. Example:
Chess. For games, chess was the endpoint — the deepest strategy board game.
For AI, chess was the starting point — the first benchmark. Game designers
moved away from chess toward real-time action. AI researchers moved toward
chess mastery. They parted ways at the same artifact.

**3. Anticipation** — One timeline foreshadowing a breakthrough in the
other. Example: procedural generation. Games invented PCG (Rogue, 1980;
Minecraft, 2011) decades before generative AI made "generation from
constraints" a mainstream capability. Conversely, neural style transfer
(2015) anticipated the game industry's interest in AI-generated art assets
(2023+). Each timeline contains early signals of what the other will
eventually need.

---

## Part II: The AI Timeline — Seven Eras of Machine Intelligence

This timeline is structured to parallel ADR-003 Part II's technology ladder.
Each era corresponds to a game evolution era, sharing the same years. The
question for each era: **what was AI capable of, and what would that
capability have meant for game design?**

### AI Era 0: Theoretical Foundations (Before 1950)

**Parallel game era:** Pre-electronic (physical games)

| What AI Had | What It Couldn't Do |
|-------------|-------------------|
| Turing's universal computation concept (1936) | No actual computers |
| Shannon's information theory (1948) | No learning from data |
| Boolean logic, formal proof systems | No perception, no generation |

**The connection to games:** Turing, Shannon, and von Neumann were all
fascinated by games. Shannon wrote "Programming a Computer for Playing
Chess" (1950) before any computer could actually do it. Von Neumann
co-authored *Theory of Games and Economic Behavior* (1944). The
mathematical foundations of both AI and game theory were laid by the
same people, at the same time, often in the same papers.

**Insight for the lab:** The deepest games (Go, Chess) are the ones that
attracted the deepest mathematical minds. The ancient games ARE the first
AI benchmarks, millennia before anyone conceived of artificial
intelligence. When we build ANC-series prototypes, we are literally
rebuilding the datasets that launched AI research.

### AI Era 1: Search and Symbols (1950-1971)

**Parallel game era:** Oscilloscope and Mainframe

| AI Milestone | Year | Capability Unlocked |
|-------------|------|-------------------|
| Turing Test proposed | 1950 | Defined the goal |
| Samuel's checkers program | 1952 | Machine learning from self-play |
| Dartmouth Conference ("AI" coined) | 1956 | Named the field |
| ELIZA chatbot | 1966 | Pattern-matching conversation |
| Perceptron controversy | 1969 | First AI winter approaches |

**What AI could do:** Search game trees exhaustively for small games.
Pattern-match text. Learn evaluations for board positions through
self-play. Prove simple theorems.

**What AI could NOT do:** See. Hear. Move. Generate anything creative.
Handle real-time decisions. Deal with continuous (non-discrete) spaces.

**The game connection:** While AI researchers were writing programs to play
checkers and chess on the same mainframes, Spacewar! (1962) was being
built on a PDP-1 down the hall at MIT. The AI researchers were asking
"can a machine think?" while the game developers were asking "can a
machine make you feel?" Different questions, same hardware, same building.

Samuel's checkers program (1952) is especially significant: it learned by
**playing against itself** — the exact method that would, 65 years later,
produce AlphaGo. Self-play as a training method was discovered in games,
applied to AI, and then returned to games (AlphaGo playing Go, AlphaStar
playing StarCraft). The loop between games and AI was established in the
first decade.

**Lab implication:** Our earliest prototypes (DEF, FIX) have opponents
that are if-statements — the same level of "intelligence" as 1960s AI.
Track this. The opponent AI in each prototype should be explicitly labeled
by its intelligence era.

### AI Era 2: Expert Systems and the First Winter (1972-1977)

**Parallel game era:** Arcade Dawn (Pong → Breakout)

| AI Milestone | Year | Capability Unlocked |
|-------------|------|-------------------|
| MYCIN (medical diagnosis) | 1972 | Rule-based expert reasoning |
| SHRDLU (natural language + blocks world) | 1972 | Grounded language understanding |
| First AI winter begins | ~1974 | Funding collapse, disillusionment |

**What AI could do:** Encode expert knowledge as if-then rules. Reason
in narrow, well-defined domains. Parse simple natural language about
toy worlds.

**What AI could NOT do:** Learn from experience (mostly). Handle
uncertainty. Generalize across domains. Perceive the real world.

**The game connection:** Arcade games of this era had zero AI ambition.
Pong's opponent is a paddle that tracks the ball's Y coordinate. Breakout
has no opponent at all — physics is the adversary. The simplest possible
"agent" (ball trajectory) creates compelling gameplay not because the
agent is smart, but because the physics creates patterns the HUMAN brain
finds satisfying to predict and exploit.

Meanwhile, MYCIN was encoding hundreds of medical rules to diagnose
infections — a system that was "intelligent" in a narrow sense but
couldn't react to anything in real time. The arcade industry and AI
research couldn't have been further apart in what they were building,
yet both were discovering the same thing: **specialization works.** A
system that does one thing well (diagnose infections, bounce a ball)
is more valuable than a system that does everything poorly.

**Lab implication:** The DEF-series prototypes should note this explicitly.
Pong's "AI" is pre-AI. The ball IS the intelligence — it creates the
emergent patterns. This is what AI researchers missed for decades:
sometimes the environment is smarter than the agent.

### AI Era 3: Knowledge Explosion and Neural Revival (1978-1983)

**Parallel game era:** 8-Bit Explosion (Cambrian explosion of genres)

| AI Milestone | Year | Capability Unlocked |
|-------------|------|-------------------|
| Expert systems commercialized | 1980s | AI enters industry |
| Hopfield networks | 1982 | Energy-based neural models |
| Backpropagation rediscovered | 1986 | Training deep networks (seeds planted) |
| Connection Machine (parallel computing) | 1985 | Massive parallelism |

**What AI could do:** Build sophisticated rule systems. Classify patterns
in small datasets. Play simple games at competitive levels. Search large
(but finite) possibility spaces.

**What AI could NOT do:** See images. Understand speech. Generate novel
content. Handle the real world's messiness.

**The game connection:** This is the most revealing parallel. Between 1978
and 1983, the game industry experienced its Cambrian explosion — more new
genres were invented than in any period before or since. Space Invaders,
Asteroids, Pac-Man, Defender, Donkey Kong, Tetris, Lode Runner. Every one
of those games contained an AI insight that the AI field wouldn't formally
discover for years or decades:

| Game | Year | AI Insight (Undiscovered in AI Until...) |
|------|------|-----------------------------------------|
| Space Invaders | 1978 | Emergent difficulty scaling (accidental speedup) → Curriculum learning (~2015) |
| Pac-Man | 1980 | Multi-agent behavior with distinct personalities → Cooperative multi-agent systems (~2000s) |
| Rogue | 1980 | Procedural content generation → Generative models (~2014) |
| Defender | 1981 | Real-time world larger than observation window → Partial observability in RL (~1990s) |
| Donkey Kong | 1981 | Narrative-driven level design → Goal-conditioned RL (~2018) |
| Tetris | 1985 | Optimal packing under real-time pressure → Combinatorial optimization with time constraints |

The game designers were building intuitive solutions to problems that AI
researchers were still formalizing mathematically. The 8-bit explosion
wasn't just a game explosion — it was an unrecognized explosion in applied
intelligence research.

**Lab implication:** Every Phase 1 reconstruction prototype should carry
a note identifying the AI concept it accidentally implemented. Pac-Man's
ghost personalities ARE multi-agent RL with behavioral policies. Space
Invaders' speedup IS emergent curriculum learning. Name these connections
explicitly.

### AI Era 4: The Expert System Boom and Second Winter (1985-1992)

**Parallel game era:** 16-Bit Refinement (depth within genres)

| AI Milestone | Year | Capability Unlocked |
|-------------|------|-------------------|
| Backpropagation published (Rumelhart/Hinton) | 1986 | Deep learning foundations |
| TD-Gammon (backgammon via RL) | 1992 | Reinforcement learning plays board games |
| Expert system boom, then collapse | ~1987-1993 | Over-promise → second AI winter |
| Subsumption architecture (Brooks) | 1986 | Behavior-based robotics |

**What AI could do:** Learn game evaluations through self-play (TD-
Gammon). Encode complex domain expertise. Navigate physical spaces
with simple behavior layers.

**What AI could NOT do:** See, in any useful sense. Create. Generalize
beyond narrow domains. Handle the real world reliably.

**The game connection:** The 16-bit era refined existing genres without
inventing new ones. AI followed the same pattern — refinement of known
techniques (expert systems got bigger, neural networks got theoretical
treatment) without fundamental breakthroughs. Both fields were in a
"deepening" phase.

TD-Gammon (1992) is the critical artifact. Tesauro's backgammon program
learned to play at world-champion level by playing millions of games
against itself — the same self-play principle from Samuel's 1952 checkers
program, but with neural networks. It proved neural RL could master a
game. The game industry didn't notice because they didn't need neural
networks — their AI was hand-tuned behaviors, and players loved it.

Street Fighter II's combo system (1991) is the game-side mirror: players
discovered emergent depth that designers didn't intend. In AI terms,
players were doing UNSUPERVISED EXPLORATION of the game's state-action
space and discovering high-value trajectories (combos) through pure trial
and error. The human brain was doing reinforcement learning on Capcom's
code, finding exploits the developers couldn't find with formal analysis.

**Lab implication:** When we reach Phase 2 (mutation), the AI can function
as an automated playtester — enumerate interaction combinations, flag
dominant strategies, identify emergent behaviors. This is TD-Gammon logic
applied to prototype evaluation.

### AI Era 5: Statistical Learning and Narrow Triumphs (1992-2011)

**Parallel game era:** 3D Rupture → Network/Infinite Canvas

| AI Milestone | Year | Capability Unlocked |
|-------------|------|-------------------|
| Deep Blue beats Kasparov | 1997 | Brute-force search + evaluation |
| Support Vector Machines mainstream | ~2000 | Practical classification |
| Netflix Prize | 2006 | Recommendation at scale |
| Watson wins Jeopardy! | 2011 | NLP + search + confidence estimation |
| ImageNet created | 2009 | Large-scale visual benchmark |

**What AI could do:** Beat humans at chess through exhaustive search.
Classify data. Recommend content. Parse structured text. Recognize some
visual patterns (with heavy engineering).

**What AI could NOT do:** See as well as a toddler. Generate images, text,
or code. Understand context. Transfer knowledge between domains.

**The game connection:** Deep Blue (1997) was the moment games and AI
collided in public consciousness. But it was a dead end — Deep Blue couldn't
play checkers, let alone design a game. It was the ultimate narrow AI,
and its victory over Kasparov taught the wrong lesson: that AI was about
brute force.

Meanwhile, the game industry was solving the 3D camera problem, the
real-time pathfinding problem, and the procedural generation problem —
all of which are AI problems wearing game-industry clothes. Game AI in
this era (Halo's combat AI, F.E.A.R.'s squad tactics, Left 4 Dead's
AI Director) was often more pragmatically intelligent than anything coming
out of AI research, because it had to work in real-time, under resource
constraints, and produce experiences humans found FUN, not just optimal.

F.E.A.R. (2005) deserves special mention: its GOAP (Goal-Oriented Action
Planning) system had enemies that genuinely flanked, retreated, and
coordinated. This was hierarchical task planning running at 60fps in a
shooter — practical AI that AI researchers weren't building because they
were focused on different benchmarks.

**Lab implication:** Game AI IS AI research, just published in different
conferences (GDC vs NeurIPS). Our prototypes should acknowledge this.
The minimap in `scr-001-defender` is a partial observability solution.
The ghost behaviors in `maz-001-pacman` are multi-agent policies. Name
the connection.

### AI Era 6: Deep Learning Changes Everything (2012-2022)

**Parallel game era:** Late network era → browser/mobile → AI collaborator

| AI Milestone | Year | Capability Unlocked |
|-------------|------|-------------------|
| AlexNet wins ImageNet | 2012 | Deep learning proven for vision |
| GANs introduced | 2014 | Image generation |
| AlphaGo beats Lee Sedol | 2016 | RL + deep learning masters Go |
| Transformer architecture | 2017 | Sequence modeling breakthrough |
| GPT-2 | 2019 | Coherent text generation |
| AlphaFold | 2020 | Protein structure prediction |
| DALL-E, Stable Diffusion | 2022 | Text-to-image generation |
| GitHub Copilot | 2021 | AI code generation |

**What AI could now do:** See. Read. Write. Generate images. Write code.
Play any Atari game from raw pixels. Master Go from scratch. Fold
proteins. Create art on command.

**The game connection:** This era is where the two timelines CRASH into
each other.

AlphaGo (2016) didn't just beat a Go master — it played moves that changed
how humans understand a 2500-year-old game. Move 37 in Game 2 was a play
that no human would have made, and it revealed strategic principles that
Go professionals had missed for centuries. AI didn't play the game better;
it showed humans the game was larger than they thought.

DeepMind's Atari work (2013-2015) was literally using games as AI training
grounds. The DQN paper used Breakout, Space Invaders, and Pong as
benchmarks — three of our actual prototype lineages. AI learned to play
our archaeology subjects from raw pixels, discovering strategies (like the
Breakout tunnel-behind-the-wall exploit) that human players knew but had
never been formally documented.

OpenAI Five (Dota 2, 2018-2019) and AlphaStar (StarCraft II, 2019)
showed AI could handle real-time strategy, partial information, and
long-horizon planning — exactly the capabilities the game industry had
been building ad-hoc AI for since F.E.A.R.

And then Copilot (2021). AI writing code. The same shift that took games
from "human designs and codes" to "human describes and AI generates."
Our lab IS this shift applied to game creation.

**Lab implication:** Every prototype we build is an artifact of Era 6/7
AI capabilities. We should timestamp this. Future archaeologists of THIS
work will want to know what the AI could and couldn't do when these
prototypes were built.

### AI Era 7: The Generative-Agentic Frontier (2023-Present)

**Parallel game era:** Now. The lab itself.

| AI Milestone | Year | Capability Unlocked |
|-------------|------|-------------------|
| GPT-4 | 2023 | Multimodal reasoning |
| Claude, Gemini, Llama (competition) | 2023-24 | Model diversity, open weights |
| AI agents (tool use, code execution) | 2024-25 | Autonomous multi-step workflows |
| AI co-creation in professional workflows | 2025-26 | Human-AI dyad as default creative unit |

**What AI can now do:** Reason about design. Generate complete working
prototypes from description. Understand game mechanics described in
English and translate them to code. Iterate on feedback. Remember
context across sessions. Propose mutations and cross-pollinations.

**What AI still cannot do:** Play a prototype and feel whether it's fun.
Recognize the moment of "I want to play this again." Make aesthetic
judgments about what's beautiful versus merely functional. Choose which
prototype to build next based on intuition. Decide what to share publicly
and what to protect.

**The game connection:** This is us. Right now. The lab is the first
artifact of Era 7 human-AI game co-creation. Not a tech demo, not a
research paper — a working creative partnership producing playable games.

The gap between what AI can do (generate code, describe mechanics, propose
variants) and what it cannot (judge beauty, feel satisfaction, make taste
decisions) is EXACTLY the gap this lab explores. Every session is an
experiment in where the boundary sits today and whether it moved since
last session.

---

## Part III: The Convergence Map — Where AI Meets Games

### The Fifteen Intersection Points

Mapping the two timelines reveals fifteen moments where AI and game
evolution directly intersect — either influencing each other, solving
the same problem independently, or one anticipating the other:

| # | Year | Game Event | AI Event | Relationship |
|---|------|-----------|----------|-------------|
| 1 | 1944 | — | von Neumann's *Theory of Games* | Game theory becomes AI foundation |
| 2 | 1950 | — | Shannon's chess paper | Games define what "intelligence" means |
| 3 | 1952 | — | Samuel's checkers self-play | Self-play invented in a game context |
| 4 | 1962 | Spacewar! on PDP-1 | AI research on same hardware | Same building, different questions |
| 5 | 1972 | Pong ships | MYCIN expert system | Specialization works (both prove it) |
| 6 | 1980 | Pac-Man ghost AI | Multi-agent systems nascent | Game solves multi-agent intuitively |
| 7 | 1980 | Rogue (procedural dungeons) | — | Games invent generation 34 years before GANs |
| 8 | 1985 | Tetris | — | Combinatorial optimization as entertainment |
| 9 | 1992 | SF2 combo discovery | TD-Gammon | Players and networks both do unsupervised search |
| 10 | 1997 | — | Deep Blue beats Kasparov | AI conquers the original game benchmark |
| 11 | 2005 | F.E.A.R. GOAP system | — | Game AI leads academic AI in real-time planning |
| 12 | 2013 | — | DQN plays Atari (Breakout, Invaders, Pong) | AI uses our prototype lineages as benchmarks |
| 13 | 2016 | — | AlphaGo Move 37 | AI shows humans their own game is deeper than they knew |
| 14 | 2021 | — | Copilot | AI writes game code |
| 15 | 2026 | This lab | Claude/GPT agents | Human-AI dyad creates games together |

### The Five Themes

These fifteen intersections cluster around five recurring themes:

**Theme 1: Games as Intelligence Benchmarks**
From chess (1950) through Atari (2013) through StarCraft (2019), games
have been the primary measuring stick for AI progress. Games ARE how we
test machine intelligence. This is not incidental — games are controlled
environments with clear objectives, measurable outcomes, and infinite
replayability. They are perfect laboratories, which is the same reason
WE use them as laboratories for mechanical discovery.

**Theme 2: Emergent Behavior as Discovery**
Both games and AI produce behaviors their creators didn't intend. Space
Invaders' speedup. SF2's combos. GPT's chain-of-thought reasoning.
AlphaGo's Move 37. The most important discoveries in both fields were
NOT designed — they EMERGED from the interaction of simple rules under
pressure. Our lab should be designed to encourage and capture emergence.

**Theme 3: Self-Play as the Master Teacher**
From Samuel's checkers (1952) through TD-Gammon (1992) through AlphaGo
(2016), the most powerful AI training method has been self-play in games.
AI learns fastest when playing against itself in a game. Games are not
just a metaphor for AI training — they are the literal, optimal training
environment. This theme has implications for our mutation phase: what if
we let AI play-test our prototypes against itself and surface the
interesting behaviors?

**Theme 4: The Generation Gap**
Games invented procedural generation (Rogue, 1980) 34 years before AI
invented generative models (GANs, 2014). But games generated STRUCTURE
(level layouts, dungeon maps) while AI generates CONTENT (images, text,
code). The convergence — AI generating game structures with aesthetic
intent — is happening now, in this lab. We are at the exact moment
where these two generation traditions merge.

**Theme 5: The Taste Problem**
The fundamental unsolved problem in both fields: **what makes something
good?** In games: what makes a mechanic feel fun? In AI: what makes
generated output feel right? Neither field has solved this. Game
designers rely on intuition refined through decades of play. AI
researchers rely on RLHF (human feedback). Both are approximations
of the same unsolved problem: formalizing taste.

Our lab's core bet is that a human-AI dyad is the best current approach
to the taste problem. The human provides the judgment. The AI provides
the search. Neither solves it alone.

---

## Part IV: AI as Participant in Each Game Category

This section asks: **if AI had been a game designer (not just a player)
in each of our thirteen prototype series, what would it have done
differently?** This is not counterfactual speculation for its own sake
— it directly informs what experiments we should run.

### ANC — Ancient Game Series

**AI as participant:** Rule-space explorer. Given the mechanics of Ur,
Senet, or Mancala, AI would enumerate every possible rule variant and
evaluate which combinations produce the most interesting play patterns.
Not by playing — by reasoning about the state space.

**What it would have found:** Ur's rolling/advancing mechanic has a design
space of ~500 meaningful variants (board sizes 8-30, die configurations,
safe square placements, capture rules). Of those, maybe 10-20 produce
games with both deep strategy and short play times. AI can map this space
systematically.

**Experiment unlocked:** `anc-XXX-ur-variants.html` — A prototype that
generates and lets you play random Ur variants, rated by AI analysis of
their decision-tree depth.

### DEF — Deflection / Paddle Series

**AI as participant:** Physics optimizer. The ball-and-paddle interaction
is a continuous physics problem. AI would have exhaustively mapped the
relationship between paddle hit-position, resulting angle, ball speed,
and game difficulty curve.

**What it would have discovered:** Breakout's optimal brick layouts for
fun (not difficulty). The relationship between brick density and "exciting
moments" density. The speed/angle combinations that produce the most
satisfying deflections.

**Experiments unlocked:**
- `def-XXX-ai-layouts.html` — AI-generated Breakout levels optimized
  for "interesting bounces" rather than hand-placed
- `def-XXX-adaptive.html` — Pong where the AI opponent adapts to your
  patterns (plays like a 1990s TD-learning agent, not a Y-tracker)

### FIX — Fixed-Position Shooters

**AI as participant:** Emergence engineer. Space Invaders' defining
feature (speedup as aliens die) was an accident. AI would have found it
intentionally by simulating thousands of parameter variations and
identifying which ones create escalating tension.

**What it would have discovered:** The relationship between formation
density, descent speed, and player stress. Alternative threat escalation
patterns — what if instead of speeding up, the remaining aliens changed
behavior (became erratic, started flanking, split into sub-formations)?

**Experiments unlocked:**
- `fix-XXX-ai-escalation.html` — Invaders where AI controls the tension
  curve directly, adjusting speed/behavior to maintain optimal difficulty
- `fix-XXX-emergent-formation.html` — Enemies with evolved (not designed)
  formation behaviors

### SCR — Scrolling / Shmup Series

**AI as participant:** Cognitive load manager. Defender's problem is
information overload — the world is larger than the screen, enemies come
from both sides, civilians need rescue. AI would have optimized the
information display: what to show on the minimap, when to alert, how to
direct attention.

**What it would have discovered:** The optimal minimap-to-main-view
information ratio. When auditory alerts outperform visual ones. How to
maintain "flow state" by spacing threats at intervals matched to human
reaction/cooldown cycles.

**Experiments unlocked:**
- `scr-XXX-ai-director.html` — Scrolling shooter with a Left 4 Dead-
  style AI Director that adjusts enemy spawning to maintain flow
- `scr-XXX-cognitive-load.html` — Prototype testing how much information
  a player can process at different scroll speeds

### PLT — Platformer Series

**AI as participant:** Level architect with emotional intent. Mario's
levels are hand-crafted experiences with pacing, surprise, and teaching
moments. AI could generate levels with EMOTIONAL ARCS — tension, release,
surprise, mastery — mapped to specific player positions.

**What it would have discovered:** The optimal ratio of challenge-to-
rest in platformer level design. How "safe platforms" (places where the
player can pause) affect perceived difficulty vs actual difficulty.
Mario Maker community wisdom, formalized.

**Experiments unlocked:**
- `plt-XXX-ai-level.html` — Procedurally generated platformer levels
  with specified emotional arcs (tense → relief → surprise → flow)
- `plt-XXX-difficulty-lens.html` — Same level data, displayed with a
  heat map showing where players die (simulated by AI analysis)

### MAZ — Maze Chase Series

**AI as participant:** Behavioral ecology simulator. Pac-Man's four ghost
personalities were hand-tuned. AI would have explored the full space of
possible ghost behaviors — herding, swarming, retreating, ambushing,
splitting — and found which combinations of 4 from the full behavior
space create the richest player experience.

**What it would have discovered:** The optimal number of distinct enemy
behaviors for a maze game (it might not be 4). Whether asymmetric
information (ghosts that know where YOU are but you can't see THEM until
close) creates better or worse tension.

**Experiments unlocked:**
- `maz-XXX-evolved-ghosts.html` — Pac-Man variant where ghost behaviors
  are parameters that evolve (genetic algorithm style) based on how long
  players survive — ghosts that kill you TOO fast or TOO slow get culled
- `maz-XXX-fog-of-war.html` — Pac-Man where you can only see a limited
  radius, exploring partial observability

### PHY — Physics / Inertia Series

**AI as participant:** Space mapper. Asteroids is a Newtonian physics
space. AI would have mapped the complete "safety landscape" — given
asteroid positions and velocities, what's the survival probability from
every possible ship position/vector? This is a solved RL problem
(it's literally DQN's first benchmark after Breakout).

**What it would have discovered:** The emergent geometry of Asteroids
gameplay — the "corridors" of safety that open and close as asteroids
drift. The fact that the best survival strategy isn't shooting everything
(which spawns more threats) but navigating the debris field.

**Experiments unlocked:**
- `phy-XXX-safety-map.html` — Asteroids with a real-time overlay showing
  the AI's evaluation of safe/dangerous regions
- `phy-XXX-pacifist.html` — Asteroids variant where you CAN'T shoot,
  forcing pure navigation of the physics space

### PUZ — Puzzle / Falling Block Series

**AI as participant:** Anxiety optimizer. Tetris creates a specific form
of anxiety — spatial, temporal, escalating. AI would have mapped the
relationship between piece sequence, speed, and player stress to find the
optimal anxiety curve.

**What it would have discovered:** The "unfair" sequences (long droughts
of I-pieces) and whether they improve or harm engagement. Whether truly
random piece generation is more or less fun than pseudo-random (bag
system). The mathematically optimal board states and whether human
players actually pursue them.

**Experiments unlocked:**
- `puz-XXX-piece-lens.html` — Tetris that shows the AI's evaluation of
  your board state in real time (how "healthy" is your stack?)
- `puz-XXX-adaptive-speed.html` — Speed adjusts based on AI estimate
  of player anxiety (faster when you're comfortable, slower when you're
  drowning)

### TRP — Trap / Terrain Series

**AI as participant:** Risk cartographer. Qix is about territory: the
more you claim, the more exposed your in-progress line becomes. AI would
have mapped the risk/reward surface — where on the playfield is claiming
territory most dangerous relative to the reward?

**What it would have discovered:** The optimal claiming strategy(large
areas vs many small claims). The relationship between Qix movement
patterns and claimable safe zones. Whether the 75% completion threshold
is mathematically optimal or arbitrary.

**Experiments unlocked:**
- `trp-XXX-risk-heatmap.html` — Qix with an overlay showing risk
  (proximity to Qix) vs reward (area available) for every possible
  claim starting point
- `trp-XXX-adaptive-qix.html` — Qix where the enemy learns your
  claiming patterns and counters them

### FGT — Fighting / Combat Series

**AI as participant:** Combo space enumerator. SF2's combo system was
discovered by players. AI would have found every combo, including
degenerate ones, within hours of the code compiling.

**What it would have discovered:** The full interaction graph of every
move against every other move. Which combos are satisfying to execute
(input complexity × visual reward) and which are degenerate (infinite
loops, touch-of-death). This would have caught balance issues before
release.

**Experiments unlocked:**
- `fgt-XXX-combo-viz.html` — Fighting game with a graph visualization
  showing discovered combo paths
- `fgt-XXX-balanced.html` — AI-balanced fighting game where each
  character has equal win probability against every other

### NEW — Novel Mechanics Series

**AI as participant:** Possibility-space cartographer. Given new mechanic
verbs (ECHO, TETHER, SPLIT, THREAD, PULSE, ERODE), AI can enumerate
combinations and permutations that a human would take years to explore
manually.

**What it could find:** Which pairs of novel verbs create emergent depth.
Which verb + genre combinations haven't been tried. The "gaps" in the
combinatorial space where something interesting is likely hiding.

**Experiments unlocked:**
- `new-XXX-combination-matrix.html` — An interactive matrix showing
  every verb × genre combination and which have been explored
- Series-specific novel experiments combining ADR-002 concepts with
  historical genre foundations

### HYB — Cross-Lineage Hybrids

**AI as participant:** Cross-pollination engine. AI can systematically
combine mechanics from different series and predict which combinations
will create interesting tensions.

**What it would find:** The non-obvious combinations — DEF (deflection)
+ TRP (territory claiming): a game where your "paddle" is a moving wall
that you build, and the ball claims territory where it bounces. Or FIX
(fixed position) + PUZ (falling blocks): you're at the bottom shooting
at falling Tetris pieces, trying to break them before they stack.

**Experiments unlocked:** This is the lab's growth frontier. See ADR-003
Part VI Phase 3 for the methodology.

### WLD — Wild Experiments

**AI as participant:** The other half of the dyad. Wild experiments are
where the human-AI partnership operates without genre constraints. The
human provides intuition, aesthetic vision, and the feeling of "try
THAT." The AI provides speed, variant generation, and exhaustive
exploration.

**What it could find:** The unnamed thing. The interaction that doesn't
belong in any series because it hasn't existed before. This is the gem
the entire lab is built to discover.

---

## Part V: The Dual-Lens System — Implementation

### What Changes in the Lab

Adding the AI archaeology layer means every artifact in the lab now exists
at an intersection of two coordinates:

```
Game Evolution Axis (horizontal)
Era 0  →  Era 1  →  Era 2  →  Era 3  →  Era 4  →  Era 5  →  Era 6  →  Era 7
Pre-E     Osc/Main  Arcade    8-Bit     16-Bit    3D        Network   Browser+AI

AI Evolution Axis (vertical)
Era 0: Theoretical → Era 1: Search → Era 2: Expert Systems → Era 3: Knowledge
→ Era 4: Neural Revival → Era 5: Statistical → Era 6: Deep Learning → Era 7: Agents
```

A prototype like `def-001-pong` sits at:
- **Game axis:** Era 2 (Arcade Dawn, 1972)
- **AI axis:** Era 2 (Expert Systems — AI could only do rule-matching)
- **Intersection insight:** "Pong's opponent AI is literally an if-
  statement. This IS the contemporary AI era. The game's intelligence
  is indistinguishable from the AI field's intelligence at this moment."

A prototype like `maz-001-pacman` sits at:
- **Game axis:** Era 3 (8-Bit Explosion, 1980)
- **AI axis:** Era 3 (Knowledge systems, pre-backpropagation)
- **Intersection insight:** "Pac-Man's ghost personalities are hand-
  crafted behavioral policies that predate the formal theory of multi-
  agent systems by 20 years. The game industry built intuitive MARL
  before AI researchers had the math."

### The Metadata Extension

Every prototype's metadata block gains an `AI-ERA` and `AI-INSIGHT` field:

```html
<!--
PROTOTYPE: pong
SERIES: def
NUMBER: 001
DATE: 2026-03-22
MECHANIC: deflect — ball bounces between two paddles
ANCESTRY: Tennis for Two (1958) → Odyssey (1972)
CONTROLS: W/S — left paddle, ↑/↓ — right paddle
STATUS: playable
RATING: ★★★★☆
AI-ERA: 2 (Expert Systems — rule-based, no learning)
AI-INSIGHT: Opponent is a Y-tracker if-statement. Indistinguishable from
  contemporary AI capability. The ball's physics creates more
  "intelligence" than the opponent's code.
NOTES: The original deflection loop.
-->
```

New metadata fields:
- `AI-ERA` — Which AI era this game's technology corresponds to
  (number + name)
- `AI-INSIGHT` — One to three sentences connecting this prototype's
  mechanics/opponent to AI concepts. What does this game teach us about
  intelligence? What AI concept does it accidentally implement?

### The Info Panel AI Tab

Every prototype's info panel gains a new section: **AI Archaeology**.
This sits between "History & Lineage" and "Classification" in the
existing panel structure.

Content for each AI Archaeology section:

```
## AI Archaeology

**AI Era:** [Number] — [Era Name] ([Years])

**Contemporary AI:** [What AI could do when this game was made]

**Hidden Intelligence:** [What AI concept this game accidentally
implements, with the formal AI term and approximate year it was
formally defined]

**The Convergence:** [How AI and game evolution intersect at this
specific prototype — what do they illuminate about each other?]

**If AI Had Designed This:** [One-sentence counterfactual — what
would an AI co-designer have done differently?]
```

### The Catalogue AI Columns

The CATALOGUE.md gains two new columns in the master table:

```markdown
| # | Name | Mechanic | Rating | AI Era | AI Insight | Status | Notes |
```

And a new summary section:

```markdown
## AI Archaeology Summary

**Prototypes by AI Era:**
Era 2: DEF(2)
Era 3: FIX(1), MAZ(1), PHY(1), SCR(1), PLT(1), PUZ(1), TRP(1)

**AI Convergence Points Found:** [count]
**Novel AI-Game Connections Documented:** [count]
```

---

## Part VI: The Info Panel AI Layer

### Implementation Specification

Each of the 9 current prototypes gets an AI Archaeology section added to
its info panel. The content is prototype-specific, grounded in the
research from Part II and Part IV of this ADR.

#### def-001-pong

```
AI Era: 2 — Expert Systems (1972-1977)
Contemporary AI: Rule-based expert systems (MYCIN), pattern-matching
  (ELIZA). AI could encode expert knowledge as if-then rules.
Hidden Intelligence: The AI opponent is a Y-position tracker — literally
  an if-statement. This is indistinguishable from contemporary AI
  capability. But the BALL creates more emergent intelligence than the
  opponent: its angle physics generates patterns the human brain finds
  satisfying to predict. The environment is smarter than the agent.
The Convergence: Both Pong and 1972 AI prove the same thing: a system
  doing one thing well beats a system doing everything poorly.
If AI Had Designed This: It would have added adaptive difficulty —
  tracking your preferred angles and covering them, forcing you to evolve.
```

#### def-002-breakout

```
AI Era: 2 — Expert Systems (1972-1977)
Contemporary AI: Same era as Pong. Rule-based systems, no learning.
Hidden Intelligence: Breakout removes the AI opponent entirely — physics
  IS the antagonist. The destructible brick field is the first game
  where the player reshapes the environment, foreshadowing procedural
  destruction by 30+ years.
The Convergence: Breakout proves you don't need an intelligent opponent
  to create depth. DeepMind's DQN (2013) would later discover the
  "tunnel behind the wall" strategy — a move that human players knew
  intuitively but had never been formally documented until AI found it.
If AI Had Designed This: Procedural brick layouts optimized for
  "interesting bounces" — 20 years before procedural generation existed.
```

#### fix-001-invaders

```
AI Era: 3 — Knowledge Explosion (1978-1983)
Contemporary AI: Expert systems commercializing. Hopfield networks.
  Backpropagation being rediscovered. AI could search and classify
  but not learn in real-time.
Hidden Intelligence: The speedup-as-aliens-die is emergent curriculum
  learning — the game automatically increases difficulty as the player
  succeeds. AI researchers wouldn't formalize curriculum learning until
  ~2015. Taito's bug was 37 years ahead of AI research.
The Convergence: Space Invaders was a DQN benchmark (2013). AI
  learned to play this exact game from raw pixels, discovering optimal
  strategies through the same process the game's designers used
  accidentally: trial, error, and selection.
If AI Had Designed This: Intentional difficulty curves instead of
  accidental ones. AI would have found the speedup deliberately by
  simulating thousands of parameter variations.
```

#### phy-001-asteroids

```
AI Era: 3 — Knowledge Explosion (1978-1983)
Contemporary AI: Same era. AI could handle discrete games (checkers,
  chess positions) but not continuous physics spaces.
Hidden Intelligence: Asteroids is a continuous state-space navigation
  problem — exactly the kind of problem reinforcement learning was
  built to solve, but wouldn't be applied to until DQN (2013).
  The game's Newtonian physics makes it a perfect RL environment:
  continuous state (position, velocity, angle), discrete actions
  (thrust, rotate, shoot), sparse rewards (survival, score).
The Convergence: The "shoot creates more threats" dynamic
  (asteroids splitting) mirrors the exploration-exploitation tradeoff
  in RL. Shooting is exploitation (points now). Not shooting is
  exploration (safer navigation later).
If AI Had Designed This: A real-time safety map showing survival
  probability from each position/velocity. The corridors of safety
  that open and close as asteroids drift.
```

#### maz-001-pacman

```
AI Era: 3 — Knowledge Explosion (1978-1983)
Contemporary AI: Rule-based systems at their peak. Multi-agent AI
  was theoretical. Behavior trees didn't exist yet.
Hidden Intelligence: Four ghost personalities (Blinky chases, Pinky
  ambushes, Inky flanks, Clyde wanders) are hand-crafted multi-agent
  behavioral policies. This is cooperative multi-agent reinforcement
  learning built by intuition 20 years before the formal theory.
  Each ghost has a different reward function — the game designer
  was doing reward engineering before the term existed.
The Convergence: Pac-Man ghost AI is the most-referenced example in
  game AI textbooks and a standard benchmark in multi-agent systems
  research. The game-design solution preceded and informed the
  academic formalization.
If AI Had Designed This: Explored hundreds of ghost behavior
  combinations through evolutionary search. Found the optimal
  NUMBER of distinct personalities (it might not be 4).
```

#### scr-001-defender

```
AI Era: 3 — Knowledge Explosion (1978-1983)
Contemporary AI: Limited to discrete, fully observable environments.
  No concept of partial observability in practical systems.
Hidden Intelligence: Defender invented the world-larger-than-screen
  problem — partial observability. The minimap is a dimensionality
  reduction technique: compressing the full world state into a small,
  interpretable summary. This is exactly what autoencoders (1986)
  and attention mechanisms (2017) do in AI.
The Convergence: POMDPs (Partially Observable Markov Decision Processes)
  were formalized in 1965 but not practically solved until the 1990s.
  Defender built a playable POMDP in 1981 and solved the display
  problem with pure design intuition.
If AI Had Designed This: Optimized the minimap information density.
  Tested which alert modalities (visual, auditory, haptic) best
  maintain player situation awareness at high speed.
```

#### plt-001-runner

```
AI Era: 3 — Knowledge Explosion (1978-1983)
Contemporary AI: Planning systems existed but couldn't handle
  real-time continuous control. No model-based RL.
Hidden Intelligence: Variable-height jump (hold longer = jump higher)
  is continuous action control — the player is choosing from an
  infinite action space with every jump. This is inherently harder
  for AI than discrete actions, which is why platformers remained
  challenging for AI long after Atari shooters were solved.
The Convergence: Level design in platformers is reward shaping —
  coins guide the player along intended paths, gaps punish deviation.
  Mario's levels are hand-crafted reward functions that teach the
  player through environmental design, exactly the principle behind
  curriculum learning and reward shaping in RL.
If AI Had Designed This: Procedural level generation with emotional
  arcs — tension/release patterns mapped to specific player positions.
  Mario Maker community wisdom, formalized algorithmically.
```

#### puz-001-tetris

```
AI Era: 3-4 — Late Knowledge / Early Neural Revival (1985)
Contemporary AI: Backpropagation just being published. Neural
  networks moving from theoretical to trainable. Expert systems
  at peak hype.
Hidden Intelligence: Tetris is a real-time combinatorial optimization
  problem — NP-hard in its general form. No AI in 1985 could play it
  optimally. The human brain uses heuristic spatial reasoning that
  remains difficult for AI to replicate in real-time. Tetris AI is
  STILL an active research area.
The Convergence: Tetris appears to have no game ancestry — it emerged
  from mathematics, not from iterating on prior games. Similarly,
  the hardest AI problems are often the ones that don't reduce to
  prior solved problems. Tetris is the Go of video games: simple
  rules, intractable depth.
If AI Had Designed This: Optimized the piece generation algorithm for
  maximum "fair anxiety" — preventing drought sequences while
  maintaining unpredictability. (The modern bag system approximates
  this, discovered by human designers through decades of iteration.)
```

#### trp-001-qix

```
AI Era: 3 — Knowledge Explosion (1978-1983)
Contemporary AI: Geometric reasoning existed in limited forms
  (computational geometry was emerging). No real-time spatial AI.
Hidden Intelligence: Qix is a real-time territorial control problem
  where your own actions create your vulnerability (the unfinished
  line IS the threat zone). This mirrors the exploration-exploitation
  tradeoff in RL: claiming territory (exploitation) requires exposing
  yourself (exploration cost). The game is a physical manifestation
  of the multi-armed bandit problem with spatial, temporal, and
  risk dimensions.
The Convergence: Territory-claiming under threat has direct parallels
  to adversarial search in game theory — you're playing against a
  Qix that moves through YOUR claimed territory's boundaries. The
  game is minimax with continuous state space.
If AI Had Designed This: Risk/reward heatmaps showing optimal claiming
  strategies given current Qix position and movement patterns. The
  75% threshold would have been empirically optimized rather than
  arbitrarily chosen.
```

---

## Part VII: The AI Archaeology Catalogue Extension

### Catalogue Generator Changes

The `tools/catalogue-generator.py` should be updated to:

1. **Parse AI-ERA and AI-INSIGHT** from metadata blocks
2. **Add AI columns** to the prototype table
3. **Generate AI Archaeology Summary** section showing:
   - Distribution of prototypes across AI eras
   - Count of documented convergence points
   - List of AI concepts discovered in game form before formal AI research

### New Catalogue Section Template

```markdown
## AI Archaeology Summary

### Prototypes by AI Era

| AI Era | Count | Prototypes |
|--------|-------|-----------|
| Era 2: Expert Systems (1972-1977) | [n] | DEF-001, DEF-002 |
| Era 3: Knowledge Explosion (1978-1983) | [n] | FIX-001, PHY-001, MAZ-001, ... |
| Era 4: Neural Revival (1985-1992) | [n] | PUZ-001 |

### Game-First AI Discoveries

Concepts that game designers implemented intuitively before AI
researchers formalized them:

| Concept | Game | Year | AI Formalization | Gap |
|---------|------|------|-----------------|-----|
| Emergent curriculum learning | Space Invaders | 1978 | ~2015 | 37 years |
| Multi-agent behavioral policies | Pac-Man | 1980 | ~2000 | 20 years |
| Procedural content generation | Rogue | 1980 | GANs 2014 | 34 years |
| Partial observability display | Defender | 1981 | POMDP practical ~1995 | 14 years |
| Continuous action spaces | Donkey Kong / Mario | 1981 | Continuous RL ~2015 | 34 years |
| Combinatorial optimization as play | Tetris | 1985 | Active research | 40+ years |
| Adversarial territory control | Qix | 1981 | Adversarial games ~2014 | 33 years |

### AI Eras Not Yet Represented

Series with no prototypes in these AI eras (build targets):

| AI Era | What's Missing | Suggested Prototypes |
|--------|---------------|---------------------|
| Era 0: Theoretical | Ancient games as AI benchmarks | ANC-001 through ANC-005 |
| Era 4: Neural Revival | Tournament fighters, exploration platformers | FGT-001, PLT-002+ |
| Era 5: Statistical | 3D rupture games (out of scope) | — |
| Era 6: Deep Learning | AI-aware game design | NEW-series, HYB-series |
| Era 7: Agentic | This lab's own output | Every new prototype |
```

---

## Part VIII: Future Prototypes — AI-Native Experiments

The AI archaeology layer doesn't just annotate existing prototypes — it
generates ideas for **new** prototypes that could only exist because of
the dual-lens perspective.

### Category 1: "What If AI Had Designed This?" Prototypes

Take an existing reconstruction and build the version AI WOULD have
built. Not better — different. Reflecting AI's strengths (exhaustive
search, pattern detection, variant generation) rather than human
strengths (intuition, aesthetics, physical empathy).

| Prototype | Idea | What It Tests |
|-----------|------|--------------|
| `def-003-ai-breakout` | AI-generated brick layouts optimized for "interesting bounces" | Can AI design better levels than humans for physics games? |
| `fix-002-ai-escalation` | Invaders with AI-controlled tension curve | Can AI replace the accidental speedup with intentional difficulty management? |
| `maz-002-evolved-ghosts` | Pac-Man where ghost behaviors are evolved, not designed | Does algorithmic ghost design produce richer play than hand-tuned? |
| `phy-002-safety-map` | Asteroids with real-time AI safety evaluation overlay | Can an AI lens make a game more legible without making it easier? |
| `puz-002-anxiety-optimizer` | Tetris with AI-adjusted speed curve | Can AI maintain optimal anxiety better than a linear speed ramp? |
| `trp-002-risk-heatmap` | Qix with risk/reward heatmap overlay | Does showing the AI's evaluation change how humans play? |

### Category 2: AI-Era Reconstruction Prototypes

Build games that feel like they come FROM a specific AI era — games
whose design logic mirrors the thinking of that era's AI paradigm.

| Prototype | AI Era | Design Logic | What It Feels Like |
|-----------|--------|-------------|-------------------|
| `wld-001-search-game` | Era 1 (Search) | Game IS a search tree made visible. Player navigates a branching decision space | Looking at AI's mind from the inside |
| `wld-002-rule-game` | Era 2 (Expert Systems) | Game operates on if-then rules that the player must discover and exploit | Playing against a knowledge base |
| `wld-003-neural-game` | Era 4 (Neural Revival) | Game's behavior changes through a visible learning process. It gets better at countering you in real time | Playing against something that learns |
| `wld-004-generative-game` | Era 6 (Deep Learning) | Game generates its own content (levels, enemies, rules) as you play | Playing inside a generative system |
| `wld-005-agent-game` | Era 7 (Agentic) | Game is a cooperative agent — it has goals, negotiates with you | Playing WITH an intelligence |

### Category 3: Convergence-Point Prototypes

Build games that sit exactly at the intersection of a game era and an AI
era — prototypes that make the parallel evolution visible and playable.

| Prototype | Intersection | Concept |
|-----------|-------------|---------|
| `hyb-001-self-play` | Samuel's checkers (1952) meets Pong (1972) | A game that trains itself against itself while you watch, then you play the trained version |
| `hyb-002-move-37` | AlphaGo (2016) meets Go (2500 BCE) | Visualize what AI "sees" in a simple grid game — reveal the alien intelligence |
| `hyb-003-dqn-breakout` | DQN (2013) meets Breakout (1976) | Watch an AI learn Breakout in real-time, then compete against it |
| `hyb-004-generator` | GANs (2014) meets Rogue (1980) | Procedural dungeon generated by AI taste, not random constraints |

---

## Decision Summary

### Decisions Made

1. **Adopt the dual-lens model** — Every prototype exists at an
   intersection of game evolution (horizontal) and AI evolution (vertical)
2. **Seven parallel AI eras** structured to mirror the seven game
   technology eras from ADR-003 Part II
3. **Fifteen convergence points** identified where game and AI evolution
   directly intersect, influence, or mirror each other
4. **Five recurring themes** (Benchmarks, Emergence, Self-Play, Generation
   Gap, Taste Problem) organize the convergence map
5. **AI participation analysis** for all 13 prototype series — what AI
   would have contributed as designer, not player
6. **Metadata extension** — `AI-ERA` and `AI-INSIGHT` fields added to
   prototype metadata blocks
7. **Info panel AI Archaeology section** added to every prototype's
   educational overlay
8. **Catalogue AI extension** — new columns and AI Archaeology Summary
   section
9. **Three categories of AI-native prototypes** identified for future
   development (What-If, Era-Reconstruction, Convergence-Point)
10. **"Game-First AI Discoveries" table** documents concepts that game
    designers implemented intuitively before AI researchers formalized
    them — this is original scholarship

### What This ADR Does NOT Decide

- Whether AI-native prototypes get their own series code (could be
  integrated into existing series or warrant a new `AI` series)
- The visual design of the AI Archaeology info panel section (follows
  existing CSS patterns)
- Priority order for implementing AI-native prototypes (that's a
  session-by-session decision)
- Whether AI archaeology content gets `public` visibility (same rules
  as all other content — default `private`, conscious promotion)
- How to handle prototypes that span multiple AI eras (use the primary
  era, note others in AI-INSIGHT)

### Implementation Order

1. **Phase A** — Add `AI-ERA` and `AI-INSIGHT` metadata to all 9 existing
   prototypes
2. **Phase B** — Add AI Archaeology section to all 9 info panels (content
   specified in Part VI)
3. **Phase C** — Update `catalogue-generator.py` to parse and display AI
   fields
4. **Phase D** — Regenerate CATALOGUE.md with AI columns and summary
5. **Phase E** — Begin building Category 1 "What If AI Had Designed This?"
   prototypes (one per series, starting with the strongest series)
6. **Phase F** — Build Category 2 AI-Era Reconstruction prototypes
   (starting with `wld-001-search-game`)
7. **Phase G** — Build Category 3 Convergence-Point prototypes (starting
   with `hyb-003-dqn-breakout` as the most immediately compelling)

### The Key Point

This lab was always about two things searching for one thing. A human
and an AI, looking for a game that doesn't exist yet. The AI Archaeology
Layer makes that partnership the subject of study, not just the method.
By placing AI's evolution alongside game evolution, we see both more
clearly — and we see the spaces between them where the undiscovered
things live.

The fifteen convergence points, the Game-First AI Discoveries table, the
dual-lens coordinate system — these are not just annotations. They are a
MAP of unexplored territory. Every gap in that map is a prototype waiting
to be built. Every mismatch between what AI could do and what games
needed is a design opportunity.

The game industry spent 50 years solving intelligence problems without
calling them that. The AI industry spent 70 years using games as
benchmarks without building new ones. This lab sits at the exact point
where those two histories finally merge — and uses that merger to find
what neither found alone.

---

**Last Updated:** 2026-03-22
