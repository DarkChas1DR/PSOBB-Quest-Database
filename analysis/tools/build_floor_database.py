"""Build a general floor catalogue from client map tables and Qedit definitions."""
import hashlib,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[2];OUT=ROOT/'analysis/floor-database'
def main():
    areas=json.loads((ROOT/'analysis/entity-database/areas.json').read_text())
    menus=json.loads((ROOT/'analysis/entity-database/qedit/area-lists.json').read_text())
    labels={r['dat_type']:r['qedit_name'] for r in json.loads((ROOT/'analysis/entity-database/qedit/entity-fields.json').read_text())}
    records=[];variants=[]
    for p in sorted((OUT/'tables').glob('*.txt')):
        for n,line in enumerate(p.read_text().splitlines(),1):
            m=re.match(r'([0-9A-Fa-f]+)/([0-9A-Fa-f]+)/([0-9A-Fa-f]+)\s*=>\s*(\S+)\s+(\S+)\s+(\S+)',line)
            if not m:continue
            a,l,e,o,en,s=m.groups();variants.append(dict(table=p.stem,area=int(a,16),layout=int(l,16),entities=int(e,16),object_basename=o,enemy_event_basename=en,setup_basename=s,line=n))
    assert {v['table'] for v in variants}=={'SetDataTableOn','SetDataTableOff','SetDataTableOnUlti','SetDataTableOffUlti'}
    for a in areas:
        r=dict(a,variants=[v for v in variants if v['area']==a['area']],qedit_lists=[m for m in menus if m['area']==a['area']],room_geometry_status='not decoded',complete_room_ids=False)
        records.append(r)
        page=[f'# Episode {a["episode"]}: {a["name"]}','','[General floor database](README.md)','','| Identifier | Value |','|---|---|',f'| Default floor slot | {a["default_floor"]} |',f'| Area ID | {a["area"]} / 0x{a["area"]:02X} |','','A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.','','## Available map-table entries','','Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.','','| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |','|---|---:|---:|---|---|---|']
        for v in r['variants']:page.append(f'| [{v["table"]}](tables/{v["table"]}.txt#L{v["line"]}) | {v["layout"]} | {v["entities"]} | {v["object_basename"]} | {v["enemy_event_basename"]} | {v["setup_basename"]} |')
        if not r['variants']:page+=['','No entries found in the four supplied tables; do not invent a layout.']
        page+=['','## Qedit placement menus','','Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.']
        for menu in r['qedit_lists']:
            page+=['',f'### {menu["source"]}','']
            for name,ids in menu['lists'].items():
                if name not in ('mons','item','monsv4','itemv4'):continue
                value=', '.join(f'{i} ({labels.get(i,"unnamed")})' if name.startswith('mons') else str(i) for i in ids)
                page.append(f'**{name}:** {value or "Empty list"}\n')
        page+=['','## Rooms, collision and coordinates','','Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.','','[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.','','[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)','']
        (OUT/f'area-{a["area"]:02X}.md').write_text('\n'.join(page),encoding='utf-8')
    (OUT/'floors.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
    index=['# General floor and map database','','This catalogue is independent of individual quests. It covers the 47 named area definitions for Episodes 1, 2 and 4, including boss, lobby, battle and test areas. It joins all four supplied client map tables with Qedit’s bundled and external area menus.','','**Coverage:** area IDs, default floor slots, layout/entity variation indices, resource basenames, and editor placement menus. **Not yet complete:** geometric room IDs, boundaries, transforms, collision and safe spawn locations for every layout.','','[Machine-readable floor database](floors.json) · [Observed quest sections](../map-sections/README.md) · [Monster database](../entity-database/monsters.md) · [NPC database](../entity-database/npcs.md)','','## Creating a quest','','1. Choose the episode and area.\n2. Choose the appropriate multiplayer/solo and difficulty map table.\n3. Select layout and entity variation separately.\n4. Check Qedit’s placement menu and the documented constructor restrictions.\n5. Obtain verified room geometry and spawn positions for that layout before adding entities.\n6. Link rooms/waves/switches to the quest script and test in-game.','']
    for ep in (1,2,4):
        index += [f'## Episode {ep}','','| Area | Default floor | Name | Map-table entries |','|---|---:|---|---:|']
        for r in records:
            if r['episode']==ep:index.append(f'| 0x{r["area"]:02X} | {r["default_floor"]} | [{r["name"]}](area-{r["area"]:02X}.md) | {len(r["variants"])} |')
        index.append('')
    (OUT/'README.md').write_text('\n'.join(index),encoding='utf-8')
    assert len(records)==47
    for page in OUT.glob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',page.read_text(encoding='utf-8')):assert (page.parent/target.split('#')[0]).exists(),(page,target)
    checks=dict(areas=len(records),map_table_entries=len(variants),tables=4,linked_entries=sum(len(r['variants']) for r in records),geometry_complete=False)
    assert checks['linked_entries']==len(variants)
    (OUT/'validation.json').write_text(json.dumps(checks,indent=2)+'\n')
    print(checks)
if __name__=='__main__':main()
