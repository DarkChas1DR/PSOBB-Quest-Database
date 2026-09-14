"""Recompute observed static placement counts; these are not runtime capacity limits."""
from pathlib import Path
import csv,json,collections,hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'analysis/quest-limits';OUT.mkdir(exist_ok=True)
defs={x['id']:x['kind'] for x in json.loads((ROOT/'analysis/entity-database/definitions.json').read_text())}
records=[];hashes={}
for p in sorted((ROOT/'analysis/server-catalogue').glob('*/*/enemies.csv')):
    rows=list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
    waves=collections.Counter();rooms=collections.Counter();rw=collections.defaultdict(set);unknown=0;npcs=0
    for x in rows:
        kind=defs.get(int(x['type'],0),'unknown')
        if kind=='npc':npcs+=1;continue
        if kind!='monster':unknown+=1;continue
        f,r,w=(int(x[k],0) for k in ('floor','room','wave'))
        waves[f,r,w]+=1;rooms[f,r]+=1;rw[f,r].add(w)
    key=p.parent.relative_to(ROOT/'analysis/server-catalogue').as_posix()
    records.append(dict(quest=key,monster_records=sum(waves.values()),npc_records=npcs,unclassified_records=unknown,placement_rows=len(rows),max_monster_records_in_wave=max(waves.values(),default=0),max_monster_records_in_room=max(rooms.values(),default=0),max_distinct_placement_waves_in_room=max(map(len,rw.values()),default=0),wave_groups=[dict(floor=f,room=r,wave=w,monster_records=n) for (f,r,w),n in sorted(waves.items())]))
    hashes[p.relative_to(ROOT).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
assert len(records)==527,len(records)
summary={}
for field in ('monster_records','max_monster_records_in_wave','max_monster_records_in_room','max_distinct_placement_waves_in_room'):
    n=max(x[field] for x in records);summary[field]=dict(value=n,examples=[x['quest'] for x in records if x[field]==n])
(OUT/'observed-counts.json').write_text(json.dumps(dict(scope='Static classified enemy placements, not runtime enemies or validated limits. Language variants retained. Random generated enemies excluded; wave zero included; scripts and activation paths not evaluated.',quest_variants=len(records),maxima=summary,quests=records),indent=2)+'\n')
(OUT/'input-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
md='# Observed quest counts\n\nThese are maxima in the supplied 527 quest variants, **not safe limits**. Counts include only placements classified as monsters. NPCs and unknown types are separate in the JSON. Child entities and random-generated enemies are not expanded. Wave zero is included. Distinct wave IDs do not prove a sequence is reachable or active.\n\n| Measurement | Observed maximum | Example quests |\n|---|---:|---|\n'
for field,x in summary.items():
    links=', '.join('['+q+'](../server-catalogue/'+q+'/README.md)' for q in x['examples'])
    md+=f"| {field} | {x['value']} | {links} |\n"
md+='\n[All per-quest and per-wave counts](observed-counts.json) · [Input hashes](input-hashes.json) · [Interpretation and limits](README.md)\n'
(OUT/'observed-counts.md').write_text(md,encoding='utf-8')
print(json.dumps(summary))
