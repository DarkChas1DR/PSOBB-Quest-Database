"""Build source-documented entity registries and observed quest evidence.

No placement observation is promoted to a client compatibility guarantee.
Requires the restored quest-library.sqlite. Uses only repository references.
"""
import collections, csv, gzip, hashlib, json, pathlib, re, sqlite3

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT/'analysis/entity-database'
REF = ROOT/'analysis/quest-knowledge/reference'
MAP = REF/'server-source/Map.cc'
STATIC = REF/'server-source/StaticGameData.cc'

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def entity_filename(d):
    return f'{d["id"]:04X}-'+re.sub(r'[^A-Za-z0-9_-]','_',d['constructor'])+'.md'

def main():
    mtext=MAP.read_text(encoding='utf-8'); stext=STATIC.read_text(encoding='utf-8')
    flags={n:int(v,16) for n,v in re.findall(r'static constexpr uint16_t (F_\w+) = (0x[0-9A-Fa-f]+);',mtext)}
    areas=[]
    for m in re.finditer(r'\{Episode::EP(1|2|4),\s*(0x\w+),\s*(0x\w+),\s*(0x\w+),\s*(0x\w+),[^\n]+?"([^"]+)",\s*"([^"]+)",\s*"([^"]+)"',stext):
        ep,floor,_,area,_,_,_,name=m.groups()
        areas.append(dict(episode=int(ep),default_floor=int(floor,16),area=int(area,16),name=name,source_line=stext[:m.start()].count('\n')+1))
    assert len(areas)==47,len(areas)
    dump(OUT/'areas.json',areas)
    qnames={}
    for line in (REF/'qedit-config/npcname.ini').read_text(encoding='utf-8',errors='replace').splitlines():
        cols=line.split('\t')
        if len(cols)>1 and cols[0].isdigit(): qnames[int(cols[0])]=cols[1]
    start=mtext.index('static const std::vector<DATEntityDefinition> dat_enemy_definitions')
    end=mtext.index('\n});',start)
    defs=[]; comment=[]
    for lineno,line in enumerate(mtext[:end].splitlines(),1):
        if lineno<=mtext[:start].count('\n'): continue
        stripped=line.strip()
        if stripped.startswith('//'): comment.append(stripped[2:].strip()); continue
        hit=re.match(r'\s*\{(0x\w+),\s*([^,]+),\s*(0x\w+),\s*"([^"]+)"\},?(?:\s*//\s*(.*))?',line)
        if not hit: continue
        ident,flag,mask,constructor,note=hit.groups()
        version=0
        for term in flag.split('|'): version |= flags[term.strip()]
        preceding='\n'.join(comment); comment=[]
        if not version & 0x2000: continue
        ident=int(ident,16); mask=int(mask,16)
        defs.append(dict(id=ident,id_hex=f'0x{ident:04X}',constructor=constructor,
            kind='npc' if 'npc' in constructor.lower() or ident==0x100 else 'monster',
            qedit_name=qnames.get(ident),source_description=note,parameter_notes=preceding,
            area_flags=f'0x{mask:016X}',documented_areas=[a for a in areas if mask & (1<<a['area'])],
            source_line=lineno,evidence='source-documented; not client-playtested'))
    assert defs and any(d['id']==64 for d in defs)
    bytype=collections.defaultdict(list)
    for d in defs: bytype[d['id']].append(d)
    db=sqlite3.connect((ROOT/'analysis/quest-knowledge/quest-library.sqlite').as_uri()+'?mode=ro',uri=True)
    db.row_factory=sqlite3.Row
    quests={r['key']:dict(r) for r in db.execute('SELECT * FROM quests')}
    outdb=sqlite3.connect(OUT/'entities.sqlite')
    outdb.executescript('DROP TABLE IF EXISTS definitions; DROP TABLE IF EXISTS placements; DROP TABLE IF EXISTS handlers; DROP TABLE IF EXISTS classes; CREATE TABLE definitions(id INTEGER,constructor TEXT,kind TEXT,data TEXT); CREATE TABLE placements(quest_key TEXT,episode TEXT,floor INTEGER,idx INTEGER,type INTEGER,kind TEXT,data TEXT,handler_label TEXT,handler_status TEXT); CREATE TABLE handlers(quest_key TEXT,label TEXT,line INTEGER,body TEXT,PRIMARY KEY(quest_key,label)); CREATE TABLE classes(id INTEGER PRIMARY KEY,name TEXT,data TEXT); CREATE INDEX placements_type ON placements(type);')
    observations=collections.defaultdict(list); handlers={}; kinds=collections.Counter(); unresolved=collections.Counter()
    for row in db.execute("SELECT * FROM placements WHERE kind='enemy_npc'"):
        r=dict(row); data=json.loads(r['data']); ident=r['type']; q=quests[r['quest_key']]
        candidates=bytype.get(ident,[]); kind=candidates[0]['kind'] if candidates else 'unclassified'
        label=None; status='not a standard NPC interaction'; target=None
        # Stage NPC / skin 0x33 uses a different layout. Avoid treating its action as a label.
        if kind=='npc' and ident!=0x33:
            char_id=int(data['params'][3]); fn=int(data['params'][4])
            if fn==0: status='no DAT interaction label'
            elif not 100<=char_id<=999: status='free-play script target; quest linkage not inferred'
            else:
                label=f'label{fn:04X}'
                target=db.execute('SELECT * FROM functions WHERE quest_key=? AND label=?',(r['quest_key'],label)).fetchone()
                status='static candidate resolved; inspect caller and type-specific rules' if target else 'target not resolved'
                if target: handlers[(r['quest_key'],label)]=dict(target)
        if kind=='unclassified': unresolved[ident]+=1
        record=dict(quest_key=r['quest_key'],episode=q['episode'],floor=r['floor'],index=r['idx'],type=ident,kind=kind,
            room=r['room'],wave=r['wave'],position=data['position'],angles=data['angles'],params=data['params'],
            handler_label=label,handler_status=status)
        observations[ident].append(record); kinds[kind]+=1
        outdb.execute('INSERT INTO placements VALUES(?,?,?,?,?,?,?,?,?)',(r['quest_key'],q['episode'],r['floor'],r['idx'],ident,kind,r['data'],label,status))
    for h in handlers.values(): outdb.execute('INSERT INTO handlers VALUES(?,?,?,?)',(h['quest_key'],h['label'],h['line'],h['body']))
    for d in defs:
        d['observed_placement_count']=len(observations[d['id']]); outdb.execute('INSERT INTO definitions VALUES(?,?,?,?)',(d['id'],d['constructor'],d['kind'],json.dumps(d)))
    dump(OUT/'definitions.json',defs)
    # Preserve native game-name/Ultimate-name and battle-parameter mappings as their own namespace.
    etext=(OUT/'reference/EnemyType.cc').read_text(encoding='utf-8')
    enemies=[]
    for lineno,line in enumerate(etext.splitlines(),1):
        if not re.match(r'\s*\{EnemyType::',line): continue
        names=re.findall(r'"([^"]*)"',line)
        if len(names)<2: continue
        enemies.append(dict(enum_name=names[-3] if len(names)>2 else names[0],name=names[-2] if len(names)>2 else names[1],ultimate_name=names[-1] if len(names)>2 else None,source_line=lineno,source_definition=line.strip(),note='EnemyType enum and battle indices are not DAT placement IDs'))
    dump(OUT/'monster-names.json',enemies)
    # Class IDs and visual configuration flags are a separate namespace from DAT NPC skins.
    visual=(OUT/'reference/PlayerSubordinates.hh').read_text(encoding='utf-8')
    maxblock=re.search(r'v3_v4_class_maxes\[19\] = \{(.*?)\};',visual,re.S).group(1)
    maxes=[[int(v,16) for v in re.findall(r'0x[\dA-Fa-f]+',line)] for line in maxblock.splitlines() if '{' in line]
    classblock=re.search(r'static std::array<uint8_t, 12> class_flags = \{(.*?)\};',stext,re.S).group(1)
    visualflags=[int(x,16) for x in re.search(r'flags\[12\] = \{([^}]+)',stext).group(1).split(',')]
    classes=[]
    for i,line in enumerate(x for x in classblock.splitlines() if 'ClassFlag::' in x):
        name=line.split('//')[1].strip(); tokens=re.findall(r'ClassFlag::(\w+)',line)
        c=dict(id=i,id_hex=f'0x{i:02X}',name=name,race=next(t for t in tokens if t in ('HUMAN','NEWMAN','ANDROID')),
            gender='male' if 'MALE' in tokens else 'female',role=next(t for t in tokens if t in ('HUNTER','RANGER','FORCE')),
            visual_class_flags=visualflags[i],appearance_counts=dict(zip(('costume','skin','face','head','hair'),maxes[i])),
            evidence='newserv V3/V4 lobby normalization bounds; not a visual gallery or complete quest-NPC model validation')
        classes.append(c); outdb.execute('INSERT INTO classes VALUES(?,?,?)',(i,name,json.dumps(c)))
    assert len(classes)==12
    dump(OUT/'classes.json',classes)
    # Separate every NPC-related opcode with its preserved documentation.
    opcodes=json.loads((ROOT/'analysis/quest-knowledge/opcode-reference.json').read_text(encoding='utf-8'))
    npcops=[o for o in opcodes if o['supports_bb'] and any('npc' in alias.lower() for alias in o['aliases'])]
    dump(OUT/'npc-opcodes.json',npcops)
    # Preserve decoded appearance/configuration blocks where the disassembler recognized them.
    visuals=[]
    for q in quests:
        path=ROOT/'analysis/server-catalogue'/q/'script-offsets.txt'
        text=path.read_text(encoding='utf-8')
        for match in re.finditer(r'// As PlayerVisualConfig[^\n]*',text):
            lineno=text[:match.start()].count('\n')+1
            body=text[match.start():].split('\n\n',1)[0]
            visuals.append(dict(quest_key=q,line=lineno,source=path.relative_to(ROOT).as_posix(),body=body))
    dump(OUT/'npc-visual-blocks.json',visuals)
    # Per-type pages and complete observed placements CSVs are browsable without SQLite.
    for ident,records in observations.items():
        if not records: continue
        p=OUT/'observations'/f'{ident:04X}.csv'; p.parent.mkdir(exist_ok=True)
        with p.open('w',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=list(records[0])); writer.writeheader(); writer.writerows(records)
    for kind,title in [('monster','Monster database'),('npc','NPC database')]:
        index=[f'# {title}', '', '[Entity database guide](README.md) · [Area compatibility](areas.md) · [Classes and appearance](classes.md)', '',
            'IDs below are DAT enemy/NPC placement IDs. Names retain Qedit labels where available. Documented areas come from the stored BB constructor definition; observed placements alone do not prove compatibility.', '',
            '| DAT ID | Qedit name / constructor | Observed records |', '|---|---|---:|']
        for d in sorted((x for x in defs if x['kind']==kind),key=lambda x:(x['id'],x['constructor'])):
            ident=d['id']; filename=entity_filename(d); name=d['qedit_name'] or d['constructor']; seen=observations[ident]
            index.append(f'| {d["id_hex"]} ({ident}) | [{name.replace("|","/")}]({kind}s/{filename}) | {len(seen)} |')
            page=[f'# {name}', '', f'DAT ID **{d["id_hex"]} / {ident}**, constructor **{d["constructor"]}**.', '',
                f'[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L{d["source_line"]}) · [Database index](../{kind}s.md)', '',
                '## Source-documented areas', '', '; '.join(f'Episode {a["episode"]}: {a["name"]} (area 0x{a["area"]:02X}, default floor {a["default_floor"]})' for a in d['documented_areas']), '',
                'Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.', '',
                '## Parameters and source notes', '', '```text', d['parameter_notes'] or 'No per-type parameter comment in this definition. Inspect the source and generic NPC rules where applicable.', d['source_description'] or '', '```', '',
                '## Observed quest placements', '', f'{len(seen)} records, including language duplicates. These are observations, not spawn permissions.', '']
            if seen: page += [f'[All observed positions, angles, parameters and handler candidates](../observations/{ident:04X}.csv)', '', '| Quest | Floor | Room / wave | Handler candidate |', '|---|---:|---|---|']
            for r in seen[:30]:
                h=handlers.get((r['quest_key'],r['handler_label']))
                target=f'[{h["label"]}](../../server-catalogue/{r["quest_key"]}/script.txt#L{h["line"]})' if h else (r['handler_label'] or '—')
                page.append(f'| [{r["quest_key"]}](../../server-catalogue/{r["quest_key"]}/README.md) | {r["floor"]} | {r["room"]} / {r["wave"]} | {target} |')
            p=OUT/f'{kind}s'/filename; p.parent.mkdir(exist_ok=True); p.write_text('\n'.join(page)+'\n',encoding='utf-8')
        (OUT/f'{kind}s.md').write_text('\n'.join(index)+'\n',encoding='utf-8')
    area_page=['# Source-documented monster availability by area', '', 'These BB constructor masks are not inferred from quest frequency. A type excluded here must not be used without separately verified client support. Map designation must be resolved before comparing a floor slot to an area.', '']
    for a in areas:
        area_page += [f'## Episode {a["episode"]}: {a["name"]} — area 0x{a["area"]:02X}', '', '| DAT ID | Monster |', '|---|---|']
        for d in defs:
            if d['kind']=='monster' and a in d['documented_areas']:
                area_page.append(f'| {d["id_hex"]} | [{d["qedit_name"] or d["constructor"]}](monsters/{entity_filename(d)}) |')
        area_page.append('')
    (OUT/'areas.md').write_text('\n'.join(area_page)+'\n',encoding='utf-8')
    cp=['# Classes, races and appearance IDs', '', 'Player class IDs are not NPC DAT skin IDs: RAmar is class 3, while the Qedit default Bernie/RAmar DAT type is 36 (0x24). Race is derived from class flags, not an interchangeable DAT race ID.', '',
        'Appearance counts below come from newserv V3/V4 lobby normalization. For a positive count N the indices are 0 to N−1; zero means normalization forces zero. These are not face thumbnails or proof that every extra NPC model supports each combination.', '',
        '| Class ID | Class | Race | Gender | Costume count | Skin count | Face count | Head count | Hair count |', '|---|---|---|---|---:|---:|---:|---:|---:|']
    for c in classes: cp.append(f'| {c["id"]} | {c["name"]} | {c["race"]} | {c["gender"]} | '+ ' | '.join(str(v) for v in c['appearance_counts'].values())+' |')
    cp += ['', '[Visual structure, limits and NPC safety substitutions](reference/PlayerSubordinates.hh) · [Machine-readable classes](classes.json) · [Decoded quest visual blocks](npc-visual-blocks.json)', '', 'See README for remaining appearance and NPC linkage gaps.']
    (OUT/'classes.md').write_text('\n'.join(cp)+'\n',encoding='utf-8')
    outdb.commit(); assert outdb.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
    assert outdb.execute('SELECT count(*) FROM placements').fetchone()[0]==146753
    hilde=next(d for d in defs if d['id']==64)
    assert not int(hilde['area_flags'],16)&(1<<1) and int(hilde['area_flags'],16)&(1<<2)
    stats=dict(definitions=len(defs),monster_definitions=sum(d['kind']=='monster' for d in defs),npc_definitions=sum(d['kind']=='npc' for d in defs),placements=dict(kinds),resolved_handler_candidates=len(handlers),visual_blocks=len(visuals),classes=len(classes),unclassified_types=dict(unresolved),hildebear_forest1_excluded_forest2_included=True,integrity='ok')
    dump(OUT/'validation.json',stats)
    inputs=[MAP,STATIC,REF/'qedit-config/npcname.ini',REF/'server-source/Map.hh']+list((OUT/'reference').glob('*'))
    dump(OUT/'provenance.json',[dict(path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in inputs])
    outdb.close(); db.close()
    database=OUT/'entities.sqlite'; archive=OUT/'entities.sqlite.gz'
    with archive.open('wb') as raw, gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as z:
        z.write(database.read_bytes())
    entry=dict(archive=archive.relative_to(ROOT).as_posix(),destination=database.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(database.read_bytes()).hexdigest(),size=database.stat().st_size,compressed_size=archive.stat().st_size)
    archives=json.loads((ROOT/'archives.json').read_text(encoding='utf-8'))
    archives=[a for a in archives if a['destination']!=entry['destination']]+[entry]
    dump(ROOT/'archives.json',archives)
    print(json.dumps(stats))

if __name__=='__main__': main()
