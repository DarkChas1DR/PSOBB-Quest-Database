import contextlib,io,json
import extract_forest_geometry as extract
def main():
    results=[]
    for p in sorted(extract.SOURCE.glob('*c.rel')):
        stem=p.name[:-5]
        try:
            with contextlib.redirect_stdout(io.StringIO()):extract.main([stem])
            d=json.loads((extract.OUT/(stem+'.json')).read_text())
            results.append(dict(map=stem,status='extracted',section_ids=[r['id'] for r in d['rooms'] if r['id']<1000],triangles=sum(len(b['triangles']) for b in d['collision_blocks'])))
        except Exception as e:results.append(dict(map=stem,status='failed',error=type(e).__name__+': '+str(e)))
    (extract.OUT/'extraction-index.json').write_text(json.dumps(results,indent=2)+'\n')
    print('Maps:',len(results),'extracted:',sum(r['status']=='extracted' for r in results))
    print([r for r in results if r['status']!='extracted'])
if __name__=='__main__':main()
