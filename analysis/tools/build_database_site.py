"""Build the read-only web catalogue from preserved reference outputs, never AI imports."""
import hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
def read(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def link(label, path):
    assert (ROOT/path).is_file(), path
    return {'label':label, 'path':path}
def make(kind, name, ident, description, links, **extra):
    return dict(kind=kind,name=name,id=str(ident),description=description,links=links,**extra)

def main():
    rows=[]
    downloads={x['key']:x for x in read('downloads/index.json')}
    for q in read('analysis/quest-knowledge/quest-index.json'):
        base='analysis/server-catalogue/'+q['key']+'/'
        d=downloads[q['key']]
        links=[link(label,base+f) for label,f in [('Quest dossier','README.md'),('Script','script.txt'),('Map data','map.txt'),('Enemies / NPCs','enemies.csv'),('Objects','objects.csv'),('Waves','waves.csv'),('Rooms','sections.md'),('Room data','sections.json')]]
        links += [link('Download ZIP',d['zip'])]+[link(f['label'],f['path']) for f in d['files']]
        rows.append(make('Quests',q['name'],q['key'],f"{q['episode']} · {q['language']} · {q['enemy_npc_records']} enemy/NPC records · {q['events']} events · {q['roundtrip']}",links,episode=q['episode'],data={k:q[k] for k in ('objects','enemy_npc_records','events','floors','issues','roundtrip','map_designations') if k in q},evidence='Decoded corpus example; not a gameplay test',download_sha256=d['sha256']))
        current_label=None
        cameras=[]
        for lineno,line in enumerate((ROOT/(base+'script.txt')).read_text(encoding='utf-8').splitlines(),1):
            if re.match(r'^\w+:',line):current_label=line.split(':',1)[0]
            m=re.match(r'^\s+([A-Za-z_][A-Za-z_0-9]*)\s',line)
            if m and ('camera' in m[1] or m[1].startswith(('cam_','pcam_'))):
                cameras.append(dict(label=current_label,line=lineno,instruction=line.strip()))
        if cameras:
            rows.append(make('Scenes',q['name'],q['key'],f"{len(cameras)} camera-related instructions; scene candidates",[link('Full scene script',base+'script.txt'),link('Script call references',base+'script-references.csv'),link('Actor placements',base+'enemies.csv')],episode=q['episode'],data={'camera_references':cameras},evidence='Static camera opcode references; not a reconstructed or runtime-verified cutscene'))
    for f in read('analysis/floor-database/floors.json'):
        rows.append(make('Floors',f['name'],f"Ep{f['episode']} area 0x{f['area']:02X}",f"Episode {f['episode']} · default floor {f['default_floor']} · {len(f['variants'])} table entries",[link('Area and variants',f"analysis/floor-database/area-{f['area']:02X}.md")],episode=f"Episode{f['episode']}",data=f,evidence='Source map tables; floor slot and area ID are separate'))
    for m in read('analysis/floor-database/geometry/extraction-index.json'):
        stem='analysis/floor-database/geometry/'+m['map']
        rows.append(make('Maps',m['map'],m['map'],f"{len(m['section_ids'])} section markers · {m['triangles']} collision triangles",[link('Map notes',stem+'.md'),link('Geometry JSON',stem+'.json'),link('Wireframe SVG',stem+'.svg'),link('Wireframe PNG',stem+'.png')],image=stem+'.png',data={'section_ids':m['section_ids']},evidence='Extracted section origins and collision mesh; room boundaries and safe spawn locations not proven'))
    gallery={x['dat_type']:x for x in read('analysis/entity-database/appearance-gallery/npcs.json')}
    for d in read('analysis/entity-database/definitions.json'):
        kind='NPCs' if d['kind']=='npc' else 'Monsters'
        file=f"{d['id']:04X}-"+re.sub(r'[^A-Za-z0-9_-]','_',d['constructor'])+'.md'
        links=[link('Parameters, areas and quest placements',f"analysis/entity-database/{d['kind']}s/{file}")]
        image=None
        if kind=='NPCs':
            links.append(link('Appearance gallery','analysis/entity-database/appearance-gallery/README.md'))
            g=gallery.get(d['id'],{})
            if g.get('preview'):image='analysis/entity-database/appearance-gallery/'+g['preview']
        rows.append(make(kind,d['qedit_name'] or d['source_description'] or d['constructor'],d['id_hex'],f"{d['constructor']} · {d['observed_placement_count']} observed placements",links,image=image,data=d,evidence=d['evidence']))
    for o in read('analysis/object-database/objects.json'):
        file=f"analysis/object-database/objects/{o['id']:04X}.md"
        rows.append(make('Objects',o['name'],o['id_hex'],'Qedit fields, presets, area menus and observed placements',[link('Object record',file)],data=o,evidence='Source-documented / observed; consult per-field evidence'))
    opcode_rows={}
    for o in read('analysis/quest-knowledge/opcode-reference.json'):
        if not o.get('supports_bb'):continue
        key=(o['opcode'],tuple(o['aliases']),o['schema_and_flags'])
        if key not in opcode_rows:
            opcode_rows[key]=make('Opcodes',' / '.join(o['aliases']),o['opcode'],o['schema_and_flags'],[link('Decoder opcode source','analysis/quest-knowledge/reference/decoder-source/QuestScript.cc'),link('Server opcode source','analysis/quest-knowledge/reference/server-source/QuestScript.cc'),link('Compiler profiles','analysis/quest-knowledge/COMPILER-PROFILES.md')],data={'definitions':[]},evidence='Source opcode definition; equivalent signatures grouped, both source records retained')
        opcode_rows[key]['data']['definitions'].append(o)
    rows.extend(opcode_rows.values())
    for a in read('analysis/entity-database/qedit/native-builder/appearance-ids.json'):
        rows.append(make('Appearance',a['name'],f"Visual class {a['visual_class_id']}",'Hair, face, skin, costume and head selector ranges',[link('Qedit selector evidence','analysis/entity-database/qedit/native-builder/README.md'),link('All appearance IDs','analysis/entity-database/qedit/native-builder/appearance-ids.json')],data=a,evidence='Qedit selector tables; not all appearance combinations visually verified'))
    for a in read('analysis/entity-database/appearance-gallery/special-characters.json'):
        rows.append(make('Appearance',a['name'],a.get('extra_model',a.get('dat_type','Unresolved')),a.get('namespace') or 'Unresolved character mapping',[link('Special character evidence','analysis/entity-database/appearance-gallery/special-characters.md')],data=a,evidence=a['evidence']))
    refs=[('Coverage and outstanding gaps','DATABASE-COVERAGE.md'),('Audit of Antigravity changes','analysis/audit/antigravity-review.md'),('NPC special character IDs','analysis/entity-database/appearance-gallery/special-characters.md'),('Appearance selector IDs','analysis/entity-database/qedit/native-builder/README.md'),('NPC appearance gallery','analysis/entity-database/appearance-gallery/README.md'),('Observed NPC appearance configurations','analysis/entity-database/npc-visual-blocks.json'),('Monster names and Ultimate variants','analysis/entity-database/monster-names.json'),('Qedit NPC fields and presets','analysis/entity-database/qedit/README.md'),('Native NPC Builder','analysis/entity-database/qedit/native-builder/README.md'),('DAT format','analysis/quest-knowledge/DAT-SCHEMA.md'),('Validation results','analysis/quest-knowledge/validation-results.json'),('Known quest findings','analysis/quest-knowledge/review-findings.json'),('Quest library SQLite archive','analysis/quest-knowledge/quest-library.sqlite.gz'),('Entity SQLite archive','analysis/entity-database/entities.sqlite.gz'),('Unreviewed import inventory','analysis/import-review/antigravity/README.md')]
    for name,p in refs:rows.append(make('References',name,p,'Open the full source reference or coverage record',[link('Open reference',p)],evidence='See source-specific status'))
    counts={k:sum(r['kind']==k for r in rows) for k in dict.fromkeys(r['kind'] for r in rows)}
    assert counts['Quests']==527 and counts['Floors']==47 and counts['Maps']==126 and counts['Objects']==280
    for r in rows:
        if r.get('image'): assert (ROOT/r['image']).is_file()
    out=ROOT/'database-data';out.mkdir(exist_ok=True)
    (out/'catalogue.json').write_text(json.dumps(dict(counts=counts,records=rows),ensure_ascii=False,separators=(',',':')),encoding='utf-8',newline='\n')
    (ROOT/'analysis/audit/site-validation.json').write_text(json.dumps({'counts':counts,'local_link_targets':'all present','catalogue_sha256':hashlib.sha256((out/'catalogue.json').read_bytes()).hexdigest(),'generator_on_database_site':False},indent=2)+'\n',encoding='utf-8',newline='\n')
    print(counts)
if __name__=='__main__':main()
