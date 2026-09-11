"""Extract Forest geometry following Qedit main.pas DrawBBRELFile."""
import hashlib,json,pathlib,struct
ROOT=pathlib.Path(__file__).resolve().parents[2];OUT=ROOT/'analysis/floor-database/geometry'
SOURCE=pathlib.Path(r'C:\Users\chasm\Documents\ChatGPT\PSOBB\Qedit\map')
def unpack(b,fmt,offset):
    assert 0<=offset<=len(b)-struct.calcsize(fmt),(offset,len(b),fmt)
    return struct.unpack_from(fmt,b,offset)
def main():
    OUT.mkdir(exist_ok=True)
    for number in (1,2):
        stem=f'map_forest{number:02}';c=(SOURCE/(stem+'c.rel')).read_bytes();n=(SOURCE/(stem+'n.rel')).read_bytes()
        root=unpack(n,'<I',len(n)-16)[0];header=unpack(n,'<5I',root);count=header[2];table=header[4]
        assert count<10000
        rooms=[]
        for i in range(count):
            off=table+i*0x34;rid,x,y,z,unknown,rotation=unpack(n,'<IfffII',off)
            rooms.append(dict(id=rid,position=[x,y,z],rotation_raw=rotation,record_offset=off,raw=n[off:off+0x34].hex()))
        root=unpack(c,'<I',len(c)-16)[0];table=unpack(c,'<I',root)[0];blocks=[]
        for i in range(10000):
            ptr=unpack(c,'<I',table+i*0x18)[0]
            if not ptr:break
            unknown,vertices_at,tri_count,triangles_at=unpack(c,'<4I',ptr)
            assert triangles_at>=vertices_at and (triangles_at-vertices_at)%12==0
            vertices=[list(unpack(c,'<3f',p)) for p in range(vertices_at,triangles_at,12)]
            triangles=[]
            for j in range(tri_count):
                off=triangles_at+j*36;a,b,d,flags=unpack(c,'<4H',off)
                assert max(a,b,d)<len(vertices)
                triangles.append(dict(indices=[a,b,d],flags=flags,raw=c[off:off+36].hex()))
            blocks.append(dict(index=i,vertices=vertices,triangles=triangles))
        else:raise ValueError('Missing collision table terminator')
        data=dict(map=stem,rooms=rooms,collision_blocks=blocks,room_boundary_assignment='not inferred',
            provenance=[dict(file=stem+suffix,sha256=hashlib.sha256(blob).hexdigest()) for suffix,blob in [('c.rel',c),('n.rel',n)]])
        (OUT/(stem+'.json')).write_text(json.dumps(data,indent=2)+'\n')
        points=[v for b in blocks for v in b['vertices']]+[r['position'] for r in rooms]
        xmin=min(v[0] for v in points)-80;xmax=max(v[0] for v in points)+80;zmin=min(v[2] for v in points)-80;zmax=max(v[2] for v in points)+80
        svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{xmin} {zmin} {xmax-xmin} {zmax-zmin}" width="1000" height="1000">',f'<rect x="{xmin}" y="{zmin}" width="{xmax-xmin}" height="{zmax-zmin}" fill="white"/>']
        for b in blocks:
            for t in b['triangles']:
                f=t['flags'];color='blue' if f&64 else '#7fff7f' if f&16 else '#999' if f&1 else 'black'
                xy=' '.join(f'{b["vertices"][i][0]},{b["vertices"][i][2]}' for i in t['indices'])
                svg.append(f'<polygon points="{xy}" fill="none" stroke="{color}" stroke-width="0.65"/>')
        for r in rooms:
            if r['id']>=1000:continue
            x,y,z=r['position'];svg+= [f'<circle cx="{x}" cy="{z}" r="60" fill="#87bce6" fill-opacity="0.65" stroke="black" stroke-width="0.7"/>',f'<text x="{x}" y="{z}" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="40">{r["id"]}</text>']
        svg.append('</svg>');(OUT/(stem+'.svg')).write_text('\n'.join(svg))
        print(stem,'rooms',[r['id'] for r in rooms],'vertices',sum(len(b['vertices']) for b in blocks),'triangles',sum(len(b['triangles']) for b in blocks))
if __name__=='__main__':main()
