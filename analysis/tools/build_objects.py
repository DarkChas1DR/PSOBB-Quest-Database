"""Qedit-first object catalogue; observed use is not runtime validation."""
import collections,csv,json,pathlib,re,sqlite3
ROOT=pathlib.Path(__file__).resolve().parents[2];OUT=ROOT/'analysis/object-database';REF=ROOT/'analysis/quest-knowledge/reference'
def dump(name,data):
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def main():
    OUT.mkdir(exist_ok=True);labels={};presets=collections.defaultdict(list)
    for n,line in enumerate((REF/'qedit-config/itemsname.ini').read_text(encoding='utf-8').splitlines(),1):
        cols=line.split('\t')
        if cols[0].isdigit():labels[int(cols[0])]=dict(name=cols[1],field_labels=cols[2:],line=n)
    current=None
    for n,line in enumerate((REF/'qedit-config/Objs.txt').read_text(encoding='utf-8').splitlines(),1):
        if line.startswith('\t') and line.strip():current=dict(name=line.strip(),line=n,fields=[])
        elif current and '\t' in line:
            key,value=line.split('\t',1);current['fields'].append(dict(label=key,value=value))
            if key=='Skin' and value.isdigit():presets[int(value)].append(current)
    source=(REF/'server-source/Map.cc').read_text(encoding='utf-8');flags={k:int(v,16) for k,v in re.findall(r'static constexpr uint16_t (F_\w+) = (0x\w+);',source)}
    lo=source.index('static const std::vector<DATEntityDefinition> dat_object_definitions');hi=source.index('\n});',lo)
    defs=collections.defaultdict(list);comments=[]
    for n,line in enumerate(source[:hi].splitlines(),1):
        if n<=source[:lo].count('\n'):continue
        if line.strip().startswith('//'):comments.append(line.strip()[2:].strip());continue
        m=re.match(r'\s*\{(0x\w+),\s*([^,]+),\s*(0x\w+),\s*"([^"]+)"\},?(?:\s*//\s*(.*))?',line)
        if not m:continue
        ident,f,mask,ctor,note=m.groups();v=0
        for t in f.split('|'):v|=flags[t.strip()]
        text='\n'.join(comments);comments=[]
        if v&0x2000:defs[int(ident,16)].append(dict(constructor=ctor,area_mask=mask,notes=text,inline_note=note,line=n))
    menus=json.loads((ROOT/'analysis/entity-database/qedit/area-lists.json').read_text());areas=collections.defaultdict(list)
    for menu in menus:
        for key,ids in menu['lists'].items():
            if key not in ('item','itemv4'):continue
            for ident in ids:areas[ident].append(dict(area=menu['area'],source=menu['source'],list=key))
    observations=collections.defaultdict(list)
    db=sqlite3.connect((ROOT/'analysis/quest-knowledge/quest-library.sqlite').as_uri()+'?mode=ro',uri=True);db.row_factory=sqlite3.Row
    for row in db.execute("SELECT quest_key,floor,idx,type,data FROM placements WHERE kind='object'"):
        data=json.loads(row['data']);observations[row['type']].append(dict(quest=row['quest_key'],floor=row['floor'],index=row['idx'],data=data))
    known=sorted(set(labels)|set(presets)|set(defs)|set(areas)|set(observations));index=[]
    for ident in known:
        q=labels.get(ident,{});name=q.get('name',f'Unnamed object {ident}');key=f'{ident:04X}';seen=observations.get(ident,[])
        record=dict(id=ident,id_hex='0x'+key,name=name,qedit_fields=q,presets=presets.get(ident,[]),qedit_area_menus=areas.get(ident,[]),supporting_bb_definitions=defs.get(ident,[]),observed_records=len(seen),status=dict(catalogued=True,qedit_named=bool(q),source_documented=bool(defs.get(ident)),visually_checked=False,playtested=False))
        index.append(record);dump('objects/'+key+'.json',record)
        if seen:
            p=OUT/'observations'/f'{key}.csv';p.parent.mkdir(exist_ok=True)
            with p.open('w',encoding='utf-8',newline='') as f:
                w=csv.writer(f);w.writerow(['quest','floor','index','full_DAT_fields'])
                for x in seen:w.writerow([x['quest'],x['floor'],x['index'],json.dumps(x['data'])])
        page=[f'# {name} — {ident} / 0x{key}','','[Object catalogue](../README.md) · [Structured record](%s.json)'%key,'','Status: catalogued; source evidence below. **Not visually checked or playtested.**','','## Qedit field labels','','Labels preserve the supplied order, spelling and unknowns. Do not equate label position with a binary offset without checking the DAT schema.','',' | Field ordinal | Qedit label |','|---:|---|']
        page.extend(f'| {i+1} | {label} |' for i,label in enumerate(q.get('field_labels',[])))
        page+=['','[Qedit definitions](../../quest-knowledge/reference/qedit-config/itemsname.ini) · [DAT binary layout](../../quest-knowledge/DAT-SCHEMA.md)','','## Placement presets','']
        for preset in presets.get(ident,[]):page+=['### '+preset['name'],'','```text']+[x['label']+' = '+x['value'] for x in preset['fields']]+['```','']
        page+=['## Area menu availability','','These are Qedit menu entries, not proof of client compatibility. Bundled and external BB lists stay separate.','','| Area ID | Source |','|---:|---|']
        page.extend(f'| {a["area"]} | {a["source"]}: {a["list"]} |' for a in areas.get(ident,[]))
        page+=['','## Supporting constructor and parameter documentation','']
        for d in defs.get(ident,[]):page += [f'### {d["constructor"]}', '',f'[Source](../../quest-knowledge/reference/server-source/Map.cc#L{d["line"]}); BB area mask: {d["area_mask"]}.','','```text',d['notes'],d['inline_note'] or '', '```','']
        page+=['## Quest examples','',f'{len(seen)} observed placements, including language duplicates. References are examples, not validated templates.','']
        if seen:page += [f'[Every placement and its complete stored DAT fields](../observations/{key}.csv)','','| Quest | Floor | Entry |','|---|---:|---:|']
        unique=[]
        for x in seen:
            if x['quest'] not in unique:
                unique.append(x['quest']);page.append(f'| [{x["quest"]}](../../server-catalogue/{x["quest"]}/README.md) | {x["floor"]} | {x["index"]} |')
            if len(unique)>=20:break
        page+=['','Unknown parameters, valid ranges, precise switch/event/function semantics and appearance still need type-specific review. Do not assume one object type’s linking rules apply to another.','']
        (OUT/'objects'/f'{key}.md').write_text('\n'.join(page),encoding='utf-8')
    dump('objects.json',index)
    stats=dict(catalogued_ids=len(known),qedit_named_ids=len(labels),preset_types=len(presets),bb_defined_types=len(defs),observed_types=len(observations),observed_records=sum(len(v) for v in observations.values()),playtested=0)
    assert stats['observed_records']==186967
    dump('coverage.json',stats)
    page=['# Object catalogue','','A Qedit-first reference for quest creators. **First data batch: not a 100% validated behavior or appearance catalogue.**','','[Coverage](coverage.json) · [All structured object records](objects.json) · [Floor database](../floor-database/README.md)','','Includes the union of Qedit named IDs, presets, bundled/external BB area menus, supporting BB constructor definitions and observed quest object types. IDs missing from one source remain visible. Presets retain repeated parameter labels and raw values.','','Click an object for its fields, presets, area lists, source-documented parameters and quest examples. Complete placement exports retain positions, angles, groups and unknown fields. Dialogue/event/switch links are not automatically inferred from generic parameter names.','','| ID | Object | Presets | Placements | BB source definition |','|---|---|---:|---:|---|']
    for r in index:page.append(f'| {r["id"]} / {r["id_hex"]} | [{r["name"].replace("|","/")}](objects/{r["id"]:04X}.md) | {len(r["presets"])} | {r["observed_records"]} | {bool(r["supporting_bb_definitions"])} |')
    page+=['','## Remaining work','','Visual examples, per-field range validation, complete script linkage, classifying source disagreements, and in-game verification remain pending. Source comments may contain TODOs or incomplete reverse engineering. No unknown is silently marked verified.','']
    (OUT/'README.md').write_text('\n'.join(page),encoding='utf-8')
    for p in OUT.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):assert (p.parent/target.split('#')[0]).exists(),(p,target)
    print(stats)
if __name__=='__main__':main()
