# Research: Niche Archetypes — The Edges Between Genres

**Date:** 2026-03-24
**Purpose:** Identify 20 games that represent underexplored mechanical niches,
drawing from the full breadth of human play — not just video games, but board
games, card games, parlor games, physical games, pub games, and folk games that
translate beautifully to a single HTML5 canvas.

---

## The Gap Analysis

Pixel Vault's 120 base archetypes draw heavily from the arcade and console
lineage (1975–2020). That lineage privileges certain activities:

**Well-represented:** shooting, jumping, maze navigation, block stacking,
racing, role-playing, scrolling combat, turn-based strategy, physics sandbox

**Underrepresented or missing entirely:**

| Activity | Description | Pre-digital Origin |
|----------|-------------|-------------------|
| **Territory encirclement** | Surround to capture, not destroy | Go (~2500 BCE) |
| **Flanking capture** | Place to flip opponent's pieces | Reversi (1883) |
| **Dice racing** | Race with probabilistic movement + blocking | Backgammon (~3000 BCE) |
| **Jump capture** | Leap over pieces to remove them | Checkers (~3000 BCE) |
| **Memory recall** | Remember hidden positions | Concentration (~1700s) |
| **Sequence memory** | Repeat growing sequences | Simon (1978) |
| **Code breaking** | Deduce hidden pattern from feedback | Mastermind (1970) |
| **Shape fitting** | Rotate and place geometric pieces | Tangram (~1800) |
| **Letter deduction** | Guess words from positional clues | Jotto (1955), Wordle (2021) |
| **Number chaining** | Match ends of played tiles | Dominoes (~1200 CE) |
| **Precision aiming** | Throw at scored target zones | Darts (~1860s) |
| **Lane physics** | Roll + aim + power at pins | Bowling (~3200 BCE) |
| **Grid search** | Probe hidden grid to locate targets | Battleship (1931) |
| **Reaction targeting** | Hit targets that appear and vanish | Whac-A-Mole (1975) |
| **Risk management** | Bet against probability with partial info | Blackjack (~1700s) |
| **Bluffing** | Claim + challenge with hidden dice | Liar's Dice (~1400s) |
| **Tile permutation** | Slide tiles to solve configuration | 15-puzzle (1874) |
| **Word clue solving** | Fill grid from intersecting definitions | Crossword (1913) |
| **Motor speed** | Type accurately under time pressure | Typing games (~1980s) |
| **Physics stacking** | Build tall without toppling | Jenga (1983) |

These 20 activities each represent a **fundamentally different cognitive or
motor skill** from anything in the current collection. They are the edges
between genres — the places where video game taxonomy ends but human play
continues.

---

## Why These Matter

### 1. They Complete the Taxonomy

The current collection answers "what mechanics define video games?" These 20
answer the deeper question: "what mechanics define *play itself*?" A library
of games that omits Go, Backgammon, and Darts is like a library of music that
omits jazz, folk, and blues.

### 2. They Represent Different Cognitive Modes

| Cognitive Mode | Example | Current Coverage |
|---------------|---------|-----------------|
| Spatial reasoning | Tangram | Minimal (Tetris is procedural, not spatial-fit) |
| Memory | Simon, Concentration | None |
| Deduction | Mastermind, Wordle | Minesweeper only |
| Probability | Blackjack, Liar's Dice | None |
| Precision motor | Darts, Bowling | Marble Madness (physics, not aiming) |
| Language | Crossword, Wordle | Scrabble only |
| Bluffing/social | Liar's Dice | None |
| Sequence recall | Simon | None |
| Pattern search | Battleship | None |

### 3. They Have Deep History

Seven of these 20 games predate writing. Backgammon boards were found in the
Royal Tombs of Ur alongside the Royal Game of Ur (already in the collection).
Go has been played continuously for 4,000 years. Checkers boards were found in
the ruins of Ur (3000 BCE). These aren't curiosities — they're the foundation
of human play.

### 4. They Map to AI Milestones

| Game | AI Milestone | Year |
|------|-------------|------|
| Checkers | Samuel's checkers (first self-learning game AI) | 1959 |
| Backgammon | TD-Gammon (temporal-difference learning) | 1992 |
| Go | AlphaGo defeats Lee Sedol | 2016 |
| Blackjack | Card counting (information-theoretic strategy) | 1962 |
| Battleship | Optimal search theory | 1960s |
| Mastermind | Information entropy (Knuth's algorithm) | 1977 |
| Wordle | Information theory applied to word games | 2022 |

---

## The 20 Selected Prototypes

### Board Games (Ancient + Classical)

**1. anc-008-go** — Go (Weiqi)
- **Origin:** China, ~2500 BCE
- **Mechanic:** Place stones to surround territory; captured groups are removed
- **Why it matters:** Deepest game ever created. 10^170 possible positions. AlphaGo's 2016 victory was a landmark in AI history. The ko rule creates infinite game theory depth.
- **Creators:** Unknown (Chinese tradition attributes it to Emperor Yao)
- **AI-ERA:** 6 (AlphaGo, Monte Carlo tree search + deep neural networks)

**2. anc-009-reversi** — Reversi / Othello
- **Origin:** England, 1883 (Lewis Waterman); Othello variant 1971 (Goro Hasegawa)
- **Mechanic:** Place discs to flank and flip opponent's pieces; most discs wins
- **Why it matters:** "A minute to learn, a lifetime to master." Corner and edge strategy creates deep positional play from simple rules.
- **AI-ERA:** 4 (Logistello defeated world champion Takeshi Murakami, 1997)

**3. anc-010-backgammon** — Backgammon
- **Origin:** Mesopotamia, ~3000 BCE (Royal Game of Ur is a distant ancestor)
- **Mechanic:** Race pieces around board using dice; block opponent; bear off first
- **Why it matters:** TD-Gammon (1992) by Gerald Tesauro was the first neural network to achieve expert-level play through self-play — a precursor to AlphaZero.
- **AI-ERA:** 4-5 (TD-Gammon, temporal difference learning)

**4. anc-011-checkers** — Checkers / Draughts
- **Origin:** Ur, ~3000 BCE; modern rules ~1100 CE (France)
- **Mechanic:** Jump diagonally to capture; reach opposite end to king (moves both directions)
- **Why it matters:** Arthur Samuel's checkers program (1959) was the FIRST self-learning game AI. Chinook solved checkers in 2007 (the most complex game ever solved).
- **AI-ERA:** 1-5 (Samuel 1959, Chinook 1994, Schaeffer solved 2007)

**5. anc-012-dominoes** — Dominoes
- **Origin:** China, ~1200 CE; European rules ~1700s
- **Mechanic:** Match tile ends; play from your hand; first to empty wins
- **Why it matters:** Combinatorial reasoning with partial information (you can't see opponent's tiles). The draw pile adds a probabilistic element.
- **AI-ERA:** 2 (rule-based expert systems, probabilistic reasoning)

### Deduction + Logic

**6. puz-016-mastermind** — Mastermind
- **Origin:** Mordechai Meirowitz, 1970 (Israel); published by Invicta Plastics
- **Mechanic:** Guess a hidden 4-color code; receive feedback (correct color+position, correct color only)
- **Why it matters:** Donald Knuth proved the optimal strategy in 1977 (5 guesses max). The game IS information entropy — each guess maximally reduces the solution space.
- **AI-ERA:** 3 (Knuth's minimax algorithm, information theory)

**7. puz-017-wordle** — Wordle (5-letter word deduction)
- **Origin:** Josh Wardle, 2021 (originally for his partner)
- **Mechanic:** Guess 5-letter words; green = right letter + position, yellow = right letter wrong position, grey = not in word
- **Why it matters:** Became a global phenomenon overnight. The mechanic applies information theory to language. Optimal play requires maximizing information gain per guess — the same strategy AI uses.
- **AI-ERA:** 7 (information-theoretic word solving, 3Blue1Brown's analysis)

### Spatial + Permutation

**8. puz-018-slidepuzzle** — 15-Puzzle (Sliding Tiles)
- **Origin:** Noyes Chapman, 1874; popularized by Sam Loyd
- **Mechanic:** Slide numbered tiles in a 4×4 grid (one empty space) to reach sorted order
- **Why it matters:** The first viral puzzle craze (1880). Proved that exactly half of all starting positions are unsolvable. A* search was partially inspired by tile-puzzle heuristics.
- **AI-ERA:** 1-5 (A* search, Manhattan distance heuristic, IDA*)

**9. puz-019-tangram** — Tangram
- **Origin:** China, ~1800 (Song dynasty origins debated)
- **Mechanic:** Arrange 7 geometric pieces (tans) to match a silhouette shape
- **Why it matters:** Pure spatial reasoning with no arithmetic, no text, no cultural knowledge. Universal across languages. Used in cognitive psychology research.
- **AI-ERA:** 5 (computer vision, shape recognition)

### Memory + Sequence

**10. trp-004-simon** — Simon
- **Origin:** Ralph Baer & Howard Morrison, 1978 (Milton Bradley)
- **Mechanic:** Watch a sequence of colored lights/tones; repeat the sequence; it grows by one each round
- **Why it matters:** Ralph Baer also invented the home video game console (1967). Simon tested sequence memory — the same working memory that LSTMs and transformers model.
- **AI-ERA:** 3-6 (sequence modeling, LSTM, attention mechanisms)

**11. puz-020-concentration** — Concentration / Memory Match
- **Origin:** Unknown, ~1700s parlor game; TV game show 1958
- **Mechanic:** Flip pairs of cards; remember positions; match all pairs
- **Why it matters:** Pure spatial memory. Used extensively in cognitive science to study memory decay and chunking. The simplest possible memory game.
- **AI-ERA:** 2 (pattern matching, associative memory)

### Precision + Physics

**12. spt-010-darts** — Darts
- **Origin:** England, ~1860s (soldiers threw shortened arrows at tree trunks)
- **Mechanic:** Aim and throw at a scored dartboard (bullseye, doubles, triples ring); 501 countdown
- **Why it matters:** Precision under pressure. The scoring zones create risk/reward decisions — go for the triple-20 (risky, high reward) or play safe?
- **AI-ERA:** 5 (motor control optimization, precision robotics)

**13. spt-011-bowling** — Bowling
- **Origin:** Ancient Egypt, ~3200 BCE; modern ten-pin ~1840s (New York)
- **Mechanic:** Aim, set power, and release ball down a lane to knock down pins; spare/strike scoring
- **Why it matters:** Physics simulation with spin, deflection, and pin scatter. The scoring system (spares multiply, strikes cascade) is elegant game design.
- **AI-ERA:** 3 (physics simulation, trajectory optimization)

### Hidden Information + Search

**14. hyb-005-battleship** — Battleship
- **Origin:** Pencil-and-paper game, ~1930s (France); Milton Bradley 1967
- **Mechanic:** Place ships on a hidden grid; take turns guessing coordinates; "hit" or "miss"
- **Why it matters:** Optimal play is a search problem. The probability distribution of ship positions given known hits/misses IS Bayesian inference. Hunt mode → target mode is a fundamental search algorithm.
- **AI-ERA:** 3-5 (Bayesian search, probability distributions)

**15. hyb-006-liarsdice** — Liar's Dice (Perudo)
- **Origin:** South America, ~1400s (Inca); European ~1800s
- **Mechanic:** Roll hidden dice; make claims about total dice showing a face; opponent calls "liar" or raises
- **Why it matters:** Bluffing as core mechanic. The game requires modeling your opponent's beliefs about your beliefs — theory of mind. Nash equilibrium strategies exist but humans play with psychology.
- **AI-ERA:** 4-7 (game theory, imperfect information, Libratus poker AI)

### Reaction + Reflex

**16. def-005-whackamole** — Whac-A-Mole
- **Origin:** Aaron Fechter, 1975 (Creative Engineering Inc.)
- **Mechanic:** Moles pop up from holes randomly; hit them before they disappear; speed increases
- **Why it matters:** Pure reaction time measurement. The escalating speed creates a natural difficulty curve. Used in cognitive psychology to measure processing speed.
- **AI-ERA:** 2-5 (reaction time models, attention allocation)

### Risk + Probability

**17. anc-013-blackjack** — Blackjack (Twenty-One)
- **Origin:** France/Spain, ~1700s; Edward Thorp's *Beat the Dealer* (1962)
- **Mechanic:** Draw cards to reach 21 without going over; beat the dealer's hand
- **Why it matters:** Edward Thorp proved card counting works using information theory. The game teaches expected value, risk management, and when to deviate from optimal strategy.
- **AI-ERA:** 2-5 (probability theory, card counting, optimal strategy)

### Language + Words

**18. puz-021-crossword** — Crossword Puzzle
- **Origin:** Arthur Wynne, 1913 (*New York World* newspaper)
- **Mechanic:** Fill a word grid from intersecting clue definitions (across and down)
- **Why it matters:** The most widely solved puzzle format in history. Requires vocabulary, lateral thinking, and constraint satisfaction (intersecting letters must agree).
- **AI-ERA:** 5-7 (NLP, constraint satisfaction, Dr.Fill AI crossword solver 2021)

### Motor Speed

**19. sim-013-typeracer** — Typing Speed Game
- **Origin:** Mavis Beacon Teaches Typing (1987); TypeRacer (2008)
- **Mechanic:** Type displayed text as fast and accurately as possible; WPM scoring
- **Why it matters:** Direct measurement of human-computer interface speed. Touch typing is the most practiced motor skill in computing. WPM is the bandwidth of human text output.
- **AI-ERA:** 1-7 (human-computer interaction, motor learning, input bandwidth)

### Physics + Tension

**20. phy-008-tower** — Tower Stacking (Jenga-inspired)
- **Origin:** Leslie Scott, 1983 (based on a family game from Ghana)
- **Mechanic:** Stack blocks as high as possible; physics determines stability; one wrong move and it falls
- **Why it matters:** Physics simulation under increasing tension. Each placement raises the stakes. The game teaches structural engineering intuition — center of mass, moment of inertia, friction.
- **AI-ERA:** 6 (physics simulation, structural stability AI, robot manipulation)

---

## Classification

| # | File | Series | Mechanic | Origin |
|---|------|--------|----------|--------|
| 1 | anc-008-go | ANC | Territory encirclement | ~2500 BCE China |
| 2 | anc-009-reversi | ANC | Flanking capture | 1883 England |
| 3 | anc-010-backgammon | ANC | Dice race + blocking | ~3000 BCE Mesopotamia |
| 4 | anc-011-checkers | ANC | Jump capture | ~3000 BCE |
| 5 | anc-012-dominoes | ANC | Number end-matching | ~1200 CE China |
| 6 | puz-016-mastermind | PUZ | Code-breaking deduction | 1970 Israel |
| 7 | puz-017-wordle | PUZ | Letter position deduction | 2021 USA |
| 8 | puz-018-slidepuzzle | PUZ | Tile permutation | 1874 USA |
| 9 | puz-019-tangram | PUZ | Shape fitting | ~1800 China |
| 10 | puz-020-concentration | PUZ | Card memory matching | ~1700s |
| 11 | puz-021-crossword | PUZ | Word clue grid | 1913 USA |
| 12 | trp-004-simon | TRP | Sequence memory | 1978 USA |
| 13 | spt-010-darts | SPT | Precision aiming | ~1860s England |
| 14 | spt-011-bowling | SPT | Lane physics + aim | ~3200 BCE Egypt |
| 15 | hyb-005-battleship | HYB | Grid search + hidden info | ~1930s France |
| 16 | hyb-006-liarsdice | HYB | Bluffing + probability | ~1400s South America |
| 17 | def-005-whackamole | DEF | Reaction time targeting | 1975 USA |
| 18 | anc-013-blackjack | ANC | Risk + probability | ~1700s France |
| 19 | sim-013-typeracer | SIM | Motor speed + accuracy | 1987 USA |
| 20 | phy-008-tower | PHY | Physics stacking | 1983 UK/Ghana |

---

## Design Notes

### Translation to Canvas Constraints

All 20 translate naturally to 800×600 canvas:
- Board games → top-down grid rendering
- Card games → card face rendering with Unicode suits/symbols
- Physical games (darts, bowling) → aim-and-release physics
- Word games → keyboard input + grid display
- Memory games → flip animation + position tracking
- Typing games → real-time keyboard input comparison

### Controls

- Board/card games: **mouse click** (place piece, flip card, select)
- Aiming games: **mouse aim + click/hold-release** (power gauge)
- Word/typing games: **keyboard** (type letters)
- Simon: **click colored quadrants** or **1-4 keys**

### Under 50KB Viability

All 20 should fit easily under 50KB:
- Board games are grid-based (compact data)
- No image assets (canvas-drawn everything)
- Word lists for crossword/wordle can be small (100-200 words)
- Physics sims are lightweight (simple gravity + collision)

---

*This document serves as the research foundation for the Niche Archetype batch.
Each game fills a specific gap in the mechanical taxonomy, extends the collection
beyond video game lineage, and adds historical depth spanning 5,000 years of
human play.*
