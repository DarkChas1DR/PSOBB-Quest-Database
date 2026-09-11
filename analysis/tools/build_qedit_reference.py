"""Index Qedit's actual labels/presets separately from client class IDs."""
import hashlib,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[2]
REF=ROOT/'analysis/quest-knowledge/reference'
OUT=ROOT/'analysis/entity-database/qedit'

def dump(name,data):
    (OUT/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def main():
    OUT.mkdir(exist_ok=True)
    rows=[]
    for n,line in enumerate((REF/'qedit-config/npcname.ini').read_text(encoding='utf-8').splitlines(),1):
        cols=line.split('\t')
        if cols[0].isdigit(): rows.append(dict(dat_type=int(cols[0]),hex=f'0x{int(cols[0]):04X}',qedit_name=cols[1],field_labels=cols[2:],line=n))
    dump('entity-fields.json',rows)
    presets=[]; current=None
    for n,line in enumerate((REF/'qedit-config/monsters.txt').read_text(encoding='utf-8').splitlines(),1):
        if line.startswith('\t') and line.strip():
            current=dict(name=line.strip(),line=n,fields=[]); presets.append(current)
        elif current and '\t' in line:
            label,value=line.split('\t',1); current['fields'].append(dict(label=label,value=value))
    # Preserve repeated field labels (e.g. Unknown and wave fields) in their original order.
    for p in presets:
        skin=next((f['value'] for f in p['fields'] if f['label']=='Skin'),None)
        p['dat_type']=int(skin) if skin and skin.isdigit() else None
    dump('placement-presets.json',presets)
    floors=[]
    for variant in ('qedit-config','qedit-external'):
        current=None
        for n,line in enumerate((REF/variant/'FloorSet.ini').read_text(encoding='utf-8').splitlines(),1):
            line=line.split('//')[0].strip()
            if line.startswith('area '):
                current=dict(source=variant,area=int(line.split()[1]),line=n,lists={});floors.append(current)
            elif current and re.match(r'(mons|item)',line):
                parts=line.split(None,1); name=parts[0]; values=parts[1] if len(parts)>1 else ''
                current['lists'][name]=[int(x.strip()) for x in values.split(',') if x.strip()]
    dump('area-lists.json',floors)
    changes=[]
    for area in sorted({f['area'] for f in floors}):
        bundled=next((f['lists'].get('mons',[]) for f in floors if f['area']==area and f['source']=='qedit-config'),[])
        external=next((f['lists'].get('monsv4',[]) for f in floors if f['area']==area and f['source']=='qedit-external'),[])
        if set(bundled)!=set(external):changes.append(dict(area=area,bundled_only=sorted(set(bundled)-set(external)),external_v4_only=sorted(set(external)-set(bundled))))
    dump('area-differences.json',changes)
    # Assets are inventoried without inferring class or appearance selectors from filenames.
    client=pathlib.Path(r'C:\Users\chasm\Documents\ChatGPT\PSOBB\PSOBB.IO [Modded][DarkChas]')
    files=[client/'psobb.exe',client/'data/npcplayerchar.dat',client/'data/data.gsl']+sorted((client/'data').glob('pl*'))
    assets=[]
    for p in files:
        if p.is_file():assets.append(dict(path=p.relative_to(client).as_posix(),size=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),mapping_status='not yet decoded/visually verified'))
    dump('client-appearance-inputs.json',dict(client_status='user states this is a clean client; folder name is not used to infer modification status',files=assets))
    visual=json.loads((OUT.parent/'npc-visual-blocks.json').read_text(encoding='utf-8'))
    appearance=[]
    for block in visual:
        fields={}
        for line in block['body'].splitlines()[1:]:
            hit=re.match(r'\s*[0-9A-Fa-f]+\s+(\w+)\s+(.*)',line)
            if hit:fields[hit[1]]=hit[2]
        appearance.append(dict(quest_key=block['quest_key'],line=block['line'],decoded_fields=fields,evidence='newserv-decoded visual block; Qedit interpretation still requires verification'))
    dump('appearance-examples.json',appearance)
    page=['# Qedit quest entity fields and presets','', '[Reference guide](README.md)', '', 'These are DAT placement types, not player class IDs. Labels are copied as supplied, including spelling and unknown fields.', '', '| DAT type | Qedit name | Field labels | Presets |', '|---|---|---|---:|']
    for r in rows:
        page.append(f'| {r["dat_type"]} / {r["hex"]} | {r["qedit_name"]} | '+', '.join(r['field_labels']).replace('|','/')+f' | {sum(p["dat_type"]==r["dat_type"] for p in presets)} |')
    (OUT/'entity-fields.md').write_text('\n'.join(page)+'\n',encoding='utf-8')
    assert next(r for r in rows if r['dat_type']==33)['qedit_name'].startswith('Default Humar')
    assert next(r for r in rows if r['dat_type']==36)['qedit_name'].startswith('Default Ramar')
    for source,field in [('qedit-config','mons'),('qedit-external','monsv4')]:
        assert 64 not in next(f for f in floors if f['source']==source and f['area']==1)['lists'][field]
        assert 64 in next(f for f in floors if f['source']==source and f['area']==2)['lists'][field]
    stats=dict(entity_types=len(rows),presets=len(presets),area_entries=len(floors),differing_area_lists=len(changes),appearance_examples=len(appearance),client_inputs_hashed=len(assets),id_separation_checks='passed',hildebear_forest_checks='passed',qedit_runtime_builder_validation='not performed')
    dump('validation.json',stats);print(json.dumps(stats))

if __name__=='__main__':main()
