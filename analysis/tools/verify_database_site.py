"""Check publication links, corpus download hashes and repaired entity classification."""
from pathlib import Path
import hashlib, json, sqlite3
ROOT=Path(__file__).resolve().parents[2]
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
catalogue=read('database-data/catalogue.json')
all_paths={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts}
targets={l['path'] for r in catalogue['records'] for l in r['links']}
targets.update(r['image'] for r in catalogue['records'] if r.get('image'))
assert targets<=all_paths, sorted(targets-all_paths)
expected={}
for d in read('downloads/index.json'):
    expected[d['zip']]=d['sha256']
    for f in d['files']:
        if f['path'] in expected:assert expected[f['path']]==f['sha256']
        expected[f['path']]=f['sha256']
for path,sha in expected.items():
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==sha,path
db=sqlite3.connect((ROOT/'analysis/entity-database/entities.sqlite').as_uri()+'?mode=ro',uri=True)
assert db.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
assert db.execute('SELECT kind FROM definitions WHERE id=280').fetchone()[0]=='npc'
assert db.execute('SELECT COUNT(*) FROM placements WHERE type=280 AND kind="npc"').fetchone()[0]==161
db.close()
site=(ROOT/'index.html').read_text(encoding='utf-8')
for removed in ('compileQuestBin','compileQuestDat','api.openai.com','generativelanguage.googleapis.com','web_data/'):
    assert removed not in site, removed
assert not (ROOT/'generate_quest.py').exists()
report=read('analysis/audit/site-validation.json')
report.update(case_sensitive_link_targets=len(targets),download_files_hash_verified=len(expected),entity_sqlite_integrity='ok',quest_npc_0x0118_placements=161,verification_scope='Static links, hashes, SQLite integrity and absence of generator entry points; not game-runtime validation')
(ROOT/'analysis/audit/site-validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(report,indent=2))
