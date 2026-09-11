"""Read-only retrieval for the PSOBB quest library. No generated SQL is executed."""
import argparse,json,pathlib,sqlite3,sys
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
p=argparse.ArgumentParser()
p.add_argument('action',choices=['search','quests','function','events','placements','opcodes'])
p.add_argument('query',nargs='?',default='')
p.add_argument('--quest',default=''); p.add_argument('--floor',type=int); p.add_argument('--room',type=int)
p.add_argument('--limit',type=int,default=8)
a=p.parse_args(); root=pathlib.Path(__file__).resolve().parents[1]/'quest-knowledge'
db=sqlite3.connect('file:'+str((root/'quest-library.sqlite').as_posix())+'?mode=ro',uri=True); db.row_factory=sqlite3.Row
limit=max(1,min(a.limit,100)); params=[]
if a.action=='search':
    sql="SELECT c.quest_key,c.kind,c.label,c.path,c.line,snippet(chunks_fts,0,'[',']',' ... ',32) AS excerpt FROM chunks_fts JOIN chunks c ON c.id=chunks_fts.rowid WHERE chunks_fts MATCH ? AND c.quest_key LIKE ? ORDER BY rank LIMIT ?"
    params=[a.query,'%'+a.quest+'%',limit]
elif a.action=='quests':
    sql='SELECT key,name,episode,language,category FROM quests WHERE (name LIKE ? OR key LIKE ?) LIMIT ?'; params=['%'+a.query+'%','%'+a.query+'%',limit]
elif a.action=='function':
    sql='SELECT * FROM functions WHERE quest_key=? AND label=? LIMIT ?'; params=[a.quest,a.query,limit]
elif a.action=='opcodes':
    specs=json.loads((root/'opcode-reference.json').read_text(encoding='utf-8'))
    print(json.dumps([x for x in specs if x['supports_bb'] and (a.query.lower() in x['opcode'].lower() or any(a.query.lower() in n.lower() for n in x['aliases']))][:limit],ensure_ascii=False,indent=2)); sys.exit(0)
else:
    table='events' if a.action=='events' else 'placements'
    sql=f'SELECT * FROM {table} WHERE quest_key=?'; params=[a.quest]
    if a.floor is not None: sql+=' AND floor=?'; params.append(a.floor)
    if a.room is not None: sql+=' AND room=?'; params.append(a.room)
    sql+=' LIMIT ?'; params.append(limit)
rows=[]
for result in db.execute(sql,params):
    row=dict(result)
    for k,v in row.items():
        if isinstance(v,bytes): row[k]=v.hex()
    rows.append(row)
print(json.dumps(rows,ensure_ascii=False,indent=2))
