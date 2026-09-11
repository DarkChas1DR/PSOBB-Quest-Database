"""Read-only lookups in the companion monster/NPC database."""
import argparse,json,pathlib,sqlite3
p=argparse.ArgumentParser()
p.add_argument('action',choices=['type','class','placements','check-area'])
p.add_argument('id',type=lambda x:int(x,0))
p.add_argument('--area',type=lambda x:int(x,0))
p.add_argument('--limit',type=int,default=10)
a=p.parse_args()
root=pathlib.Path(__file__).resolve().parents[1]/'entity-database'
db=sqlite3.connect((root/'entities.sqlite').as_uri()+'?mode=ro',uri=True);db.row_factory=sqlite3.Row
if a.action=='class':
    results=[json.loads(r['data']) for r in db.execute('SELECT data FROM classes WHERE id=?',(a.id,))]
elif a.action=='placements':
    results=[dict(r) for r in db.execute('SELECT * FROM placements WHERE type=? LIMIT ?',(a.id,max(1,min(a.limit,100))))]
else:
    results=[json.loads(r['data']) for r in db.execute('SELECT data FROM definitions WHERE id=?',(a.id,))]
    if a.action=='check-area':
        if a.area is None or not 0<=a.area<64: p.error('--area must be between 0 and 63')
        results=[dict(id=r['id_hex'],constructor=r['constructor'],area=a.area,source_mask_lists_area=bool(int(r['area_flags'],16)&(1<<a.area)),evidence=r['evidence']) for r in results]
print(json.dumps(results,indent=2,ensure_ascii=False))
