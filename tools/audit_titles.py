#!/usr/bin/env python3
"""Audit all game titles from PROTOTYPE metadata blocks and document.title."""
import glob, re, os, sys

# Extract PROTOTYPE name from metadata comment block
proto_re = re.compile(r'<!--.*?PROTOTYPE:\s*(.+?)\n', re.DOTALL)
title_re = re.compile(r"document\.title\s*=\s*['\"]([^'\"]+)['\"]", re.IGNORECASE)

# Known copyrighted / trademarked titles and characters
# Covers Nintendo, Sega, Atari, Midway, Namco, Capcom, Konami, etc.
KNOWN_IP = {
    # Nintendo
    "DONKEY KONG", "MARIO", "SUPER MARIO", "LUIGI", "ZELDA", "LINK", "METROID",
    "SAMUS", "KID ICARUS", "EXCITEBIKE", "BALLOON FIGHT", "ICE CLIMBER",
    "DUCK HUNT", "GYROMITE", "WRECKING CREW", "CLU CLU LAND",
    # Sega
    "SONIC", "ZAXXON", "CONGO BONGO", "SPACE FURY", "TRON", "STAR WARS",
    # Atari
    "MISSILE COMMAND", "TEMPEST", "BATTLEZONE", "CENTIPEDE", "MILLIPEDE",
    "ASTEROIDS", "BREAKOUT", "PONG", "ASTEROIDS DELUXE",
    # Namco
    "GALAGA", "GALAXIAN", "PAC-MAN", "PACMAN", "PAC MAN", "DIG DUG",
    "POLE POSITION", "XEVIOUS", "BOSCONIAN", "RALLY-X",
    # Midway
    "DEFENDER", "JOUST", "ROBOTRON", "SINISTAR", "PAPERBOY", "RAMPAGE",
    "TAPPER", "SPY HUNTER", "MORTAL KOMBAT", "GAUNTLET", "SMASH TV",
    # Konami
    "SCRAMBLE", "TIME PILOT", "GYRUSS", "FROGGER", "TURTLES",
    "GRADIUS", "CONTRA", "CASTLEVANIA", "MEGA MAN", "MEGAMAN",
    "RUSH N ATTACK", "SUPER COBALT",
    # Capcom
    "STREET FIGHTER", "GHOSTS N GOBLINS", "COMMANDO", "BIONIC COMMANDO",
    "1942", "1943", "TROJAN",
    # Data East
    "BURGERTIME", "BURGER TIME", "BADDUDES", "BAD DUDES",
    "KARATEKA", "HEAVY BARREL",
    # Irem
    "MOON PATROL", "R-TYPE", "KUNG FU",
    # Taito
    "SPACE INVADERS", "BUBBLE BOBBLE", "RAINBOW ISLANDS", "ARKANOID",
    "ELEVATOR ACTION", "JUNGLE KING", "QBERT", "Q*BERT",
    # Cinematronics / Coleco / other
    "BERZERK", "VENTURE", "PHOENIX", "POOYAN",
    "DRAGON'S LAIR", "DRAGONS LAIR",
    # Williams
    "DEFENDER", "STARGATE",
    # SNK
    "IKARI WARRIORS", "IKARI", "TIME SOLDIERS",
    # Activision
    "PITFALL", "RIVER RAID",
    # Other
    "LODE RUNNER", "BOULDER DASH", "BOMBERMAN", "LEMMINGS",
    "OUT RUN", "OUTRUN", "NIGHT STALKER", "PENGO",
    "DOUBLE DRAGON", "STREETS OF RAGE",
    "NETHACK", "ULTIMA", "WASTELAND",
    "TETRIS", "PUYO PUYO", "COLUMNS",
    "DOOM", "QUAKE",
    # International / foreign IP
    "YUME NIKKI", "TOUHOU", "CAVE STORY", "SPELUNKY", "MINECRAFT",
    "TERRARIA", "BINDING OF ISAAC", "SUPER MEAT BOY",
    "KATAMARI", "ICO", "SHADOW OF COLOSSUS",
}

def check_file(path):
    try:
        content = open(path, encoding='utf-8', errors='ignore').read()
    except:
        return None, []
    
    # Get the PROTOTYPE name from metadata
    m = proto_re.search(content)
    proto_name = m.group(1).strip() if m else None
    
    # Get document.title
    t = title_re.search(content)
    doc_title = t.group(1).strip() if t else None
    
    # Check for IP violations in prototype name and doc title
    violations = []
    for check in [proto_name, doc_title]:
        if not check:
            continue
        check_upper = check.upper()
        for ip in KNOWN_IP:
            if ip in check_upper:
                violations.append(f"'{check}' contains '{ip}'")
                break
    
    return proto_name, violations

dirs = ['prototypes', 'games']
results = []
for d in dirs:
    for f in sorted(glob.glob(f'{d}/**/*.html', recursive=True)):
        gid = os.path.basename(f).replace('.html', '')
        proto_name, violations = check_file(f)
        results.append((gid, proto_name, violations, f))

print(f"{'ID':<35} {'PROTOTYPE NAME':<40} ISSUE")
print("-" * 110)
violations_count = 0
for gid, name, violations, path in sorted(results):
    if violations:
        for v in violations:
            print(f"  {gid:<33} {str(name):<40} *** {v}")
        violations_count += 1

print(f"\nTotal violations found: {violations_count}")
print(f"Total files checked: {len(results)}")
