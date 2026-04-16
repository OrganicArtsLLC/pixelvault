# Pixel Vault — Historical Compendium

**A Playable Museum of Game Mechanics, Genre Archaeology & AI History**

> *"Games consistently solved problems AI researchers were formalizing mathematically.
> Games invented by intuition; AI reinvented by theory."*
> — Pixel Vault, ADR-003

---

## What This Is

This compendium is the research backbone of the Pixel Vault — a collection of
playable HTML5 prototypes that reconstruct the foundational mechanics of video gaming
from 1958 to 1985, then ask: *what if AI had been there?*

Each prototype is a time capsule. Not a port. Not a clone. A reconstruction of the
**core mechanic** — the irreducible loop that made each game matter — rebuilt in a
modern browser with attribution to its creators and context for its place in history.

This compendium documents **150+ creators** across **7 AI eras**, tracing the
lineage from ancient board games (~3200 BCE) through modern games (2020s), with 33
AI convergence points and 30 game-first discoveries that ran decades ahead
of formal AI research. The collection now includes 460 playable prototypes
spanning ancient board games, arcade classics, global folk games, Japanese arcade
rarities, Korean gaming culture, modern multiplayer games (with AI opponents), and
141 AI-originated experiments that explore mechanics no human designer has tried.

**How to use this document:**
- Browse the **Creator Index** for proper attribution
- Read the **Genre Lineage** to understand how mechanics evolved
- Study the **AI Convergence Timeline** to see where games and AI touched
- Play any prototype via the [Gallery](index.html)

---

## Creator Index

Every game referenced in this laboratory was created by real people solving real
problems with the technology available to them. These are the architects.

### Era 0–1: The Pioneers (1958–1971)

| Year | Game | Creator(s) | Organization | Innovation |
|------|------|-----------|-------------|------------|
| 1958 | Tennis for Two | **William Higinbotham** | Brookhaven National Lab | First real-time physics game; oscilloscope display; gravity as mechanic |
| 1962 | Spacewar! | **Steve Russell**, Martin Graetz, Wayne Wiitanen | MIT (PDP-1) | First multiplayer game; Newtonian physics; gravity wells; inertia |
| 1971 | Computer Space | **Nolan Bushnell**, Ted Dabney | Nutting Associates | First commercial arcade game; Spacewar! adapted for public |

### Era 2: Arcade Dawn (1972–1977)

| Year | Game | Creator(s) | Organization | Innovation |
|------|------|-----------|-------------|------------|
| 1972 | Pong | **Allan Alcorn** (designed by Nolan Bushnell) | Atari | Deflection mechanic; Y-tracking opponent; the origin of commercial gaming |
| 1975 | Gun Fight | **Dave Nutting** (based on Tomohiro Nishikado's Western Gun) | Midway / Taito | First game with a microprocessor (Intel 8080) |
| 1976 | Breakout | **Steve Wozniak** & **Steve Jobs** (concept: Nolan Bushnell) | Atari | Solo deflection; brick destruction; paddle-to-wall loop |
| 1976 | Night Driver | Atari engineering team | Atari | First pseudo-3D racing; perspective road rendering |

### Era 3: The Cambrian Explosion (1978–1983)

More new genres were invented in this six-year period than any before or since.
Every game below introduced a mechanic that became a permanent genre.

| Year | Game | Creator(s) | Organization | Innovation |
|------|------|-----------|-------------|------------|
| 1978 | Space Invaders | **Tomohiro Nishikado** | Taito | Fixed-position shooting; formation descent; accidental curriculum learning (speedup-as-fewer-enemies was a CPU optimization bug that became core design) |
| 1979 | Asteroids | **Ed Logg** & **Lyle Rains** | Atari | Continuous physics space; inertia-based movement; thrust-and-rotate; wrap-around topology |
| 1979 | Lunar Lander | **Rich Moore** | Atari | Thrust-based descent with fuel management; gravity as primary mechanic; physics simulation as gameplay |
| 1979 | Galaxian | **Kazunori Sawano** | Namco | Individual enemy attack patterns; breaking formation AI |
| 1980 | Pac-Man | **Toru Iwatani** | Namco | Maze chase; 4 ghost personalities (Blinky, Pinky, Inky, Clyde); power reversal; multi-agent behavioral policies before AI had the term |
| 1980 | Berzerk | **Alan McNeil** | Stern Electronics | Voice synthesis ("Intruder alert!"); arena shooter with room-to-room navigation; Evil Otto as persistent, unkillable pursuer; first game associated with player death (urban legend) |
| 1980 | Missile Command | **Dave Theurer** | Atari | Area defense; resource management under escalating pressure |
| 1980 | Battlezone | **Ed Rotberg** | Atari | First-person 3D vector graphics; tank combat |
| 1980 | Rogue | **Michael Toy**, Glenn Wichman, Ken Arnold | UC Santa Cruz | Procedural generation; permadeath; ASCII graphics — invented roguelikes 34 years before GANs |
| 1981 | Defender | **Eugene Jarvis** & Larry DeMar | Williams | Horizontal scrolling; minimap as dimensionality reduction; partial observability — solved POMDPs intuitively |
| 1981 | Donkey Kong | **Shigeru Miyamoto** | Nintendo | Narrative-driven platforming; character identity; jump-over-obstacles loop |
| 1981 | Frogger | **Konami** development team | Konami | Grid-based traversal; pattern recognition; rhythm-based movement |
| 1981 | Galaga | **Shigeru Yokoyama** | Namco | Capture/rescue mechanic; evolved formation attacks; score maximization via intentional risk |
| 1981 | Lock 'n' Chase | **Data East** development team | Data East | Maze game with door placement; first game where player modifies maze topology in real-time |
| 1981 | Scramble | **Konami** development team | Konami | First side-scrolling shooter with forced scrolling; multi-section level design; fuel management adds resource pressure |
| 1981 | Sokoban | **Hiroyuki Imabayashi** | Thinking Rabbit | Push-block warehouse puzzle; PSPACE-complete; can push but never pull; deadlock detection is itself hard |
| 1981 | Vanguard | **TOSE** / **SNK** | SNK (Centuri in US) | Multi-directional scrolling shooter; four-directional firing; one of the first games with a continue feature |
| 1981 | Qix | **Randy Pfeiffer** & **Sandy Pfeiffer** | Taito America | Territorial control; area claiming under threat; multi-armed bandit problem as entertainment |
| 1982 | Joust | **John Newcomer** | Williams | Flap-to-fly physics; lance combat; co-op/competitive duality; vertical movement = advantage |
| 1982 | Pengo | **Coreland** development team | Sega | Ice-block pushing combat in a maze; push blocks to crush enemies; puzzle-action hybrid where environment IS the weapon |
| 1982 | Pitfall! | **David Crane** | Activision | First side-scrolling platformer with diverse environments; LFSR procedural generation creates 256 screens from minimal algorithm; 20-minute timer |
| 1982 | Robotron: 2084 | **Eugene Jarvis** & Larry DeMar | Williams | Twin-stick controls; arena survival; overwhelming enemy count; rescue mechanic (humans add score) |
| 1982 | Pole Position | **Toru Iwatani** (supervised) | Namco | Pseudo-3D racing; perspective road with scaling sprites; qualifying lap; the racing game template |
| 1982 | Bump 'n' Jump | **Data East** development team | Data East | Vehicular combat racer with altitude mechanic; jumping over obstacles creates a 2.5D gameplay plane |
| 1982 | Zaxxon | **Ikegami Tsushinki** | Sega | First isometric-perspective arcade game; implied depth through shadows and altitude indicator; spatial reasoning in 2.5D |
| 1982 | Dig Dug | **Shouichi Fukatani** | Namco | Tunneling + inflating enemies; terrain is weapon |
| 1981 | Tempest | **Dave Theurer** | Atari | Tube-rim shooter; geometric 3D perspective; first game with selectable starting level; Theurer also created Missile Command (1980) |
| 1982 | Q*bert | **Warren Davis** & Jeff Lee | Gottlieb | Isometric grid; tile-color puzzles; navigational enemy avoidance |
| 1982 | Tron | **Bill Adams** | Bally Midway | Light cycle trail mechanic; territory denial via movement history; your path becomes walls |
| 1982 | Taipan! | **Art Canfil** | Mega Micro Computers | Trading simulation inspired by James Clavell's novel; buy low/sell high across Asian ports; risk-reward economics |
| 1983 | Archon | **Jon Freeman** & **Anne Westfall** | Free Fall Associates | Chess board + real-time arena combat hybrid; first game requiring two incompatible cognitive modes simultaneously; proto-multimodal AI demand |
| 1983 | Libble Rabble | **Namco** development team | Namco | Two-stick string-enclosure mechanic; encircle objects with elastic cord; unique control scheme predating twin-stick conventions |
| 1983 | M.U.L.E. | **Dani Bunten Berry** | Ozark Softscape / Electronic Arts | Multiplayer economic auction game; real-time supply-demand dynamics; pioneered multiplayer game design philosophy |
| 1983 | Lode Runner | **Douglas E. Smith** (age 19) | Brøderbund | Platform puzzle with trap-digging mechanic; level editor included (one of the first); player creates and fills holes to trap enemies; 150 levels |
| 1983 | Mario Bros. | **Shigeru Miyamoto** & Gunpei Yokoi | Nintendo | Arena platformer; enemy stunning via floor hit; two-player cooperative |
| 1983 | BurgerTime | **Data East** development team | Data East | Multi-lane assembly under pursuit; gravity-driven ingredient stacking; walking across bun layers to assemble burgers while avoiding food enemies |
| 1983 | Tapper | **Larry Demar** & **Steve Ritchie** | Bally Midway | Multi-lane service dispatch; real-time queue scheduling as entertainment; return-acknowledgement loop; Budweiser-sponsored cabinet; re-released as Root Beer Tapper (1984). Hidden minigames (rodeo, Burger King, Buck Rogers). Mechanically identical to Erlang M/M/N queueing theory (1909) and CPU EDF scheduling — nobody named this connection at the time |

### Era 3–4: The Refinement Surge (1984–1985)

Genres solidified and deepened. Designers no longer invented mechanics from nothing —
they refined, combined, and pushed existing forms into new territory.

| Year | Game | Creator(s) | Organization | Innovation |
|------|------|-----------|-------------|------------|
| 1984 | Kung-Fu Master | **Takashi Nishiyama** | Irem | First side-scrolling beat-em-up; hierarchical progression (floor-by-floor boss encounters); Nishiyama later created Street Fighter at Capcom. Japanese title: *Spartan X* |
| 1984 | Karateka | **Jordan Mechner** (age 19, at Yale) | Brøderbund | Cinematic pacing in real-time combat; rotoscoped animation from film footage; stance-switching mechanic; dramatic camera techniques integrated into gameplay |
| 1984 | Punch-Out!! | **Genyo Takeda** & **Makoto Wada** | Nintendo | Pattern-recognition boxing; behind-the-player camera; each opponent is a puzzle disguised as a fight — memorize telegraph patterns, exploit openings |
| 1984 | 1942 | **Yoshiki Okamoto** | Capcom | Vertical scrolling WWII shooter; Okamoto's first Capcom game after leaving Konami; loop maneuver as evasion mechanic; spawned Capcom's longest-running shooter series |
| 1984 | Marble Madness | **Mark Cerny** (age 18) | Atari Games | Trackball-controlled physics with isometric perspective; FM synthesis soundtrack (first in arcade); Cerny became one of gaming's most influential system architects (PS4/PS5) |
| 1984 | Tetris | **Alexey Pajitnov** | Soviet Academy of Sciences, Moscow | Real-time NP-hard spatial optimization; falling-block mechanic; the most elegant game design ever made |
| 1985 | Carmen Sandiego | **Dane Bigham**, **Lauren Elliott** et al. | Brøderbund | Educational detective adventure; constraint satisfaction as gameplay — cross-reference clues against encyclopedia; geography learning via deduction |
| 1985 | Gauntlet | **Ed Logg** | Atari Games | Four-player cooperative dungeon crawl; role-differentiated classes (warrior/valkyrie/wizard/elf); same Ed Logg who created Asteroids (1979) and Centipede (1981) |
| 1985 | The Bard's Tale | **Michael Cranford** | Interplay | First-person party RPG with bard music mechanic; dynamic party composition; mapped dungeon exploration; defined the CRPG template for a generation |
| 1985 | Paperboy | **Dave Ralston** & **John Salwitz** | Atari Games | Newspaper delivery on bicycle; obstacle avoidance with projectile aiming; isometric suburban world; one of the first "job simulation" games |
| 1985 | Doki Doki Penguin Land | **Sega** development team | Sega | Egg-guiding puzzle; guide fragile egg downward through obstacles; breakable terrain + gravity = planning under fragility |
| 1985 | Paradroid | **Andrew Braybrook** | Hewson Consultants | Body-possession mechanic; take over enemy robots via circuit mini-game; identity-as-resource; C64 classic |
| 1985 | Little Computer People | **Activision** (David Crane involved) | Activision | Virtual life simulation; autonomous digital person in a house; proto-virtual pet; precursor to The Sims |
| 1985 | Thexder | **Game Arts** (Satoshi Uesaka) | Game Arts | Side-scrolling shooter with jet-to-robot transformation; auto-aiming laser; Shield resource management; one of Japan's first major PC games |
| 1985 | Ultima IV: Quest of the Avatar | **Richard Garriott** ("Lord British") | Origin Systems | First game with ethical virtue system as core mechanic; player judged by moral choices, not combat score; invented alignment-through-behavior 35 years before RLHF |
| 1985 | Super Mario Bros. | **Shigeru Miyamoto** & Takashi Tezuka | Nintendo | Scrolling platformer perfected; reward shaping via level design; momentum-based physics; power-up system |

### Era 4–5: The Expansion Wave (1986–1989)

The arcade golden age gave way to home computers and consoles. Designers pushed
into cinematic storytelling, open worlds, moral complexity, and genre fusion.
Several paradigm-class AI discoveries originate here.

| Year | Game | Creator(s) | Organization | Innovation |
|------|------|-----------|-------------|------------|
| 1986 | Bubble Bobble | **Fukio "MTJ" Mitsuji** | Taito | Trap-then-pop platformer; 100-level arcade progression; hidden mechanics and secret endings; cooperative play that changes game behavior |
| 1986 | Castlevania | **Hitoshi Akamatsu** | Konami | Whip-based platformer with horror setting; deliberate, weighty movement; sub-weapon system; spawned the "Metroidvania" genre with Symphony of the Night (1997) |
| 1986 | Ikari Warriors | **SNK** development team | SNK | Vertically scrolling run-and-gun with rotary joystick control; 8-directional movement + independent aim; tank commandeering; cooperative gameplay |
| 1986 | Kid Icarus | **Toru Osawa** | Nintendo R&D1 | Vertical scrolling platformer + RPG progression; shared engine with Metroid; mythological setting with ascending world structure |
| 1986 | Metroid | **Yoshio Sakamoto** & **Gunpei Yokoi** | Nintendo R&D1 | Non-linear exploration platformer; ability-gated backtracking; atmospheric isolation; co-defined the Metroidvania genre |
| 1986 | Out Run | **Yu Suzuki** | Sega AM2 | Pseudo-3D branching-path racer; player-selected routes at forks; hydraulic deluxe cabinet; radio station selection (player chooses soundtrack); defined the "experience racer" genre |
| 1986 | Rampage | **Brian Colin** & **Jeff Nauman** | Bally Midway | 3-player cooperative destruction; players ARE the monsters (kaiju); building-demolition as core loop; perspective inversion — you are the disaster, not the hero |
| 1987 | Contra | **Konami** development team | Konami | Side-scrolling run-and-gun; 8-directional shooting; choreographed enemy wave patterns; definitive two-player cooperative action |
| 1987 | Dungeon Master | **FTL Games** (Doug Bell) | FTL Games | Real-time first-person dungeon crawl; grid-based movement with party management under time pressure; hunger/thirst survival layer |
| 1987 | Maniac Mansion | **Ron Gilbert** & **Gary Winnick** | Lucasfilm Games | First SCUMM engine game; verb-based natural language interface for adventure puzzles; multiple playable characters with unique abilities; multiple endings based on choices and character selection; invented the grammar that became prompt engineering 36 years early |
| 1987 | Metal Gear | **Hideo Kojima** | Konami | Stealth-action; success means NOT fighting; guard patrol patterns, vision cones, alert states; inverted the action game premise |
| 1987 | NetHack | **NetHack Dev Team** (Mike Stephenson et al.) | Open source (community) | Community-evolved roguelike; vast item interaction matrix; procedural + combinatorial emergence; "the DevTeam thinks of everything" |
| 1987 | Adventures of Iljimae | **Aproman** | Aproman (Korea, MSX) | Korean folk hero action game; one of Korea's earliest original video games; MSX platform |
| 1987 | Mavis Beacon Teaches Typing | **Mavis Beacon Software** (Les Crane) | Software Toolworks | Typing tutor as game; motor speed + accuracy measurement; adaptive difficulty based on weakness |
| 1987 | Nonogram | **Non Ishida** (Japan) & **Gwynneth Flower** (UK) | Independent (simultaneously) | Picture logic puzzle; row/column numeric clues encode hidden image; constraint propagation to solve; Nintendo's Picross (1995) made it mainstream |
| 1987 | Ys | **Nihon Falcom** (Masaya Hashimoto) | Nihon Falcom | Action RPG with "bump combat" system; cinematic boss battles; distinctive soundtrack by Yuzo Koshiro; bridge between turn-based and action RPGs |
| 1988 | Battle Chess | **Interplay Productions** (led by **Brian Fargo**) | Interplay | Animated chess with combat sequences per capture; standard chess rules + visual entertainment layer; proved that presentation transforms engagement without changing mechanics |
| 1988 | Wasteland | **Brian Fargo** & **Alan Pavlish** | Interplay | Post-apocalyptic party RPG; moral choice with permanent consequences; character skill-based puzzle solving; spiritual predecessor to Fallout; paragraph book system for narrative depth |
| 1989 | Populous | **Peter Molyneux** | Bullfrog Productions | God game; indirect control via terraforming; autonomous agents respond to environment changes; invented the god game genre; predates Molyneux's later Black & White (2001) |
| 1989 | Prince of Persia | **Jordan Mechner** | Brøderbund | Cinematic platformer; rotoscoped human motion (filmed his brother David); fluid animation at the cost of precise control; 60-minute real-time countdown; Mechner also created Karateka (1984, age 19) — two paradigm games before age 25 |
| 1989 | Cameltry | **Taito** development team | Taito | Rotate-the-maze marble game; player rotates world, not ball; gravity does the work; precursor to Super Monkey Ball |
| 1989 | Chip's Challenge | **Chuck Sommerville** | Epyx (later Microsoft) | Tile-based logic puzzle; collect chips, avoid hazards, find keys; 149 levels of escalating complexity; bundled with Windows |
| 1989 | Quinty / Mendel Palace | **Game Freak** (Satoshi Tajiri & Ken Sugimori) | Namco | Floor-panel flipping combat; Game Freak's first game before creating Pokémon; push enemies into walls via panel manipulation |
| 1989 | Shufflepuck Cafe | **Brøderbund** development team | Brøderbund | Air hockey with personality-modeled AI opponents; each opponent has distinct behavioral parameters (aggression, speed, accuracy); character-driven difficulty curve |

### Era 5–6: The Digital Renaissance (1990–1993)

The 16-bit era and early PC gaming explosion. Genres matured into definitive forms.
Designers pushed into 3D, complex AI opponents, agent-based systems, and the
first networked multiplayer. Several games here defined entire genres.

| Year | Game | Creator(s) | Organization | Innovation |
|------|------|-----------|-------------|------------|
| 1989 | Pipe Mania | **The Assembly Line** | Empire Interactive | Flow connection puzzle; place pipe segments before fluid arrives; random piece queue adds Tetris-like stochastic element; rebranded as Pipe Dream; mechanic appears in countless games as hacking/lockpicking minigame |
| 1990 | Columns | **Jay Geertsen** | Sega | Vertical falling-block puzzle with color-matching; gems fall in columns of three; match 3+ horizontally, vertically, or diagonally to clear; Sega's answer to Tetris |
| 1990 | Liquid Kids / Mizubaku Adventure | **Taito** development team | Taito | Water-wave platformer; throw water bombs that become waves; environment interaction through fluid dynamics |
| 1990 | Perestroika | **Nikita Skripkin** | Locis Software (USSR) | Frog-hopping on shrinking lily pads; political allegory during glasnost; one of the first Soviet-made computer games |
| 1990 | Minesweeper | **Robert Donner** & **Curt Johnson** | Microsoft | Logic deduction grid; numeric clues encode adjacent mine count; NP-complete constraint satisfaction; bundled with Windows 3.1, possibly most-installed game ever |
| 1990 | Solitaire (Windows) | **Wes Cherry** (Microsoft intern) | Microsoft | Klondike card game bundled with Windows 3.0 to teach drag-and-drop mouse skills; became most-played computer game in history; ~1 billion hours/year at peak |
| 1990 | Wing Commander | **Chris Roberts** | Origin Systems | Cockpit space combat with AI wingmen using behavior trees; personality-driven ally/enemy AI; cinematic branching narrative between missions |
| 1991 | Another World / Out of This World | **Éric Chahi** | Delphine Software | Cinematic platformer; polygon-based animation; no HUD; one-person masterwork |
| 1991 | Civilization | **Sid Meier** | MicroProse | 4X turn-based strategy (Explore, Expand, Exploit, Exterminate); multi-objective AI opponents; defined the genre; tech tree as progression structure |
| 1991 | Gorillas | **IBM** (QBasic sample program) | IBM / Microsoft | QBasic artillery game bundled with MS-DOS 5.0; angle-and-velocity projectile physics; taught a generation to program |
| 1991 | Lemmings | **David Jones** | DMA Design | Agent-programming puzzle; autonomous walkers with player-assigned behavior modifications (dig, build, block, etc.); indirect control over independent agents |
| 1991 | Scorched Earth | **Wendell Hicken** | Wendell Hicken (shareware) | "Mother of all games"; tank artillery with terrain destruction; weapons marketplace; definitive artillery game |
| 1991 | SkiFree | **Chris Pirih** | Microsoft | Procedural downhill obstacle generation; infamous chase agent (the Abominable Snow Monster); deceptively simple mechanics with emergent replayability |
| 1992 | JezzBall | **Dima Pavlovsky** | Microsoft | Territory division; build walls to trap bouncing balls; claim 75% of area to advance; simplifies Qix's freeform lines into axis-aligned walls |
| 1992 | Color Lines | **Olga Demina**, **Gennady Denisov** & **Igor Ivkin** | Gamos, Moscow | Move colored balls on grid to form lines of 5+; Russian-made puzzle phenomenon; WinLines spread across post-Soviet PCs |
| 1992 | Gimmick! | **Sunsoft** development team | Sunsoft | Bouncing star projectile platformer; released only in Japan/Scandinavia; cult classic physics-based NES platformer; one of the system's greatest hidden gems |
| 1992 | Mortal Kombat | **Ed Boon** & **John Tobias** | Midway | 1v1 fighting with digitized actors; finishing moves as cultural phenomenon; input-reading AI difficulty scaling; gore controversy drove industry-wide rating system (ESRB) |
| 1992 | Pinball Dreams | **Digital Illusions** (now DICE) | 21st Century Entertainment | Real-time pinball physics simulation on home computers; accurate ball dynamics; Digital Illusions later created the Battlefield series |
| 1992 | Super Mario Kart | **Hideki Konno** & **Tadashi Sugiyama** | Nintendo | Kart racing with items and rubber-banding AI; Mode 7 pseudo-3D; created the kart racing genre; drift/boost mechanic |
| 1993 | The Incredible Machine | **Kevin Ryan** | Sierra Entertainment | Rube Goldberg physics puzzle; place objects to create chain reactions; sandbox physics experimentation; one of the first physics puzzle games |
| 1993 | Doom | **John Carmack** & **John Romero** | id Software | Raycasting 3D engine; BSP tree spatial partitioning; networked deathmatch invented multiplayer FPS; defined an entire genre; mod community pioneered user-generated content |
| 1994 | Astonishia Story | **Sonnori** | Sonnori (Korea) | Korea's first RPG; hex-grid SRPG; foundational title for Korean game development industry |
| 1994 | Umihara Kawase | **TNN** development team | TNN (Super Famicom) | Rubber-band grappling hook physics platformer; elastic rope mechanics; Japanese cult classic; uniquely satisfying swing physics |
| 1995 | Baku Baku Animal | **Sega** development team | Sega | Animal-food matching falling puzzle; animals eat their food — visual logic matching mechanic |
| 1995 | Magical Drop | **Data East** development team | Data East | Speed-based grab-and-throw puzzle; vertical columns with active piece manipulation; fastest competitive puzzle series |
| 1995 | Panel de Pon / Tetris Attack | **Intelligent Systems** | Nintendo | Horizontal swap matching with rising stack; continuous pressure; competitive combo system; skill ceiling much higher than Tetris |

### Era 6: The Genre Maturation (1995–2019)

Genres refined into definitive modern forms. Indie developers proved that one person
could create a genre-defining hit. Mobile gaming and free-to-play transformed economics.
The deck-building roguelike, auto-battler, battle royale, and idle game emerged as new genres.

| Year | Game | Creator(s) | Organization | Innovation |
|------|------|-----------|-------------|------------|
| 1995 | Worms | **Andy Davidson** (age 17) | Team17 | Turn-based artillery with destructible pixel terrain; wind physics; team management; humor as design element; teenage creator won a game design competition |
| 1996 | Diablo | **David Brevik**, **Max Schaefer** & **Erich Schaefer** | Blizzard North (Condor) | Click-to-move action RPG; procedurally generated dungeons; randomized loot with stat variations; defined the ARPG genre; addictive item-hunt loop |
| 1996 | Mole Mania | **Shigeru Miyamoto** | Nintendo (Game Boy) | Two-layer push puzzle; dig underground to bypass surface obstacles; Miyamoto's overlooked handheld gem |
| 1996 | The Kingdom of the Winds | **Jake Song** | Nexon (Korea) | Korea's first MMORPG; one of the world's first graphical online RPGs; predates Ultima Online; launched Korean online gaming industry |
| 1996 | Tamagotchi | **Aki Maita** & **Akihiro Yokoi** | Bandai | Virtual pet on keychain; need-based lifecycle simulation; digital responsibility toy; cultural phenomenon |
| 1996 | Touhou Project | **ZUN** (Jun'ya Ōta) | Team Shanghai Alice | Bullet hell (danmaku); dense beautiful bullet patterns with tiny player hitbox; graze system rewards near-misses; one-man indie phenomenon spanning 18+ games |
| 1996 | Densha de Go! | **Taito** development team | Taito | Train driving simulation; stop accuracy within centimeters; Japanese rail culture as game; specialized controller |
| 1996 | Bishi Bashi Special | **Konami** development team | Konami | Rapid-fire mini-game anthology; absurd button-mashing challenges; precursor to WarioWare; party game perfection |
| 1997 | Money Idol Exchanger | **Face** | Face (arcade/Neo Geo) | Coin arithmetic puzzle; match coins that add to the same value; mental math as fast puzzle mechanic |
| 1997 | Nokia Snake | **Taneli Armanto** | Nokia | Trail-growth maze game pre-installed on 400M+ phones; growing body as self-obstacle; possibly most-played game in history by install base |
| 1997 | Puchi Carat | **Taito** development team | Taito | Competitive Breakout; paddle-based block breaking against an opponent; Arkanoid meets Puzzle Bobble |
| 1998 | Dance Dance Revolution | **Konami** (Bemani division) | Konami | Rhythm action; physical foot-pad controller; timing-based scoring; proved games could be athletic; spawned rhythm game genre |
| 1998 | Puzz Loop | **Mitchell Corporation** | Mitchell Corporation (Japan) | Rotating marble shooter into moving chain; match colors to eliminate; precursor to Zuma (2003) and Luxor (2005) |
| 1999 | Fortress | **CCR Inc.** | CCR Inc. (Korea) | Team-based wind artillery; Korean national esport; weather-affected trajectory physics; pioneered Korean competitive gaming |
| 1999 | Pump It Up | **Andamiro** | Andamiro (Korea) | 5-panel diagonal rhythm game; Korean DDR rival; became Latin America's dominant rhythm game |
| 1999 | QuizQuiz | **Nexon** | Nexon (Korea) | First free-to-play online game; quiz + Puzzle Fighter hybrid; Nexon invented F2P monetization model |
| 1999 | EZ2DJ | **Amuseworld** | Amuseworld (Korea) | Korean DJ rhythm arcade; 5-key + turntable + pedal; precursor to DJMAX |
| 2001 | Advance Wars | **Intelligent Systems** | Nintendo | Turn-based grid tactics; terrain advantage system; CO powers; fog of war; defined portable strategy gaming |
| 2001 | Bejeweled | **Jason Kapalka** | PopCap Games | Swap-to-match-3 with cascading chains; elegant simplification of matching puzzles; generated more mobile revenue than any other genre |
| 2001 | Crazy Arcade / BnB | **Nexon** development team | Nexon (Korea) | Korean Bomberman-style water balloon game; massive Korean online hit; simplified trap mechanics for accessibility |
| 2001 | Kuru Kuru Kururin | **Eighting** | Nintendo (GBA, Japan/Europe) | Navigate rotating stick through tight corridors; patience and timing with an unwieldy avatar |
| 2002 | GROW | **On Nakayama** | Eyezmaze (Japan) | Combinatorial sequence puzzle; place items in correct order; each choice affects all others; 12!=479M permutations, one solution |
| 2003 | GunBound | **Softnyx** | Softnyx (Korea) | Online artillery combat; Worms meets Korean competitive gaming; mobile units + terrain + wind |
| 2004 | DJMAX | **Pentavision** | Pentavision (Korea) | Premium 6-lane rhythm game; Korean music game franchise; high production value; DJMAX Respect on PS4 |
| 2004 | Katamari Damacy | **Keita Takahashi** | Namco | Roll sticky ball to collect objects; scale from thumbtack to continent; joyful absurdist design; size-as-progression |
| 2004 | Motherload | **XGen Studios** | XGen Studios | Mining loop — dig, collect, sell, upgrade, dig deeper; addictive resource extraction; SteamWorld Dig lineage |
| 2004 | Pangya | **Ntreev Soft** | Ntreev Soft (Korea) | Anime-style online golf; social MMO golf game; Korean casual gaming landmark |
| 2004 | Tontie | **On Nakayama** | Eyezmaze (Japan) | Numpad-based whacking game; hammer moles mapped to number keys; Flash browser classic |
| 2004 | Yume Nikki | **Kikiyama** | Independent (Japan) | Dream-world exploration with no objectives; atmospheric surrealism; no combat; RPG Maker art game; massively influential indie |
| 2004 | Audition Online | **T3 Entertainment** | T3 Entertainment (Korea) | Social dance combo rhythm game; arrow sequence memorization; Korean online gaming cultural phenomenon |
| 2005 | Dicewars | **Taro Ito** | Independent (Flash, Japan) | Risk-like territory with dice combat; elegant 1-page strategy; auto-attack resolution; addictive Flash game |
| 2005 | Freestyle (basketball) | **JCE** | JCE (Korea) | Arcade street basketball online; character skill builds; Korean sports MMO |
| 2005 | Guitar Hero | **Harmonix** (Alex Rigopulos, Eran Egozy) | RedOctane/Activision | Guitar-shaped controller rhythm game; note highways; star power; made rhythm games mainstream in the West |
| 2005 | Falling Sand Game | Various Flash developers | Web community | Cellular automata sandbox; particles with material-specific rules; emergence from simple local interactions; Noita (2019, Nolla Games) proved it could power a full commercial game |
| 2005 | Nanaca Crash | Anonymous Japanese Flash developer | Independent (Japan) | Launch-and-bounce combo game; angle + power + mid-air combo triggers; addictive Flash physics toy |
| 2006 | Line Rider | **Boštjan Čadež** | Independent (Slovenia) | Draw-your-own-track physics sandbox; emergent sled runs on user-drawn lines; viral Flash phenomenon |
| 2007 | Bloons TD | **Chris Harris** & **Stephen Harris** | Ninja Kiwi | Tower defense with layered balloon-popping mechanics; monkey towers with upgrade paths; one of the defining tower defense franchises |
| 2007 | Hoshi Saga | **Yoshio Ishii** | Nekogames (Japan) | Hidden-star puzzle anthology; each stage has unique rules; same creator as Cursor*10 |
| 2007 | Recettear: An Item Shop's Tale | **EasyGameStation** | EasyGameStation (doujin, Japan) | RPG item shop management sim; buy low from dungeons, sell high to heroes; capitalism-as-RPG perspective inversion |
| 2007 | Teeworlds | **Magnus Auvinen** (matricks) | Open source | 2D platform combat with grappling hook physics; fast-paced online multiplayer; open source community development |
| 2008 | Cursor*10 | **Yoshio Ishii** | Nekogames (Japan) | Time-clone cooperative puzzle; your past selves replay alongside you; cooperation with your own history |
| 2008 | QWOP | **Bennett Foddy** | Independent | Deliberately awkward physics controls; each leg muscle mapped to a key; difficulty IS the mechanic; rage game pioneer |
| 2008 | World of Goo | **Kyle Gabler** & **Ron Carmel** | 2D Boy | Living physics bridge construction; goo balls as structural material; indie game landmark |
| 2009 | Canabalt | **Adam Saltsman** | Semi Secret Software | Invented the endless runner; one-button auto-run platformer; procedural building gaps; iPhone gaming milestone |
| 2009 | Cho Chabudai Gaeshi | **Taito** | Taito (Japan-only arcade) | Table-flipping rage simulation; flip a dinner table in anger; uniquely Japanese stress-relief arcade |
| 2009 | Doodle Jump | **Igor Pusenjak** & **Marko Pusenjak** | Lima Sky | Auto-jump vertical platformer; tilt controls; procedural platform generation; defined early mobile gaming alongside Angry Birds |
| 2009 | This Is the Only Level | **John Cooney** (jmtb02) | Independent | Same level, changing rules; meta-game puzzle; the level doesn't change but your assumptions must |
| 2010 | Cut the Rope | **Semyon Voinov** & **Efim Voinov** | ZeptoLab | Rope-cutting physics puzzle; feed candy to Om Nom; verlet rope integration; elegant touch-first design |
| 2010 | VVVVVV | **Terry Cavanagh** | Independent | Gravity-flip platformer; no jump — only gravity reversal; binary state toggle creates complex level design from minimal controls; retro minimalism |
| 2011 | Kingdom Rush | **Alvaro Azofra**, **Pablo Realini** & **Gonzalo Sande** | Ironhide Game Studio | Tower defense with hero unit and barracks blocking; four tower types with branching upgrades; set the standard for mobile TD |
| 2012 | Clash of Clans | **Supercell** (Ilkka Paananen, CEO) | Supercell | Base building + army deployment; asynchronous multiplayer raids; clan system; free-to-play economics that generated billions |
| 2012 | Dragon Flight | **NextFloor** | NextFloor (Korea) | Vertical-scrolling dragon shooter; Korean mobile gaming hit; accessible shmup |
| 2012 | Mark of the Ninja | **Klei Entertainment** | Klei | 2D stealth platformer; formalized stealth mechanics with visible sound rings and sight lines; proved stealth works in 2D |
| 2013 | A Dark Room | **Michael Townsend** | Doublespeak Games | Text-based genre-reveal; starts as idle game, becomes RPG, becomes exploration; narrative through mechanic revelation |
| 2013 | Cookie Clicker | **Julien "Orteil" Thiennot** | Independent | Idle/incremental game; exponential growth with diminishing returns; prestige system as meta-learning reset; stripped all traditional game design to expose pure progress psychology |
| 2013 | Cookie Run | **Devsisters** | Devsisters (Korea) | Cookie-themed auto-runner; Korean mobile gaming phenomenon; evolved into Cookie Run: Kingdom |
| 2013 | Papers, Please | **Lucas Pope** | 3909 LLC | Bureaucracy as gameplay; check documents against rules; moral dilemmas in monotony; "glory to Arstotzka" |
| 2013 | Wind Runner | **Actoz Soft** | Actoz Soft (Korea) | Wind-glide runner; Korean casual mobile runner |
| 2014 | Munin | **Gojira** | Gojira (Sweden) | Norse mythology puzzle platformer; rotate world sections; gravity-based level manipulation |
| 2014 | Nidhogg | **Messhof** (Mark Essen) | Messhof | Fencing tug-of-war; advance/retreat swordfighting with respawn; minimalist competitive brilliance |
| 2015 | Agar.io | **Matheus Valadares** | Independent (Brazil) | Cell-growth browser game; eat smaller, flee larger; viral .io phenomenon; simplest possible multiplayer |
| 2015 | Downwell | **Ojiro Fumoto** | Independent (Japan) | Vertical-descent shooter; gunboots fire downward and slow descent; combo system rewards continuous falling |
| 2015 | Rocket League | **Psyonix** (Dave Hagewood) | Psyonix | Car soccer with boost physics and aerial mechanics; physics-driven competitive sport; esports phenomenon |
| 2016 | Clash Royale | **Supercell** | Supercell | Lane-based real-time card battler; elixir economy; deck building meets tower defense; 3-minute matches |
| 2016 | Okhlos | **Coffee Powered Machine** | Devolver Digital (Argentina) | Angry mob management; lead a crowd of mythological rioters; Pikmin meets Greek mythology |
| 2016 | Replica | **SOMI** | Independent (South Korea) | Found-phone surveillance narrative; search a stranger's phone for evidence; privacy ethics as gameplay |
| 2016 | Overcooked | **Ghost Town Games** (Phil Duncan, Ol De-Gaulle) | Team17 | Cooperative kitchen chaos; multi-step recipes under time pressure; real-time job-shop scheduling as cooperative fun |
| 2016 | Stardew Valley | **Eric "ConcernedApe" Barone** (solo developer) | Self-published | Farming sim; plant/tend/harvest/sell + social simulation; one developer created a cultural phenomenon; proved indie can rival AAA in engagement |
| 2017 | Baba Is You | **Arvi Teikari** (Hempuli) | Independent (Finland) | Rules ARE moveable objects; push "BABA IS YOU" to change win conditions; Sokoban meets programming; paradigm-shattering puzzle design |
| 2017 | Cinco Paus | **Michael Brough** | Independent (New Zealand) | Portuguese-language roguelike; 5 wands with discoverable effects; experimentation as core mechanic |
| 2017 | Detention | **Red Candle Games** | Red Candle Games (Taipei, Taiwan) | Taiwanese White Terror horror; side-scrolling point-and-click; cultural history as horror; folk religion mechanics |
| 2017 | Engare | **Mahdi Bahrami** | Independent (Tehran, Iran) | Islamic geometric pattern drawing; find the tracing point on rotating gears; mathematics as art |
| 2017 | Farsh | **Mahdi Bahrami** | Independent (Tehran, Iran) | Persian carpet folding puzzle; fold carpet to align patterns; Sokoban meets origami |
| 2017 | Getting Over It | **Bennett Foddy** | Independent | Rage climbing with a hammer and pot; Sisyphean ascent; deliberate frustration as philosophical statement |
| 2017 | Slay the Spire | **Casey Yano** & **Anthony Giovannetti** | MegaCrit | Deck-building roguelike; each card is both capability and dilution risk; online policy optimization through play; created an entirely new genre |
| 2017 | PUBG / Fortnite | **Brendan "PlayerUnknown" Greene** / **Epic Games** | PUBG Corp / Epic | Battle royale; 100 players, shrinking zone, last one standing; PUBG pioneered, Fortnite popularized with building mechanic |
| 2018 | Chuchel | **Jakub Dvorsky** | Amanita Design (Prague, Czech Republic) | Absurdist point-and-click comedy; slapstick animation puzzles; Czech indie studio's signature humor |
| 2018 | Dungreed | **Team Horay** | Team Horay (Korea) | Dash combat roguelite; Korean indie action platformer with weapon variety |
| 2018 | Minit | **Jan Willem Nijman**, **Kitty Calis**, **Jukio Kallio** & **Dominik Johann** | Independent (Netherlands) | 60-second adventure game; Zelda in one-minute loops; death resets timer but progress persists |
| 2018 | MO:Astray | **Archpray** | Archpray (Korea/Taiwan) | Slime possession platformer; sticky wall-climbing slime that takes over enemies; body-horror action |
| 2018 | Semblance | **Nyamakop** (Ben Myers & Cukia Kimani) | Nyamakop (Cape Town, South Africa) | Deformable terrain platformer; squish the world to create paths; first South African console game |
| 2019 | Auto Chess | **Drodo Studio** (Dota 2 mod) | Independent | Auto-battler; buy and position units, combat runs automatically; synergy bonuses; separated strategy from execution; spawned TFT, Underlords |
| 2020 | Coffee Talk | **Toge Productions** | Toge Productions (Jakarta, Indonesia) | Barista visual novel; brew drinks, listen to stories; Southeast Asian indie storytelling |
| 2021 | Cris Tales | **Dreams Uncorporated / SYCK** | Modus Games (Colombia) | Time-split RPG; see past/present/future simultaneously; Colombian-made JRPG-style game |
| 2021 | Skul: The Hero Slayer | **SouthPAW Games** | SouthPAW Games (Korea) | Skull-swapping roguelite; steal enemy heads for their powers; Korean indie breakout hit |
| 2021 | Unpacking | **Witch Beam** | Witch Beam (Brisbane, Australia) | Unpack boxes into rooms; spatial organization as narrative; environmental storytelling through belongings |
| 2021 | Wordle | **Josh Wardle** | Independent (later NYT) | Daily 5-letter word deduction; information-theoretic optimal play; social sharing via colored squares; cultural phenomenon |

### Era 7: Scrabble & the Ancient Outliers

Some prototypes reference games whose origins predate computing entirely.

| Year | Game | Creator(s) | Organization | Innovation |
|------|------|-----------|-------------|------------|
| ~3200 BCE | Bowling | Unknown | Ancient Egypt | Lane physics + pin scatter; one of the oldest physical skill games |
| ~3000 BCE | Backgammon | Unknown | Ancient Persia/Mesopotamia | Dice-race with blocking strategy; TD-Gammon (1992) was RL breakthrough |
| ~3000 BCE | Checkers | Unknown | Ancient (Alquerque lineage) | Jump capture on grid; Arthur Samuel's 1959 checkers program was the first learning AI |
| ~2600 BCE | Royal Game of Ur | Unknown | Ancient Mesopotamia | One of the oldest known board games; race game with dice; discovered in the Royal Tombs of Ur |
| ~2500 BCE | Go (Weiqi) | Unknown | Ancient China | Territory encirclement; 10^170 possible positions; AlphaGo (2016) was deep learning's triumph |
| ~2000 BCE | Kabaddi | Unknown | Indian subcontinent | Tag-wrestling breath-hold sport; raid-and-retreat with physical risk |
| ~2000 BCE | Yutnori | Unknown | Korea | Stick-throw race game; one of Korea's oldest traditional games |
| ~1800 CE | Tangram | Unknown | China | Seven geometric pieces; spatial decomposition puzzle; constraint satisfaction |
| ~1700 CE | Concentration | Unknown | European parlor game | Card memory matching; working memory capacity test |
| ~1680 CE | Fanorona | Unknown | Madagascar | Line capture strategy; 44-stone board; used to decide military disputes |
| ~1200 CE | Dominoes | Unknown | China (later Italy) | Number end-matching chain; combinatorial tile placement |
| ~1000 CE | Makruk | Unknown | Thailand | Thai chess variant; closer to original Chaturanga than modern chess |
| ~900 CE | Janggi | Unknown | Korea | Korean chess variant; elephants, chariots, palace confinement rules |
| ~700 CE | Mancala | Unknown | African/Asian origin | Sowing/count-and-capture mechanic; one of the world's oldest and most widespread game families |
| ~600 CE | Chess | Unknown (evolved over centuries) | India/Persia/Arabia | Perfect information strategy; became AI's original benchmark (Deep Blue, 1997) |
| ~500 CE | Tuho | Unknown | Korea/China | Arrow-throwing accuracy into a pot; aristocratic court game |
| ~400 CE | Hnefatafl | Unknown | Norse/Sami peoples | Asymmetric board game; king escape vs. besiegers; documented by Linnaeus (1732) |
| ~200 BCE | Patolli | Unknown | Mesoamerica (Aztec) | Cross-shaped board race; ritual gambling game; pre-Columbian strategy |
| Traditional | Surakarta | Unknown | Java, Indonesia | Capture by loop movement along curved tracks; unique capture mechanic |
| Traditional | Togyzkumalak | Unknown | Central Asian nomadic peoples | 162-stone mancala variant; deeper strategy than Oware |
| Traditional | Congkak | Unknown | Malaysia/Philippines (~16th century) | Mancala variant with 7-hole boards; Southeast Asian sowing game |
| Traditional | Carrom | Unknown | South Asia (~18th century) | Tabletop flicking physics; striker-and-pocket billiards on wood |
| Traditional | Pétanque | **Jules Lenoir** (formalized 1907) | La Ciotat, France | Metal ball tossing; proximity scoring; pointing vs. shooting strategy |
| Traditional | Sepak Takraw | Unknown | Southeast Asia (~15th century) | Rattan ball football-volleyball; bicycle-kick acrobatics |
| Traditional | Ddakji | Unknown | Korea (traditional) | Card-slamming impact physics; flip opponent's card to capture |
| Traditional | Gonggi | Unknown | Korea (centuries-old) | Korean jacks; toss-and-catch dexterity; similar to Knucklebones |
| Traditional | Ssireum | Unknown | Korea (4th century Goguryeo murals) | Korean wrestling; belt-grip throws; UNESCO cultural heritage |
| Traditional | Jegichagi | Unknown | Korea (traditional) | Shuttlecock keepie-uppie; foot juggling endurance |
| Traditional | Paengi | Unknown | Korea (traditional) | Top spinning; spin duration and trick performance |
| ~1860s | Darts | Unknown | England | Precision aiming at numbered sectors; explore-exploit scoring strategy |
| 1874 | 15-Puzzle | **Noyes Chapman** (Sam Loyd popularized) | USA | Sliding tile permutation; foundational A* search heuristic benchmark |
| 1883 | Reversi | **Lewis Waterman** (Othello: **Goro Hasegawa**, 1971) | England / Japan | Flanking capture on grid; Logistello (1997) dominated human play |
| 1913 | Crossword | **Arthur Wynne** | New York World newspaper | Word-clue grid; constraint satisfaction + NLP; Dr.Fill AI (2021) |
| ~1930s | Battleship | Unknown (pencil-and-paper origin) | France / Milton Bradley (1967) | Grid search + hidden information; Bayesian inference as gameplay |
| ~1400s | Liar's Dice | Unknown (Dudo, Inca Peru) | South America | Bluffing + probability; Nash equilibrium in deception |
| 1947 | Stratego | **Jacques Johan Mogendorff** | Hausemann and Hötte | Hidden-information strategy; imperfect information game; fog of war via concealed piece identities |
| 1948 | Scrabble | **Alfred Mosher Butts** (architect, 1938) & **James Brunot** (manufacturer) | Selchow & Righter | Crossword word placement on bonus-square grid; letter frequency from newspaper analysis; vocabulary as competitive advantage |
| 1955 | Jotto | Unknown | USA | Word deduction game; precursor to Lingo (1987) and Wordle (2021) |
| 1970 | Mastermind | **Mordechai Meirowitz** | Invicta Plastics, Israel | Code-breaking deduction; Knuth's 1977 minimax algorithm solves in 5 guesses |
| 1975 | Whac-A-Mole | **Aaron Fechter** (TOGO's Mogura Taiji also 1975) | Bob's Space Racers / TOGO | Reaction-time targeting; Fitts's Law as gameplay; arcade redemption pioneer |
| 1978 | Simon | **Ralph Baer** & **Howard Morrison** | Milton Bradley | Sequence memory; expanding pattern recall; precursor to rhythm game mechanics |
| 1981 | Mahjong Solitaire | **Brodie Lockard** | Independent (later Activision's Shanghai, 1986) | Layered tile matching from traditional Mahjong tiles; 2.5D spatial puzzle with free-tile constraints; Shanghai (1986) made it mainstream |

---

## Genre Lineage

How the foundational mechanics evolved and branched.

### The Deflection Family
```
Tennis for Two (1958) → Pong (1972) → Breakout (1976) → Arkanoid (1986)
                                    ↘ Air Hockey variants
                                    ↘ Every paddle game since
```
**Core mechanic:** Object bounces between surfaces; player controls angle via position.
**Prototypes:** `DEF-001-pong`, `DEF-002-breakout`, `DEF-003-shufflepuck`

### The Fixed-Position Shooter Family
```
Space Invaders (1978) → Galaxian (1979) → Galaga (1981) → Bullet-hell shmups
                      ↘ Centipede (1981)
                      ↘ Tower defense (2000s)
```
**Core mechanic:** Player holds position (or moves along one axis), eliminates approaching threats.
**Prototypes:** `FIX-001-invaders`, `FIX-003-centipede`, `FIX-004-missile-command`, `FIX-005-bloons`, `FIX-006-kingdomrush`

### The Physics / Inertia Family
```
Spacewar! (1962) → Asteroids (1979) → Gravitar (1982) → Thrust (1986) → Lunar Lander variants
                                     ↘ Every space sim since
Pinball — real tables (1930s+) → Video Pinball (1978) → Pinball Dreams (1992) → accurate physics simulation
       ↘ Digital Illusions (Pinball Dreams) → DICE → Battlefield series
```
**Core mechanic:** Newtonian physics; thrust changes velocity, not position directly.
**Pinball branch:** Real-time physics simulation; flipper control + ball dynamics; Digital Illusions proved accurate physics sells.
**Prototypes:** `PHY-001-asteroids`, `PHY-003-lunar-lander`, `PHY-004-marble-madness`, `PHY-005-pinball`, `PHY-006-worms`, `PHY-007-sandbox`

### The Maze / Chase Family
```
Pac-Man (1980) → Ms. Pac-Man (1982) → Lock 'n' Chase → Pac-Land → ...
               ↘ Stealth game ancestors
               ↘ Every pursuit/evasion game
Lock 'n' Chase (1981) → door-placement mechanic → real-time environment manipulation
                      ↘ Terrain-denial strategy → Splatoon (2015, territory painting)
Frogger (1981) → grid-based traversal → rhythm-pattern recognition
Dig Dug (1982) → tunnel creation as weapon → Mr. Driller (1999)
Night Stalker (1982) → arena predator/prey with weapon scarcity → Resident Evil (1996)
                     ↘ Resource-limited survival horror DNA
Tron (1982) → light cycle trails → Snake (1997) → Slither.io (2016)
           ↘ Territory denial via movement history
```
**Core mechanic:** Navigate maze, collect items, avoid or reverse-hunt pursuers.
**Lock 'n' Chase branch:** Data East added real-time environment manipulation (closing doors behind you) — the first game where the player changes the maze topology during play.
**Night Stalker branch:** Mattel's invisible-stalker arena with limited ammunition — survival horror DNA 14 years before Resident Evil.
**Tron variant:** Trail-based territory denial — your path becomes walls; spatial memory as weapon.
**Snake variant:** Nokia Snake (1998) perfected the trail-growth mechanic — your own growing body becomes the obstacle. The self-avoiding walk problem is NP-complete.
**Prototypes:** `MAZ-001-pacman`, `MAZ-002-frogger`, `MAZ-003-pengo`, `MAZ-004-dig-dug`, `MAZ-005-tron`, `MAZ-006-night-stalker`, `MAZ-007-lock-n-chase`, `MAZ-008-capturetheflag`, `MAZ-009-snake`

### The Scrolling Shooter / Shmup Family
```
Vanguard (1981) → multi-directional firing lineage
Defender (1981) → Scramble (1981) → Gradius (1985) → R-Type (1987) → Ikaruga (2001)
               ↘ Side-scrolling action games
Zaxxon (1982) → isometric scrolling branch → Desert Strike (1992)
1942 (1984) → 1943 → 19XX → vertical WWII shooter series (Capcom)
Contra (1987) → run-and-gun lineage → Metal Slug (1996) → Cuphead (2017)
             ↘ 8-directional shooting + cooperative action
Wing Commander (1990) → space combat sim → Star Fox (1993) → Freelancer (2003)
                      ↘ AI wingmen with personality-driven behavior trees
```
**Core mechanic:** Continuous scrolling; player moves freely within scrolling frame; partial observability.
**Contra branch:** Side-scrolling run-and-gun with 8-directional shooting; defined cooperative action gaming.
**Wing Commander branch:** Chris Roberts added AI wingmen with behavior trees and cinematic narrative between missions; pioneered the space combat sim.
**Bullet hell branch:** Touhou Project (1996+) by ZUN specialized the shmup into danmaku — dense, beautiful bullet patterns with tiny hitboxes. The genre proves that beautiful difficulty creates its own appeal.
**Prototypes:** `SCR-001-defender`, `SCR-002-scramble`, `SCR-003-thexder`, `SCR-004-ikari`, `SCR-005-1942`, `SCR-006-zaxxon`, `SCR-007-vanguard`, `SCR-008-wing-commander`, `SCR-009-contra`, `SCR-010-bullethell`

### The Platformer Family
```
Donkey Kong (1981) → Mario Bros. (1983) → Super Mario Bros. (1985) → Sonic (1991) → ...
                   ↘ Metroidvania
                   ↘ Roguelike platformers (Spelunky)
Pitfall! (1982) → side-scrolling exploration → Adventure Island (1986) → open-world platformers
               ↘ First horizontally-scrolling platformer with environment variety
               ↘ David Crane's LFSR procedural generation → roguelike DNA
Bubble Bobble (1986) → Puzzle Bobble/Bust-a-Move (1994) → trap-platformer lineage
Kid Icarus (1986) → vertical scrolling platformer + RPG progression → genre fusion
                  ↘ Shared engine with Metroid (Nintendo R&D1)
Karateka (1984) → Prince of Persia (1989) → cinematic platformer lineage
                                            ↘ Flashback (1992) → Another World
                                            ↘ Tomb Raider (1996)
```
**Core mechanic:** Gravity + jump; traverse platforms; avoid/defeat enemies.
**Pitfall! branch:** David Crane created the first platformer with horizontal scrolling and diverse environments (swamps, underground, vines). Used LFSR for procedural screen generation — 256 screens from a trivial algorithm.
**Kid Icarus branch:** Toru Osawa fused vertical platforming with RPG progression; shared the same engine with Metroid.
**Cinematic branch:** Rotoscoped animation trades precise control for fluid motion; Jordan Mechner created both Karateka and Prince of Persia before age 25.
**Gravity-flip branch:** VVVVVV (2010) by Terry Cavanagh reduced the platformer to its essence: move and flip gravity. No jump variance, no power-ups — pure level design and timing.
**Prototypes:** `PLT-001-runner`, `PLT-002-lode-runner`, `PLT-003-castlevania`, `PLT-004-metroid`, `PLT-005-donkey-kong`, `PLT-006-bubble-bobble`, `PLT-007-prince-of-persia`, `PLT-008-pitfall`, `PLT-009-kid-icarus`, `PLT-010-doodlejump`, `PLT-011-gravity`

### The Puzzle / Falling Block Family
```
Q*bert (1982) → isometric tile-color puzzles → Marble Madness (1984, physics variant)
Tetris (1984) → Dr. Mario (1990) → Columns (1990) → Puyo Puyo (1991) → Lumines (2004)
             ↘ Match-3 (Bejeweled)
             ↘ Every block-placement puzzle
Lemmings (1991) → agent-programming puzzles → Pikmin (2001) → indirect control lineage
               ↘ Autonomous agents with player-assigned behaviors
```
**Core mechanic:** Pieces descend (Tetris branch) or tiles transform (Q*bert branch); arrange/navigate under time pressure.
**Lemmings branch:** David Jones created autonomous walkers the player modifies by assigning behaviors (dig, build, block) — indirect agent programming as puzzle mechanic.
**Minesweeper branch:** Minesweeper (1990) is NP-complete constraint satisfaction — each number is a local constraint, solving requires Boolean inference.
**Sokoban branch:** Sokoban (1981) is PSPACE-complete push-block planning. Deadlock detection is itself a hard problem.
**Pipe Dream branch:** Pipe Mania (1989) is online stochastic graph construction — build paths before knowing future pieces.
**Match-3 branch:** Bejeweled (2001) popularized cascade matching — swap-to-match with gravity creates emergent chain reactions.
**Nonogram branch:** Picross/Nonogram (1987) is picture logic via constraint propagation — row/column clue systems.
**Prototypes:** `PUZ-001-tetris`, `PUZ-002-columns`, `PUZ-003-incredible-machine`, `PUZ-004-qbert`, `PUZ-005-lemmings`, `PUZ-006-cuttherope`, `PUZ-007-scrabble`, `PUZ-008-minesweeper`, `PUZ-009-sokoban`, `PUZ-010-pipedream`, `PUZ-011-match3`, `PUZ-012-nonogram`

### The Trap / Terrain Family
```
Qix (1981) → Volfied (1989) → Jezzball (1992) → territory.io (2018)
           ↘ Area-control strategy
```
**Core mechanic:** Claim territory under threat; risk increases with claim size.
**JezzBall branch:** JezzBall (1992) simplified Qix's freeform lines into axis-aligned walls — accessible spatial reasoning that preserves the territory-capture tension.
**Prototypes:** `TRP-001-qix`, `TRP-003-jezzball`

### The Fighting / Combat Family
```
Joust (1982) ──→ Platform fighters (Smash Bros.)
                ↘ Flap-to-fly combat lineage
Kung-Fu Master (1984) → Double Dragon (1987) → Streets of Rage (1991) → ...
                      ↘ First side-scrolling beat-em-up
                      ↘ Nishiyama → Street Fighter (1987) → SF2 (1991)
Karateka (1984) ──→ cinematic combat (stance-switching, dramatic pacing)
                  ↘ Prince of Persia (1989) (same creator: Jordan Mechner)
Rampage (1986) ──→ destruction-as-gameplay; player IS the monster
               ↘ Kaiju genre → Godzilla games → disaster sims
Mortal Kombat (1992) ──→ digitized actors + finishing moves
                     ↘ Input-reading AI difficulty scaling
                     ↘ Gore controversy → ESRB rating system (1994)
```
**Core mechanic:** Direct combat; spatial positioning determines advantage.
**Six combat paradigms:** Flap combat (Joust), side-scroll beat-em-up (Kung-Fu Master), cinematic stance (Karateka), competitive fighting (Street Fighter), cooperative destruction (Rampage), digitized martial arts (Mortal Kombat).
**Prototypes:** `FGT-001-joust`, `FGT-002-kung-fu`, `FGT-003-rampage`, `FGT-004-karateka`, `FGT-005-mortal-kombat`, `FGT-006-teeworlds`

### The Racing Family
```
Night Driver (1976) → Pole Position (1982) → Out Run (1986) → Ridge Racer (1993) → ...
                                            ↘ Branching-path (Out Run)
                                            ↘ Kart racers (1992)
                                            ↘ Open-world racing
Bump 'n' Jump (1982) → vehicular combat racer → Road Rash (1991) → Twisted Metal (1995)
                     ↘ Altitude mechanic: jumping OVER obstacles changes the game plane
```
**Core mechanic:** Perspective road; speed/steering tradeoff; competitive time.
**Out Run innovation:** Yu Suzuki added player-selected routes at forks — the racer as journey, not just competition.
**Bump 'n' Jump innovation:** Data East added vertical jumping to a racer — altitude as evasion mechanic, creating a 2.5D gameplay plane.
**Prototypes:** `RAC-001-racer`, `RAC-002-outrun`, `RAC-003-bump-n-jump`, `RAC-004-kart`

### The Twin-Stick / Arena Shooter Family
```
Robotron (1982) → Smash TV (1990) → Geometry Wars (2003) → Binding of Isaac (2011) → Vampire Survivors (2022)
               ↘ Roguelite arena games
Doom (1993) → Quake (1996) → Half-Life (1998) → Halo (2001) → ...
           ↘ BSP tree spatial partitioning
           ↘ Networked deathmatch → multiplayer FPS genre
           ↘ Mod community → user-generated content revolution
```
**Core mechanic:** Move and shoot independently; overwhelming enemy waves; survival.
**Doom/FPS branch:** Carmack's raycasting engine and BSP trees created the first-person shooter genre; networked play invented competitive multiplayer.
**Prototypes:** `SHT-001-robotron`, `SHT-002-berzerk`, `SHT-003-biplanes`, `SHT-004-doom`, `SHT-005-royale`, `SHT-006-tactical`

### The Service / Dispatch Family
```
Tapper (1983) ──── Root Beer Tapper (1984, Bally Midway Sega port)
               ↘ Diner Dash (2004)
                    ↘ Wedding Dash (2007)
                    ↘ Good Pizza Great Pizza (2014)
                    ↘ Overcooked (2016)
                         ↘ Plate Up! (2022)
```
**Core mechanic:** Multi-lane dispatch with return acknowledgement. Player allocates service tokens across simultaneous queues under deadline pressure. Position switching has friction. Loss on deadline miss or token wastage.
**Origin:** Tapper (1983) by Larry Demar & Steve Ritchie. Mechanically a real-time game of Erlang queueing theory; CPU task scheduling as entertainment.
**AI lineage:** Erlang M/M/N queueing (1909) → Operations Research scheduling (1940s) → CPU EDF/SJF algorithms (1960s) → Expert system queue priority (1976) → Tapper (1983) → RL multi-queue environments (2000s)
**Kitchen branch:** Overcooked (2016) turned cooking into real-time job-shop scheduling — multi-step recipes, station management, and order priority under time pressure.
**Prototypes:** `SRV-001-tapper`, `SRV-003-burgertime`, `SRV-004-paperboy`, `SRV-005-kitchen`, `SRV-002-smartbar` (ai-archaeology), `SRV-003-flowbar` (ai-evolution)

### The Ancient Games Family
```
Royal Game of Ur (~2600 BCE) → Backgammon (~3000 BCE) → Modern board games
Mancala (~700 CE) → Oware, Kalah, Bao
Stratego (1947) → Battleship (1967) → Hidden-information strategy
Chess (~600 CE) → Computer Chess (1950s) → Battle Chess (1988) → AI chess era
```
**Core mechanic:** Abstract strategy; perfect/imperfect information; territory/capture/calculation.
**Battle Chess note:** Same rules, animated captures. Proved presentation transforms engagement without altering mechanics.
**Solitaire branch:** Klondike Solitaire (1990, bundled with Windows 3.0) taught millions drag-and-drop; became the most-played computer game in history.
**Mahjong branch:** Mahjong Solitaire (1981/1986 Shanghai) creates a 2.5D spatial puzzle from 2D matching — layered tiles with free-tile constraints.
**Prototypes:** `ANC-001-ur`, `ANC-002-mancala`, `ANC-003-stratego`, `ANC-004-chess`, `ANC-005-solitaire`, `ANC-006-mahjong`

### The Adventure Family
```
Colossal Cave (1976) → Zork (1977) → King's Quest (1984) → Zelda (1986) → ...
                      ↘ Text adventures (Infocom)
                      ↘ Point-and-click:
                           Maniac Mansion (1987, SCUMM engine) → Monkey Island → Day of the Tentacle
                      ↘ Action-adventure (Zelda lineage)
Dragon's Lair (1983) → laserdisc interactive cinema → FMV games (1990s) → QTE sequences (God of War, RE4)
                     ↘ Don Bluth animation quality → proved premium visual fidelity sells
Carmen Sandiego (1985) → educational adventure → geography-meets-deduction
                       ↘ Constraint satisfaction as gameplay
                       ↘ Encyclopedic knowledge → search engine precursor
Oregon Trail (1971/1985) → survival simulation → educational gaming lineage
                         ↘ Resource management under uncertainty (Monte Carlo-like risk)
                         ↘ Don Rawitsch's classroom tool became cultural touchstone
```
**Core mechanic:** Explore rooms, solve puzzles, manage inventory; progression through discovery.
**Dragon's Lair branch:** Interactive cinema — player watches animated narrative, responds with timed inputs. Rick Dyer (hardware/concept) + Don Bluth (animation) created a new medium.
**Maniac Mansion branch:** Ron Gilbert's SCUMM engine invented the verb-based natural language interface for puzzles — the grammar that became prompt engineering 36 years later.
**Carmen Sandiego branch:** Brøderbund's detective-adventure used constraint satisfaction (cross-referencing clues against an encyclopedia) as core gameplay — procedural mystery generation decades before AI-generated quests.
**Oregon Trail branch:** Classroom simulation that taught resource management under uncertainty; probabilistic event systems (disease, weather, river crossings) function as Monte Carlo risk modeling.
**Stealth branch:** Metal Gear (1987) inverted the action game — success means NOT fighting. Guard vision cones, patrol FSMs, and stealth detection create a perception-exploitation puzzle.
**Prototypes:** `ADV-001-zork`, `ADV-002-kings-quest`, `ADV-003-zelda`, `ADV-004-dragons-lair`, `ADV-005-maniac-mansion`, `ADV-006-carmen-sandiego`, `ADV-007-stealth`

### The Role-Playing Family
```
Wizardry (1981) → Bard's Tale (1985) → Final Fantasy (1987) → ...
                ↘ Ultima (1981) → Ultima IV (1985, ethical virtues) → Elder Scrolls
Hydlide (1984) → Ys (1987) → Action RPG lineage → Diablo (1996)
Gauntlet (1985) → cooperative dungeon crawl → 4-player role specialization
               ↘ Diablo (1996) (multiplayer loot lineage)
Wasteland (1988) → Fallout (1997) → post-apocalyptic RPG with moral consequence
                 ↘ Party-based skill RPG lineage
Dungeon Master (1987) → Eye of the Beholder (1991) → first-person dungeon RPG lineage
                      ↘ Real-time grid movement + party management under pressure
NetHack (1987) → community roguelike evolution → Spelunky (2008) → Hades (2020)
              ↘ Vast item interaction matrix; combinatorial emergence
              ↘ "The DevTeam thinks of everything" = exhaustive edge-case AI
```
**Core mechanic:** Character progression through stats, combat, and exploration.
**Ultima IV innovation:** Richard Garriott replaced kill-count scoring with ethical virtue tracking — the game judges HOW you play, not how much you kill. Invented alignment-through-behavior 35 years before RLHF.
**Gauntlet innovation:** Ed Logg (Asteroids, Centipede) created the first 4-player cooperative game with role-differentiated classes.
**Dungeon Master innovation:** FTL Games created real-time first-person dungeon crawling with survival mechanics (hunger/thirst) — the template for Dark Souls' tension design.
**NetHack innovation:** Community-evolved complexity with emergent item interactions; procedural generation + permadeath + combinatorial depth = the purest roguelike.
**Prototypes:** `RPG-001-bards-tale`, `RPG-002-ys`, `RPG-003-gauntlet`, `RPG-004-ultima`, `RPG-005-wasteland`, `RPG-006-nethack`, `RPG-007-dungeon-master`, `RPG-008-diablo`

### The Sports Family
```
Tennis for Two (1958) → Pong (1972) → Track & Field (1983) → Summer Games (1984)
                                    ↘ Golf games → Mini Golf
                                    ↘ Skateboard/extreme (Skate or Die, 1987)
                                    ↘ Winter/skiing (Slalom, 1987)
SkiFree (1991) → infinite runner precursor → Temple Run (2011) → Subway Surfers (2012)
              ↘ Procedural obstacle generation with chase agent
              ↘ The Abominable Snow Monster: gaming's most infamous emergent villain
```
**Core mechanic:** Athletic mechanics translated to digital form; physics-based competition.
**SkiFree branch:** Chris Pirih's deceptively simple downhill game pioneered procedural obstacle generation and the chase-agent mechanic that became the infinite runner genre.
**Punch-Out branch:** Punch-Out!! (1984) disguised puzzle games as boxing — each opponent is a finite state machine with telegraphed patterns. Players perform real-time pattern recognition.
**Rhythm branch:** DDR (1998) proved games could be athletic; Guitar Hero (2005) went mainstream. Pure temporal precision — input timing IS the game.
**Prototypes:** `SPT-001-minigolf`, `SPT-002-summer-games`, `SPT-003-skateboard`, `SPT-004-slalom`, `SPT-005-skifree`, `SPT-006-carsoccer`, `SPT-007-punchout`, `SPT-008-rhythm`

### The Simulation / Trading Family
```
Lemonade Stand (1979) → Taipan! (1982) → Elite (1984) → Civilization (1991)
                       ↘ Tycoon games (1990s)
                       ↘ 4X strategy
Utopia (1981) → SimCity (1989) → god game / city builder lineage
             ↘ First real-time strategy game; split-screen competitive resource management
             ↘ Don Daglow: designed for Mattel Intellivision
Oregon Trail (1971/1985) → survival sim → educational gaming phenomenon
                         ↘ Resource management + probabilistic events (Monte Carlo-like)
Populous (1989) → Black & White (2001) → god game lineage
               ↘ Peter Molyneux: indirect control via terraforming
               ↘ Autonomous agents respond to environment, not direct commands
Civilization (1991) → Alpha Centauri (1999) → Civ II–VI → 4X genre canon
                    ↘ Multi-objective AI opponents
                    ↘ Tech tree as progression structure
```
**Core mechanic:** Economy, trading, resource management; optimize under uncertainty.
**Utopia innovation:** Don Daglow created the first real-time strategy game on the Intellivision — split-screen competitive civilization-building, 8 years before SimCity.
**Oregon Trail innovation:** Classroom survival simulation with probabilistic event systems; resource management under uncertainty.
**Populous innovation:** Peter Molyneux invented the god game — indirect control via terraforming, where autonomous agents respond to environmental changes rather than direct commands.
**Civilization innovation:** Sid Meier's 4X masterwork with multi-objective AI opponents; the tech tree became a universal progression structure across genres.
**Farming branch:** Harvest Moon (1996) created the farming sim — plant/tend/harvest/sell/upgrade is a perfect economic feedback loop. Stardew Valley (2016) proved one developer could build a cultural phenomenon with it.
**Idle branch:** Cookie Clicker (2013) stripped all traditional game design to expose pure progress psychology — exponential growth with diminishing returns is the multi-armed bandit problem as entertainment.
**Prototypes:** `SIM-001-taipan`, `SIM-002-utopia`, `SIM-003-oregon-trail`, `SIM-004-civilization`, `SIM-005-populous`, `SIM-006-clashroyale`, `SIM-007-clashofclans`, `SIM-008-tactics`, `SIM-009-farmstead`, `SIM-010-idle`

### The Hybrid / Genre-Fusion Family
```
Archon (1983) → chess board + real-time arena combat hybrid
             ↘ Proved incompatible interaction models can fuse
             ↘ Ogre Battle (1993) → strategy/RPG hybrid lineage
             ↘ Auto-battler (2019) — strategic positioning + autonomous combat
```
**Core mechanic:** Two incompatible gameplay modes fused into one coherent system. Strategic layer (board/turn-based) determines context; tactical layer (real-time/action) resolves outcomes.
**Key insight:** Jon Freeman & Anne Westfall at Free Fall Associates created the first game that required the player to be good at two completely different kinds of thinking simultaneously — a proto-multimodal cognitive demand.
**Deck-building branch:** Slay the Spire (2017) fused roguelikes with deck-building — each card addition is both a capability and a dilution risk. Online policy gradient optimization through play.
**Auto-battler branch:** Auto Chess (2019) separated strategy from execution — design a system, watch it fight. This IS the AI alignment challenge: specifying objectives rather than actions.
**Prototypes:** `HYB-001-archon`, `HYB-002-deckbuilder`, `HYB-003-autobattler`

### The Physics Playground Family
```
Marble Madness (1984) → Super Monkey Ball (2001) → physics sandbox lineage
                      ↘ Trackball-controlled rolling with learned-feeling gravity
                      ↘ Mark Cerny (age 18) → PS4/PS5 system architect
```
**Core mechanic:** Physics-driven navigation where the world's physical properties ARE the challenge. Player learns an implicit physics model through play.
**Prototypes:** `PHY-004-marble-madness`

---

## AI Convergence Timeline

Where the game timeline and the AI timeline touched — 33 key moments.
(See also [ADR-004](ADR-004-ai-archaeology-layer.md) Part III for the full convergence map with theme analysis.)

| # | Year | Game Event | AI Event | Relationship |
|---|------|-----------|----------|-------------|
| 1 | 1944 | — | von Neumann's *Theory of Games* | Game theory becomes AI foundation |
| 2 | 1950 | — | Shannon's chess-playing paper | Games define what "intelligence" means |
| 3 | 1952 | — | Samuel's checkers program (self-play) | Self-play invented via games |
| 4 | 1962 | Spacewar! on PDP-1 | AI research on same hardware | Same buildings, different questions |
| 5 | 1972 | Pong ships | MYCIN expert system | Specialization works — both prove it |
| 6 | 1980 | Pac-Man's ghost AI | Multi-agent systems nascent | Games solve multi-agent intuitively |
| 7 | 1980 | Rogue (procedural generation) | — | Games invent generation 34 years before GANs |
| 8 | 1985 | Tetris | — | Combinatorial optimization as entertainment |
| 9 | 1992 | SF2 combo discovery | TD-Gammon (self-play RL) | Players and networks both do unsupervised search |
| 10 | 1997 | — | Deep Blue beats Kasparov | AI conquers its original benchmark |
| 11 | 2005 | F.E.A.R. GOAP system | — | Game AI leads academic AI in real-time planning |
| 12 | 2013 | — | DQN plays Atari from pixels | AI uses our prototype lineages as benchmarks |
| 13 | 2016 | — | AlphaGo Move 37 | AI shows humans their game is deeper than they knew |
| 14 | 2021 | — | GitHub Copilot | AI writes game code |
| 15 | 2026 | This laboratory | Claude/GPT agents | Human-AI dyad creates games together |
| 16 | 1909/1983 | Tapper (Bally Midway) | Erlang M/M/N Queueing Theory | Tapper's 4-lane beer dispatch is mathematically identical to telephone exchange operator scheduling (Erlang 1909) and CPU task dispatch (Dijkstra/Knuth 1960s–70s). Three independent formalizations of the same problem across 74 years. Nobody connected them at the time. |
| 17 | 1976/1983 | Tapper hidden information | MYCIN Expert Systems | MYCIN (1976, Stanford) encoded rule-based medical urgency ranking. The same architecture applied to Tapper would produce a real-time queue priority overlay. Expert systems of 1983 had complete capability to build SRV-002 SmartBar. The experiment: what would Tapper have been if a Bally Midway engineer had called a Stanford AI Lab consultant? |
| 18 | 2024/1983 | Demand elasticity (Flow Bar) | Recommendation engine engagement loops | TikTok For You Page and SRV-003 FlowBar are the same algorithm: measure user performance → adjust content delivery rate → maximize time-in-session. Same architecture, different ethics. |
| 19 | 1985/2020 | Ultima IV virtue system | RLHF / Constitutional AI | Richard Garriott built a game that judges players by ethical behavior, not kill count. Replaced "maximize score" with "demonstrate virtue." This IS reward shaping through human feedback — formalized as RLHF 35 years later by Christiano et al. (2017) and deployed as Constitutional AI by Anthropic (2022). |
| 20 | 1987/2023 | Maniac Mansion SCUMM verbs | Prompt engineering / LLM UX | Ron Gilbert's verb interface ("Open door", "Give tentacle the manuscript") required players to compose natural language commands from a constrained vocabulary to manipulate a world model. This is prompt engineering. The grammar games invented in 1987 became the dominant human-AI interaction paradigm in 2023. |
| 21 | 1983/2023 | Archon board+arena hybrid | Multimodal AI systems | Jon Freeman & Anne Westfall fused chess-like strategy with real-time arena combat — two incompatible cognitive modes in one game. This is multimodal intelligence: the system that must reason symbolically AND react in real-time simultaneously. GPT-4V (2023) faces the same integration problem. |
| 22 | 1985/2024 | Gauntlet 4-player roles | Multi-agent role specialization | Ed Logg created four agents (warrior/valkyrie/wizard/elf) with differentiated capabilities cooperating in real-time. Each "agent" has a different action space optimized for different subtasks. This is the multi-agent specialization architecture that CrewAI and AutoGen formalized in 2024. |
| 23 | 1983/2024 | Dragon's Lair interactive cinema | Generative video / Sora | Rick Dyer and Don Bluth created interactive animated cinema where player choices branch a visual narrative in real-time. This is exactly what Sora (2024) and generative video aim to produce: responsive cinematic content shaped by input. Dragon's Lair solved the UX problem 41 years before the generation problem was solved. |
| 24 | 1989/2023 | Prince of Persia rotoscoping | Neural motion synthesis | Jordan Mechner filmed his brother running and fighting, then traced those frames into game animation. This is motion capture → synthesis, the same pipeline that physics-based character animation and neural motion synthesis use today. The human body as training data — 34 years before learned locomotion became standard. |
| 25 | 1984/2023 | Marble Madness physics | Learned physics models / world models | Mark Cerny (age 18) built a game where the player must learn an implicit physics model through play — gravity, momentum, friction, surface response. This is exactly what world models (Ha & Schmidhuber 2018, Dreamer 2020) attempt: learn a physics simulator from interaction. The game IS the learned world model, taught to humans instead of networks. |
| 76 | 1982/2014 | Pitfall! LFSR generation | Procedural content generation | David Crane used a linear feedback shift register to generate 256 unique screens from a trivial seed algorithm. This IS procedural content generation — deterministic infinite worlds from minimal data. The same principle underlies Minecraft's world seeds (2009) and modern PCG research. |
| 27 | 1971/2020 | Oregon Trail risk modeling | Monte Carlo simulation | Don Rawitsch's classroom game models probabilistic survival events (disease, weather, river crossings) that function as Monte Carlo risk simulation. Players intuitively learn expected value and risk management. The same stochastic modeling underlies modern ML training pipelines. |
| 28 | 1985/2023 | Carmen Sandiego deduction | Constraint satisfaction / search | Broderbund's detective game requires cross-referencing clues against an encyclopedia to narrow suspect location — this IS constraint satisfaction problem (CSP) solving. The game teaches backtracking search strategy 38 years before LLM-based reasoning chains. |
| 29 | 1991/2024 | Lemmings agent behaviors | Agent programming / behavior modification | David Jones created autonomous walkers that the player modifies by assigning behaviors (dig, build, block). This IS agent programming — composing capabilities onto autonomous entities. The same pattern drives LangChain tool-use and function-calling agents in 2024. |
| 30 | 1991/2024 | Civilization multi-objective AI | Multi-objective optimization | Sid Meier's AI opponents must simultaneously optimize military, economic, scientific, and diplomatic objectives — true multi-objective optimization. Modern MORL (multi-objective reinforcement learning) formalizes what Civilization's AI did intuitively. |
| 31 | 1993/2020 | Doom BSP spatial reasoning | Spatial AI / neural scene representation | Carmack's BSP tree partitions 3D space for efficient rendering and collision — spatial data structures that neural implicit representations (NeRF, 2020) now learn automatically. Same problem: represent 3D space efficiently for real-time queries. |
| 32 | 1989/2024 | Populous indirect control | Emergent agent environments | Peter Molyneux's god game controls outcomes by modifying the environment, not commanding agents directly. This IS the emergent agent paradigm — set conditions, let agents self-organize. Same architecture as modern multi-agent simulations (Generative Agents, Stanford 2023). |
| 33 | 1987/2023 | NetHack combinatorial emergence | Emergent complexity from simple rules | The NetHack Dev Team built a system where simple item properties combine to produce emergent behaviors ("dip scroll in fountain" type interactions). This IS combinatorial emergence — the same principle that makes LLM tool-use unpredictably powerful when tools compose. |

---

## Game-First AI Discoveries

Concepts that games invented intuitively, years or decades before AI formalized them.
The average gap between game intuition and AI formalization: **~35 years.**

| # | Game | Year | Creator(s) | Discovered Concept | AI Formalized (~Year) | Gap |
|---|------|------|-----------|-------------------|----------------------|-----|
| 1 | Space Invaders | 1978 | Nishikado | Emergent curriculum learning (speedup bug) | Curriculum Learning (~2015) | 37yr |
| 2 | Asteroids | 1979 | Logg & Rains | Exploration-exploitation in continuous state space | RL formalization (~1990s) | ~15yr |
| 3 | Pac-Man | 1980 | Iwatani | Multi-agent behavioral policies (ghost personalities) | MARL theory (~2000) | 20yr |
| 4 | Rogue | 1980 | Toy, Wichman, Arnold | Procedural content generation | GANs / PCG formalized (~2014) | 34yr |
| 5 | Defender | 1981 | Jarvis & DeMar | Partial observability + dimensionality reduction (minimap) | POMDPs (~1990s) | ~12yr |
| 6 | Qix | 1981 | Pfeiffer & Pfeiffer | Territorial control as multi-armed bandit | Spatial bandit theory (~1985+) | ~4yr |
| 7 | Zaxxon | 1982 | Ikegami Tsushinki/Sega | Isometric perspective with implicit depth | 3D scene understanding / NeRF (~2020) | 38yr |
| 8 | Archon | 1983 | Freeman & Westfall | Multi-modal gameplay (strategic + reactive) | Multi-modal AI systems (~2023) | 40yr |
| 9 | Dragon's Lair | 1983 | Dyer & Bluth | Interactive animated narrative (laserdisc) | Generative video / Sora (~2024) | 41yr |
| 10 | Kung-Fu Master | 1984 | Nishiyama | Side-scrolling hierarchical progression | Hierarchical task networks (~2000s) | ~18yr |
| 11 | Karateka | 1984 | Mechner | Cinematic pacing in real-time combat | Temporal attention mechanisms (~2017) | 33yr |
| 12 | Marble Madness | 1984 | Cerny | Physics-based learned control | World models / learned physics (~2023) | 39yr |
| 13 | Tetris | 1984 | Pajitnov | Real-time NP-hard heuristic spatial reasoning | Active research (ongoing) | 40yr+ |
| 14 | Gauntlet | 1985 | Logg | Cooperative multi-agent role specialization | Multi-agent RL specialization (~2024) | 39yr |
| 15 | Ultima IV | 1985 | Garriott | Ethical constraint system as game mechanic | RLHF / Constitutional AI (~2020) | 35yr |
| 16 | Super Mario Bros. | 1985 | Miyamoto & Tezuka | Reward shaping via level design | Reward shaping in RL (~1999) | 14yr |
| 17 | Maniac Mansion | 1987 | Gilbert & Winnick | Natural language verb interface for world interaction | Prompt engineering / LLM UX (~2023) | 36yr |
| 18 | Prince of Persia | 1989 | Mechner | Rotoscoped human motion capture → animation | Neural motion synthesis (~2023) | 34yr |
| 19 | Lock 'n' Chase | 1981 | Data East | Real-time maze topology modification (door placement) | Dynamic environment manipulation (~2015) | 34yr |
| 20 | Night Stalker | 1982 | Mattel | Arena predator/prey with weapon scarcity | Resource-limited survival AI (~1996) | 14yr |
| 21 | Pitfall! | 1982 | Crane | LFSR procedural world generation (256 screens from seed) | Procedural content generation (~2014) | 32yr |
| 22 | BurgerTime | 1982 | Data East | Multi-lane assembly under pursuit (gravity-driven ingredient stacking) | Assembly-line optimization (~2000s) | ~20yr |
| 23 | Utopia | 1981 | Daglow | Real-time competitive civilization building (split-screen) | Real-time strategy formalization (~1992) | 11yr |
| 24 | Carmen Sandiego | 1985 | Broderbund | Constraint satisfaction detective gameplay (cross-reference clues) | CSP / automated reasoning (~2023) | 38yr |
| 25 | Oregon Trail | 1971 | Rawitsch | Probabilistic survival simulation (stochastic event modeling) | Monte Carlo methods in games (~2006) | 35yr |
| 76 | NetHack | 1987 | Dev Team | Combinatorial item interaction emergence | LLM tool composition (~2023) | 36yr |
| 27 | Populous | 1989 | Molyneux | Indirect control via environment modification | Emergent multi-agent systems (~2023) | 34yr |
| 28 | Lemmings | 1991 | Jones | Agent-programming puzzle (assign behaviors to autonomous walkers) | LLM tool-use agents (~2024) | 33yr |
| 29 | Civilization | 1991 | Meier | Multi-objective AI opponents (military/economic/science/diplomacy) | Multi-objective RL (~2020) | 29yr |
| 30 | Doom | 1993 | Carmack & Romero | BSP tree spatial partitioning for real-time 3D | Neural scene representations / NeRF (~2020) | 27yr |

**Pattern:** Games with the longest gaps (35+ years) tend to involve problems that required
the deep learning revolution to formalize: generative content, multimodal reasoning, motion
synthesis, and value alignment. The designers who solved these problems earliest were working
from pure intuition about what made interactions feel right — and that intuition ran decades
ahead of the mathematical frameworks that would eventually describe what they'd built.

The average gap between game intuition and AI formalization: **~27 years.** The 1982
cluster (Lock 'n' Chase, Night Stalker, Pitfall!, BurgerTime) shows four simultaneous
independent inventions — each solving a different AI problem through game design intuition.

---

## AI Era Definitions

The laboratory maps every prototype to an AI era — the state of artificial
intelligence when the original game was created. This reveals how games were
*already solving* problems that AI hadn't yet formalized.

### Era 0 — Theoretical Foundations (before 1950)
- von Neumann, Shannon, Turing define computation and game theory
- No working AI systems exist yet
- Games as mathematical objects (Game Theory, 1944)

### Era 1 — Search and Symbols (1950–1971)
- Samuel's checkers, Newell-Simon GPS, ELIZA
- AI can search finite trees, match patterns in text
- Cannot see, cannot learn from experience, cannot handle continuous state

### Era 2 — Expert Systems (1972–1977)
- MYCIN, DENDRAL, rule-based reasoning
- Can encode human expertise as if-then rules
- Pong's AI (Y-tracker) IS an expert system — indistinguishable from contemporary AI

### Era 3 — Knowledge Explosion & Neural Revival (1978–1983)
- Hopfield networks, early backpropagation, Connection Machine
- Can classify patterns, search large spaces, play simple games
- Cannot see images, understand speech, or generate anything novel
- **This era produced the most game genres in history**

### Era 4 — Expert Boom & Second Winter (1985–1992)
- TD-Gammon, expert system collapse, subsumption architecture
- Can learn game evaluations through self-play
- Cannot see usefully, create, or generalize across domains

### Era 5 — Statistical Learning (1992–2011)
- Deep Blue, SVMs, Netflix Prize, Watson, ImageNet
- Can beat humans at chess via brute search, classify data
- Cannot see like a toddler or transfer knowledge across domains

### Era 6 — Deep Learning (2012–2022)
- AlexNet, GANs, AlphaGo, Transformers, GPT-2, DALL-E, Copilot
- Can see, read, write, generate, play any Atari game from pixels
- Cannot judge if a game is *fun*, recognize beauty, or make taste decisions

### Era 7 — Generative-Agentic Frontier (2023–Present)
- GPT-4, Claude, Gemini, agent tool use, AI co-creation in workflows
- Can reason about design, generate working prototypes, iterate on feedback
- **Cannot play a game and feel whether it's fun.** Cannot decide what to build by intuition.
- **This laboratory is the first artifact of Era 7 human-AI game co-creation.**

---

## Timeline by Decade

Chronological span of all 460 prototypes, anchored by the original creation date
of the game or concept each prototype reconstructs. Decades with > 10 entries
show the first 10 entries; the total count covers all prototypes.

**~1000 CE** (4 games)
- 1000: anc-014-fanorona — dual-direction capture — move a piece toward enemies to capture
- 1000: anc-018-hnefatafl — asymmetric siege — King + 8 defenders start in center; 16 attackers
- 1000: anc-019-makruk — Thai chess variant — pawns on 3rd rank at start, promote to queen
- 1000: puz-037-penguinland — downward egg navigation — guide a penguin egg downward through ice

**~1040 CE** (1 game)
- 1046: anc-008-go — territory encirclement — place black and white stones on a grid

**~1050 CE** (1 game)
- 1055: plt-016-perestroika — shrinking platforms — jump between lily pads that shrink and sink

**~1070 CE** (1 game)
- 1072: new-041-ostranenie — a platformer that progressively defamiliarizes itself

**~1100 CE** (2 games)
- 1100: anc-011-checkers — jump capture — move diagonally on dark squares; jump over opponent
- 1100: anc-025-checkers-tree — jump capture with search tree — play Checkers while seeing the minimax tree

**~1200 CE** (1 game)
- 1200: anc-012-dominoes — number chain matching — play tiles by matching their pip values

**~1390 CE** (1 game)
- 1392: spt-021-tuho — arrow throwing precision — throw thin arrows into a narrow-necked pot

**~1450 CE** (1 game)
- 1452: new-040-chiaroscuro — position a movable light source to create a gradient zone

**~1470 CE** (2 games)
- 1475: anc-004-chess — chess with animated piece captures against AI opponent
- 1475: anc-007-deepthink — chess with search tree visualization — play chess with minimax overlay

**~1560 CE** (1 game)
- 1569: anc-016-patolli — X-shaped race with bean dice — roll marked beans as dice; race to finish

**~1580 CE** (1 game)
- 1583: new-066-pendulum — grappling pendulum — click to attach to anchor points, swing to goal

**~1640 CE** (3 games)
- 1640: anc-010-backgammon — dice race with blocking — roll dice to move checkers around the board
- 1644: new-116-voronoi — Voronoi cell manipulation — place and drag points to form Voronoi cells
- 1646: new-039-entelechy — nurture hidden-purpose entities by applying elemental forces

**~1650 CE** (1 game)
- 1656: new-038-abyme — recursive self-referencing puzzle — the game contains a miniature version of itself

**~1730 CE** (2 games)
- 1736: new-075-onelineall — one-line path completion — draw one continuous line through all nodes
- 1736: new-128-graphwalk — Eulerian path survival — navigate a visible graph; each edge disappears when crossed

**~1770 CE** (1 game)
- 1770: new-023-dialectic — guide floating idea-shapes into dialectical collisions

**~1800 CE** (4 games)
- 1800: puz-019-tangram — shape fitting — arrange 7 geometric pieces to exactly fill an outline
- 1800: puz-046-tangram-fit — shape fitting with constraint hints
- 1801: new-017-ripple — every action creates propagating waves — time actions for constructive interference
- 1801: new-115-waveinterference — wave platform construction — two wave sources emit circular ripples

**~1810 CE** (1 game)
- 1812: sim-008-tactics — turn-based grid tactics with unit types, terrain bonuses

**~1830 CE** (1 game)
- 1839: new-035-semiotics — interpret context-dependent symbols to navigate grid levels

**~1840 CE** (3 games)
- 1841: spt-011-bowling — lane physics — aim, set power and spin, roll a ball down a lane
- 1844: new-121-harmonograph — coupled oscillator art — two pendulums swing at adjustable frequencies
- 1847: new-132-gradient — gradient descent exploration — navigate a 2D heightmap to the lowest point

**~1850 CE** (1 game)
- 1854: new-125-boolcircuit — digital logic construction — build logic circuits from AND, OR, NOT gates

**~1860 CE** (1 game)
- 1868: new-033-tsundoku — books fall endlessly — stack or read them to harvest knowledge

**~1870 CE** (3 games)
- 1870: anc-006-mahjong — tile matching — remove matching pairs of free tiles from a layered stack
- 1874: puz-018-slidepuzzle — tile permutation — slide numbered tiles in a 4×4 grid with one space
- 1876: spt-013-carrom — disc-flicking precision — flick a striker disc to pocket carrom men

**~1880 CE** (2 games)
- 1883: anc-009-reversi — flanking capture — place discs to outflank opponent's pieces
- 1883: anc-024-reversi-weights — flanking capture with position evaluation

**~1890 CE** (4 games)
- 1896: anc-005-solitaire — card sorting — build four foundation piles by suit (Ace to King)
- 1896: spt-010-darts — precision aiming — aim and throw darts at a scored dartboard
- 1896: sim-011-pareto — civilization builder with Pareto frontier visualization
- 1896: spt-030-darts-accuracy — precision aiming with accuracy heatmap

**1900s** (4 games)
- 1907: spt-014-petanque — precision ball placement — throw metal boules to land closest to jack
- 1909: anc-003-stratego — move hidden-rank pieces, bluff and deduce to capture flag
- 1909: srv-002-smartbar — serve beer with real-time queue priority overlay (M/M/N queueing)
- 1909: new-029-liminal — navigate a building only through its in-between spaces

**1910s** (2 games)
- 1911: new-129-pidcontroller — PID tuning — a ball on a tilting beam; adjust P/I/D gains
- 1913: puz-021-crossword — word clue grid — fill a grid with words from intersecting across/down clues

**1930s** (2 games)
- 1935: new-031-terroir — you ARE a landscape — tilt terrain, direct water, compress soil
- 1936: spt-016-kabaddi — raid and return — one raider enters enemy half, must tag opponents

**1940s** (8 games)
- 1940: anc-002-mancala — seed sowing — pick up seeds from a pit, distribute one-by-one
- 1940: new-118-resonance — resonant destruction — objects have hidden natural frequencies
- 1942: scr-005-1942 — vertical scrolling WWII dogfight with loop roll evasion
- 1942: scr-015-dragonflight — dragon mount vertical shooter
- 1942: scr-017-1942-formations — vertical shooter with formation analysis overlay
- 1947: maz-008-capturetheflag — team-based flag capture in divided arena
- 1948: puz-007-scrabble — crossword-style word placement on premium-square grid against AI
- 1948: new-119-tensegrity — tension network engineering — build structures from rigid struts and elastic cables

**1950s** (10 games)
- 1950: wld-001-search-game — player navigates a maze while A*/BFS/DFS search visualizes in real time
- 1952: new-134-reactiondiffusion — morphogenesis control — two chemicals diffuse and react on a grid
- 1955: puz-017-wordle — letter position deduction — guess 5-letter words with green/yellow/grey feedback
- 1955: new-131-statemachine — FSM programming — design a finite state machine by placing states and transitions
- 1957: sim-020-dicewars — dice territory conquest — Risk-like territory control on a hex grid
- 1957: wld-003-neural-game — Pong where the AI opponent builds a visible neural network
- 1958: def-001-pong — deflect — ball bounces between two paddles, angles change based on hit position
- 1958: puz-020-concentration — card memory matching — flip pairs of face-down cards to find all matches
- 1958: new-024-apophenia — identify real patterns emerging from visual noise before the noise takes over
- 1958: new-028-desire — observe pedestrian desire lines forming on grass, then pave the optimal paths

**1960s** (13 games)
- 1962: anc-013-blackjack — risk management — draw cards to reach 21 without going over
- 1962: phy-001-asteroids — inertia combat — you don't move to a position; you apply thrust and momentum
- 1962: anc-026-blackjack-count — risk management with card counting overlay
- 1962: new-034-bricolage — combine random found objects to solve construction problems
- 1962: new-062-graviton — orbital physics puzzle — place gravity wells to guide a comet
- 1963: new-117-attractor — chaos theory precision — a particle follows a Lorenz attractor
- 1965: puz-026-engare — geometric pattern tracing — place a point on a moving/rotating mechanism
- 1967: hyb-005-battleship — grid search — place ships then fire to find opponent's hidden fleet
- 1967: trp-004-simon — sequence memory — watch a growing sequence of colored light/sound patterns
- 1967: hyb-014-battleship-bayes — grid search with Bayesian inference overlay
- ... and 3 more

**1970s** (45 games)
- 1970: puz-016-mastermind — code-breaking deduction — guess a hidden 4-color code
- 1970: puz-041-mastermind-knuth — code-breaking with minimax (Knuth's algorithm)
- 1970: new-008-catalyst — you cannot touch anything — only change how OTHER objects interact
- 1970: new-011-bloom — cellular automaton strategy — place living cells, guide emergence
- 1970: new-020-accrete — start as one pixel — everything you touch sticks to you, grows your mass
- 1970: new-068-chainblast — chain reaction optimization — click one orb to trigger the largest chain
- 1970: new-098-ecosystem — ecosystem management — three species interact: plants, herbivores, predators
- 1970: new-123-cellularengine — emergence programming — design cellular automaton rules
- 1970: new-135-lifeengineer — emergence engineering — Conway's Game of Life where YOU design the rules
- 1971: sim-003-oregontrail — resource management journey with random events and survival decisions
- ... and 35 more

**1980s** (139 games)
- 1980: adv-002-kings-quest — explore rooms, collect items, solve inventory puzzles
- 1980: fix-004-missile-command — area defense — target cursor-guided explosions to intercept incoming missiles
- 1980: maz-001-pacman — maze chase — collect all dots while avoiding 4 ghosts with distinct AI behaviors
- 1980: maz-006-nightstalker — top-down maze shooter with limited ammo and stealth evasion
- 1980: maz-007-locknchase — collect coins in maze while locking doors behind you to trap pursuers
- 1980: phy-010-katamari — sticky ball rolling — roll a ball that picks up objects; everything sticks
- 1980: plt-005-donkey-kong — climb ladders, dodge barrels, reach the top to rescue
- 1980: rpg-006-nethack — turn-based roguelike with procedural dungeons and permadeath
- 1980: rpg-008-diablo — click-to-move action RPG with procedural dungeons and loot
- 1980: sht-002-berzerk — room-by-room arena — shoot robots, avoid walls, flee Evil Otto
- ... and 129 more

**1990s** (73 games)
- 1990: fix-005-bloons — place fixed towers to pop balloons following a winding path
- 1990: puz-002-columns — match-3 alignment — cycle jewel colors in a falling column
- 1990: puz-032-bakubaku — animal-food matching — falling pairs of animals and food blocks
- 1990: sim-007-clashofclans — base building defense and army deployment
- 1990: spt-015-sepaktakraw — kick volleyball — hit a rattan ball over a net using feet
- 1990: puz-014-probefield — minesweeper with per-cell mine probability fields
- 1990: spt-009-flowstate — rhythm game with flow channel visualization
- 1991: fgt-005-mortalkombat — 1v1 fighting with special moves, combo system, and fatalities
- 1991: phy-006-worms — turn-based artillery with destructible terrain and wind physics
- 1991: plt-011-gravity — gravity flip — instead of jumping, reverse gravity to fall upward
- ... and 63 more

**2000s** (43 games)
- 2000: anc-017-yutnori — stick-throwing race — throw 4 half-round sticks; flat/round sides determine move
- 2000: sht-005-royale — last-standing arena shooter with shrinking safe zone
- 2000: spt-023-paengi — top spinning — spin a top and keep it spinning by whipping it
- 2001: hyb-009-okhlos — mob control — recruit citizens into an angry mob; the mob is the agent
- 2001: maz-015-kururin — rotating stick navigation — guide a constantly rotating stick through corridors
- 2001: maz-024-crazyarcade-blast — water balloon bombing with blast prediction overlay
- 2001: sim-024-dicewars-prob — dice territory with probability visualization
- 2001: new-016-inversion — all rules periodically invert — gravity flips, walls become floors
- 2001: new-063-chromashift — color-matching reflex — you ARE a color; match your color to the environment
- 2002: hyb-008-getoverit — rage climbing — climb a mountain using only a sledgehammer for a cane
- ... and 33 more

**2010s** (15 games)
- 2011: adv-016-replica — found-phone narrative — you unlock a stranger's phone and investigate
- 2012: new-101-lightandshadow — light as constructor — drag a light source; its rays create solid platforms
- 2013: adv-009-papersplease — document inspection — compare passports and permits against ever-changing rules
- 2013: adv-010-adarkroom — genre-revealing narrative — starts as fire-stoking clicker, reveals full RPG
- 2013: plt-023-dungreed — roguelite side-scrolling combat with dashing
- 2013: puz-029-cincopaus — mystery wand roguelike — 5 wands with unknown random abilities per run
- 2013: new-067-dualcontrol — split-brain coordination — two characters on split screen controlled simultaneously
- 2015: sht-008-agario — cell growth arena — eat smaller cells and food pellets to grow and absorb others
- 2016: anc-023-go-territory — territory encirclement with AI territory evaluation overlay
- 2016: new-032-hygge — build a cozy sanctuary by placing items that harmonize
- ... and 5 more

**2020s** (5 games)
- 2020: anc-021-togyzkumalak — mancala with tuzdyk — 2×9 pits with 162 stones and capture hole mechanic
- 2020: new-106-deathloop — strategic death — every death changes the world; death unlocks new paths
- 2021: spt-018-ddakji — paper card slamming — slam your folded paper card onto opponent's card to flip it
- 2021: puz-040-wordle-entropy — letter deduction with information entropy analysis overlay
- 2023: new-113-tesselate — evolving tessellation — place geometric shapes to tile a plane

*402 of 460 games have extractable creation dates. Remaining 58 are AI Evolution experiments
with no direct historical anchor (NEW series, phases 1–8).*

---

## The Laboratory Today

| Track | Count | Purpose |
|-------|-------|---------|
| Base Archetypes | 241 | Reconstruct foundational mechanics across 20 series (~3200 BCE–2020s) |
| AI Archaeology | 76 | Ask "what if AI had participated?" — classic games with AI concept visualization overlays |
| AI Evolution | 143 | How AI would evolve games independently; 141 NEW-series experimental prototypes + 2 others |

**Total playable prototypes:** 460 (across 20 series)

**Series breakdown (all tracks):** ADV(18), ANC(27), DEF(7), FGT(9), FIX(9), HYB(15), MAZ(24), NEW(141), PHY(14), PLT(27), PUZ(51), RAC(5), RPG(11), SCR(18), SHT(11), SIM(26), SPT(31), SRV(6), TRP(6), WLD(4)

### Niche Archetypes Batch (20 games, 2026)

Twenty prototypes from the edges of play — board games, card games, parlor games,
pub games, and folk games spanning 5,000 years of human play. Each represents a
cognitive or motor activity not yet covered by the video game lineage.

| Prototype | Origin | Mechanic |
|-----------|--------|----------|
| anc-008-go | ~2500 BCE China | Territory encirclement (AlphaGo benchmark) |
| anc-009-reversi | 1883 England | Flanking capture (Logistello 1997) |
| anc-010-backgammon | ~3000 BCE Mesopotamia | Dice race with blocking (TD-Gammon 1992) |
| anc-011-checkers | ~3000 BCE | Jump capture (Samuel 1959, first learning AI) |
| anc-012-dominoes | ~1200 CE China | Number end-matching chain |
| anc-013-blackjack | ~1700s France | Risk + probability (Thorp card counting) |
| puz-016-mastermind | 1970 Israel | Code-breaking deduction (Knuth minimax) |
| puz-017-wordle | 2021 USA | Letter position deduction (information entropy) |
| puz-018-slidepuzzle | 1874 USA | Tile permutation (A* search heuristic) |
| puz-019-tangram | ~1800 China | Shape fitting (geometric CSP) |
| puz-020-concentration | ~1700s | Card memory matching (working memory) |
| puz-021-crossword | 1913 USA | Word clue grid (NLP + constraint satisfaction) |
| trp-004-simon | 1978 USA | Sequence memory (LSTM, attention) |
| spt-010-darts | ~1860s England | Precision aiming (explore-exploit) |
| spt-011-bowling | ~3200 BCE Egypt | Lane physics + pin scatter |
| hyb-005-battleship | ~1930s France | Grid search + hidden info (Bayesian inference) |
| hyb-006-liarsdice | ~1400s Peru | Bluffing + probability (Nash equilibrium) |
| def-005-whackamole | 1975 USA | Reaction time targeting (Fitts's Law) |
| sim-013-typeracer | 1987 USA | Motor speed + accuracy (input bandwidth) |
| phy-008-tower | 1983 UK/Ghana | Physics stacking (structural stability) |

### Genre Gap-Filling Batch (20 games, 2026)

Twenty new prototypes targeting specific genre and mechanic gaps identified through systematic archetype analysis:

| Prototype | Genre Gap Filled | Core Mechanic |
|-----------|-----------------|---------------|
| maz-009-snake | Trail growth (Nokia Snake) | Growing body as self-obstacle; self-avoiding walk problem |
| puz-008-minesweeper | Logic deduction | Constraint satisfaction grid; Boolean inference from numeric clues |
| puz-009-sokoban | Push-block puzzle | PSPACE-complete box pushing; undo-based planning |
| puz-010-pipedream | Flow connection | Online graph construction under time pressure |
| puz-011-match3 | Cascade matching | Swap-to-match with gravity cascades and chain multipliers |
| puz-012-nonogram | Picture logic | Row/column constraint propagation revealing hidden pixel art |
| anc-005-solitaire | Card games | Klondike sorting — most-played computer game in history |
| anc-006-mahjong | Tile matching | Layered 2.5D tile pairs with free-tile constraints |
| spt-007-punchout | Pattern boxing | FSM opponents with telegraph states; real-time classification |
| spt-008-rhythm | Rhythm action | Temporal precision — timing IS the entire game |
| sim-009-farmstead | Farming sim | Plant/tend/harvest/sell economic feedback loop |
| sim-010-idle | Idle/incremental | Exponential growth with prestige meta-learning |
| hyb-002-deckbuilder | Deck-building roguelike | Online policy optimization — build strategy while executing it |
| hyb-003-autobattler | Auto-battler | System design separated from execution; AI alignment analogue |
| scr-010-bullethell | Bullet hell (danmaku) | Dense pattern dodging with tiny hitbox; graze system |
| plt-011-gravity | Gravity-flip platformer | Binary state toggle replacing continuous jump arc |
| adv-007-stealth | Stealth infiltration | Vision cones, guard FSMs, perception exploitation |
| srv-005-kitchen | Kitchen service | Real-time job-shop scheduling with multi-step recipes |
| trp-003-jezzball | Territory division | Spatial partitioning of bouncing balls via wall construction |
| phy-007-sandbox | Falling sand simulation | Cellular automata with emergent material interactions |

### AI Archaeology Batch (20 games, 2026)

Twenty new AI archaeology games that take classic prototypes and add AI concept visualization overlays.
Each game is fully playable — press **H** to toggle the AI overlay on/off.

| Prototype | Base Game | AI Concept Visualized |
|-----------|-----------|----------------------|
| maz-010-ghostmind | Pac-Man | Ghost targeting tiles, patrol state, multi-agent decision-making |
| puz-013-blockplanner | Tetris | Heuristic placement scores, optimal move recommendation |
| def-004-trajectron | Breakout | Multi-bounce trajectory prediction, optimal paddle position |
| scr-011-foglifter | Defender | POMDP off-screen threat awareness, predicted enemy paths |
| sht-007-threatmap | Robotron | Per-enemy threat ranking, danger heatmap, escape vectors |
| rpg-009-virtuescope | Ultima IV | 8-virtue radar chart, RLHF alignment as reward shaping |
| anc-007-deepthink | Chess | Minimax search tree, alpha-beta pruning, evaluation heatmap |
| puz-014-probefield | Minesweeper | Per-cell mine probability, constraint propagation visualization |
| maz-011-gapfinder | Frogger | Safe crossing windows, lane timing prediction, ghost landings |
| fgt-007-framereader | Mortal Kombat | Frame data overlay, AI move prediction, pattern matching |
| plt-012-pathsense | Platformer | Danger zones, jump success probability, optimal safe path |
| sim-011-pareto | Civilization | Multi-objective Pareto frontier, projected action positions |
| rac-005-routemind | Out Run | Branching path expected value, decision quality tracking |
| adv-008-explorermap | Zelda | Exploration value per room, curiosity-driven path suggestion |
| puz-015-lemmingbrain | Lemmings | Optimal behavior assignment, per-lemming survival probability |
| scr-012-bullettime | Touhou | Safe corridor prediction, survival probability field |
| hyb-004-cardcounter | Slay the Spire | Draw probabilities, expected value per card, optimal play |
| sim-012-antfarm | Populous | Agent FSM states, need bars, social connections, emergent behavior |
| plt-013-metroidmap | Metroid | Ability-gate analysis, room reachability, backtracking planner |
| spt-009-flowstate | DDR | Adaptive difficulty, flow channel chart, skill-challenge balance |

Each game asks a design question: **does seeing the AI's analysis enhance the experience, or replace the skill?**

### Modern Archetypes (16 games, 2026)

The collection expanded beyond its retro origins to include modern game mechanics that, when stripped to their core loop, prove surprisingly compact. Each replaces multiplayer networking with competent AI opponents:

| Prototype | Inspired By | Core Mechanic |
|-----------|-------------|---------------|
| plt-010-doodlejump | Doodle Jump (2009) | Auto-jump vertical platformer with procedural platform types |
| phy-006-worms | Worms (1995) | Turn-based artillery with destructible pixel terrain and wind |
| puz-006-cuttherope | Cut the Rope (2010) | Rope-cutting physics puzzle with verlet integration |
| spt-006-carsoccer | Rocket League (2015) | Car soccer with boost physics and momentum transfer |
| rac-004-kart | Super Mario Kart (1992) | Kart racing with items, drifting, and rubber-banding AI |
| rpg-008-diablo | Diablo (1997) | Click-to-move action RPG with procedural dungeons and loot |
| sht-005-royale | Fortnite/PUBG (2017) | Battle royale with shrinking zone and 20 AI opponents |
| sht-006-tactical | Call of Duty (2003) | Tactical top-down shooter with cover-seeking enemy AI |
| fgt-006-teeworlds | Teeworlds (2007) | 2D platform combat with grappling hook physics |
| puz-007-scrabble | Scrabble (1948) | Crossword word placement with AI opponent and compact dictionary |
| sim-006-clashroyale | Clash Royale (2016) | Lane-based card battler with elixir economy |
| sim-007-clashofclans | Clash of Clans (2012) | Base building + army deployment with star scoring |
| fix-005-bloons | Bloons TD (2007) | Tower defense with layered balloon popping mechanics |
| fix-006-kingdomrush | Kingdom Rush (2011) | Tower defense with hero unit and barracks blocking |
| maz-008-capturetheflag | CTF (traditional) | Team-based flag capture with AI role assignment |
| sim-008-tactics | Advance Wars (2001) | Turn-based grid tactics with terrain and economy |

### The NEW Series (141 experiments)

AI-first prototypes exploring mechanics with no clear human-history ancestor.

**Phase 1 — Novel Mechanics (21 games):** Thread (weaving), Echo (temporal), Pulse (rhythm), Fold (origami), Swarm (flocking), Decay (entropy), Signal (communication), Catalyst (chain reaction), Negative (absence), Tether (connection), Bloom (growth), Shadow (darkness), Drift (momentum), Fractal (self-similarity), Membrane (permeability), Inversion (reversal), Ripple (propagation), Symbiont (mutualism), Spectrum (frequency), Accrete (accumulation), Mycelium (network).

**Phase 2 — Interdisciplinary Humanities (20 games):** Kintsugi (Japanese golden repair), Dialectic (Hegelian philosophy), Apophenia (cognitive bias), Saudade (Portuguese longing), Ubuntu (African communitarian ethics), Palimpsest (manuscript history), Desire (urban planning), Liminal (anthropological thresholds), Ikigai (Japanese purpose), Terroir (French viticulture), Hygge (Danish coziness), Tsundoku (Japanese bibliophilia), Bricolage (Lévi-Strauss anthropology), Semiotics (sign theory), Heterotopia (Foucault), Rhizome (Deleuze & Guattari), Abyme (recursive art), Entelechy (Aristotelian teleology), Chiaroscuro (Renaissance art), Ostranenie (Russian defamiliarization).

**Phase 3 — Warm & Familiar (20 games):** A deliberate pivot from conceptual/philosophical to warm, humanized gameplay. Every game feels like a childhood memory with something uniquely new:

| Prototype | Core Mechanic | The Novel Thing |
|-----------|---------------|-----------------|
| new-042-lullaby | Rhythm-rock a cradle | Anti-twitch: score by doing *less* |
| new-043-puddle | Stomp rain puddles | Ripples as indirect collection tool |
| new-044-blanketfort | Drape physics blankets | Soft-body construction with shadow monsters |
| new-045-firefly | Catch fireflies in a jar | Light as fading consumable resource |
| new-046-toast | Breakfast counter timing | Parallel timing across 3 cooking stations |
| new-047-snowball | Roll growing snowball downhill | Collection phase IS the creation phase |
| new-048-kite | Fly a kite via string tension | Indirect control — you adjust string, wind does the rest |
| new-049-treehouse | Stack planks in a tree | Living reward: birds nest in completed platforms |
| new-050-seedling | Nurture a plant through seasons | Asymmetric agency — you prepare, nature acts |
| new-051-paperfold | Fold origami along creases | Sequential transformation reveals hidden shape |
| new-052-carousel | Run a merry-go-round | Rotational timing as matchmaking puzzle |
| new-053-mittens | Pair falling mittens | Catch-and-match with limited basket capacity |
| new-054-campfire | Feed a campfire just right | Temperature range management attracts wildlife |
| new-055-lighthouse | Rotate beam to guide ships | Guardian mechanic — control environment, not actors |
| new-056-paperboat | Steer paper boat down gutter | Fragile temporary vehicle with sogginess clock |
| new-057-starmap | Connect stars into constellations | Temporal availability — interact only when stars are bright |
| new-058-bakery | Decorate cookies on conveyor | Freehand creation with fuzzy pattern matching |
| new-059-birdnest | Fly as bird, build nest, hatch eggs | Complete lifecycle arc as game structure |
| new-060-bubblebath | Rubber duck popping bubbles | Shrinking play space as draining bathtub |
| new-061-musicbox | Place missing notes on music box | Music theory as spatial puzzle on rotating cylinder |

These 20 games represent a new direction: AI-originated mechanics that feel like they've always existed — warm, intuitive, immediately playable, yet each contains something no game has done before.

**Phase 4 — AI Challenger (20 games):** Accessible arcade-style games designed for instant pickup-and-play: Graviton (orbital physics), Chromashift (color reflex), Timeshadow (self-chase), Bloom Garden (peaceful beauty), Pendulum (grapple swing), Dual Control (split-brain), Chain Blast (cascade), Color Flood (flood fill), Wordweave (vocabulary sprint), Orbiter (orbital precision), Mirrorbound (mirror survival), Stack Physics (weighted blocks), Weavethrough (graceful dodge), One Line All (path completion), Bouncewall (minimal redirect), Alchemist (element discovery), Beat Jump (rhythm platforms), Shape Morph (one-button reflex), Ink Trail (self-made maze), Sort Catch (falling sort).

**Phase 5 — Genre Fusion (10 games):** AI-originated genre mashups that combine two incompatible game types into coherent new experiences: Gravity Pong (orbital deflection), Puzzle Fight (competitive Tetris-fighting), Stealth Garden (stealth + gardening), Rhythm Craft (rhythm + crafting), Race Puzzle (racing + Sokoban), Card Platform (deck-building + platformer), Tower Brawl (tower defense + fighting), Bullet Garden (bullet hell + gardening), Wrestle Chess (wrestling + chess), Cooking Runner (cooking sim + endless runner).

**Phase 6 — Impossible Games (10 games):** Experiments in mechanics that subvert fundamental game design assumptions: Reverse Maze (you ARE the maze), Anti-Gravity (falling upward), Healer Shooter (you can only heal), Shrink World (world contracts as you play), Silent Rhythm (rhythm game with no music), Build Destroy (simultaneous creation and destruction), Ecosystem (manage a living food web), Paint Physics (paint changes physics properties), Music Terrain (terrain generates music), Light & Shadow (play simultaneously in two light states).

**Phase 7 — Meta & Philosophical (10 games):** Games that interrogate what games are: Emotion Engine (mood-responsive mechanics), Time Waves (non-linear time), Crowd Source (players contribute to shared world), Memory Game (the game remembers you), Death Loop (death IS the mechanic), Pixel Erosion (the game degrades as you play), Shared Score (your score is everyone's score), Meta Breaker (break the fourth wall mechanically), Nothing (a game about nothing), You Are The AI (play as the opponent AI).

**Phase 8 — Mathematical Playgrounds (30 games):** Games built directly from mathematical and computational concepts, each making abstract theory tangible through play: Manifold (topology navigation), Tesselate (tiling puzzles), Field Lines (electromagnetic play), Wave Interference (wave superposition), Voronoi (territory via nearest-point), Attractor (strange attractor navigation), Resonance (frequency matching), Tensegrity (structural tension), Fluid Router (fluid dynamics routing), Harmonograph (pendulum art), Spring Mesh (spring network physics), Cellular Engine (programmable cellular automata), Sort Machine (sorting algorithm play), Bool Circuit (logic gate construction), Entropy (thermodynamic puzzles), Compression (data compression game), Graph Walk (graph traversal), PID Controller (feedback control), Neural Play (train a neural net), State Machine (FSM construction), Gradient (gradient descent navigation), L-System (fractal growth rules), Reaction Diffusion (Turing pattern creation), Life Engineer (Game of Life design), Particle Swarm (swarm optimization), Fractal Zoom (infinite zoom exploration), Quantum Coin (superposition probability), Phasor (phase relationship control), Feedback (feedback loop management), Rule Explorer (emergent rule discovery).

**Play them all:** Open [index.html](index.html) in a browser.

### Weird, Viral & Niche Batch (20 games, 2026)

Games from the strange corners: M.U.L.E. (economic auction), Paradroid (body possession), Virtual Pet (life sim ancestor), GROW (combinatorial sequence), Cursor*10 (time-clone), QWOP (awkward physics), Line Rider (physics sandbox), Baba Is You (rule tiles), Papers Please (bureaucracy), Tempest (tube-rim shooter), Canabalt (invented endless runners), Chip's Challenge (tile puzzle), Goo Bridge (living physics), Agar.io (cell growth), Gorillas (QBasic artillery), A Dark Room (genre-revealing text), This Is the Only Level (rule mutation), Another World (cinematic platformer), Motherload (mining loop), Getting Over It (rage climbing).

### Global Unknown Batch (31 games, 2026)

31 games from 25 countries spanning 4,000 years: Fanorona (Madagascar), Surakarta (Indonesia), Patolli (Aztec), Yutnori (Korea), Hnefatafl (Viking), Makruk (Thai Chess), Janggi (Korean Chess), Carrom (India), Petanque (France), Sepak Takraw (SE Asia), Kabaddi (India), Perestroika (Russia), Color Lines (Russia), Engare (Iran), Farsh (Iran), Okhlos (Argentina), Laberinto (Cuba), Semblance (South Africa), Okada Ride (Nigeria), Coffee Talk (Indonesia), Munin (Sweden), Minit (Netherlands), Chuchel (Czech), Cinco Paus (NZ), Nidhogg (USA), Downwell (Japan), Cris Tales (Colombia), Detention (Taiwan), Unpacking (Australia), Togyzkumalak (Kazakhstan), Congkak (Malaysia).

### Japanese Boom Batch (25 games, 2026)

25 lesser-known games from the Japanese gaming ecosystem: Cameltry (rotate maze), Puzz Loop (Zuma precursor), Baku Baku Animal (animal-food matching), Libble Rabble (string enclosure), Kuru Kuru Kururin (rotating stick), Quinty (Game Freak's first), Umihara Kawase (rubber grapple), Liquid Kids (water waves), Puchi Carat (competitive Breakout), Bishi Bashi (WarioWare precursor), Cho Chabudai Gaeshi (table flipping), Densha de Go (train driving), Katamari Damacy (sticky ball), Magical Drop (grab-throw speed), Panel de Pon (swap match), Recettear (item shop RPG), Yume Nikki (dream exploration), Hoshi Saga (hidden stars), Tontie (numpad whacking), Nanaca Crash (launch bounce), Dicewars (dice territory), Penguin Land (egg guide), Mole Mania (two-layer puzzle), Gimmick! (bouncing star), Money Exchanger (coin arithmetic).

### Korean Gaming Batch (25 games, 2026)

25 games from South Korea's gaming ecosystem: Ddakji (card slamming), Gonggi (Korean jacks), Ssireum (wrestling), Tuho (arrow throwing), Jegichagi (keepie uppie), Paengi (top spinning), Fortress (team artillery), Crazy Arcade (water balloon Bomberman), Pangya (anime golf), Audition (dance combo), QuizQuiz (first F2P game, Nexon 1999), GunBound (mobile artillery), Freestyle (street basketball), Pump It Up (5-panel rhythm), DJMAX (6-lane premium rhythm), Cookie Run (auto-running cookie), Dragon Flight (dragon vertical shooter), Wind Runner (wind glide runner), Skul (skull-swapping roguelite), MO:Astray (slime possession), Replica (found-phone narrative), Kingdom of the Winds (Korea's first online game 1996), Astonishia Story (hex SRPG), Iljimae (Korean folk hero MSX), Dungreed (dash combat roguelite).

---

## Game Lineage — Ancestry & Evolution Map

The 460 prototypes form an interconnected web of influence. Each game's
ANCESTRY field traces its mechanical lineage. The lineage graph reveals
three types of relationships:

### Relationship Types

| Type | Arrow | Meaning |
|------|-------|---------|
| **AI Overlay** | Archetype → AI Archaeology | "What if AI were there?" visualization |
| **Evolution** | Archetype → AI Evolution | AI-designed game inspired by the archetype |
| **Variant** | Game → Game | Same series, different expression |

### Most Influential Archetypes

Games that inspired the most children (AI archaeology overlays + AI evolution experiments):

| Archetype | Children | What It Inspired |
|-----------|----------|-----------------|
| Mortal Kombat (fgt-005) | 3 | Frame reader, combo display, puzzle-fight fusion |
| Asteroids (phy-001) | 3 | Safety map, trajectory prediction, gravity pong |
| Runner (plt-001) | 3 | Path sense, card platform, anti-gravity |
| Rhythm (spt-008) | 3 | Flow state, rhythm craft, silent rhythm |
| Chess (anc-004) | 2 | Deep think search tree, wrestle chess |
| Space Invaders (fix-001) | 2 | AI escalation, healer shooter |
| Pac-Man (maz-001) | 2 | Ghost mind, reverse maze |
| Tetris (puz-001) | 2 | Block planner, puzzle fight |
| Sokoban (puz-009) | 2 | Deadlock detection, race puzzle |
| Bullet Hell (scr-010) | 2 | Bullet time, bullet garden |

### Lineage Chains (Deepest Ancestry)

```
Tapper (1983) → SmartBar (AI queue overlay) → FlowBar (AI demand elasticity)
Zelda (1986) → Explorer Map (AI curiosity-driven exploration)
Carmen Sandiego (1985) → Carmen Deduction (AI constraint elimination)
Chess (~600 CE) → Deep Think (AI search tree) + Wrestle Chess (AI fusion)
Go (~2500 BCE) → Go Territory (AI Monte Carlo evaluation)
Asteroids (1979) → Safety Map (AI threat zones) + Gravity Pong (AI orbital fusion)
```

### The Three Tracks Visualized

```
ARCHETYPE (241)                    AI ARCHAEOLOGY (76)           AI EVOLUTION (143)
━━━━━━━━━━━━━━━                    ━━━━━━━━━━━━━━━              ━━━━━━━━━━━━━━━━━
Pac-Man ─────────────────────→ Ghost Mind (AI targeting)
                              └→ Gap Finder (AI timing)
                                                        ┌──→ Reverse Maze (you ARE the maze)
Chess ───────────────────────→ Deep Think (search tree)
                                                        ├──→ Wrestle Chess (chess + wrestling)
Asteroids ───────────────────→ Asteroids Predict
                              └→ Safety Map             ├──→ Gravity Pong (orbital physics)
Sokoban ─────────────────────→ Sokoban Deadlock
                                                        ├──→ Race Puzzle (racing + sokoban)
```

The full machine-readable lineage graph is in `lineage.json` (101 edges across 460 nodes).
In the public gallery, each game shows its parents ("Based on") and children ("Inspired")
as clickable links.

---

## Attribution

Every prototype in this laboratory was built by a human-AI creative partnership
(Joshua Ayson + Claude, 2026) as acts of reconstruction and research. No original
game code, assets, or ROMs are included. Each prototype recreates the **core
mechanic** — the irreducible design loop — not the original implementation.

All original games are the creative and intellectual property of their respective
creators, studios, and publishers. This laboratory exists for educational purposes:
to study, preserve, and celebrate the history of game design and its deep
interconnection with the history of artificial intelligence.

**Mechanical reconstruction ≠ cloning.** We study the loop, not the skin.

---

*Generated for the Pixel Vault, v0.9.0*
*Last updated: March 2026*
