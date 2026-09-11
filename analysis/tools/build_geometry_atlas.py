import json,pathlib,re,math
ROOT=pathlib.Path(__file__).resolve().parents[2];F=ROOT/'analysis/floor-database';G=F/'geometry'
def main():
    maps=json.loads((G/'extraction-index.json').read_text());floors=json.loads((F/'floors.json').read_text());links={};total=0
    for r in maps:
        if r['status']!='extracted':continue
        stem=r['map'];d=json.loads((G/(stem+'.json')).read_text());total+=r['triangles']
        assert all(math.isfinite(x) for b in d['collision_blocks'] for v in b['vertices'] for x in v)
        for b in d['collision_blocks']:
            assert all(max(t['indices'])<len(b['vertices']) for t in b['triangles'])
        lines=[f'# {stem}','','[All map wireframes](README.md)','','[SVG](%s.svg) · [PNG](%s.png) · [Geometry JSON](%s.json)'%(stem,stem,stem),'',f'![Numbered wireframe]({stem}.svg)','','## Section reference positions','','These are markers, not room boundaries or safe spawn points. Positions use the file’s XYZ axes; the wireframe projects X/Z. Rotation is retained raw, not interpreted here.','','| Section ID | X | Y | Z | Raw rotation |','|---:|---:|---:|---:|---:|']
        for room in d['rooms']:
            if room['id']<1000:lines.append(f'| {room["id"]} | '+ ' | '.join(f'{x:g}' for x in room['position'])+f' | {room["rotation_raw"]} |')
        lines+=['',f'Collision triangles: {r["triangles"]}. Sentinel/unlabelled records remain in JSON. Overlapping marker positions are preserved, not moved to invent room locations.','']
        (G/(stem+'.md')).write_text('\n'.join(lines),encoding='utf-8')
    index=['# All Qedit map wireframes','','**126 supplied collision maps extracted**, with numbered section markers and downloadable SVG, PNG and geometry JSON. This includes available map variations and additional lobby/battle maps.','','Extraction follows [Qedit DrawBBRELFile](https://github.com/schthack/qedit/blob/master/main.pas): c.rel supplies collision triangles; n.rel supplies section records. File bounds, triangle indices and finite coordinates are checked. Forest renders were compared with the supplied screenshots; not every other map has been visually compared with Qedit.','','Blue circles are section reference positions, not exact room boundaries. Overlapping markers, layered geometry and special boss behavior still need interpretation. Vol Opt’s Qedit-specific marker adjustment is not applied; these exports retain raw positions.','','[Extraction manifest](extraction-index.json) · [General floor database](../README.md)','','## Browse by area','','Area links below match map-table setup resource basenames to supplied geometry filenames. They do not resolve runtime map switches or guarantee all client layouts are available.','','| Episode | Area | Matching wireframes |','|---|---|---|']
    for a in floors:
        prefixes={v['setup_basename'] for v in a['variants']}
        matches=[r['map'] for r in maps if r['status']=='extracted' and any(r['map']==p or r['map'].startswith(p+'_') for p in prefixes)]
        if a['episode']==1 and a['area']==14:
            # Qedit Unit1.pas: MapID[14]=51; MapFileName[51]=map_darkfalz00c.rel.
            matches=['map_darkfalz00']
            assert any(r['map']=='map_darkfalz00' and r['status']=='extracted' for r in maps)
        links[a['area']]=matches
        index.append(f'| {a["episode"]} | {a["name"]} | '+(' · '.join(f'[{s}]({s}.md)' for s in matches) or 'No filename match; see full list below')+' |')
        path=F/f'area-{a["area"]:02X}.md';text=path.read_text(encoding='utf-8')
        block='<!-- geometry-atlas:start -->\n## Extracted map wireframes\n\n'+(' · '.join(f'[{s}](geometry/{s}.md)' for s in matches) or 'No matching geometry filename found for this area. See the [full map list](geometry/README.md).')+'\n\nMatching uses setup-resource filenames. Section reference positions and collision triangles are extracted; section boundary ownership and safe spawning remain unverified.\n<!-- geometry-atlas:end -->\n'
        text=re.sub(r'<!-- geometry-atlas:start -->.*?<!-- geometry-atlas:end -->\n*','',text,flags=re.S)
        path.write_text(text+'\n'+block,encoding='utf-8')
    index+=['','## Every supplied map','','| Map | Section markers | Triangles |','|---|---:|---:|']
    for r in maps:index.append(f'| [{r["map"]}]({r["map"]}.md) | {len(r.get("section_ids",[]))} | {r.get("triangles",0)} |')
    index+=['','## Forest 1','','[Forest 1 wireframe](map_forest01.md)','','## Forest 2','','[Forest 2 wireframe](map_forest02.md)','']
    (G/'README.md').write_text('\n'.join(index),encoding='utf-8')
    checks=dict(maps=len(maps),triangles=total,areas_with_filename_matches=sum(bool(v) for v in links.values()),areas_without_matches=[a['name'] for a in floors if not links[a['area']]],geometry_bounds_and_indices='passed',room_boundary_ownership='unverified')
    (G/'validation.json').write_text(json.dumps(checks,indent=2)+'\n');print(checks)
if __name__=='__main__':main()
