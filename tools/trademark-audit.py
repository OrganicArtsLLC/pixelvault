#!/usr/bin/env python3
"""Scan PixelVault HTML game files for trademark/IP issues in filenames and METADATA."""
import os, re, glob, json

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = '/tmp/pv-trademark-audit-report.md'

# ── Generic-name suggestions keyed by trademark slug ──────────────────────
GENERIC = {
    'pacman':'maze-chase','tetris':'falling-blocks','zelda':'top-down-quest',
    'donkey-kong':'barrel-climb','dk':'barrel-climb','metroid':'explore-upgrade',
    'metroidmap':'explore-upgrade-map','castlevania':'whip-platformer',
    'mortal-kombat':'arena-fighter','mk':'arena-fighter','doom':'fps-arena',
    'diablo':'action-dungeon','carmen':'geo-detective','civilizat':'civ-builder',
    'scrabble':'word-tiles','wordle':'word-guess','prince-of-persia':'acrobat-platformer',
    'clashroyale':'lane-battle','clashofclans':'base-builder','punchout':'boxing-reflex',
    'kid-icarus':'vertical-climb','bubble-bobble':'bubble-trap','cuttherope':'rope-physics',
    'cookierun':'dash-runner','deathloop':'time-loop','kingdomrush':'tower-defense',
    'paneldepon':'swap-chain','kururin':'rotate-navigate','molemania':'burrow-puzzle',
    'frogger':'road-crosser','qbert':'pyramid-hopper','dig-dug':'tunnel-digger',
    'digdug':'tunnel-digger','tron':'light-trail','katamari':'roll-collect',
    'lemmings':'guide-crowd','wing-commander':'space-dogfight','gauntlet':'dungeon-crawl',
    'ultima':'tile-rpg','worms':'artillery-battle','populous':'god-game',
    'kings-quest':'graphic-adventure','maniac-mansion':'point-click',
    'dragons-lair':'action-choice','burgertime':'ingredient-stack',
    'battleship':'grid-strike','outrun':'road-racer','zaxxon':'iso-shooter',
    'pengo':'ice-pusher','bloons':'pop-defense','agario':'absorb-arena',
    'gunbound':'arc-artillery','doodlejump':'vertical-bounce',
    'bardstale':'party-dungeon','bards-tale':'party-dungeon',
    'wasteland':'post-apoc-rpg','skifree':'downhill-ski','rampage':'kaiju-smash',
    'joust':'flap-fight','asteroids':'space-drift','centipede':'bug-shooter',
    'missile':'intercept','tempest':'tube-shooter','pong':'paddle-rally',
    'breakout':'brick-breaker','marble-madness':'marble-roll',
    'oregon':'trail-survival','paperboy':'delivery-run','tapper':'serve-rush',
    'papersplease':'doc-inspector','karateka':'martial-advance',
    'berzerk':'robot-escape','robotron':'twin-stick','1942':'ww2-shmup',
    'contra':'run-gun','stratego':'hidden-army','lode-runner':'trap-runner',
    'pitfall':'jungle-swing','sokoban':'crate-push','chipschallenge':'tile-quest',
    'chips':'tile-quest','nightstalker':'dark-hunt','night-stalker':'dark-hunt',
    'crazyarcade':'bomb-maze','crazy-arcade':'bomb-maze','recettear':'shop-keeper',
    'motherload':'drill-mine','unpacking':'unbox-place','nidhogg':'tug-duel',
    'bishibashi':'minigame-party','paradroid':'takeover','linerider':'draw-ride',
    'line-rider':'draw-ride','coffeetalk':'brew-chat','coffee-talk':'brew-chat',
    'chuchel':'slapstick-puzzle','yumenikki':'dream-explore','canabalt':'auto-runner',
    'anotherworld':'cinematic-platformer','thexder':'transform-shmup',
    'downwell':'well-dive','bump-n-jump':'hop-racer','lock-n-chase':'door-maze',
    'liquidkids':'water-platformer','gimmick':'star-bounce','scramble':'side-shmup',
    'ikari':'commando-run','defender':'side-rescue','taipan':'trade-voyage',
    'zork':'text-adventure','puzzloop':'marble-match','magicaldrop':'drop-match',
    'bakubaku':'feed-match','quinty':'flip-panel','penguinland':'egg-guide',
    'cameltry':'tilt-maze','hoshisaga':'star-discovery','quizquiz':'trivia-battle',
    'skul':'skull-swap','puchicarat':'gem-deflect','tontie':'whack-grid',
    'libblerabble':'line-capture','pangya':'fantasy-golf','pumpit':'dance-step',
    'djmax':'music-cascade','ys':'bump-rpg','dungeon-master':'first-person-dungeon',
    'dicewars':'dice-territory','astonishia':'tactics-rpg',
    'cristales':'time-crystal-rpg','vanguard':'multi-scroll-shmup',
    'qix':'territory-claim','jezzball':'divide-field','teeworlds':'grapple-arena',
    'archon':'chess-combat','nanacacrash':'launch-bounce','qwop':'ragdoll-run',
    'chabudai':'table-flip','semblance':'deform-platformer',
    'umihara':'elastic-platformer','dungreed':'roguelite-action',
    'moastray':'slime-crawl','mastermind':'code-breaker','minit':'micro-adventure',
    'detention':'horror-explore','replica':'phone-snoop','mole':'burrow-puzzle',
    'nethack':'ascii-dungeon','audition':'dance-rhythm','perestroika':'reform-puzzle',
    'kart':'kart-racer','denshadego':'train-sim','mule':'colony-trade',
    'grow':'sequence-grow','tangram':'shape-fit','colorlines':'color-path',
    'money':'coin-cascade','bowling':'bowling-scatter','carrom':'disc-strike',
    'blackjack':'card-count','backgammon':'race-board','liarsdice':'bluff-dice',
    'pinball':'pinball-predict',
}

def suggest(path, mechanic, series, num):
    name_only = re.sub(r'^[a-z]+-\d+-', '', os.path.basename(path).replace('.html','')).lower()
    nk = name_only.replace('-','')
    for k,v in GENERIC.items():
        if k.replace('-','') in nk:
            return f'{series}-{num}-{v}'
    if mechanic:
        s = re.sub(r'[^a-z0-9]+','-',mechanic.lower())[:30].strip('-')
        return f'{series}-{num}-{s}'
    return f'{series}-{num}-NEEDS-RENAME'

# ── Trademark patterns ────────────────────────────────────────────────────
TM = [
    # HIGH — major companies, aggressively enforced
    ('pac.?man','Bandai Namco','HIGH'),
    ('tetris','Tetris Holding LLC','HIGH'),
    ('zelda','Nintendo','HIGH'),
    ('donkey.?kong','Nintendo','HIGH'),
    ('metroid','Nintendo','HIGH'),
    ('castlevania','Konami','HIGH'),
    ('mortal.?kombat','Warner Bros','HIGH'),
    (r'\bdoom\b','id Software/Bethesda','HIGH'),
    ('diablo','Blizzard/Microsoft','HIGH'),
    ('carmen.?sandiego','HMH','HIGH'),
    ('civilizat','Take-Two/Firaxis','HIGH'),
    ('scrabble','Hasbro/Mattel','HIGH'),
    ('wordle','NYT','HIGH'),
    ('prince.?of.?persia','Ubisoft','HIGH'),
    ('clash.?royale','Supercell','HIGH'),
    ('clash.?of.?clans','Supercell','HIGH'),
    ('punch.?out','Nintendo','HIGH'),
    ('kid.?icarus','Nintendo','HIGH'),
    ('bubble.?bobble','Taito/Square Enix','HIGH'),
    ('cut.?the.?rope','ZeptoLab','HIGH'),
    ('cookie.?run','Devsisters','HIGH'),
    ('deathloop','Arkane/Bethesda','HIGH'),
    ('kingdom.?rush','Ironhide','HIGH'),
    ('panel.?de.?pon','Nintendo','HIGH'),
    ('kururin','Nintendo','HIGH'),
    ('mole.?mania','Nintendo','HIGH'),
    # MEDIUM — established studios, likely enforced
    ('frogger','Konami','MEDIUM'),
    ('q.?bert','Sony/Gonzo','MEDIUM'),
    ('dig.?dug','Bandai Namco','MEDIUM'),
    (r'\btron\b','Disney','MEDIUM'),
    ('katamari','Bandai Namco','MEDIUM'),
    ('lemmings','Team17','MEDIUM'),
    ('wing.?commander','EA','MEDIUM'),
    ('gauntlet','Warner Bros','MEDIUM'),
    (r'\bultima\b','EA','MEDIUM'),
    (r'\bworms\b','Team17','MEDIUM'),
    ('populous','EA','MEDIUM'),
    ('king.?s.?quest','Activision','MEDIUM'),
    ('maniac.?mansion','Disney/LucasArts','MEDIUM'),
    ('dragon.?s.?lair','Don Bluth','MEDIUM'),
    ('burgertime','G-Mode','MEDIUM'),
    ('battleship','Hasbro','MEDIUM'),
    ('out.?run','Sega','MEDIUM'),
    ('zaxxon','Sega','MEDIUM'),
    ('pengo','Sega','MEDIUM'),
    ('bloons','Ninja Kiwi','MEDIUM'),
    ('agar.?io','Miniclip','MEDIUM'),
    ('gunbound','Softnyx','MEDIUM'),
    ('doodle.?jump','Lima Sky','MEDIUM'),
    ('bard.?s.?tale','EA/inXile','MEDIUM'),
    ('wasteland','inXile/Microsoft','MEDIUM'),
    ('ski.?free','Microsoft','MEDIUM'),
    ('rampage','Warner Bros','MEDIUM'),
    (r'\bjoust\b','Warner Bros','MEDIUM'),
    ('asteroids','Atari','MEDIUM'),
    ('centipede','Atari','MEDIUM'),
    ('missile.?command','Atari','MEDIUM'),
    ('tempest','Atari','MEDIUM'),
    (r'\bpong\b','Atari','MEDIUM'),
    ('breakout','Atari','MEDIUM'),
    ('marble.?madness','Atari','MEDIUM'),
    ('oregon.?trail','HMH','MEDIUM'),
    ('paperboy','Atari/Midway','MEDIUM'),
    (r'\btapper\b','Midway','MEDIUM'),
    ('papers.?please','Lucas Pope','MEDIUM'),
    ('karateka','Mechner/Ubisoft','MEDIUM'),
    ('berzerk','Stern','MEDIUM'),
    ('robotron','Williams/Midway','MEDIUM'),
    (r'\b1942\b','Capcom','MEDIUM'),
    ('contra','Konami','MEDIUM'),
    ('stratego','Jumbo/Hasbro','MEDIUM'),
    ('lode.?runner','Tozai','MEDIUM'),
    ('pitfall','Activision','MEDIUM'),
    # LOWER — smaller/defunct studios, open source, niche
    ('sokoban','Thinking Rabbit','LOWER'),
    ('chips.?challenge','Chuck Sommerville','LOWER'),
    ('night.?stalker','Mattel','LOWER'),
    ('crazy.?arcade','Nexon','LOWER'),
    ('densha.?de.?go','Taito','LOWER'),
    ('recettear','EasyGameStation','LOWER'),
    ('motherload','XGen Studios','LOWER'),
    ('unpacking','Witch Beam','LOWER'),
    ('nidhogg','Messhof','LOWER'),
    ('bishi.?bashi','Konami','LOWER'),
    ('paradroid','Hewson','LOWER'),
    ('line.?rider','InXile','LOWER'),
    ('coffee.?talk','Toge Productions','LOWER'),
    ('chuchel','Amanita Design','LOWER'),
    ('yume.?nikki','Kikiyama','LOWER'),
    ('canabalt','Semi Secret','LOWER'),
    ('another.?world','Delphine/Chahi','LOWER'),
    ('thexder','Game Arts','LOWER'),
    ('downwell','Devolver','LOWER'),
    ('bump.?n.?jump','G-Mode','LOWER'),
    ('lock.?n.?chase','G-Mode','LOWER'),
    ('liquid.?kids','Taito','LOWER'),
    (r'\bgimmick\b','Sunsoft','LOWER'),
    ('scramble','Konami','LOWER'),
    (r'\bikari\b','SNK','LOWER'),
    ('defender','Williams/Midway','LOWER'),
    ('taipan','Public domain','LOWER'),
    (r'\bzork\b','Activision','LOWER'),
    ('puzz.?loop','Mitchell','LOWER'),
    ('magical.?drop','G-Mode','LOWER'),
    ('baku.?baku','Sega','LOWER'),
    ('quinty','Namco','LOWER'),
    ('penguin.?land','Sega','LOWER'),
    ('cameltry','Taito','LOWER'),
    ('hoshi.?saga','Eyezmaze','LOWER'),
    ('quiz.?quiz','Nexon','LOWER'),
    (r'\bskul\b','SouthPAW Games','LOWER'),
    ('puchi.?carat','Taito','LOWER'),
    ('tontie','Eyezmaze','LOWER'),
    ('libble.?rabble','Namco','LOWER'),
    ('pangya','Gamepot','LOWER'),
    ('pump.?it.?up','Andamiro','LOWER'),
    ('djmax','Neowiz','LOWER'),
    (r'\bys\b','Nihon Falcom','LOWER'),
    (r'\bmule\b','EA','LOWER'),
    ('dungeon.?master','FTL Games','LOWER'),
    ('dice.?wars','GameDesign','LOWER'),
    ('astonishia','Sonnori','LOWER'),
    ('cristales','Dreams Uncorporated','LOWER'),
    ('vanguard','SNK','LOWER'),
    (r'\bqix\b','Taito','LOWER'),
    ('jezzball','Microsoft','LOWER'),
    ('teeworlds','Open Source','LOWER'),
    ('archon','EA/Free Fall','LOWER'),
    ('nanaca.?crash','Web game','LOWER'),
    (r'\bqwop\b','Bennett Foddy','LOWER'),
    ('chabudai','Taito','LOWER'),
    ('semblance','Nyamakop','LOWER'),
    ('umihara','TNN','LOWER'),
    ('dungreed','Team Horay','LOWER'),
    ('mo.?astray','Archpray','LOWER'),
    ('mastermind','Hasbro','LOWER'),
    (r'\bminit\b','Devolver','LOWER'),
    ('detention','Red Candle Games','LOWER'),
    ('replica','SOMI','LOWER'),
]

# ── Scan ──────────────────────────────────────────────────────────────────
all_files = sorted(
    f for d in ('prototypes','ai-archaeology','ai-evolution')
    for f in glob.glob(f'{d}/**/*.html', recursive=True)
)

flagged = []
for fpath in all_files:
    fname = os.path.basename(fpath).lower()
    with open(fpath,'r',encoding='utf-8',errors='ignore') as fp:
        content = fp.read()
    m = re.search(r'<!--(.*?)-->',content,re.DOTALL)
    meta = m.group(1) if m else ''
    pm = re.search(r'PROTOTYPE:\s*(.+)',meta)
    mm = re.search(r'MECHANIC:\s*(.+)',meta)
    proto = pm.group(1).strip() if pm else ''
    mech  = mm.group(1).strip() if mm else ''
    visual_text = []
    for vm in re.finditer(r'(?:hudText|fillText|strokeText)\(\s*(["\'])(.*?)\1', content, re.DOTALL):
        visual_text.append(vm.group(2))
    issues = []
    for pat,holder,risk in TM:
        if re.search(pat,fname,re.I):
            issues.append(('FILENAME',pat,holder,risk))
        if proto and re.search(pat,proto,re.I):
            issues.append(('PROTOTYPE',pat,holder,risk))
        if mech and re.search(pat,mech,re.I):
            issues.append(('MECHANIC',pat,holder,risk))
        for txt in visual_text:
            if re.search(pat,txt,re.I):
                issues.append(('VISUAL_TEXT',pat,holder,risk))
                break
    seen=set(); uniq=[]
    for loc,p,h,r in issues:
        k=(loc,p)
        if k not in seen: seen.add(k); uniq.append((loc,p,h,r))
    if uniq:
        risks=set(r for _,_,_,r in uniq)
        mx='HIGH' if 'HIGH' in risks else 'MEDIUM' if 'MEDIUM' in risks else 'LOWER'
        flagged.append(dict(path=fpath,fn=fname,proto=proto,mech=mech,mx=mx,iss=uniq,visual_text=visual_text))

# ── Report ────────────────────────────────────────────────────────────────
with open(OUT,'w') as f:
    def w(s=''):
        f.write(s+'\n')

    w('# PixelVault Trademark / IP Audit Report')
    w()
    w(f'**Total files scanned:** {len(all_files)}')
    w(f'**Files with trademark issues:** {len(flagged)}')
    w(f'**Files clean:** {len(all_files)-len(flagged)}')
    w()
    hc=len([r for r in flagged if r['mx']=='HIGH'])
    mc=len([r for r in flagged if r['mx']=='MEDIUM'])
    lc=len([r for r in flagged if r['mx']=='LOWER'])
    w('| Risk | Count |')
    w('|---|---|')
    w(f'| HIGH | {hc} |')
    w(f'| MEDIUM | {mc} |')
    w(f'| LOWER | {lc} |')
    w()

    for rl in ('HIGH','MEDIUM','LOWER'):
        rf=[r for r in flagged if r['mx']==rl]
        if not rf: continue
        w(f'## {rl} RISK ({len(rf)} files)')
        w()
        for i,r in enumerate(sorted(rf,key=lambda x:x['path']),1):
            parts=r['fn'].replace('.html','').split('-',2)
            ser=parts[0] if len(parts)>0 else ''
            num=parts[1] if len(parts)>1 else ''
            sg=suggest(r['path'],r['mech'],ser,num)
            holders=sorted(set(h for _,_,h,_ in r['iss']))
            locs=sorted(set(l for l,_,_,_ in r['iss']))
            w(f'{i}. **`{r["path"]}`**')
            w(f'   - PROTOTYPE: "{r["proto"]}"')
            if r['mech']:
                w(f'   - MECHANIC: "{r["mech"]}"')
            w(f'   - TM: {", ".join(holders)} | In: {", ".join(locs)}')
            if 'VISUAL_TEXT' in locs:
                samples=[]
                for pat,_,_,_ in r['iss']:
                    if pat == 'VISUAL_TEXT':
                        continue
                for txt in r.get('visual_text', []):
                    if any(re.search(p, txt, re.I) for loc,p,_,_ in r['iss'] if loc == 'VISUAL_TEXT'):
                        samples.append(txt.strip())
                if samples:
                    w(f'   - Visible text: {", ".join("\"" + s[:60] + "\"" for s in samples[:3])}')
            w(f'   - Rename → `{sg}.html`')
        w()

    w('## Notes')
    w()
    w('- ANCESTRY fields were NOT flagged (educational attribution — kept intentionally)')
    w('- Some LOWER risk items may be safe to keep (open source, defunct companies)')
    w('- HIGH risk items MUST be renamed before public publishing')
    w('- MEDIUM risk items should be reviewed case-by-case')
    w('- During rename: also update PROTOTYPE field, title in HTML, and any TM references in HUD/comments')
    w('- VISUAL_TEXT findings are especially important for gallery thumbnails because the screenshot pipeline captures rendered canvas text')

print(f'Scanned {len(all_files)} files, found {len(flagged)} with trademark issues.')
print(f'HIGH={hc}  MEDIUM={mc}  LOWER={lc}')
print(f'Report → {OUT}')
