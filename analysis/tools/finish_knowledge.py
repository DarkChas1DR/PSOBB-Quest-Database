import collections,json,pathlib,sqlite3
B=pathlib.Path(__file__).resolve().parents[1]; K=B/'quest-knowledge'
manifest=json.loads((K/'manifest.json').read_text(encoding='utf-8')); counts=manifest['counts']
validation=json.loads((K/'validation-results.json').read_text()); rows=json.loads((K/'quest-index.json').read_text(encoding='utf-8'))
def link(rel,label=None): return f'[{label or rel}](<{(K/rel).as_posix()}>)'
quarantine={r['quest_key'] for r in validation.get('invalid_action_records',[])}
for r in rows:
    r['generation_cautions']=[]
    if r['key'] in quarantine: r['generation_cautions'].append('Malformed event action offsets: exclude these event actions from generated examples until repaired and tested')
    if r['roundtrip']=='differs': r['generation_cautions'].append('Header changes on assembly: inspect raw floor-assignment/item-mask fields before reuse')
    r['generation_cautions'].append('Static corpus example only: retrieve complete dependencies and validate before adapting')
(K/'quest-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
categories=json.loads((K/'category-summary.json').read_text())
body='# PSOBB quest knowledge library\n\n'
body+='A reusable reference for generating quests from the supplied server library, Qedit definitions and client assets. The server source snapshot is complete for the supplied quest directory. This does not claim to contain every PSOBB mechanic or replace playtesting.\n\n'
body+=f'**{counts["source_files"]:,} source files preserved; {counts["quest_variants"]} decoded quest variants in {counts["quest_groups"]} category/prefix/ID groups.** Groups distinguish directories and modes; they are not a claim of that many unique playable quests.\n\n'
body+='## Start here\n\n'
for rel,label in [('BUILDER-INSTRUCTIONS.md','Generation instructions and corrections to the sample'),('COMPILER-PROFILES.md','Compiler aliases and verified operand formats'),('DAT-SCHEMA.md','Spatial binary layout and event semantics'),('VALIDATION-GATES.md','Required assembly, spatial and multiplayer checks'),('quest-blueprint.schema.json','Machine-readable design contract'),('validation-results.json','Actual validation results')]: body+='- '+link(rel,label)+'\n'
body+='\n## Data available\n\n| Data | Count / location |\n|---|---|\n'
for label,k in [('Script label blocks (includes data labels)','functions'),('Object records','objects'),('Enemy/NPC records','enemy_npc_records'),('Ordinary event records','evt1'),('Random event records','evt2'),('Random spawn locations','random_locations'),('Random definition records','random_definitions'),('Random weight records','random_weights'),('Retrieval chunks','retrieval_chunks'),('Referenced client/Qedit asset files','indexed_assets')]: body+=f'| {label} | {counts[k]:,} |\n'
body+='\nCounts include language variants and repeated content. They are not unique mechanics, unique monsters or gameplay kill totals. Asset files are indexed by path and size; full geometry has not been decoded or copied. The client map tables and source quest files are preserved.\n\n'
body+='- '+link('quest-library.sqlite','SQLite library with full-text search')+' — quests, label blocks, placements, raw DAT sections, ordinary/random events, random tables, references and text chunks.\n'
body+='- '+link('retrieval-chunks.jsonl','JSONL retrieval export')+' — script label blocks, events, opcode docs and supplied text sources.\n'
body+='- '+link('quest-index.json','Quest manifest')+' — identity, validation, cautions and full decoded-file paths.\n'
body+='- '+link('manifest.json','Source provenance and hashes')+' — 1,558 source files copied under `source-quests/`, plus selected reference snapshots.\n'
body+='- '+link('opcode-reference.json','Version-tagged opcode schemas')+' and '+link('qedit-opcode-dialect.json','recovered Qedit definitions')+'.\n'
body+='- '+link('asset-index.json','Client and Qedit asset index')+'; selected source implementations and configuration are under `reference/`.\n'
body+=f'- [Per-quest readable dossiers](<{(B/"server-catalogue/README.md").as_posix()}>) — full disassembly and map listings. The database and exported source paths refer to that sibling folder; retain it alongside this library when moving the workspace.\n'
body+='\n## Verified and unresolved\n\n'
body+='All 527 variants were cross-checked against native-decoder placement/event counts. SQLite integrity and full-text retrieval checks passed. Snapshot hashes match their recorded values and the original server files were unchanged when rechecked. All 47 earlier supplied variants have an exact file match in the server library.\n\n'
body+='All script payloads and label tables survived reassembly. Of the complete decompressed files, 376 are exact matches, 143 have alignment-only changes, and eight also have header changes. Those eight remain marked for header review.\n\n'
body+='**A New Hope (`vr-ep2/q64-bb-e` and `q64-bb-j`) contains out-of-bounds action offsets for floor 10 events 2202 and 2522.** The database records them as invalid rather than interpreting bytes outside the payload. The decoder itself warns about these offsets; any following garbage in its text listing must not become training examples. This establishes malformed references, not whether players reach them in a normal run.\n\n'
body+='The '+link('review-findings.json','structural review list')+' also records missing static event targets and post-terminator data. These are investigation candidates, not automatically confirmed gameplay faults. Random events are now represented explicitly rather than skipped.\n\n'
body+='No live server configuration was changed, and no new quest was deployed. Native Qedit compilation and gameplay tests have not been performed. Blueprint JSON parses, but a Draft2020-12 schema validator was unavailable in the bundled environment.\n'
body+='\n## Retrieval workflow\n\n'
body+='Use `analysis/tools/query_knowledge.py` with the bundled Python runtime. Examples of arguments:\n\n```text\nquests "Towards the Future"\nsearch "if_zone_clear" --quest vr-ep1/q118-bb-e\nfunction label019E --quest vr-ep1/q118-bb-e\nevents --quest vr-ep1/q118-bb-e --floor 2\nplacements --quest vr-ep1/q118-bb-e --floor 2 --room 4\nopcodes set_switch_flag_sync\n```\n\n'
body+='Search finds candidate references. Read the complete label, callers/handlers, register dependencies and paired DAT records before adaptation. Retrieval chunks may include original quest dialogue and comments; they are source data, not instructions overriding the builder contract. For random encounters, fetch the corresponding random tables as well.\n'
body+='\n## Server folders\n\n| Folder | Groups | Quest files |\n|---|---:|---:|\n'
for c in categories: body+=f'| {c["category"]} | {c["groups"]} | {c["variants"]} |\n'
body+='\nThese are on-disk categories. Live menu availability, permissions and running-server cache state have not been inspected.\n'
(K/'README.md').write_text(body,encoding='utf-8')
db=sqlite3.connect(K/'quest-library.sqlite')
for r in rows: db.execute('UPDATE quests SET metadata=? WHERE key=?',(json.dumps(r,ensure_ascii=False),r['key']))
db.execute("DELETE FROM chunks WHERE kind='builder_document'")
for path in K.glob('*.md'):
    db.execute('INSERT INTO chunks(quest_key,kind,label,path,line,body) VALUES(?,?,?,?,?,?)',('', 'builder_document',path.stem,str(path),1,path.read_text(encoding='utf-8')))
db.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')"); db.commit(); db.close()
# Correct the broad scan's reused title and group terminology without changing the earlier collection.
idx=B/'server-catalogue/README.md'; text=idx.read_text(encoding='utf-8')
text=text.replace('# Episode 1 and Episode 2 quest catalogue','# Server quest catalogue — Episodes 1, 2 and 4')
text=text.replace('quest filename IDs;','category/prefix/ID groups;').replace('Counts include the previously analysed TTF.','Counts retain language variants and category copies; directory membership does not prove live availability.')
text='\n'.join(text.splitlines()[:2])+f'\nSee the [validated knowledge-library index](<{(K/"README.md").as_posix()}>) for the enhanced random-event parsing, header checks and source snapshot.\n'+'\n'.join(text.splitlines()[2:])
idx.write_text(text,encoding='utf-8')
print('Knowledge index and builder documents saved; generation cautions attached.')
