"""Check publication links, full placement coverage and representative rules."""
import gzip,hashlib,json,pathlib,re,sqlite3
ROOT=pathlib.Path(__file__).resolve().parents[2]; OUT=ROOT/'analysis/entity-database'
for page in OUT.rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)',page.read_text(encoding='utf-8')):
        if '://' not in target:
            assert (page.parent/target.split('#')[0]).exists(),(page,target)
db=sqlite3.connect((OUT/'entities.sqlite').as_uri()+'?mode=ro',uri=True)
assert db.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
assert db.execute('SELECT count(*) FROM placements').fetchone()[0]==146753
c=json.loads(db.execute('SELECT data FROM classes WHERE id=3').fetchone()[0])
assert c['name']=='RAmar' and c['race']=='HUMAN' and c['appearance_counts']['face']==5
h=json.loads(db.execute('SELECT data FROM definitions WHERE id=64').fetchone()[0])
assert [a['area'] for a in h['documented_areas']]==[2,16,17,19,20]
assert db.execute('SELECT count(*) FROM handlers').fetchone()[0]==3370
with gzip.open(OUT/'entities.sqlite.gz','rb') as f:
    assert hashlib.sha256(f.read()).hexdigest()==hashlib.sha256((OUT/'entities.sqlite').read_bytes()).hexdigest()
print('Verified entity links, complete placement count, class IDs, Hildebear area mask, handlers and compressed database.')
