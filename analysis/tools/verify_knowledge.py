import collections,hashlib,json,pathlib,re,sqlite3,sys
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
B=pathlib.Path(__file__).resolve().parents[1]; K=B/'quest-knowledge'; C=B/'server-catalogue'
manifest=json.loads((K/'manifest.json').read_text(encoding='utf-8')); rows=json.loads((K/'quest-index.json').read_text(encoding='utf-8'))
db=sqlite3.connect(K/'quest-library.sqlite')
checks={}; mismatches=[]
for f in manifest['files']:
    p=K/f['snapshot']; h=hashlib.sha256(p.read_bytes()).hexdigest(); assert h==f['sha256'],p
    if f['kind']=='server-quest-source' and hashlib.sha256(pathlib.Path(f['original']).read_bytes()).hexdigest()!=h: mismatches.append(f['original'])
checks['snapshot_files_verified']=len(manifest['files']); checks['server_original_changes_since_snapshot']=mismatches
cross=[]
for r in rows:
    key=r['key']; text=(C/key/'map.txt').read_text(encoding='utf-8')
    expected=[len(re.findall(r'\[ObjectSetEntry ',text)),len(re.findall(r'\[EnemySetEntry ',text)),len(re.findall(r'\[Event1Entry ',text)),len(re.findall(r'\[Event2Entry ',text))]
    actual=[db.execute('SELECT count(*) FROM placements WHERE quest_key=? AND kind=?',(key,'object')).fetchone()[0],db.execute('SELECT count(*) FROM placements WHERE quest_key=? AND kind=?',(key,'enemy_npc')).fetchone()[0]]
    actual.extend(db.execute('SELECT count(*) FROM events WHERE quest_key=? AND format=?',(key,fmt)).fetchone()[0] for fmt in ('evt1','evt2'))
    if expected!=actual: cross.append(dict(key=key,expected=expected,actual=actual))
assert not cross,cross[:4]
checks['variants_cross_checked_against_native_map_listing']=len(rows)
checks['database_integrity']=db.execute('PRAGMA integrity_check').fetchone()[0]; assert checks['database_integrity']=='ok'
checks['invalid_actions']=db.execute("SELECT count(*) FROM events WHERE data LIKE '%invalid_action_offset%' OR data LIKE '%unknown_action%'").fetchone()[0]
checks['event_stream_eof']=db.execute("SELECT count(*) FROM events WHERE data LIKE '%end_of_stream%'").fetchone()[0]
if checks['invalid_actions']:
    checks['invalid_action_records']=[dict(quest_key=r[0],floor=r[1],event=r[2],data=json.loads(r[3])) for r in db.execute("SELECT quest_key,floor,event_id,data FROM events WHERE data LIKE '%invalid_action_offset%' OR data LIKE '%unknown_action%'")]
ttf=db.execute("SELECT data FROM events WHERE quest_key='vr-ep1/q118-bb-e' AND floor=2 AND event_id=41").fetchone()
assert ttf and json.loads(ttf[0])['actions'][0]['target']==411
checks['known_ttf_event_41_targets_411']=True
checks['fts_if_zone_clear_results']=db.execute("SELECT count(*) FROM chunks_fts WHERE chunks_fts MATCH ?",('"if_zone_clear"',)).fetchone()[0]
assert checks['fts_if_zone_clear_results']>0
earlier=json.loads((B/'catalogue/catalogue.json').read_text(encoding='utf-8')); comparisons=[]
for old in earlier:
    matched=[r for r in rows if pathlib.Path(r['source']).name==pathlib.Path(old['source']).name]
    comparisons.append(dict(old_key=old['key'],server_matches=[dict(key=r['key'],compressed_source_identical=r['source_sha256']==old['source_sha256']) for r in matched]))
checks['earlier_variants']=len(comparisons); checks['earlier_variants_with_exact_server_match']=sum(any(m['compressed_source_identical'] for m in r['server_matches']) for r in comparisons)
(K/'earlier-collection-comparison.json').write_text(json.dumps(comparisons,indent=2))
bycat=collections.defaultdict(list)
for r in rows: bycat[r['category']].append(r)
summary=[]
for cat,rs in sorted(bycat.items()):
    grouped=collections.defaultdict(list)
    for r in rs: grouped[(r['prefix'],r['filename_quest_id'])].append(r)
    representatives=[next((r for r in g if r['language']=='E'),g[0]) for g in grouped.values()]
    summary.append(dict(category=cat,groups=len(grouped),variants=len(rs),episodes=dict(collections.Counter(r['episode'] for r in representatives))))
(K/'category-summary.json').write_text(json.dumps(summary,indent=2))
json.loads((K/'quest-blueprint.schema.json').read_text())
try:
    import jsonschema
    jsonschema.Draft202012Validator.check_schema(json.loads((K/'quest-blueprint.schema.json').read_text()))
    checks['blueprint_schema']='Draft2020-12 checked'
except ImportError: checks['blueprint_schema']='JSON parsed; schema validator unavailable'
checks['roundtrip_outcomes']=dict(collections.Counter(r['roundtrip'] for r in rows))
checks['all_script_payloads_and_label_tables_preserved']=all(r['validation_detail']['script_bytes_preserved'] and r['validation_detail']['label_table_preserved'] for r in rows)
(K/'validation-results.json').write_text(json.dumps(checks,indent=2))
print(json.dumps(checks,indent=2))
