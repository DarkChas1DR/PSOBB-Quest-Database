from pathlib import Path
import json, hashlib, re
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / 'analysis/entity-database'
if not DB.exists(): DB = ROOT / 'github-publish/analysis/entity-database'
OUT = DB / 'appearance-gallery'
OUT.mkdir(exist_ok=True)
(OUT/'images').mkdir(exist_ok=True)
SRC = ROOT/'analysis/qedit-images'
if not SRC.exists(): SRC = ROOT.parent/'analysis/qedit-images'
defs = json.loads((DB/'definitions.json').read_text())
images = {p.stem.lower(): p for p in SRC.glob('*.bmp')}
records=[]
cards=[]
for d in defs:
    if d['kind'] != 'npc' and d['constructor'] != '__QUEST_NPC__': continue
    key=f"{d['id']:02x}"
    p=images.get(key)
    name=d.get('source_description') or d.get('qedit_name') or d['constructor']
    r={'dat_type':d['id'],'dat_type_hex':d['id_hex'],'name':name,'qedit_name':d.get('qedit_name'),'constructor':d['constructor'],'documented_areas':d['documented_areas'],'observed_placement_count':d['observed_placement_count'],'parameter_notes':d['parameter_notes'],'preview':None,'preview_status':'No matching Qedit preview in supplied archive'}
    if p:
        target=OUT/'images'/f"{d['id']:04x}.png"
        im=Image.open(p).convert('RGB'); im.save(target)
        r.update(preview='images/'+target.name,preview_status='Qedit bundled preview; not a live client render',source_archive_entry=p.name,source_image_sha256=hashlib.sha256(p.read_bytes()).hexdigest())
        tile=Image.new('RGB',(180,220),'white'); thumb=ImageOps.contain(im,(170,185));tile.paste(thumb,((180-thumb.width)//2,0));ImageDraw.Draw(tile).text((8,195),d['id_hex']+' '+str(d.get('qedit_name',''))[:18],fill='black');cards.append(tile)
    records.append(r)
(OUT/'npcs.json').write_text(json.dumps(records,indent=2)+'\n')
lines=['# NPC appearance gallery','','Actual preview pictures extracted from the supplied Qedit `images.ppk`. NPC preview filenames are mapped to hexadecimal DAT types by `GenerateMonsterName(..., -1)` in Qedit Unit1.pas. These are reference previews, not proof of every client appearance combination.','','[Special characters and IDs](special-characters.md) · [Class, hair, face, head, skin and costume IDs](../qedit/native-builder/appearance-ids.json) · [NPC parameters and placements](../npcs.md) · [Machine-readable gallery](npcs.json)','','Player class IDs, DAT NPC types, instance/character IDs, script labels and special appearance selectors are separate namespaces. Select a DAT entry below for positions, facing, interaction and source documentation.','',f"Coverage: {sum(bool(r['preview']) for r in records)} previews across {len(records)} NPC definitions. Missing previews are listed explicitly. Hair/face/costume combination renders and special-model pictures remain incomplete.",'','## Gallery','']
for r in records:
    name=r['name'].replace('|','/')
    lines += [f"### {r['dat_type_hex']} ({r['dat_type']}) — {name}",'']
    if r['preview']: lines += [f"![Qedit NPC {r['dat_type_hex']}]({r['preview']})",'']
    else: lines += ['Preview unavailable in the supplied Qedit archive.','']
    matches=list((DB/'npcs').glob(f"{r['dat_type']:04X}-*.md"))
    if matches: lines += [f"[Full ID, parameters, areas and observed placements](../npcs/{matches[0].name})",'']
    lines += [f"Qedit label: {r['qedit_name']}. Constructor: `{r['constructor']}`. Observed placements: {r['observed_placement_count']}.",'']
lines += ['## Coverage notes','','This gallery includes `0x0118 / 280` (`__QUEST_NPC__`, 161 observed placements), which the older entity index incorrectly grouped as a monster because its classifier checked mixed-case `Npc`. The gallery recognizes it as an NPC; its parameters are included in `npcs.json`. The older index and SQLite classification have not yet been rebuilt.','','## Evidence','','[Qedit preview lookup](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/Unit1.pas) and [image archive loading](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/main.pas). Original preview rights remain with their owners. Archive entry hashes are retained in `npcs.json`.','']
(OUT/'README.md').write_text('\n'.join(lines),encoding='utf-8')
sheet=Image.new('RGB',(180*6,220*((len(cards)+5)//6)), '#dddddd')
for i,c in enumerate(cards):sheet.paste(c,((i%6)*180,(i//6)*220))
sheet.save(OUT/'contact-sheet.png')
special=[]
for i,name in enumerate(['GM','Rico','Sonic','Knuckles','Tails','Flowen','Elly']):
    letter=chr(ord('Y')-i)
    special.append({'name':name,'qedit_label':'Knux' if name=='Knuckles' else name,'namespace':'Player visual configuration extra_model','extra_model':i,'required_preview_flag_mask':2,'qedit_assets':[f'pl{letter}bdy00.nj',f'pl{letter}hed00.nj',f'pl{letter}tex.afs'],'preview_status':'Not present as a named special-model screenshot in extracted archive','evidence':'Qedit NPCBuild.pas NPC_Name and model loader; not client-playtested'})
special.extend([{'name':'NiGHTS sitting','namespace':'DAT stage NPC','dat_type':51,'area_id':34,'qedit_field':'unknow7','selector':7,'evidence':'MyConst.pas NPC51Name[34,7]; Unit1.pas stage NPC model selection'}, {'name':'NiGHTS flying','namespace':'DAT stage NPC','dat_type':51,'area_id':34,'qedit_field':'unknow7','selector':8,'evidence':'MyConst.pas NPC51Name[34,8]; Unit1.pas stage NPC model selection'}, {'name':'Eggman','namespace':None,'id':None,'evidence':'No verified Eggman/Robotnik entry found in supplied Qedit Pascal definitions; absence globally is not established'}])
(OUT/'special-characters.json').write_text(json.dumps(special,indent=2)+'\n')
print(json.dumps({'definitions':len(records),'previews':len(cards),'special_records':len(special)}))

