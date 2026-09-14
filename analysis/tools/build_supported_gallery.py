"""Render source-backed Qedit selector sheets from supplied NJ/AFS assets."""
from appearance_renderer import *
import re,json,hashlib
import argparse
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--assets',type=Path,required=True,help='Qedit charmodel directory')
parser.add_argument('--source',type=Path,required=True,help='Pinned Qedit NPCBuild.pas')
parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'entity-database/appearance-gallery/supported')
args=parser.parse_args()
R=Path(__file__).resolve().parents[2];OUT=args.output;ASSET=args.assets
OUT.mkdir(parents=True,exist_ok=True);(OUT/'images').mkdir(exist_ok=True)
source=args.source.read_text(encoding='utf-8',errors='replace');source=re.sub(r'//[^\n]*','',source)

def arr(name,width=0):
    m=re.search(r'\b'+name+r'\s*:\s*array.*?=\s*\((.*?)\);',source,re.S|re.I);assert m,name
    v=[float(x) for x in re.findall(r'(?<![\w])\d+(?:\.\d+)?',m[1])]
    return [v[i:i+width] for i in range(0,len(v),width)] if width else v
arrays={n:arr(n) for n in ('NBofCostTex','CosthaveSkin','OffofCostTex','SectionIDOff','FaceOff','Faceway','HeadPos','handpos','NPC4hat','NPC7hat','NPC8hat','NPC9hat','NPC10hat','NPC11hat')}
arrays['HairOff']=arr('HairOff',10);arrays['TexOrder']=arr('TexOrder',20)
def A(n,c):return arrays[n][c]
models={};archives={};hashes={}
unbound={}
def model(name):
    if name not in models:
        path=ASSET/name;models[name]=mesh(path);hashes[name]=hashlib.sha256(path.read_bytes()).hexdigest()
    return models[name]
def tex(letter):
    if letter not in archives:
        p=ASSET/f'pl{letter}tex.afs';b=p.read_bytes();hashes[p.name]=hashlib.sha256(b).hexdigest();archives[letter]=[texture(b,i) for i in range(struct.unpack_from('<I',b,4)[0])]
    return archives[letter]
def part(name,y,mapping,tint=(1,1,1)):
    triangles=model(name);mapping={int(k):int(v) for k,v in mapping.items()}
    missing=set(t for v,u,t in triangles)-set(mapping)
    if missing:unbound[name]=sorted(missing)
    return (triangles,np.array((0,y,0)),mapping,tint)
def standard(c,values):
    skin,cost,face,head,hair=[values.get(k,0) for k in ('skin','costume','face','head','hair')];robot=c in (2,4,5,9);letter=chr(65+c);prefix='pl'+letter;sid=skin if robot else cost
    bmap={0:A('SectionIDOff',c)};i=1;y=A('NBofCostTex',c)*sid+A('OffofCostTex',c);cs=int(A('CosthaveSkin',c));order=arrays['TexOrder'][c]
    for x in range(cs):
        if order[i-1]:bmap[order[i-1]]=y+cs*skin+x
        i+=1
    y+=cs*4
    for x in range(int(A('NBofCostTex',c)-cs*4)):
        if order[i-1]:bmap[order[i-1]]=y+x
        i+=1
    if A('handpos',c):
        bmap[i]=A('handpos',c)+sid
        if c==1:bmap.update({i:A('handpos',c)+skin,i+1:A('handpos',c)+sid+4,i+2:A('handpos',c)+sid+4})
    f=A('FaceOff',c);way=int(A('Faceway',c))
    if way==0:hmap={0:f+face*8+skin*2,1:f+face*8+skin*2+1}
    elif way in (1,5):hmap={1 if way==1 else 0:f+face*4+skin+4,0 if way==1 else 1:f+skin}
    elif way==2:hmap={0:f+face*4+skin}
    elif way==4:
        y=f+sid*2+head*50-(50 if head>0 else 0)
        if head==3:y+=sid
        elif head>3:y+=25
        if head==4:y+=sid
        hmap={j:y+j for j in range(3)}
    elif way==6:
        y=f+sid*2+head*50+(sid if head==0 else 25)-(sid if head==4 else 0)
        hmap={0:y+1,1:y,2:y+2} if head==2 and c==5 else {j:y+j for j in range(3)}
    elif way==7:
        y=f+sid+head*25+(sid if head==0 else 25)
        if c==4:y+=sid if head==2 else 25 if head>2 else 0
        hmap={0:y}
        if c==2:hmap[1]=164
    else:raise ValueError(way)
    parts=[part(prefix+'bdy00.nj',0,bmap),part(prefix+f'hed{head:02x}.nj',A('HeadPos',c),hmap)]
    if not robot:
        off=arrays['HairOff'][c][hair];parts.append(part(prefix+f'hai{hair:02x}.nj',A('HeadPos',c)+.1,{j:off+j for j in range(4)}))
        cap=prefix+f'cap{hair:02x}.nj'
        if (ASSET/cap).exists():
            if c==0:cmap={0:103}
            elif c==3:
                y=A('NBofCostTex',c)*sid+A('OffofCostTex',c)+arrays['NPC4hat'][hair];cmap={j:y+j for j in range(4)}
            else:
                arrname={6:'NPC7hat',7:'NPC8hat',8:'NPC9hat',10:'NPC10hat',11:'NPC11hat'}[c];off=arrays[arrname][hair];y=A('NBofCostTex',c)*sid+A('OffofCostTex',c);cmap={j:y+off+j for j in range(4)}
                if c==6 and hair==7:cmap[1]=y+5
                if c==7 and hair==0:cmap[2]=330
                if c==7 and hair==5:cmap[2]=335
                if c==7 and hair==9:cmap[2]=y+16
                if c==10 and hair==1:cmap[2]=299
                if c==8 and hair==8:cmap[1]=y+24
                if c==8 and hair==7:cmap[1]=493
                if off>30:cmap[0]=off
            parts.append(part(cap,A('HeadPos',c)+.1,cmap))
    return parts,tex(letter)

def special(i):
    letter=chr(ord('Y')-i);prefix='pl'+letter;y=[15.7,14.5,7.3,7.9,5,17,14.5][i]
    bm={0:3 if i<5 else 6 if i==5 else 5,1:0,2:1}
    if i==5:bm.update({3:0,1:1,2:2,4:3})
    if i==6:bm.update({3:0,2:2,1:1})
    hm={0:1,1:2}
    if i==0:hm={0:2,1:1}
    if i==5:hm={0:5,1:4}
    if i==6:hm={0:3}
    parts=[part(prefix+'bdy00.nj',0,bm),part(prefix+'hed00.nj',y,hm)]
    if i>4:parts.append(part(prefix+'hai00.nj',y,{3:5 if i==5 else 4}))
    return parts,tex(letter)

def views(parts,ts,key):
    sheet=Image.new('RGB',(840,320),(239,239,239))
    sheet.paste(render(parts,ts,280,math.pi),(0,20))
    sheet.paste(render(parts[1:],ts,280,math.pi),(280,20))
    sheet.paste(render(parts,ts,280,0),(560,20))
    from PIL import ImageDraw
    dr=ImageDraw.Draw(sheet)
    for x,t in [(8,'Front'),(288,'Head detail'),(568,'Back')]:dr.text((x,4),t,fill=(30,30,30))
    sheet.save(OUT/'images'/f'{key}.png')

if __name__=='__main__':
    classes=json.loads((R/'analysis/entity-database/qedit/native-builder/appearance-ids.json').read_text())
    records=[];errors=[]
    for c in classes:
        cid=c['visual_class_id'];variants=[('baseline',0,{})]
        for field,info in c['fields'].items():
            for v in info['ids']:variants.append((field,v,{field:v}))
        for field,v,values in variants:
            key=f'{cid:02d}-{field}-{v:02d}';r=dict(id=key,name=c['name'],visual_class_id=cid,selector=field,value=v,baseline={'skin':0,'costume':0,'face':0,'head':0,'hair':0,'section_id':0,'hair_rgb':[255,255,255]},status='pending')
            try:
                parts,ts=standard(cid,values);views(parts,ts,key);r.update(status='offline-render',image='images/'+key+'.png')
            except Exception as e:r.update(status='unrendered',reason=str(e));errors.append((key,str(e)))
            records.append(r)
    for i,name in enumerate(['GM','Rico','Sonic','Knuckles','Tails','Flowen','Elly']):
        key=f'special-{i:02d}';r=dict(id=key,name=name,extra_model=i,selector='extra_model',value=i,status='pending')
        try:
            parts,ts=special(i);views(parts,ts,key);r.update(status='offline-render',image='images/'+key+'.png')
        except Exception as e:r.update(status='unrendered',reason=str(e));errors.append((key,str(e)))
        records.append(r)
    (OUT/'selectors.json').write_text(json.dumps(records,indent=2)+'\n')
    (OUT/'asset-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
    (OUT/'unbound-materials.json').write_text(json.dumps(unbound,indent=2)+'\n')
    print('Rendered',sum(r['status']=='offline-render' for r in records),'/',len(records),'errors',errors[:25])
