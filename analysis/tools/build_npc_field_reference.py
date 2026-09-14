"""Cross-check preserved BB visual blocks against source-documented field offsets."""
from pathlib import Path
import json,re,struct
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'analysis/qedit-coverage/npc-appearance'
OUT.mkdir(parents=True,exist_ok=True)
layout=[('name_color',0x18,'I'),('extra_model',0x1C,'B'),('name_color_checksum',0x2C,'I'),('section_id',0x30,'B'),('char_class',0x31,'B'),('validation_flags',0x32,'B'),('version',0x33,'B'),('class_flags',0x34,'I'),('costume',0x38,'H'),('skin',0x3A,'H'),('face',0x3C,'H'),('head',0x3E,'H'),('hair',0x40,'H'),('hair_r',0x42,'H'),('hair_g',0x44,'H'),('hair_b',0x46,'H'),('proportion_x',0x48,'f'),('proportion_y',0x4C,'f')]
aliases={'name_color_checksum':'name_color_cs'}
blocks=json.loads((ROOT/'analysis/entity-database/npc-visual-blocks.json').read_text(encoding='utf-8'))
output=[];comparisons=0
for sample in blocks:
    body=sample['body'];m=re.search(r'^\s*([0-9A-F]+)\s+__unused_name__',body,re.M)
    assert m,sample['source']
    code_relative=int(m[1],16)
    path=ROOT/'analysis/server-catalogue'/sample['quest_key']/'script.bind'
    blob=path.read_bytes();code_base=struct.unpack_from('<I',blob)[0]
    offset=code_base+code_relative;raw=blob[offset:offset+0x70]
    assert len(raw)==0x70
    values={name:struct.unpack_from('<'+fmt,raw,off)[0] for name,off,fmt in layout}
    checks=0
    for name,off,fmt in layout:
        if name.startswith(('hair_r','hair_g','hair_b','proportion_')):continue
        annotation=aliases.get(name,name)
        hit=re.search(r'^\s*[0-9A-F]+\s+'+re.escape(annotation)+r'\s+([0-9A-F]+)\b',body,re.M)
        if hit:
            assert values[name]==int(hit[1],16),(sample['quest_key'],name)
            comparisons+=1;checks+=1
    output.append(dict(quest_key=sample['quest_key'],script_source=sample['source'],source_line=sample['line'],code_relative_offset=code_relative,decompressed_bin_offset=offset,code_base=code_base,size=112,raw_hex=raw.hex(),fields=values,name_buffer_utf16le=raw[0x50:0x70].decode('utf-16le',errors='replace').rstrip('\0'),matching_annotation_fields=checks,status='preserved-bytes-match-decoder-annotations; not Qedit save/reopen tested'))
def dump(n,v):(OUT/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
dump('observed-blocks.json',output)
dump('fields.json',[dict(name=n,bb_visual_offset=o,offset_hex=f'0x{o:02X}',size=struct.calcsize('<'+f),encoding={'I':'uint32 little-endian','H':'uint16 little-endian','B':'uint8','f':'IEEE754 float32 little-endian'}[f],offset_scope='relative to PlayerVisualConfigV4, not the quest BIN start',evidence='PlayerSubordinates.hh shared structure at +0x10; observed corpus bytes',qedit_save_reopen_tested=False) for n,o,f in layout])
dump('validation.json',dict(observed_blocks=len(output),annotation_field_comparisons=comparisons,bb_visual_size=112,save_reopen_tested=False,client_playtested=False,scope='Existing byte/annotation consistency only; decoder source and annotations are related evidence, not independent runtime validation.'))
print(len(output),'blocks;',comparisons,'matching integer-field annotations')
