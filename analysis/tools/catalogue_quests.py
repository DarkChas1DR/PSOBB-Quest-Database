"""Catalogue supplied quest files without writing beside originals or executing quests."""
import collections,csv,hashlib,json,pathlib,re,shutil,struct,subprocess,sys
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
ROOT=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(r'C:\Users\chasm\Documents\ChatGPT\PSOBB')
BASE=pathlib.Path(__file__).resolve().parents[1]
OUT=pathlib.Path(sys.argv[2]).resolve() if len(sys.argv)>2 else BASE/'catalogue'; OUT.mkdir(exist_ok=True)
NS=BASE/'tools/newserv/release/newserv-windows.exe'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run(args,log):
    r=subprocess.run([str(NS),*map(str,args)],capture_output=True,timeout=90)
    log.append({'action':str(args[0]),'returncode':r.returncode,'stderr':r.stderr.decode('utf-8','replace')[-4000:]})
    if r.returncode: raise RuntimeError(log[-1]['stderr'])
def savecsv(p,rows):
    if not rows: p.write_text('',encoding='utf-8'); return
    with p.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
def link(p,label=None): return f'[{label or p.name}](<{p.as_posix()}>)'
def decode_dat(b):
    offset=0; objects=[]; enemies=[]; sections=[]; evts=[]; issues=[]
    while offset+16<=len(b):
        typ,size,floor,ds=struct.unpack_from('<4I',b,offset)
        if typ==0:
            if any(b[offset:]): issues.append('Nonzero data after terminal header')
            break
        assert size>=16 and ds<=size-16 and offset+size<=len(b),(offset,typ,size,ds)
        data=b[offset+16:offset+16+ds]; sec=dict(floor=floor,type=typ,offset=offset,data_bytes=ds)
        if typ in (1,2):
            stride=68 if typ==1 else 72; assert ds%stride==0
            sec['records']=ds//stride
            for n in range(ds//stride):
                r=data[n*stride:(n+1)*stride]
                row=dict(floor=floor,index=n,type=f'0x{struct.unpack_from("<H",r)[0]:04X}',room=struct.unpack_from('<H',r,12)[0])
                if typ==1:
                    row['group']=struct.unpack_from('<H',r,10)[0]; po=16
                else:
                    row['wave'],row['wave2']=struct.unpack_from('<2H',r,14); row['children']=struct.unpack_from('<H',r,6)[0]; po=20
                row.update(zip(('x','y','z'),struct.unpack_from('<3f',r,po)))
                params=struct.unpack_from('<3f3i',r,40) if typ==1 else struct.unpack_from('<5f2h',r,44)
                row.update({f'p{i+1}':v for i,v in enumerate(params)})
                (objects if typ==1 else enemies).append(row)
        elif typ==3:
            actionoff,entryoff,count,fmt=struct.unpack_from('<4I',data); sec['records']=count; sec['format']=fmt
            if fmt: issues.append(f'Floor {floor}: random-format events require separate interpretation')
            else:
                assert entryoff+count*20<=len(data)
                for n in range(count):
                    eid,flags,et,room,wave,delay,ap=struct.unpack_from('<I4H2I',data,entryoff+n*20)
                    p=actionoff+ap; actions=[]; targets=[]
                    while p<len(data):
                        op=data[p]; p+=1
                        if op==1: actions.append('stop'); break
                        if op==0: actions.append('nop'); continue
                        if op in (8,9):
                            a,c=struct.unpack_from('<2H',data,p); p+=4
                            actions.append(f'{"construct_objects" if op==8 else "construct_enemies"}(room={a},group_or_wave={c})')
                        elif op in (10,11):
                            v=struct.unpack_from('<H',data,p)[0]; p+=2
                            actions.append(f'{"set_switch" if op==10 else "clear_switch"}({v})')
                        elif op==12:
                            v=struct.unpack_from('<I',data,p)[0]; p+=4; targets.append(v); actions.append(f'trigger_event({v})')
                        else:
                            issues.append(f'Floor {floor} event {eid}: unparsed action 0x{op:02X}; see native map listing')
                            actions.append(f'UNPARSED_0x{op:02X}'); break
                    evts.append(dict(floor=floor,event_id=eid,room=room,wave=wave,delay_frames=delay,event_type=et,actions='; '.join(actions),targets=targets))
        sections.append(sec); offset+=size
    else: issues.append('No complete terminal header encountered')
    ids={(e['floor'],e['event_id']) for e in evts}
    for e in evts:
        for t in e.pop('targets'):
            if (e['floor'],t) not in ids: issues.append(f'Floor {e["floor"]}: event {e["event_id"]} targets absent event {t}')
        matches=[n for n in enemies if (n['floor'],n['room'],n['wave'])==(e['floor'],e['room'],e['wave'])]
        e['enemy_records']=len(matches)
        e['enemy_types']=json.dumps(dict(collections.Counter(n['type'] for n in matches)))
    return objects,enemies,evts,sections,issues
def inspect_script(text):
    labels={}; current=None; opcounts=collections.Counter(); refs=[]; floor_maps=[]; important=[]
    for lineno,line in enumerate(text.splitlines(),1):
        m=re.match(r'^(start|label[0-9A-F]+)(?:@0x[0-9A-F]+)?:',line)
        if m:
            current=m[1]; labels[current]=dict(label=current,line=lineno,instructions=0); continue
        m=re.match(r'^  ([a-zA-Z_][\w!<>=]*)\s*(.*)',line)
        if not m: continue
        op,args=m.groups(); opcounts[op]+=1
        if current: labels[current]['instructions']+=1
        for dst in re.findall(r'\blabel[0-9A-F]+\b',args):
            refs.append(dict(source=current,opcode=op,target=dst,line=lineno))
        if op=='bb_map_designate': floor_maps.append(args)
        if re.search(r'handler|set_qt_|timer|time|sync_register|item|meseta|flag|switch',op) or re.search(r'\br25[345]\b',args):
            important.append(dict(label=current,line=lineno,opcode=op,args=args))
    return labels,opcounts,refs,floor_maps,important

inputs=sorted([p for p in (ROOT.rglob('*') if len(sys.argv)>1 else ROOT.iterdir()) if p.is_file() and re.fullmatch(r'[a-z]\d+-bb-[a-z]\.(bin|qst)',p.name)],key=lambda p:(str(p.parent),int(re.search(r'\d+',p.name)[0]),p.name))
catalogue=[]
for source in inputs:
    stem=source.stem; key=(source.relative_to(ROOT).parent/stem).as_posix(); folder=OUT/key; folder.mkdir(exist_ok=True,parents=True); log=[]
    record=dict(key=key,category=source.relative_to(ROOT).parent.as_posix(),prefix=stem[0],filename_quest_id=int(re.search(r'\d+',stem)[0]),language=stem[-1].upper(),source=str(source),source_sha256=sha(source),status='pending')
    try:
        if source.suffix=='.qst':
            copied=folder/source.name; shutil.copyfile(source,copied); run(['decode-qst',copied],log)
            bins=list(folder.glob(source.name+'-*.bin')); dats=list(folder.glob(source.name+'-*.dat'))
            assert len(bins)==1 and len(dats)==1,(bins,dats)
            binp,datp=bins[0],dats[0]
        else:
            binp=source
            datp=source.parent/(stem+'.dat')
            if not datp.exists(): datp=source.parent/(re.sub(r'-[a-z]$','',stem)+'.dat')
            assert datp.exists(),f'Missing DAT for {source.name}'
        record['map_sha256']=sha(datp)
        run(['decompress-prs',binp,folder/'script.bind'],log)
        run(['decompress-prs',datp,folder/'map.datd'],log)
        run(['disassemble-quest-script','--bb','--language='+record['language'],'--map-file='+str(datp),binp,folder/'script-offsets.txt'],log)
        run(['disassemble-quest-script','--bb','--language='+record['language'],'--reassembly','--map-file='+str(datp),binp,folder/'script.txt'],log)
        run(['disassemble-quest-map','--bb',datp,folder/'map.txt'],log)
        text=(folder/'script.txt').read_text(encoding='utf-8')
        for field,pat in [('name',r'^\.name "(.*)"'),('episode',r'^\.episode (\w+)'),('header_quest_id',r'^\.quest_num (\d+)')]:
            m=re.search(pat,text,re.M); record[field]=m[1] if m else 'unknown'
        oo,ee,ev,secs,issues=decode_dat((folder/'map.datd').read_bytes())
        record.update(objects=len(oo),enemy_npc_records=len(ee),events=len(ev),floors=sorted(set(s['floor'] for s in secs)),issues=issues)
        labels,ops,refs,maps,important=inspect_script(text)
        record.update(labels=len(labels),instructions=sum(ops.values()),map_designations=maps)
        savecsv(folder/'objects.csv',oo); savecsv(folder/'enemies.csv',ee); savecsv(folder/'waves.csv',ev)
        savecsv(folder/'labels.csv',list(labels.values())); savecsv(folder/'script-references.csv',refs); savecsv(folder/'state-and-rewards.csv',important)
        (folder/'opcodes.json').write_text(json.dumps(ops,indent=2))
        try:
            run(['assemble-quest-script',folder/'script.txt',folder/'rebuilt.bin'],log)
            run(['decompress-prs',folder/'rebuilt.bin',folder/'rebuilt.bind'],log)
            original=(folder/'script.bind').read_bytes(); rebuilt=(folder/'rebuilt.bind').read_bytes()
            same=original==rebuilt
            record['roundtrip']='byte-identical' if same else 'differs'
            if not same:
                ot,ol,osize=struct.unpack_from('<3I',original); nt,nl,nsize=struct.unpack_from('<3I',rebuilt)
                header_same=original[:4]==rebuilt[:4] and original[12:ot]==rebuilt[12:nt]
                padding=rebuilt[nt+ol-ot:nl]
                alignment_only=(ot==nt and header_same and original[ot:ol]==rebuilt[nt:nt+ol-ot] and original[ol:]==rebuilt[nl:] and 0<len(padding)<=3 and not any(padding) and nl%4==0)
                record['roundtrip']='alignment-only' if alignment_only else 'differs'
                if alignment_only: record['padding_bytes_added']=len(padding)
                else: issues.append('Reassembled bytes differ beyond recognized alignment; inspect before rebuilding')
        except Exception as ex:
            record['roundtrip']='failed'; issues.append('Reassembly failed; see tool-log.json')
        for feat,pat in [('timers',r'timer|winset_time|set_timer'),('item_operations',r'item'),('meseta',r'meseta'),('synchronization',r'sync_register|sync_leti'),('quest_flags',r'flag')]:
            record[feat]=sum(v for k,v in ops.items() if re.search(pat,k))
        savecsv(folder/'floor-summary.csv',[dict(floor=f,objects=sum(x['floor']==f for x in oo),enemy_npc_records=sum(x['floor']==f for x in ee),events=sum(x['floor']==f for x in ev)) for f in record['floors']])
        # File-difference checks are evidence, not a claim that language variants behave identically.
        record['decompressed_map_sha256']=sha(folder/'map.datd')
        record['script_shape_sha256']=hashlib.sha256('\n'.join(re.sub(r'"(?:\\.|[^"\\])*"','"TEXT"',line) for line in text.splitlines() if not line.startswith('.') and not line.lstrip().startswith('//')).encode()).hexdigest()
        backup=source.parent/(source.name+'.bak')
        if backup.exists():
            run(['decompress-prs',backup,folder/'backup.bind'],log)
            record['backup_decompressed_identical']=(folder/'backup.bind').read_bytes()==(folder/'script.bind').read_bytes()
            run(['disassemble-quest-script','--bb','--language=E','--reassembly',backup,folder/'backup-script.txt'],log)
            import difflib
            normalize=lambda s:[line for line in s.splitlines(True) if not line.lstrip().startswith('//')]
            diff=''.join(difflib.unified_diff(normalize((folder/'backup-script.txt').read_text(encoding='utf-8')),normalize(text),fromfile='backup-script',tofile='current-script'))
            (folder/'backup-diff.txt').write_text(diff,encoding='utf-8')
        metadata=source.parent/(stem.split('-')[0]+'.json')
        if metadata.exists(): shutil.copyfile(metadata,folder/'server-metadata.json')
        record['status']='decoded'
        body=f'# {record["name"]} — {key}\n\n'
        body+=f'{record["episode"]}; header quest ID {record["header_quest_id"]}; language {record["language"]}. Static scan: **{len(oo)} objects, {len(ee)} enemy/NPC records, {len(ev)} events, {len(labels)} script labels.** Script roundtrip: {record["roundtrip"]}.\n\n'
        body+='This is a structural dossier, not a claim that every branch has been manually interpreted or playtested. Enemy/NPC records are not gameplay kill totals. Event IDs, wave numbers, object groups and script labels are distinct namespaces.\n\n'
        body+='## Read and inspect\n\n'
        for fn,desc in [('script-offsets.txt','Script with byte offsets and map references'),('script.txt','Reassembly syntax with explicit labels'),('map.txt','Complete placements and event actions'),('waves.csv','Every parsed wave and its next actions'),('objects.csv','Object fields'),('enemies.csv','Enemy/NPC fields'),('script-references.csv','Explicit script references, including handlers; not a complete dynamic call graph'),('state-and-rewards.csv','State, timing and reward operation locations'),('labels.csv','Function/label index')]:
            body+=f'- {link(folder/fn,desc)}\n'
        body+='\n## Area designations\n\nOperands: floor, area, type, layout variation, entities variation.\n\n'
        body+='```text\n'+'\n'.join(maps)+'\n```\n'
        body+='\n## Floors\n\n| Floor | Objects | Enemy/NPC records | Events |\n|---|---:|---:|---:|\n'
        for f in record['floors']: body+=f'| {f} | {sum(x["floor"]==f for x in oo)} | {sum(x["floor"]==f for x in ee)} | {sum(x["floor"]==f for x in ev)} |\n'
        body+='\n## Wave progression\n\nNumbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.\n\n| Floor | Event | Room / wave | Records | Delay | Completion actions |\n|---|---:|---|---:|---:|---|\n'
        for e in ev: body+=f'| {e["floor"]} | {e["event_id"]} | {e["room"]} / {e["wave"]} | {e["enemy_records"]} | {e["delay_frames"]} | {e["actions"]} |\n'
        body+='\n## Review notes\n\n'+('\n'.join('- '+i for i in issues) if issues else 'No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.')+'\n'
        if backup.exists(): body+=f'\nA backup is present; decompressed content identical: {record["backup_decompressed_identical"]}. See {link(folder/"backup-diff.txt","text differences")}.\n'
        if metadata.exists(): body+=f'\nAdditional {link(folder/"server-metadata.json","server metadata")} is supplied. It is separate from quest bytecode and can affect drops.\n'
        (folder/'README.md').write_text(body,encoding='utf-8')
    except Exception as ex:
        record['status']='failed'; record['error']=str(ex)
    (folder/'tool-log.json').write_text(json.dumps(log,indent=2),encoding='utf-8')
    (folder/'summary.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
    catalogue.append(record)
    print(key,record.get('name'),record['status'],record.get('roundtrip'),flush=True)
(OUT/'catalogue.json').write_text(json.dumps(catalogue,indent=2),encoding='utf-8')
groups=collections.defaultdict(list)
for r in catalogue: groups[(r['category'],r['prefix'],r['filename_quest_id'])].append(r)
body='# Episode 1 and Episode 2 quest catalogue\n\nStatic analysis of the quest files in the supplied PSOBB folder. Original inputs are unchanged. Each dossier includes every parsed wave, placements, script labels, reference links and state/reward operation locations. Runtime behavior and full branch semantics require further review.\n\n'
body+=f'**{len(groups)} quest filename IDs; {len(catalogue)} language variants; {sum(r["status"]=="decoded" for r in catalogue)} decoded.** Counts include the previously analysed TTF.\n\n'
body+='| ID | Quest | Episode | Languages | Objects | Enemy/NPC records | Events | English roundtrip |\n|---|---|---|---|---:|---:|---:|---|\n'
comparisons=[]
for group,rs in sorted(groups.items()):
    qid='/'.join(map(str,group))
    en=next((r for r in rs if r['language']=='E'),rs[0]); folder=OUT/en['key']
    body+=f'| {qid} | {link(folder/"README.md",en.get("name",en["key"]))} | {en.get("episode","?")} | '+', '.join(link(OUT/r['key']/'README.md',r['language']) for r in rs)+f' | {en.get("objects","?")} | {en.get("enemy_npc_records","?")} | {en.get("events","?")} | {en.get("roundtrip","failed")} |\n'
    if len(rs)>1 and all(r['status']=='decoded' for r in rs):
        comparisons.append(dict(quest_id=qid,maps_identical=len({r['decompressed_map_sha256'] for r in rs})==1,script_shape_identical_ignoring_text=len({r['script_shape_sha256'] for r in rs})==1))
body+='\n## Validation and limits\n\n'
body+=f'- Byte-identical decompressed script roundtrips: {sum(r.get("roundtrip")=="byte-identical" for r in catalogue)} / {len(catalogue)} variants.\n'
body+=f'- Alignment-only roundtrip differences: {sum(r.get("roundtrip")=="alignment-only" for r in catalogue)} variants. These preserve script bytes and label tables, adding 1–3 zero bytes before the table and updating header offsets/size. They are not byte-identical files.\n'
body+='- Enemy counts include NPCs and constructor records; they are not kill counts.\n- Script references include callbacks and registrations, not just calls. Dynamic targets are not fully resolved.\n- Header and filename quest IDs are retained separately. Language variants are compared; identical maps do not prove identical script behavior.\n- Newserv assembly text is not directly promised to import into Qedit.\n'
issues=[(r['key'],i) for r in catalogue for i in r.get('issues',[])]
body+='\n## Items requiring review\n\n'+ ('\n'.join(f'- {k}: {i}' for k,i in issues) if issues else 'No structural/event-target issues found by the implemented checks.')+'\n'
for r in catalogue:
    if r['status']=='failed': body+=f'- FAILED {r["key"]}: {r["error"]}\n'
(OUT/'README.md').write_text(body,encoding='utf-8')
(OUT/'language-comparisons.json').write_text(json.dumps(comparisons,indent=2))
print('TOTAL',len(groups),'quests',len(catalogue),'variants',len(issues),'review notes',flush=True)
