"""Inventory Qedit application resources and declared fields; no inferred binary offsets.

Usage: python analysis/tools/build_qedit_coverage.py --source /path/to/schthack/qedit
Source revision is pinned below. UI inventory is not semantic or runtime verification.
"""
import argparse, hashlib, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'analysis/qedit-coverage'
REV='2af5d144485b58ba28b57d98d2daa1a6b141ff4f'
BASE=f'https://github.com/schthack/qedit/blob/{REV}/'
def read(p):return p.read_text(encoding='utf-8',errors='replace')
def dump(name,value):(OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def clean(s):return str(s).replace('|',' / ').replace('\n',' ')
def ref(file,line):return BASE+file+f'#L{line}'

def main(src):
    OUT.mkdir(parents=True,exist_ok=True);(OUT/'forms').mkdir(exist_ok=True)
    project=src/'qedit.dpr';text=read(project)
    units=re.findall(r"\bin\s+'([^']+\.pas)'",text,re.I)
    # Include transitive form units (e.g. FFind is used by FScriptTE but not listed in DPR).
    local={p.stem.lower():p.name for p in src.glob('*.pas') if p.with_suffix('.dfm').exists()}
    for unit in units:
        for clause in re.findall(r'\buses\s+(.*?);',read(src/unit),re.I|re.S):
            for token in re.findall(r'\b\w+\b',clause):
                candidate=local.get(token.lower())
                if candidate and candidate.lower() not in {u.lower() for u in units}:units.append(candidate)
    sources=[project]+[src/u for u in units]
    controls=[]; forms=[]; records=[]; limitations=[]
    for unit in units:
        pas=src/unit;pt=read(pas);dfm=pas.with_suffix('.dfm')
        # Retain record declaration text, rather than guessing packing or serialization.
        for m in re.finditer(r'(?im)^[ \t]*(\w+)\s*=\s*(?:packed\s+)?record\b',pt):
            tail=pt[m.end():];end=re.search(r'(?im)^\s*end\s*;',tail)
            if not end:
                limitations.append(f'No simple record terminator: {unit}:{m[1]}');continue
            body=tail[:end.start()];line=pt[:m.start()].count('\n')+1
            fields=[]
            for i,raw in enumerate(body.splitlines()):
                code=raw.split('//',1)[0].strip()
                f=re.match(r'([\w,\s]+):\s*(.+?);',code)
                if f:fields.append({'names':[v.strip() for v in f[1].split(',')],'declared_type':f[2],'source_text':raw.strip()})
            records.append(dict(unit=unit,name=m[1],line=line,source=ref(unit,line),declaration=pt[m.start():m.end()+end.end()].strip(),fields=fields,status='declared-source-only',offsets_verified=False,layout_note='Record declarations can contain pointers, strings and internal editor state; no disk offsets or compiler alignment inferred.'))
        if not dfm.exists():continue
        sources.append(dfm);lines=read(dfm).splitlines();stack=[];found=[]
        for lineno,line in enumerate(lines,1):
            indent=len(line)-len(line.lstrip());s=line.strip()
            m=re.match(r'(object|inherited|inline)\s+(\w+):\s*(\w+)',s)
            if m:
                while stack and stack[-1]['indent']>=indent:stack.pop()
                c=dict(id=f'{dfm.stem}:{m[2]}',form=dfm.stem,name=m[2],component_type=m[3],parent=stack[-1]['name'] if stack else None,line=lineno,source=ref(dfm.name,lineno),properties={},events=[],status='resource-inventoried',indent=indent)
                found.append(c);stack.append(c);continue
            if s=='end':
                if stack and stack[-1]['indent']==indent:stack.pop()
                continue
            if not stack:continue
            prop=re.match(r'(\w+)\s*=\s*(.*)',s)
            if not prop:continue
            key,value=prop.groups();c=stack[-1]
            if key in ('Caption','Text','Hint','Enabled','Visible','ReadOnly','MinValue','MaxValue','Value','Checked','ItemIndex','MaxLength','Style'):
                c['properties'][key]=value
            if key.startswith('On'):
                match=re.search(r'(?im)^[ \t]*(?:procedure|function)\s+\w+\.'+re.escape(value)+r'\b',pt)
                event=dict(event=key,handler=value,resource_line=lineno,implementation_source=ref(unit,pt[:match.start()].count('\n')+1) if match else None,trace_status='handler-definition-located' if match else 'unresolved-handler')
                c['events'].append(event)
        for c in found:del c['indent']
        controls.extend(found)
        if not found:limitations.append(f'No textual resource objects extracted from {dfm.name}');continue
        root=found[0];title=root['properties'].get('Caption',root['name'])
        forms.append(dict(unit=unit,resource=dfm.name,title=title,controls=len(found),events=sum(len(c['events']) for c in found),source=root['source'],page='forms/'+dfm.stem+'.md'))
        md=[f'# {dfm.stem} — {clean(title)}','','Resource objects are inventoried, not certified features. Captions may be changed at runtime; container objects, labels and controls all count. Complex/multiline property values are not fully decoded.','','[Coverage guide](../README.md) · [Source resource]('+root['source']+')','','| Resource object | Component | Caption / text | Declared event handler(s) |','|---|---|---|---|']
        for c in found:
            events='; '.join(f"{e['event']}: "+(f"[{e['handler']}]({e['implementation_source']})" if e['implementation_source'] else e['handler']+' (unresolved)') for e in c['events'])
            md.append(f"| [{c['name']}]({c['source']}) | {c['component_type']} | {clean(c['properties'].get('Caption',c['properties'].get('Text','')))} | {events} |")
        (OUT/'forms'/f'{dfm.stem}.md').write_text('\n'.join(md)+'\n',encoding='utf-8',newline='\n')
    fields=[]
    entities=json.loads(read(ROOT/'analysis/entity-database/qedit/entity-fields.json'))
    for e in entities:
        for i,label in enumerate(e['field_labels']):
            fields.append(dict(namespace='DAT enemy/NPC',type_id=e['dat_type'],name=e['qedit_name'],field_slot=i,label=label,status='label-only' if label not in ('-','Empty','') else 'placeholder',meaning_verified=False,evidence='../entity-database/qedit/entity-fields.json',note='Zero-based position in the Qedit label list; not a byte offset.'))
    objects=json.loads(read(ROOT/'analysis/object-database/objects.json'))
    for o in objects:
        for i,label in enumerate((o.get('qedit_fields') or {}).get('field_labels',[])):
            fields.append(dict(namespace='DAT object',type_id=o['id'],name=o['name'],field_slot=i,label=label,status='label-only' if label not in ('-','Empty','') else 'placeholder',meaning_verified=False,evidence='../object-database/objects.json',note='Label-list slot, not a byte offset; see the object record for separate parameter evidence.'))
    areas=[
      ('file-formats','BIN / DAT / QST structures','../quest-knowledge/DAT-SCHEMA.md','Documented format and decoded corpus','Trace Qedit read/write routines to each serialized field, including conditional formats.'),
      ('opcode','Opcodes, operands and assembler dialect','../quest-knowledge/COMPILER-PROFILES.md','Source opcode definitions and corpus round trips','Match each editor instruction and alias to BB operands; verify F_ARGS, strings, labels and unsupported versions.'),
      ('npc','NPC placement and interaction','../entity-database/npcs.md','62 constructor definitions and corpus placements','Trace editor control → stored field → client behavior; verify every type-specific handler.'),
      ('appearance','Class and appearance selectors','../entity-database/qedit/native-builder/README.md','12 classes and seven native special selectors','Map all serialized appearance fields and render every supported selection; prove source/executable correspondence.'),
      ('monster','Monster types and area restrictions','../entity-database/monsters.md','63 constructor definitions, area masks and examples','Resolve menu/constructor differences; test subtypes, rares and Ultimate behavior.'),
      ('object','Object parameters and links','../object-database/README.md','280 ID records and Qedit field labels','Verify unresolved flags/parameters and door/switch links; complete images.'),
      ('floor','Floor slots, area IDs and variations','../floor-database/README.md','47 areas and source variant tables','Trace all map designation controls and variation restrictions.'),
      ('geometry','Map sections, coordinates and collision','../floor-database/geometry/README.md','126 collision maps with section transforms','Prove room ownership, transform conventions, navigation links and valid spawn bounds.'),
      ('events','Waves, events, switches and threads','../map-sections/README.md','Per-quest event and placement evidence','Verify action chains, completion, yielding and multiplayer state.'),
      ('scene','Dialogue, cameras and scene timing','../../DATABASE-COVERAGE.md','351 camera-reference quest variants','Reconstruct full actor/dialogue/camera call chains and timing.'),
      ('editor','Editor forms, menus and settings','controls.json','Application resource inventory in this audit','Resolve runtime-created controls and dynamic captions; map commands to data writes.'),
      ('runtime','Qedit save/reopen and PSOBB execution','../quest-knowledge/validation-results.json','Static decoder/reassembly results','Run Qedit save/reopen fixtures and client tests; these are not covered by decoder round trips.'),
    ]
    matrix=[dict(id=i,feature=n,evidence=e,current_evidence=c,next_verification=t,status='partial',qedit_save_reopen_tested=False,client_runtime_tested=False) for i,n,e,c,t in areas]
    for row in matrix:assert (OUT/row['evidence']).resolve().exists() or row['evidence']=='controls.json',row
    dump('controls.json',controls);dump('forms.json',forms);dump('record-declarations.json',records);dump('field-labels.json',fields);dump('matrix.json',matrix)
    provenance=[dict(file=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),source=BASE+p.name) for p in sources]
    dump('provenance.json',dict(source_revision=REV,project='qedit.dpr explicit local units plus transitive form units; external SDK units excluded',files=provenance,supplied_executable=json.loads(read(ROOT/'analysis/entity-database/qedit/native-builder/provenance.json')),source_executable_equivalence='Not established. The public source snapshot is not claimed to be the exact build source of supplied Qedit1.exe.'))
    stats=dict(application_units=len(units),form_resources=len(forms),resource_objects=len(controls),event_bindings=sum(len(c['events']) for c in controls),resolved_event_bindings=sum(bool(e['implementation_source']) for c in controls for e in c['events']),record_declarations=len(records),declared_record_fields=sum(len(r['fields']) for r in records),entity_object_label_slots=len(fields),placeholder_label_slots=sum(f['status']=='placeholder' for f in fields),semantic_completion_percentage=None,limitations=limitations)
    dump('validation.json',stats)
    md=['# QEdit Feature & Field Coverage Matrix','','This is the first source inventory for the supplied Qedit/PSOBB research scope. **It is not a 100% compatibility certification.** Resource objects and label slots are inventory counts, not verified feature counts. No completion percentage is assigned.','','## Build scope','','Public Qedit source revision `'+REV+'`, application units explicitly referenced by `qedit.dpr`, their textual DFM resources, and existing Qedit entity/object label exports. External DirectX/Windows SDK units are excluded. See [source hashes and executable identity](provenance.json). **Exact equivalence between this public source and the supplied executable is not established.**','','## Verification matrix','','| Feature | Available evidence | Next required verification |','|---|---|---|']
    md += [f"| {r['feature']} | [{r['current_evidence']}]({r['evidence']}) | {r['next_verification']} |" for r in matrix]
    md += ['','## Inventoried resources','',f"{stats['application_units']} application units; {stats['form_resources']} forms; {stats['resource_objects']} resource objects; {stats['event_bindings']} event bindings ({stats['resolved_event_bindings']} matching implementation definitions located).",'',f"{stats['record_declarations']} record declarations, {stats['declared_record_fields']} declared field entries, and {stats['entity_object_label_slots']} Qedit label slots ({stats['placeholder_label_slots']} placeholders).",'','[Full controls and events](controls.json) · [Record declarations](record-declarations.json) · [Field labels](field-labels.json) · [Machine-readable matrix](matrix.json) · [Extraction counts](validation.json)','','| Editor form | Resource objects | Event bindings |','|---|---:|---:|']
    md += [f"| [{clean(f['title'])} — {f['unit']}]({f['page']}) | {f['controls']} | {f['events']} |" for f in forms]
    md += ['','## How a field becomes verified','','1. Locate its resource/control or command and handler in the appropriate source/build.','2. Trace the value into the internal record and serialization code; distinguish editor-only state.','3. Document exact disk type, offset, ranges, defaults and episode/version conditions from evidence.','4. Save and reopen a minimal fixture in the supplied Qedit and compare bytes.','5. Where behavior matters, test the matching clean client, including multiplayer where applicable.','','A label alone does not establish parameter semantics. A record declaration does not establish disk packing. A handler link does not prove the full call path. Runtime-created controls, multiline resource values, conditional records and alternate builds require further inspection.','','## Next bounded audit','','Trace the main.pas `TMonster`, `TObj`, `TMapSection` and `NPCBuild.pas` `TNPCDATA` records through their loaders and save callers. Produce field-by-field mappings and a fixture plan before claiming serialized-field completeness.','']
    md += ['[First NPC appearance writeback trace](npc-writeback-trace.md) — editor record to script HEX data, with outstanding fixture checks.','']
    (OUT/'README.md').write_text('\n'.join(md),encoding='utf-8',newline='\n')
    print(json.dumps(stats))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);a=p.parse_args();main(a.source)
