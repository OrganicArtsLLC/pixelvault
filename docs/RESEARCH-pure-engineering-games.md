# Research: Pure Engineering Games — 30 Games Made by Machines, for Machines

**Date:** 2026-03-24
**Purpose:** 30 games designed purely from engineering principles. No genre
conventions. No mashups. No human nostalgia. These are games that emerge when
you ask: "What mechanics are mathematically interesting, physically elegant,
or computationally beautiful?" They should feel alien, precise, and deeply
satisfying to master — like learning a new physics.

---

## Design Principles

These games follow ENGINEERING constraints, not design conventions:

1. **Mathematical elegance** — the rules should be expressible in few equations
2. **Emergent complexity** — simple code, complex behavior
3. **Computational beauty** — the visuals emerge from the math, not from art direction
4. **Novel input-output mapping** — the relationship between input and effect should feel alien
5. **Information density** — every pixel carries meaning
6. **Deterministic chaos** — reproducible systems that feel unpredictable
7. **State-space exploration** — the game IS finding the system's behavior

No shooting. No jumping. No collecting. No enemies in the traditional sense.
These are interactions with SYSTEMS, not narratives.

---

## The 30 Pure Engineering Games

### Topology & Space (6)

**1. new-112-manifold** — Manifold
Play on a surface that wraps in non-Euclidean ways. Move on a torus — going
off the right edge doesn't bring you to the left edge of the SAME row. It
maps to a different row based on a configurable twist. Navigate to a goal
while your intuitions about space fail.

**2. new-113-tesselate** — Tesselate
Place geometric shapes to tile a plane with zero gaps. But the shapes
morph as you place them — each placement slightly changes the shapes
available next. The tiling must be perfect. A living jigsaw that evolves.

**3. new-114-fieldlines** — Field Lines
You are a charged particle in an electromagnetic field. Other charges are
fixed. Your movement follows field lines — you can't move freely, only
along the gradient. Reach the target by understanding the field topology.
Place new charges to reshape the field.

**4. new-115-topology** — Topology
Transform one shape into another through continuous deformation only.
Stretch, compress, bend — but never tear or glue. A circle can become
a square but not a figure-eight. Solve which transformations are
topologically possible.

**5. new-116-waveinterference** — Wave Interference
Two wave sources emit circular waves. Where waves constructively interfere,
platforms exist. Where they destructively interfere, void. Move a particle
along the interference pattern. Adjust wave frequencies to create new
paths. Standing waves as architecture.

**6. new-117-voronoi** — Voronoi
Place points on a plane. Voronoi cells form automatically — each cell
contains all space closest to its point. A particle bounces between cells.
Manipulate cell boundaries by moving points to guide the particle to the
exit. Computational geometry as gameplay.

### Dynamics & Physics (6)

**7. new-118-attractor** — Strange Attractor
A particle follows a Lorenz attractor. You can nudge its initial conditions
with tiny adjustments. Small changes create wildly different trajectories.
Guide the particle through gates by finding the right initial condition.
Chaos theory as precision sport.

**8. new-119-resonance** — Resonance
Objects have natural frequencies. You emit waves. When your wave frequency
matches an object's natural frequency, it shatters. Find the resonant
frequency of each obstacle by experimenting. Sweep through frequencies
to feel for the resonance. Tuning as destruction.

**9. new-120-tensegrity** — Tensegrity
Build structures from rigid struts and elastic cables. The structure
must support itself through tension, not compression. Place struts and
cables to build a bridge that stands. If the tension network fails,
it collapses. Structural engineering as puzzle.

**10. new-121-fluidrouter** — Fluid Router
Fluid flows from a source. Place splitters, mergers, and valves to route
it to multiple outlets in precise ratios. 60% to outlet A, 40% to B.
The fluid follows Navier-Stokes-lite physics. Plumbing as mathematics.

**11. new-122-harmonograph** — Harmonograph
Two pendulums swing at different frequencies. Their combined motion draws
a pattern (Lissajous figures). Adjust frequency ratios, phase, and damping
to draw a target pattern. The math of coupled oscillators visualized.

**12. new-123-springmesh** — Spring Mesh
A mesh of mass-spring nodes. Click to disturb. The mesh propagates waves,
dampens, resonates. Place rigid anchors and mass nodes to create a mesh
that oscillates in a target pattern. Wave propagation engineering.

### Information & Logic (6)

**13. new-124-cellularengine** — Cellular Engine
Design cellular automaton rules (birth/survival conditions like Conway's
Life). Your rules run on a grid. The challenge: design rules that produce
a specific emergent behavior (glider, oscillator, growing pattern). You're
programming emergence.

**14. new-125-sortmachine** — Sort Machine
Numbers flow down pipes. Place comparators (swap if out of order) at
pipe junctions. Build a sorting network that correctly sorts any input.
The minimum number of comparators IS the optimization challenge.
Algorithms as physical contraption.

**15. new-126-boolcircuit** — Boolean Circuit
Build logic circuits from AND, OR, NOT, XOR gates. Input signals enter
from the left. Your circuit must produce the correct output pattern on
the right. 8 puzzles from simple (AND two inputs) to complex (4-bit
adder). Digital logic as spatial puzzle.

**16. new-127-entropy** — Entropy
A grid of ordered colored tiles. Each action you take INCREASES entropy
(disorder). But you need to CREATE a specific pattern. The paradox: every
move disorders the rest while you try to order one part. Fight the
second law of thermodynamics.

**17. new-128-compression** — Compression
A sequence of symbols streams past. Place pattern-matchers to compress
the stream. When you identify a repeating pattern and create a shorthand,
the stream flows faster (you've compressed it). Miss patterns and the
buffer overflows. Data compression as reflex game.

**18. new-129-graphwalk** — Graph Walk
Navigate a visible graph (nodes and edges). But each edge you traverse
REMOVES it. Find an Eulerian path (visit every edge exactly once) or
the graph becomes disconnected and you're trapped. Graph theory as
survival.

### Control & Feedback (6)

**19. new-130-pidcontroller** — PID Controller
A ball on a beam. The beam tilts. You adjust three parameters: P
(proportional — react to error), I (integral — react to accumulated error),
D (derivative — react to rate of change). Tune the PID controller to
balance the ball. Control theory as game.

**20. new-131-feedback** — Feedback Loop
A system output feeds back into its input. Adjust the gain. Too low = no
response. Too high = oscillation and instability. Find the sweet spot
where the system tracks a moving target. Nyquist stability as gameplay.

**21. new-132-neuralplay** — Neural Play
A simple neural network (3 inputs, hidden layer, 1 output). You adjust
weights by clicking connections. The network controls a simple agent.
Train it by tweaking weights until the agent behaves correctly. Manual
gradient descent.

**22. new-133-statemachine** — State Machine
Design a finite state machine to control a character. Place states and
transitions. Define conditions (see wall → turn, see item → collect).
Run the machine and watch your automaton navigate a world. Programming
without code.

**23. new-134-phasor** — Phasor
Control a point on the complex plane. It rotates and scales based on
multiplication by complex numbers. Navigate through gates by choosing
the right complex multiplier. Rotation + scaling as movement. Complex
arithmetic as spatial navigation.

**24. new-135-gradient** — Gradient Descent
You're on a 2D surface (heightmap). You can only see your immediate
gradient (which direction is downhill). Navigate to the global minimum,
not a local one. The surface has multiple valleys. Escape local minima
through momentum. Optimization as exploration.

### Generative & Emergent (6)

**25. new-136-lsystem** — L-System
Define rewriting rules (A → AB, B → A). The system iterates, producing
longer strings. Each character maps to a drawing instruction (forward,
turn left, turn right). Design rules that grow a target shape (tree,
snowflake, dragon curve). Grammar as geometry.

**26. new-137-reactiondiffusion** — Reaction-Diffusion
Two chemicals diffuse and react on a grid. Adjust reaction rates and
diffusion speeds. Watch Turing patterns emerge — spots, stripes, labyrinths.
Guide the pattern formation to match a target. Alan Turing's morphogenesis
as interactive art.

**27. new-138-gameoflife** — Life Engineer
Conway's Game of Life, but YOU design the initial state to produce a
specific outcome. Target: create a pattern that produces exactly 5 gliders.
Or one that oscillates with period 15. Or one that grows to exactly 100
cells. Reverse-engineering emergence.

**28. new-139-particleswarm** — Particle Swarm
100 particles search for a hidden target. Each particle remembers its
personal best position and knows the swarm's global best. You control
the swarm parameters: inertia, cognitive pull, social pull. Tune the
swarm to find the target. Optimization algorithm as game.

**29. new-140-fractalzoom** — Fractal Zoom
Navigate through a Mandelbrot set. Your "character" is a zoom level and
position. Move through the fractal landscape — each direction reveals
new structure at deeper zoom. Find specific patterns (spirals, seahorses,
minibrots) to score. Mathematics as infinite world.

**30. new-141-quantumcoin** — Quantum Coin
A coin exists in superposition (both heads AND tails). Apply quantum
gates: H (Hadamard — create superposition), X (flip), Z (phase shift).
Measure to collapse. The probability of the outcome depends on your
gate sequence. Build gate sequences to maximize probability of the
desired outcome. Quantum computing as puzzle.

---

## Why These Feel Alien

These games have no ancestors in the arcade, no genre to reference, no
cultural touchstone. They emerge from:
- Topology, not level design
- Field equations, not enemy patterns
- Information theory, not score counters
- Control theory, not button inputs
- Generative algorithms, not authored content

A human playing these games is learning to think like a machine. An AI
playing these games is exploring its own computational foundations. The
common ground between human and machine IS the game.

*These are games made from the language machines speak — mathematics,
physics, information, and emergence. They are playable. They are
satisfying. They are games. But they are not human games. They are
the games that exist in the space between human creativity and
computational possibility.*
