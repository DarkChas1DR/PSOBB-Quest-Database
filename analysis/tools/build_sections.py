"""Index observed DAT rooms without claiming complete map geometry."""
import collections,json,pathlib,re,sqlite3
ROOT=pathlib.Path(__file__).resolve().parents[2];CAT=ROOT/'analysis/server-catalogue';OUT=ROOT/'analysis/map-sections'
def main():
    OUT.mkdir(exist_ok=True)
    db=sqlite3.connect((ROOT/'analysis/quest-knowledge/quest-library.sqlite').as_uri()+'?mode=ro',uri=True)
    db.row_factory=sqlite3.Row
    quests=json.loads((CAT/'catalogue.json').read_text(encoding='utf-8'))
    allrooms=collections.defaultdict(dict)
    def room(key,floor,rid):
        return allrooms[key].setdefault((floor,rid),dict(floor=floor,room=rid,objects=0,enemy_npc_records=0,waves=set(),events=[],random_locations=0))
    for r in db.execute('SELECT quest_key,floor,room,kind,wave,count(*) AS n FROM placements GROUP BY quest_key,floor,room,kind,wave'):
        x=room(r['quest_key'],r['floor'],r['room'])
        x['objects' if r['kind']=='object' else 'enemy_npc_records']+=r['n']
        if r['kind']!='object':x['waves'].add(r['wave'])
    for r in db.execute('SELECT quest_key,floor,room,event_id FROM events'):
        room(r['quest_key'],r['floor'],r['room'])['events'].append(r['event_id'])
    for r in db.execute("SELECT quest_key,floor,data FROM random_records WHERE kind='random_rooms'"):
        data=json.loads(r['data']);room(r['quest_key'],r['floor'],data['room'])['random_locations']+=data['count']
    index=[];forest=[];totals=collections.Counter()
    for q in quests:
        key=q['key'];sections=[];designations=collections.defaultdict(list)
        for text in q.get('map_designations',[]):
            values=re.findall(r'0x[0-9a-fA-F]+',text)
            if len(values)==5:
                f,a,t,l,e=map(lambda v:int(v,16),values)
                designations[f].append(dict(area=a,type=t,layout=l,entities=e,source_operands=text))
        page=['# Recorded rooms / sections — '+q['name'],'','[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)','','These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.','','[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)','','## Map designation evidence','','These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.','','```text']
        page+=q.get('map_designations',[]) or ['No direct designation operands recorded by the catalogue.']
        page+=['```','','## Observed section IDs','','| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |','|---:|---:|---:|---:|---|---|---:|']
        for (floor,rid),x in sorted(allrooms[key].items()):
            x['waves']=sorted(x['waves']);x['events']=sorted(x['events']);x['designation_candidates']=designations[floor];x['boundary_status']='not decoded'
            sections.append(x);totals['rooms']+=1;totals['objects']+=x['objects'];totals['enemy_npc_records']+=x['enemy_npc_records']
            page.append(f'| {floor} | {rid} | {x["objects"]} | {x["enemy_npc_records"]} | '+', '.join(map(str,x['waves']))+' | '+', '.join(map(str,x['events']))+f' | {x["random_locations"]} |')
            if q['episode']=='Episode1' and any(d['area']==1 for d in designations[floor]):
                forest.append(dict(quest_key=key,floor=floor,room=rid,designation_candidates=designations[floor]))
        p=CAT/key/'sections.md';p.write_text('\n'.join(page)+'\n',encoding='utf-8')
        (CAT/key/'sections.json').write_text(json.dumps(sections,indent=2)+'\n',encoding='utf-8')
        readme=CAT/key/'README.md';text=readme.read_text(encoding='utf-8')
        link='[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)'
        if link not in text:
            title,body=text.split('\n',1);readme.write_text(title+'\n\n'+link+'\n'+body,encoding='utf-8')
        index.append(dict(key=key,name=q['name'],episode=q['episode'],section_count=len(sections)))
    assert totals['objects']==186967 and totals['enemy_npc_records']==146753,totals
    (OUT/'index.json').write_text(json.dumps(index,indent=2)+'\n',encoding='utf-8')
    (OUT/'forest1-candidates.json').write_text(json.dumps(forest,indent=2)+'\n',encoding='utf-8')
    page=['# Quest room / section index','','This indexes recorded room IDs across all 527 quest variants. **It is not yet a complete map-layout atlas.** Empty geometric sections and section boundaries require decoding the selected map resources.','','Floor slots, room IDs and wave IDs are separate. Choose a quest, inspect its designation evidence, then open its section list. Reusing coordinates requires a verified matching layout and coordinate transform.','','[Forest 1 designation candidates](forest1-candidates.json) — only explicit Episode 1 area-1 designations; conditional/runtime alternatives are not resolved.','','| Quest | Episode | Recorded floor/room pairs |','|---|---|---:|']
    for q in index:page.append(f'| [{q["name"].replace("|","/")}: {q["key"]}](../server-catalogue/{q["key"]}/sections.md) | {q["episode"]} | {q["section_count"]} |')
    (OUT/'README.md').write_text('\n'.join(page)+'\n',encoding='utf-8')
    (OUT/'validation.json').write_text(json.dumps(dict(quests=len(index),**totals,boundaries_decoded=False),indent=2)+'\n')
    print(dict(quests=len(index),**totals))
if __name__=='__main__':main()
