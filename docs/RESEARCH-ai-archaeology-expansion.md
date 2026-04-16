# Research: AI Archaeology Expansion — 50 Games with "What If AI Were There?"

**Date:** 2026-03-24
**Purpose:** Select 50 base archetypes and add AI visualization overlays showing
what the game would look like if AI had co-designed it. Each game gets an H-key
toggle that reveals the AI's perspective: decision trees, probability maps,
trajectory predictions, optimization surfaces, and hidden state estimations.

---

## Selection Criteria

From our 241 base archetypes, the 50 best candidates for AI archaeology are games where:
1. The AI concept adds genuine strategic insight (not just decoration)
2. The visualization transforms how you understand the game
3. The "what if AI were there?" question has a compelling answer
4. The overlay is distinct from any existing AI archaeology game

## Existing Coverage (26 games — do not duplicate)

Already covered: ghostmind, blockplanner, trajectron, foglifter, threatmap,
virtuescope, deepthink, probefield, gapfinder, framereader, pathsense,
pareto, routemind, explorermap, lemmingbrain, bullettime, cardcounter,
antfarm, metroidmap, flowstate, ai-escalation, safety-map, smartbar,
risk-heatmap, search-game, neural-game.

---

## The 50 Selected Games

### Strategy & Decision Theory (10)

| # | Base Game | AI Overlay | AI Concept |
|---|-----------|-----------|------------|
| 1 | anc-008-go | Territory value heatmap | Monte Carlo position evaluation |
| 2 | anc-009-reversi | Positional weight display | Minimax evaluation function |
| 3 | anc-011-checkers | Move tree visualization | Alpha-beta pruning depth |
| 4 | anc-013-blackjack | Card counting probability | Information-theoretic advantage |
| 5 | anc-010-backgammon | Expected value per move | Expectimax with dice probability |
| 6 | sim-020-dicewars | Attack success probability | Bayesian territory assessment |
| 7 | hyb-005-battleship | Ship location probability map | Bayesian posterior update |
| 8 | hyb-006-liarsdice | Bluff detection confidence | Game theory Nash equilibrium |
| 9 | puz-017-wordle | Information entropy per guess | Optimal information gain |
| 10 | puz-016-mastermind | Remaining possibility count | Knuth minimax partition |

### Physics & Spatial Prediction (10)

| 11 | phy-001-asteroids | Trajectory prediction + collision forecast | Newtonian simulation |
| 12 | plt-005-donkey-kong | Barrel path prediction lines | Gravity + platform physics |
| 13 | phy-005-pinball | Ball trajectory forecast | Multi-bounce prediction |
| 14 | spt-011-bowling | Pin scatter prediction | Chain-reaction physics |
| 15 | spt-010-darts | Accuracy probability heatmap | Gaussian throw distribution |
| 16 | phy-010-katamari | Growth trajectory prediction | Exponential scaling forecast |
| 17 | spt-013-carrom | Shot trajectory + collision chain | Elastic collision prediction |
| 18 | phy-008-tower | Structural stability analysis | Center of mass + moment |

### Puzzle Pattern Prediction (10)

| 19 | puz-031-puzzloop | Chain reaction preview | Graph connectivity analysis |
| 20 | puz-032-bakubaku | Feeding cascade prediction | Flood-fill path analysis |
| 21 | puz-034-magicaldrop | Optimal grab-throw display | Greedy optimization |
| 22 | puz-035-paneldepon | Chain combo setup display | Look-ahead search |
| 23 | puz-025-colorlines | Path + alignment preview | A* pathfinding + match scoring |
| 24 | puz-038-moneyexchanger | Exchange cascade preview | Arithmetic chain optimization |
| 25 | puz-030-cameltry | Marble trajectory prediction | Rotational physics simulation |
| 26 | puz-009-sokoban | Deadlock detection overlay | State-space search |
| 27 | puz-019-tangram | Fit probability display | Geometric constraint solving |
| 28 | puz-022-grow | Optimal sequence hint | Combinatorial optimization |

### Combat & Action Intelligence (10)

| 29 | scr-009-contra | Enemy spawn prediction | Pattern recognition |
| 30 | scr-005-1942 | Formation analysis + safe zones | Threat density mapping |
| 31 | sht-004-doom | Threat prioritization + path | Spatial reasoning + A* |
| 32 | sht-005-royale | Zone prediction + player heat | Probabilistic modeling |
| 33 | plt-003-castlevania | Enemy pattern prediction | Finite state machine viz |
| 34 | fgt-005-mortal-kombat | Combo opportunity display | Sequence detection |
| 35 | rpg-008-diablo | Loot probability display | Random variable distribution |
| 36 | fgt-006-teeworlds | Momentum + trajectory prediction | Newtonian + grapple physics |
| 37 | scr-007-vanguard | Multi-directional threat heatmap | 360° threat assessment |
| 38 | fix-004-missile-command | Intercept optimization | Optimal targeting allocation |

### Navigation & Exploration (10)

| 39 | maz-005-tron | Territory value mapping | Voronoi territory partition |
| 40 | maz-009-snake | Optimal path display | Hamiltonian path approximation |
| 41 | maz-004-dig-dug | Tunnel value analysis | Strategic excavation planning |
| 42 | plt-008-pitfall | Danger zone mapping | Temporal hazard prediction |
| 43 | maz-012-chipschallenge | Optimal route solver | BFS/DFS pathfinding viz |
| 44 | maz-006-night-stalker | Threat proximity overlay | Distance-based danger mapping |
| 45 | adv-006-carmen-sandiego | Deduction probability tree | Constraint elimination |
| 46 | maz-016-molemania | Two-layer path optimization | Multi-graph routing |
| 47 | maz-017-crazyarcade | Blast zone prediction | Explosion propagation model |
| 48 | plt-014-canabalt | Gap timing prediction | Procedural pattern analysis |

### Economic & Resource Optimization (2 — to reach 50)

| 49 | sim-001-taipan | Trade route profit optimization | Linear programming |
| 50 | sim-003-oregon-trail | Survival probability forecast | Monte Carlo simulation |

---

## Implementation Plan

Each game follows the same pattern:
1. Recreate the base game (simplified if needed)
2. Add H-key toggle for AI overlay
3. The overlay shows the AI's analysis in real-time
4. Info panel documents the AI concept being visualized

Build in 10 batches of 5 games each.

---

*50 games, 50 AI concepts visualized. The largest expansion of the AI
archaeology track — tripling it from 26 to 76 games. Each one asks the
same question: "What would this game look like if AI had been there?"*
