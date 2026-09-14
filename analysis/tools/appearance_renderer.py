from pathlib import Path
import struct, math, io
import numpy as np
from PIL import Image

VF=[3,15,1,3,17,33,3,3,3,5,13,21,37,13,13,13,3,11,19]
SF=[1,3,3,9,11,11,5,7,7,1,19,19]

def texture(archive,idx):
    count=struct.unpack_from('<I',archive,4)[0];assert 0<=idx<count
    off,size=struct.unpack_from('<II',archive,8+idx*8);b=archive[off:off+size]
    assert b[:4]==b'XVRT'
    w,h=struct.unpack_from('<HH',b,20);fmt=struct.unpack_from('<I',b,12)[0];assert fmt in (6,7),fmt
    hdr=bytearray(128);hdr[:4]=b'DDS ';struct.pack_into('<7I',hdr,4,124,0x81007,h,w,len(b)-64,0,0)
    struct.pack_into('<II',hdr,76,32,4);hdr[84:88]=b'DXT1' if fmt==6 else b'DXT5';struct.pack_into('<I',hdr,108,0x1000)
    return Image.open(io.BytesIO(hdr+b[64:])).convert('RGBA')

def mesh(path):
    b=Path(path).read_bytes();assert b[:4]==b'NJCM',path
    base=8;verts={};tris=[];texture_id=0;cache={};visited=set()
    def transform(v,anc):
        v=np.array(v,dtype=float)
        for flags,pos,ang,scale in reversed(anc):
            if not flags&4:v*=scale
            if not flags&2:
                for axis,a in enumerate(ang):
                    c=math.cos((a&65535)*math.tau/65536);s=math.sin((a&65535)*math.tau/65536)
                    x,y,z=v
                    v=np.array((x,c*y-s*z,s*y+c*z)) if axis==0 else np.array((c*x+s*z,y,c*z-s*x)) if axis==1 else np.array((c*x-s*y,s*x+c*y,z))
            if not flags&1:v+=pos
        v[2]*=-1
        return v
    def chunks(p,anc,depth=0):
        nonlocal texture_id
        assert depth<20
        while True:
            start=p;t,flags=struct.unpack_from('<BB',b,p);p+=2
            if t==0:continue
            if t>=128:return
            if t<=7:
                if t==4:cache[flags]=p;return
                if t==5:chunks(cache[flags],anc,depth+1)
                continue
            if t in (8,9):
                value=struct.unpack_from('<H',b,p)[0];p+=2
                if t==8:texture_id=value&0x3fff
                continue
            size=struct.unpack_from('<H',b,p)[0];p+=2
            if 16<=t<=31 or 56<=t<=58:p+=size*2;continue
            if 32<=t<=50:
                end=start+4+size*4
                if flags&3:
                    p=end
                    continue
                first,count=struct.unpack_from('<HH',b,p);p+=4;mask=VF[t-32]
                for i in range(count):
                    xyz=struct.unpack_from('<3f',b,p);p+=12
                    if mask&2:p+=4
                    if mask&4:p+=12
                    if mask&8:p+=4
                    if mask&16:p+=4
                    idx=first+i
                    if mask&32:
                        val=struct.unpack_from('<I',b,p)[0];p+=4;idx=first+(val&65535)
                    verts[idx]=transform(xyz,anc)
                assert p==end,('vertex size',p,end,t)
                continue
            if 64<=t<=75:
                end=start+4+size*2;head=struct.unpack_from('<H',b,p)[0];p+=2;user=head>>14;count=head&0x3fff;mask=SF[t-64]
                for _ in range(count):
                    signed=struct.unpack_from('<h',b,p)[0];p+=2;strip=[]
                    for j in range(abs(signed)):
                        idx=struct.unpack_from('<H',b,p)[0];p+=2;uv=(0,0)
                        if mask&2:
                            uv=np.array(struct.unpack_from('<HH',b,p))/[1,255,1023][(t-64)%3];p+=4
                        if mask&4:p+=4
                        if mask&8:p+=6
                        if mask&16:p+=4
                        p+=user*2;strip.append((verts[idx],uv))
                    for j in range(2,len(strip)):
                        tri=[strip[j-2],strip[j-1],strip[j]]
                        tris.append((np.array([v for v,u in tri]),np.array([u for v,u in tri]),texture_id))
                assert p<=end,('strip size',p,end,t)
                p=end;continue
            raise ValueError(('unsupported NJ chunk',t,path))
    def node(off,anc):
        assert off not in visited;visited.add(off)
        p=base+off;flags,model=struct.unpack_from('<II',b,p);pos=struct.unpack_from('<3f',b,p+8);ang=struct.unpack_from('<3I',b,p+20);scale=struct.unpack_from('<3f',b,p+32);child,sibling=struct.unpack_from('<II',b,p+44)
        chain=anc+[(flags,np.array(pos),ang,np.array(scale))]
        if model:
            vp,pp=struct.unpack_from('<II',b,base+model)
            if vp:chunks(base+vp,chain)
            if pp:chunks(base+pp,chain)
        if child:node(child,chain)
        if sibling:node(sibling,anc)
    node(0,[])
    assert tris,path
    return tris

def render(parts,textures,size=300,angle=0):
    # Orthographic, per-pixel depth-buffered reference render. No animation or skin blending.
    ts=[];rot=np.array([[math.cos(angle),0,math.sin(angle)],[0,1,0],[-math.sin(angle),0,math.cos(angle)]])
    for triangles,offset,mapping,tint in parts:
        for v,uv,tid in triangles:
            target=mapping.get(tid)
            tex=np.array(textures[target]) if target is not None else np.full((1,1,4),255,dtype=np.uint8)
            ts.append(((v+offset)@rot.T,uv,tex,tint))
    pts=np.concatenate([t[0] for t in ts]);lo=pts.min(0);hi=pts.max(0);scale=(size-24)/max((hi-lo)[:2]);center=(lo+hi)/2
    canvas=np.full((size,size,3),239,dtype=np.uint8);zbuf=np.full((size,size),-np.inf)
    for v,uv,tex,tint in ts:
        p=(v-center)*scale;p[:,0]+=size/2;p[:,1]=size/2-p[:,1]
        xmin=max(0,int(p[:,0].min()));xmax=min(size-1,int(math.ceil(p[:,0].max())));ymin=max(0,int(p[:,1].min()));ymax=min(size-1,int(math.ceil(p[:,1].max())))
        if xmin>xmax or ymin>ymax:continue
        x,y=np.meshgrid(np.arange(xmin,xmax+1)+.5,np.arange(ymin,ymax+1)+.5)
        a,c,d=p;den=(c[1]-d[1])*(a[0]-d[0])+(d[0]-c[0])*(a[1]-d[1])
        if abs(den)<1e-9:continue
        w1=((c[1]-d[1])*(x-d[0])+(d[0]-c[0])*(y-d[1]))/den;w2=((d[1]-a[1])*(x-d[0])+(a[0]-d[0])*(y-d[1]))/den;w3=1-w1-w2
        z=w1*a[2]+w2*c[2]+w3*d[2];u=w1*uv[0,0]+w2*uv[1,0]+w3*uv[2,0];vv=w1*uv[0,1]+w2*uv[1,1]+w3*uv[2,1]
        rgba=tex[(vv*tex.shape[0]).astype(int)%tex.shape[0],(u*tex.shape[1]).astype(int)%tex.shape[1]]
        region=zbuf[ymin:ymax+1,xmin:xmax+1];mask=(w1>=-1e-5)&(w2>=-1e-5)&(w3>=-1e-5)&(z>region)&(rgba[:,:,3]>127)
        region[mask]=z[mask];dest=canvas[ymin:ymax+1,xmin:xmax+1];dest[mask]=(rgba[:,:,:3]*np.array(tint)).clip(0,255).astype('uint8')[mask]
    return Image.fromarray(canvas)
