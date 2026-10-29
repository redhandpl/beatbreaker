import hashlib
import json
import math
import struct
from pathlib import Path

root = Path('tmp/rev-a-release/models')
manifest_path = root / 'STL/B26-build123d03_STL_manifest.json'
manifest = json.loads(manifest_path.read_text())
parts = manifest['parts']
assert len(parts) == 36 and sum(item['quantity'] for item in parts.values()) == 155
out = {'units':'STL unitless; interpreted as mm', 'welding':'exact numeric coordinates; +0 and -0 equivalent', 'normal_opposition_cosine_threshold':-1e-5, 'degenerate_cross_magnitude_threshold_mm2':1e-12, 'parts':{}, 'limits':['No self-intersection or vertex-link manifold test.', 'Stored normals are checked for finiteness and non-opposition; they are not assumed unit length.', 'Connected surfaces are edge-connected components; no physical-fit or slicer validation.']}
for name, item in parts.items():
    path = root / 'STL' / item['filename']
    blob = path.read_bytes()
    if hashlib.sha256(blob).hexdigest() != item['sha256']:
        raise RuntimeError(f'{name}: SHA-256 mismatch')
    if len(blob) < 84:
        raise RuntimeError(f'{name}: truncated STL')
    count = struct.unpack_from('<I', blob, 80)[0]
    if not count or len(blob) != 84 + 50*count:
        raise RuntimeError(f'{name}: invalid binary STL length/count')
    parents = list(range(count))
    def find(i):
        while parents[i] != i:
            parents[i] = parents[parents[i]]
            i = parents[i]
        return i
    def union(i,j):
        i, j = find(i), find(j)
        if i != j:
            parents[j] = i
    edges = {}
    lo = [float('inf')]*3
    hi = [float('-inf')]*3
    zero_normals = opposed_normals = degenerate = 0
    for i in range(count):
        values = struct.unpack_from('<12fH',blob,84+i*50)
        if not all(math.isfinite(v) for v in values[:12]):
            raise RuntimeError(f'{name}: non-finite facet {i}')
        normal=values[:3]
        points=[tuple(values[3+j*3:6+j*3]) for j in range(3)]
        for p in points:
            for k in range(3):
                lo[k]=min(lo[k],p[k]); hi[k]=max(hi[k],p[k])
        a,b,c=points
        u=[b[k]-a[k] for k in range(3)]; v=[c[k]-a[k] for k in range(3)]
        cross=(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
        clen=math.sqrt(sum(t*t for t in cross)); nlen=math.sqrt(sum(t*t for t in normal))
        if clen <= 1e-12: degenerate += 1
        if nlen == 0: zero_normals += 1
        elif clen > 0 and sum(x*y for x,y in zip(normal,cross))/(nlen*clen) < -1e-5: opposed_normals += 1
        for p,q in ((a,b),(b,c),(c,a)):
            key=(p,q) if p<q else (q,p); direction=1 if p<q else -1
            if key in edges:
                first,nsign,n=edges[key]
                union(i,first)
                edges[key]=(first,nsign+direction,n+1)
            else:
                edges[key]=(i,direction,1)
    boundary=sum(n==1 for _,_,n in edges.values())
    nonmanifold=sum(n>2 for _,_,n in edges.values())
    winding=sum(n==2 and direction!=0 for _,direction,n in edges.values())
    components=len({find(i) for i in range(count)})
    expected=item['checker']['geometry']['bounding_box']
    bound_err=max(abs(a-b) for pair,compare in ((lo,expected['min_mm']),(hi,expected['max_mm'])) for a,b in zip(pair,compare))
    record={'filename':item['filename'],'sha256':item['sha256'],'quantity':item['quantity'],'triangles':count,'bounds_mm':[lo,hi],'max_bound_error_mm':bound_err,'boundary_edges':boundary,'nonmanifold_edges':nonmanifold,'winding_conflicts':winding,'edge_connected_components':components,'degenerate_triangles':degenerate,'zero_stored_normals':zero_normals,'opposed_stored_normals':opposed_normals}
    out['parts'][name]=record
    if boundary or nonmanifold or winding or components!=1 or degenerate or zero_normals or opposed_normals or bound_err>1e-5:
        raise RuntimeError(f'{name}: mesh check failed: {record}')
    print(f'{name}: {count} triangles, closed, 1 component, normals consistent',flush=True)
out['total_definitions']=len(parts); out['total_occurrences']=sum(item['quantity'] for item in parts.values())
path=root/'VALIDATION/REV_A_mesh_check.json'
with path.open('x') as f:
    json.dump(out,f,indent=2,allow_nan=False); f.write('\n')
print(f'PASS: {len(parts)} STL definitions, {out["total_occurrences"]} occurrences',flush=True)
