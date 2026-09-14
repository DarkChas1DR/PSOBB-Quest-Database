"""Check DAT saved-field offsets against every preserved placement CSV."""
from pathlib import Path
import csv,json,struct,math
R=Path(__file__).resolve().parents[2];O=R/'analysis/qedit-coverage/placements';O.mkdir(exist_ok=True)
common=[('type',0,'H','Skin'),('room',12,'H','map_section')]
enemy=common+[('children',6,'H','unknow2 high word'),('wave',14,'H','Unknow5'),('wave2',16,'H','unknow6 low word')]+[(k,20+i*4,'f',n) for i,(k,n) in enumerate(zip(('x','y','z'),('Pos_X','Pos_Z','Pos_Y')))]+[(f'p{i+1}',44+i*4,'f',n) for i,n in enumerate(('Movement_data','Unknow10','unknow11','Char_id','Action'))]+[('p6',64,'h','Movement_flag low word'),('p7',66,'h','Movement_flag high word')]
obj=common+[('group',10,'H','grp')]+[(k,16+i*4,'f',n) for i,(k,n) in enumerate(zip(('x','y','z'),('Pos_X','Pos_Z','Pos_Y')))]+[(f'p{i+1}',40+i*4,'f',n) for i,n in enumerate(('unknow8','unknow9','Unknow10'))]+[(f'p{i+4}',52+i*4,'i',n) for i,n in enumerate(('obj_id','Action','unknow13'))]
total={1:0,2:0};checks=0;quests=0
for summary in sorted((R/'analysis/server-catalogue').glob('*/*/summary.json')):
    folder=summary.parent;b=(folder/'map.datd').read_bytes();pos=0;seen={1:[],2:[]}
    while pos+16<=len(b):
        kind,size,floor,data_size=struct.unpack_from('<4I',b,pos)
        if kind==0:break
        assert size>=16 and pos+size<=len(b),(folder,pos,size)
        if kind in (1,2):
            stride=68 if kind==1 else 72
            assert data_size%stride==0 and data_size<=size-16,(folder,kind,data_size)
            for offset in range(pos+16,pos+16+data_size,stride):seen[kind].append((floor,b[offset:offset+stride]))
        pos+=size
    for kind,filename,layout in [(1,'objects.csv',obj),(2,'enemies.csv',enemy)]:
        rows=list(csv.DictReader((folder/filename).open(encoding='utf-8')))
        assert len(rows)==len(seen[kind]),(folder,kind,len(rows),len(seen[kind]))
        for row,(floor,raw) in zip(rows,seen[kind]):
            assert int(row['floor'])==floor
            for name,offset,fmt,qedit in layout:
                val=struct.unpack_from('<'+fmt,raw,offset)[0]
                want=float(row[name]) if fmt=='f' else int(row[name],16 if name=='type' else 10)
                assert val==want or (fmt=='f' and math.isnan(val) and math.isnan(want)),(str(folder),kind,name,val,want)
                checks+=1
        total[kind]+=len(rows)
    quests+=1
assert (quests,total[1],total[2])==(527,186967,146753)
data={'quest_variants':quests,'object_records':total[1],'enemy_npc_records':total[2],'field_comparisons':checks,'object_size':68,'enemy_size':72,'qedit_save_reopen_tested':False,'client_tested':False,'scope':'DAT byte values compared with related decoder CSV exports; not independent runtime verification.'}
(O/'validation.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
(O/'fields.json').write_text(json.dumps({k:[dict(csv_field=n,offset=o,encoding=f,qedit_field=q) for n,o,f,q in v] for k,v in [('objects',obj),('enemies',enemy)]},indent=2)+'\n',encoding='utf-8')
print(data)
