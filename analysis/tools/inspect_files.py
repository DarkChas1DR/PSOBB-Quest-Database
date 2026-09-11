"""Read-only inspection of supplied PSOBB files; outputs go to analysis/."""
import collections, csv, hashlib, json, pathlib, re, struct

ROOT = pathlib.Path(r'C:\Users\chasm\Documents\ChatGPT\PSOBB')
OUT = pathlib.Path(__file__).resolve().parents[1]
def u16(b, p): return struct.unpack_from('<H', b, p)[0]
def u32(b, p): return struct.unpack_from('<I', b, p)[0]
def csvout(name, rows):
    if not rows: return
    with (OUT/'extracted'/name).open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

inventory=[]
for rel in ['q118-bb-e.bin','q118-bb-j.bin','q118-bb.dat','Qedit/Qedit1.exe','Qedit/qedit/Qedit.exe','PSOBB.IO [Modded][DarkChas]/psobb.exe']:
    p=ROOT/rel; b=p.read_bytes()
    item={'path':str(p),'size':len(b),'sha256':hashlib.sha256(b).hexdigest()}
    if b[:2]==b'MZ':
        pe=u32(b,60); assert b[pe:pe+4]==b'PE\0\0'
        n=u16(b,pe+6); opt=pe+24; imagebase=u32(b,opt+28)
        item.update(machine=hex(u16(b,pe+4)),imagebase=hex(imagebase),entrypoint_rva=hex(u32(b,opt+16)))
        sections=[]
        for i in range(n):
            p0=opt+u16(b,pe+20)+40*i
            name=b[p0:p0+8].rstrip(b'\0').decode('ascii','replace')
            vs,va,rs,rp=struct.unpack_from('<IIII',b,p0+8)
            sections.append(dict(name=name,virtual_size=vs,rva=va,raw_size=rs,raw_offset=rp))
        item['sections']=sections
        def va_for(offset):
            for s in sections:
                if s['raw_offset']<=offset<s['raw_offset']+s['raw_size']:
                    return imagebase+s['rva']+offset-s['raw_offset']
        hits=[]
        patterns=re.compile(r'quest|\.bin|\.dat|\.qst|\.prs|\.ppk|asm\.txt|npcname|itemsname|TSetEvt|TObjQuest|TObjArea|TEnemy|bb_map|set_episode|map_forest|map_cave|map_machine|map_ancient|QEdit|Qedit|Version',re.I)
        for m in re.finditer(rb'[\x20-\x7E]{5,}', b):
            s=m.group().decode('ascii')
            if patterns.search(s) and len(s)<600:
                va=va_for(m.start()); refs=[]
                if va is not None:
                    needle=struct.pack('<I',va)
                    for sec in sections:
                        if sec['name'] in ('.text','CODE'):
                            lo=sec['raw_offset']; hi=lo+sec['raw_size']; idx=b.find(needle,lo,hi)
                            while idx>=0 and len(refs)<12:
                                refs.append(hex(va_for(idx))); idx=b.find(needle,idx+1,hi)
                hits.append({'file_offset':hex(m.start()),'va':hex(va) if va else '', 'pointer_matches':';'.join(refs),'text':s})
        csvout(pathlib.Path(rel).stem+'-strings.csv', hits)
        item['relevant_ascii_strings']=len(hits)
    inventory.append(item)
(OUT/'inventory.json').write_text(json.dumps(inventory,indent=2),encoding='utf-8')

b=(OUT/'extracted/ttf.datd').read_bytes(); off=0; sections=[]; objects=[]; enemies=[]; events=[]
while off+16<=len(b):
    typ,size,floor,ds=struct.unpack_from('<4I',b,off)
    if typ==0:
        assert b[off:]==bytes(len(b)-off); break
    assert size>=16 and ds<=size-16 and off+size<=len(b)
    data=b[off+16:off+16+ds]
    row=dict(offset=hex(off),type=typ,floor=floor,size=size,data_size=ds)
    if typ in (1,2):
        stride=68 if typ==1 else 72; assert ds%stride==0; row['count']=ds//stride
        for j in range(ds//stride):
            r=data[j*stride:(j+1)*stride]
            entry=dict(floor=floor,index=j,file_offset=hex(off+16+j*stride),type=hex(u16(r,0)),room=u16(r,12))
            if typ==1:
                entry['group']=u16(r,10); xyz=16; params=40
            else:
                entry.update(wave=u16(r,14),wave2=u16(r,16),children=u16(r,6)); xyz=20; params=44
            entry.update(zip(('x','y','z'), struct.unpack_from('<3f',r,xyz)))
            if typ==1:
                entry.update(zip(('p1','p2','p3','p4','p5','p6'),struct.unpack_from('<3f3i',r,params)))
                objects.append(entry)
            else:
                entry.update(zip(('p1','p2','p3','p4','p5','p6','p7'),struct.unpack_from('<5f2h',r,params)))
                enemies.append(entry)
    elif typ==3:
        ao,eo,count,fmt=struct.unpack_from('<4I',data); assert fmt==0 and eo+count*20<=ds and ao<=ds
        row['count']=count
        for j in range(count):
            eid,flags,et,room,wave,delay,ap=struct.unpack_from('<I4H2I',data,eo+j*20)
            actions=[]; pos=ao+ap
            while True:
                opcode=data[pos]; pos+=1
                if opcode==1: actions.append('stop'); break
                if opcode==0: actions.append('nop'); continue
                if opcode in (8,9):
                    a,c=struct.unpack_from('<HH',data,pos); pos+=4
                    actions.append(f'{"construct_objects" if opcode==8 else "construct_enemies"}(room={a},group_or_wave={c})')
                elif opcode in (10,11):
                    v=u16(data,pos); pos+=2; actions.append(f'{"set_switch" if opcode==10 else "clear_switch"}({v})')
                elif opcode==12:
                    v=u32(data,pos); pos+=4; actions.append(f'trigger_event({v})')
                else: raise ValueError(f'Unknown event opcode {opcode} on floor {floor}, event {eid}')
            events.append(dict(floor=floor,event_id=eid,room=room,wave=wave,delay_frames=delay,action_offset=ap,event_type=et,actions='; '.join(actions)))
    sections.append(row); off+=size
csvout('objects.csv',objects); csvout('enemy-sets.csv',enemies); csvout('events.csv',events)
(OUT/'extracted/dat-sections.json').write_text(json.dumps(sections,indent=2))
summary=[]
for fl in sorted(set(x['floor'] for x in sections)):
    oo=[x for x in objects if x['floor']==fl]; ee=[x for x in enemies if x['floor']==fl]; ev=[x for x in events if x['floor']==fl]
    summary.append(dict(floor=fl,objects=len(oo),enemy_sets=len(ee),events=len(ev),enemy_types=dict(collections.Counter(x['type'] for x in ee))))
(OUT/'extracted/floor-summary.json').write_text(json.dumps(summary,indent=2))
ids={(x['floor'],x['event_id']) for x in events}; missing=[]
for event in events:
    for target in re.findall(r'trigger_event\((\d+)\)',event['actions']):
        if (event['floor'],int(target)) not in ids: missing.append([event['floor'],event['event_id'],int(target)])
original=(OUT/'extracted/ttf.bind').read_bytes(); rebuilt=(OUT/'extracted/ttf-reassembled.bind').read_bytes()
validation=dict(script_roundtrip_byte_identical=original==rebuilt,script_decompressed_sha256=hashlib.sha256(original).hexdigest(),dat_bytes=len(b),section_count=len(sections),dat_end_offset=hex(off),event_action_targets_missing=missing)
assert validation['script_roundtrip_byte_identical'] and not missing
(OUT/'validation.json').write_text(json.dumps(validation,indent=2))
by_wave=collections.defaultdict(list)
for e in enemies: by_wave[(e['floor'],e['room'],e['wave'])].append(e)
wave_rows=[]
for e in events:
    group=by_wave[(e['floor'],e['room'],e['wave'])]
    wave_rows.append(dict(**e,enemy_set_records=len(group),types=json.dumps(dict(collections.Counter(x['type'] for x in group)))))
csvout('wave-chains.csv',wave_rows)
print(json.dumps({'inventory':[{k:v for k,v in i.items() if k not in ('sections',)} for i in inventory], 'floors':summary,'totals':dict(objects=len(objects),enemy_sets=len(enemies),events=len(events))},indent=2))
