"""Preserve supplied quest evidence and build a searchable, provenance-tagged library."""
import collections,csv,hashlib,json,pathlib,re,shutil,sqlite3,struct,sys
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
B=pathlib.Path(__file__).resolve().parents[1]; OUT=B/'quest-knowledge'; OUT.mkdir(exist_ok=True)
SRC=pathlib.Path(r'D:\DarkChas Main Stuff\Main Servers\PhantasyStarOnlineServer\system\quests')
CLIENT=pathlib.Path(r'C:\Users\chasm\Documents\ChatGPT\PSOBB\PSOBB.IO [Modded][DarkChas]')
CAT=B/'server-catalogue'; records=json.loads((CAT/'catalogue.json').read_text(encoding='utf-8'))
def digest(data): return hashlib.sha256(data).hexdigest()
def dump(p,data): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
files=[]
def preserve(p,rel,kind):
    data=p.read_bytes(); dest=OUT/rel; dest.parent.mkdir(exist_ok=True,parents=True); dest.write_bytes(data)
    item=dict(original=str(p),snapshot=rel.as_posix(),kind=kind,size=len(data),sha256=digest(data)); files.append(item); return item
for p in sorted(SRC.rglob('*')):
    if p.is_file(): preserve(p,pathlib.Path('source-quests')/p.relative_to(SRC),'server-quest-source')
print('Preserved',len(files),'source files',flush=True)
server_src=SRC.parent.parent/'Tools/NewServSource/src'
names=['QuestScript.cc','QuestScript.hh','Map.cc','Map.hh','Quest.cc','Quest.hh','QuestMetadata.cc','QuestMetadata.hh','CommandFormats.hh','StaticGameData.cc','StaticGameData.hh','Version.cc','Version.hh','Compression.cc','Compression.hh','Text.cc','Text.hh']
for name in names:
    p=server_src/name
    if p.exists(): preserve(p,pathlib.Path('reference/server-source')/name,'server-source-reference')
for p in (B/'reference').glob('*'):
    if p.is_file(): preserve(p,pathlib.Path('reference/decoder-source')/p.name,'decoder-source-reference')
for p in (B/'extracted/qedit-config').glob('*'):
    if p.is_file(): preserve(p,pathlib.Path('reference/qedit-config')/p.name,'recovered-qedit-config')
qedit=pathlib.Path(r'C:\Users\chasm\Documents\ChatGPT\PSOBB\Qedit')
for p in (qedit/'Information').glob('*.txt'): preserve(p,pathlib.Path('reference/qedit-notes')/p.name,'supplied-qedit-notes')
for name in ('FloorSet.ini','Eng.txt'):
    preserve(qedit/name,pathlib.Path('reference/qedit-external')/name,'external-qedit-override')
for p in (CLIENT/'data').glob('SetDataTable*.rel'): preserve(p,pathlib.Path('reference/client-map-tables')/p.name,'client-map-table')

db=sqlite3.connect(OUT/'quest-library.sqlite'); db.executescript('''
DROP TABLE IF EXISTS quests; DROP TABLE IF EXISTS functions; DROP TABLE IF EXISTS placements;
DROP TABLE IF EXISTS events; DROP TABLE IF EXISTS sections; DROP TABLE IF EXISTS random_records;
DROP TABLE IF EXISTS references_index; DROP TABLE IF EXISTS chunks; DROP TABLE IF EXISTS chunks_fts;
CREATE TABLE quests(key TEXT PRIMARY KEY, name TEXT, episode TEXT, language TEXT, category TEXT, metadata TEXT);
CREATE TABLE functions(quest_key TEXT,label TEXT,line INTEGER,body TEXT,PRIMARY KEY(quest_key,label));
CREATE TABLE placements(quest_key TEXT,kind TEXT,floor INTEGER,idx INTEGER,room INTEGER,wave INTEGER,type INTEGER,data TEXT,raw BLOB);
CREATE TABLE events(quest_key TEXT,floor INTEGER,event_id INTEGER,room INTEGER,wave INTEGER,format TEXT,data TEXT);
CREATE TABLE sections(quest_key TEXT,floor INTEGER,type INTEGER,offset INTEGER,data BLOB);
CREATE TABLE random_records(quest_key TEXT,floor INTEGER,kind TEXT,idx INTEGER,data TEXT);
CREATE TABLE references_index(quest_key TEXT,source TEXT,opcode TEXT,target TEXT,line INTEGER);
CREATE TABLE chunks(id INTEGER PRIMARY KEY,quest_key TEXT,kind TEXT,label TEXT,path TEXT,line INTEGER,body TEXT);
CREATE VIRTUAL TABLE chunks_fts USING fts5(body, content='chunks',content_rowid='id');
CREATE INDEX placement_lookup ON placements(quest_key,floor,room,wave);
CREATE INDEX event_lookup ON events(quest_key,floor,event_id);
CREATE INDEX chunk_lookup ON chunks(quest_key,kind,label);
''')
jout=(OUT/'retrieval-chunks.jsonl').open('w',encoding='utf-8'); counts=collections.Counter(); findings=[]
def chunk(key,kind,label,path,line,body):
    db.execute('INSERT INTO chunks(quest_key,kind,label,path,line,body) VALUES(?,?,?,?,?,?)',(key,kind,label,str(path),line,body))
    jout.write(json.dumps(dict(quest_key=key,kind=kind,label=label,path=str(path),line=line,verification='static-extracted',body=body),ensure_ascii=False)+'\n')
def actions(data,p):
    result=[]
    if p>len(data): return [dict(operation='invalid_action_offset',offset=p,payload_size=len(data))]
    while p<len(data):
        op=data[p]; p+=1
        if op in (0,1):
            result.append(dict(opcode=op,operation='nop' if op==0 else 'stop'))
            if op==1: return result
        elif op in (8,9,13):
            a,b=struct.unpack_from('<2H',data,p); p+=4
            result.append(dict(opcode=op,operation={8:'construct_objects',9:'construct_enemies',13:'construct_enemies_stop'}[op],room=a,group_or_wave=b))
            if op==13: return result
        elif op in (10,11):
            value=struct.unpack_from('<H',data,p)[0]; p+=2
            result.append(dict(opcode=op,operation='set_switch' if op==10 else 'clear_switch',switch=value))
        elif op==12:
            value=struct.unpack_from('<I',data,p)[0]; p+=4
            result.append(dict(opcode=op,operation='trigger_event',target=value))
        else: return result+[dict(operation='unknown_action',opcode=op,remaining_hex=data[p:].hex())]
    return result+[dict(operation='end_of_stream')]
def randomrow(key,floor,kind,idx,obj):
    db.execute('INSERT INTO random_records VALUES(?,?,?,?,?)',(key,floor,kind,idx,json.dumps(obj))); counts[kind]+=1

for n,r in enumerate(records):
    key=r['key']; folder=CAT/key
    a=(folder/'script.bind').read_bytes(); b=(folder/'rebuilt.bind').read_bytes()
    at,al,az=struct.unpack_from('<3I',a); bt,bl,bz=struct.unpack_from('<3I',b)
    codesame=a[at:al]==b[bt:bt+al-at] and not any(b[bt+al-at:bl]) and 0<=bl-bt-(al-at)<=3
    tablesame=a[al:]==b[bl:]
    assert codesame and tablesame,key
    headerdiff=[i for i,(x,y) in enumerate(zip(a[:at],b[:bt])) if x!=y]
    r['validation_detail']=dict(script_bytes_preserved=codesame,label_table_preserved=tablesame,header_different_offsets=headerdiff,padding_added=bl-bt-(al-at))
    r['generation_reuse']='review-header-before-rebuild' if r['roundtrip']=='differs' else 'static-reference-only'
    r['decoded_paths']={name:str(folder/name) for name in ('script.bind','map.datd','script.txt','script-offsets.txt','map.txt')}
    db.execute('INSERT INTO quests VALUES(?,?,?,?,?,?)',(key,r['name'],r['episode'],r['language'],r['category'],json.dumps(r,ensure_ascii=False)))
    text=(folder/'script.txt').read_text(encoding='utf-8'); starts=list(re.finditer(r'^(start|label[0-9A-F]+)(?:@0x[0-9A-F]+)?:',text,re.M))
    for i,m in enumerate(starts):
        body=text[m.start():starts[i+1].start() if i+1<len(starts) else len(text)]
        line=text.count('\n',0,m.start())+1
        db.execute('INSERT INTO functions VALUES(?,?,?,?)',(key,m[1],line,body)); counts['functions']+=1
        chunk(key,'function',m[1],folder/'script.txt',line,body)
    if (folder/'script-references.csv').stat().st_size:
        for ref in csv.DictReader((folder/'script-references.csv').open(encoding='utf-8')):
            db.execute('INSERT INTO references_index VALUES(?,?,?,?,?)',(key,ref['source'],ref['opcode'],ref['target'],int(ref['line'])))
    chunk(key,'header','header',folder/'script.txt',1,text[:starts[0].start()] if starts else text)
    data=(folder/'map.datd').read_bytes(); p=0; evts=[]; randomfloors=set()
    while p+16<=len(data):
        typ,size,floor,ds=struct.unpack_from('<4I',data,p)
        if typ==0:
            if any(data[p+16:]): findings.append(dict(key=key,kind='post-terminator-bytes',offset=p+16,length=len(data)-p-16))
            break
        assert size>=16 and ds<=size-16 and p+size<=len(data)
        payload=data[p+16:p+16+ds]; db.execute('INSERT INTO sections VALUES(?,?,?,?,?)',(key,floor,typ,p,data[p:p+size])); counts['sections']+=1
        if typ in (1,2):
            stride=68 if typ==1 else 72; assert ds%stride==0
            for idx in range(ds//stride):
                raw=payload[idx*stride:(idx+1)*stride]; u=struct.unpack_from('<8H' if typ==1 else '<10H',raw)
                obj=dict(base_type=u[0],set_flags=u[1],runtime_index=u[2],file_offset=p+16+idx*stride)
                if typ==1:
                    obj.update(floor_field=u[3],entity_id_field=u[4],group=u[5],room=u[6],unknown_a3=u[7]); pos=16; wave=None
                else:
                    obj.update(children=u[3],floor_field=u[4],entity_id_field=u[5],room=u[6],wave=u[7],wave2=u[8],unknown_a1=u[9]); pos=20; wave=u[7]
                obj['position']=struct.unpack_from('<3f',raw,pos); obj['angles']=struct.unpack_from('<3i',raw,pos+12)
                obj['params']=struct.unpack_from('<3f3i' if typ==1 else '<5f2h',raw,40 if typ==1 else 44)
                obj['unused_pointer']=struct.unpack_from('<I',raw,stride-4)[0]
                db.execute('INSERT INTO placements VALUES(?,?,?,?,?,?,?,?,?)',(key,'object' if typ==1 else 'enemy_npc',floor,idx,u[6],wave,u[0],json.dumps(obj),raw)); counts['objects' if typ==1 else 'enemy_npc_records']+=1
        elif typ==3:
            ao,eo,count=struct.unpack_from('<3I',payload); fmt=payload[12:16]; assert fmt in (b'\0\0\0\0',b'evt2'),fmt
            random=fmt==b'evt2'; stride=24 if random else 20
            assert eo+count*stride<=len(payload)
            if random: randomfloors.add(floor)
            for idx in range(count):
                raw=payload[eo+idx*stride:eo+(idx+1)*stride]
                eid,flags,et,room,wave=struct.unpack_from('<I4H',raw)
                e=dict(floor=floor,event_id=eid,flags=flags,event_type=et,room=room,wave=wave,format='evt2' if random else 'evt1')
                if random:
                    mind,maxd,mine,maxe,maxw,ap=struct.unpack_from('<2H2BHI',raw,12)
                    e.update(min_delay=mind,max_delay=maxd,min_enemies=mine,max_enemies=maxe,max_waves=maxw)
                else: e['delay_frames'],ap=struct.unpack_from('<2I',raw,12)
                e['actions']=actions(payload,ao+ap); e['file_offset']=p+16+eo+idx*stride
                evts.append(e); db.execute('INSERT INTO events VALUES(?,?,?,?,?,?,?)',(key,floor,eid,room,wave,e['format'],json.dumps(e))); counts[e['format']]+=1
                chunk(key,'event',f'floor{floor}/event{eid}',folder/'map.txt',0,json.dumps(e))
        elif typ==4:
            ro,lo,nrooms=struct.unpack_from('<3I',payload); maxoff=0; previous=-1
            for idx in range(nrooms):
                room,count,offset=struct.unpack_from('<2HI',payload,ro+idx*8)
                if room<previous: findings.append(dict(key=key,kind='random-rooms-unsorted',floor=floor))
                previous=room; maxoff=max(maxoff,offset+count*28)
                randomrow(key,floor,'random_rooms',idx,dict(room=room,count=count,location_byte_offset=offset))
            assert maxoff%28==0 and lo+maxoff<=len(payload)
            for idx in range(maxoff//28):
                pos=lo+idx*28; v=struct.unpack_from('<3f3i2H',payload,pos)
                randomrow(key,floor,'random_locations',idx,dict(position=v[:3],angles=v[3:6],unknown=v[6:]))
        elif typ==5:
            eo,wo,ec,wc=struct.unpack_from('<4I',payload)
            for idx in range(ec):
                v=struct.unpack_from('<5f2h4H',payload,eo+idx*32)
                randomrow(key,floor,'random_definitions',idx,dict(params1_to5=v[:5],param7=v[5],param6=v[6],entry_index=v[7],unknown=v[8],min_children=v[9],max_children=v[10]))
            for idx in range(wc):
                v=struct.unpack_from('<4B',payload,wo+idx*4)
                randomrow(key,floor,'random_weights',idx,dict(base_type_index=v[0],definition_index=v[1],weight=v[2],unknown=v[3]))
        else: findings.append(dict(key=key,kind='unrecognized-section',type=typ,floor=floor))
        p+=size
    ids={(e['floor'],e['event_id']) for e in evts}
    for e in evts:
        for action in e['actions']:
            if action['operation']=='trigger_event' and (e['floor'],action['target']) not in ids:
                findings.append(dict(key=key,kind='dynamic-event-target' if e['floor'] in randomfloors else 'absent-static-event-target',floor=e['floor'],event=e['event_id'],target=action['target']))
    if n%60==0: db.commit(); print('Indexed',n+1,'/',len(records),flush=True)

# Opcode specifications preserve exact source schemas; BB applicability is tagged, not inferred from names.
opcodes=[]
for source in (OUT/'reference/decoder-source/QuestScript.cc',OUT/'reference/server-source/QuestScript.cc'):
    comments=[]; last_entry=False
    for ln,line in enumerate(source.read_text(encoding='utf-8').splitlines(),1):
        if line.lstrip().startswith('//'):
            if last_entry: comments=[]
            comments.append(line.strip()[2:].strip()); last_entry=False
        m=re.match(r'^    \{(0x[0-9A-Fa-f]+), \{([^}]+)\}, (.*)\},$',line)
        if m:
            aliases=re.findall(r'"([^"]+)"',m[2]); supports=bool(re.search(r'\bF_(?:V\d_)?V4\b',m[3]))
            op=dict(opcode=m[1],aliases=aliases,schema_and_flags=m[3],supports_bb=supports,documentation='\n'.join(comments),source=str(source),line=ln)
            opcodes.append(op); last_entry=True
            if supports: chunk('', 'bb_opcode',m[1]+'/'+aliases[0],source,ln,json.dumps(op))
dump(OUT/'opcode-reference.json',opcodes)
qdefs=[]
for ln,line in enumerate((OUT/'reference/qedit-config/Asm.txt').read_text(encoding='utf-8',errors='replace').splitlines(),1):
    m=re.match(r'\{(0x[0-9a-fA-F]+), "([^"]+)", (.*)\}',line)
    if m: qdefs.append(dict(opcode=m[1],name=m[2],raw_operands=m[3],line=ln))
dump(OUT/'qedit-opcode-dialect.json',qdefs)
for f in files:
    if f['kind']=='server-quest-source' and pathlib.Path(f['snapshot']).suffix in ('.txt','.json'):
        text=(OUT/f['snapshot']).read_text(encoding='utf-8',errors='replace')
        # Keep authored include/metadata sources retrievable, without assuming they were compiled into active quests.
        if text.strip(): chunk('', 'supplied_source',f['snapshot'],OUT/f['snapshot'],1,text)
assets=[]
for directory,kind in ((CLIENT/'data/scene','client-scene'),(qedit/'map','qedit-map')):
    for p in directory.rglob('*'):
        if p.is_file(): assets.append(dict(kind=kind,path=str(p),name=p.name,bytes=p.stat().st_size,content_copied=False))
dump(OUT/'asset-index.json',assets)
db.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')"); db.commit()
assert db.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
db.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('integrity-check')")
db.commit(); jout.close()
counts['quest_variants']=len(records); counts['source_files']=sum(f['kind']=='server-quest-source' for f in files)
counts['quest_groups']=len({(r['category'],r['prefix'],r['filename_quest_id']) for r in records})
counts['indexed_assets']=len(assets); counts['retrieval_chunks']=db.execute('SELECT count(*) FROM chunks').fetchone()[0]
dump(OUT/'manifest.json',dict(date='2026-09-11',root=str(SRC),counts=counts,files=files,scope='Complete supplied quest directory snapshot; references and indexes; not all PSOBB knowledge',validation='Static only; no live Qedit compilation or game testing'))
dump(OUT/'quest-index.json',records); dump(OUT/'review-findings.json',findings)
db.close()
print(json.dumps(counts,indent=2)); print('Review classes',collections.Counter(f['kind'] for f in findings))
