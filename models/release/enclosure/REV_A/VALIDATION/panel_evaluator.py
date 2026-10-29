import base64, collections, hashlib, json, math, struct, traceback
from pathlib import Path
import numpy as np
from build123d import Solid, Face, Wire, Plane, Location, Shape, import_step
from OCP.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SOLID
from OCP.BRepGProp import BRepGProp
from OCP.GProp import GProp_GProps

ROOT = Path.cwd()
DATA = ROOT/'schematics/work/enclosure/B26-CONSOLIDATED-02/panel'
REL = ROOT/'models/release/enclosure/B26/B26-build123d03_RELEASE'
OUT = ROOT/'tmp/rev-a-panel/results-final.json'
load = lambda p: json.loads(p.read_text())
d = load(DATA/'frontpanel_data.json')
meshes = load(DATA/'B26_CONSOLIDATED_01_caps_mesh_DRAFT.json')['definitions']
poses = load(DATA/'B26_CONSOLIDATED_01_caps_poses_DRAFT.json')['occurrences']
evidence = load(REL/'STEP/assembly-evidence.json')
assert len(d['apertures']) == 69 and len(d['marks']) == 65 and len(poses) == 49
assert sum(map(len, d['closure_axes'].values())) == 28 and len(meshes) == 9
report = {'units':'mm; volume mm^3', 'tolerances':{'edge_selection_mm':1e-5, 'corner_selection_mm':1e-6, 'bounds_mm':1e-5, 'volume_mm3':1e-4, 'transform_mm':1e-8, 'rotation_component':1e-8}, 'caps':{}, 'occurrences':[], 'panels':{}, 'errors':[], 'notes':['Cap reference is released binary STL plus release STEP occurrence evidence; this is not an independent STEP geometry comparison.', 'All cap identity mapping is based on owner and full inventory ID, not collapsed STEP labels.']}
def save(): OUT.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
def box(x0,x1,y0,y1,z0,z1): return Solid.make_box(x1-x0,y1-y0,z1-z0,Plane(origin=(x0,-y1,z0)))
def cyl(x,y,r,z0,z1): return Solid.make_cylinder(r,z1-z0,Plane(origin=(x,-y,z0)))
def poly(points,z,h,table=True):
    wire=Wire.make_polygon([(x,-y if table else y,z) for x,y in points],close=True)
    return Solid.extrude(Face(wire),(0,0,h))
def rr(x,y,w,h,r,z0,z1):
    pieces=[]
    if w-2*r>1e-9: pieces.append(box(x-w/2+r,x+w/2-r,y-h/2,y+h/2,z0,z1))
    if h-2*r>1e-9: pieces.append(box(x-w/2,x+w/2,y-h/2+r,y+h/2-r,z0,z1))
    pieces.extend(cyl(x+sx*(w/2-r),y+sy*(h/2-r),r,z0,z1) for sx in (-1,1) for sy in (-1,1))
    return pieces[0].fuse(*pieces[1:])
def edges_at(shape,predicate):
    return [e for e in shape.edges() if all(predicate(e.position_at(t)) for t in (0,.25,.5,.75,1))]
def top(p): return abs(p.Z-20)<1e-5
def profile(k):
    f=96+5/math.tan(math.radians(49))
    if k=='R03': return box(220,380,f,140,18,20)
    if k=='R06': return box(220,380,140,320,18,20)
    x0,x1=(0,220) if k in ('R01','R05') else (380,600)
    a,b=(75,145) if x0==0 else (455,525)
    if k in ('R01','R04'):
        p=box(x0,x1,0,140,18,20).fuse(box(a,b,140,165,18,20))
        return p.cut(box(153.55,220,0,f,18,20) if x0==0 else box(380,446.45,0,f,18,20))
    return box(x0,x1,140,320,18,20).cut(box(a,b,140,165,18,20))
def aperture(row):
    name,x,y,kind,w,h,r,_,panel=row
    if name.startswith('T'):
        a=7.2+1.6*math.sqrt(5); s=1 if int(name[1:])%2 else -1
        return poly([(x+s*u,-y+s*v) for u,v in [(-a,0),(4,(a+4)/2),(4,-(a+4)/2)]],17,5,False)
    if kind=='circle': return cyl(x,y,w/2,17,22)
    if kind=='rect': return box(x-w/2,x+w/2,y-h/2,y+h/2,17,22)
    if kind in ('rr','slot'): return rr(x,y,w,h,min(w,h)/2 if kind=='slot' else r,17,22)
    raise ValueError(('unknown aperture',row))
def checked(shape,stage):
    if not shape or not shape.is_valid or len(shape.solids())!=1: raise ValueError(f'{stage}: invalid or not one solid')
    return shape

def panel(k):
    p=profile(k)
    rows=[r for r in d['apertures'] if r[-1]==k]
    for row in rows: p=checked(p.cut(aperture(row)), 'aperture '+row[0])
    if k not in ('R03','R06'):
        x=0 if k in ('R01','R05') else 600; y=0 if k in ('R01','R04') else 320
        es=edges_at(p,lambda v: abs(v.X-x)<1e-6 and abs(v.Y+y)<1e-6)
        assert len(es)==1, ('corner',k,len(es))
        p=checked(p.fillet(3,es),'corner fillet')
    if k != 'R03':
        def outer(v):
            if not top(v): return False
            x,y=v.X,-v.Y
            return abs(x)<1e-5 or abs(x-600)<1e-5 or abs(y)<1e-5 or abs(y-320)<1e-5 or abs(math.hypot(x-(3 if x<300 else 597),y-(3 if y<160 else 317))-3)<1e-5
        es=edges_at(p,outer); assert es, ('outer',k)
        p=checked(p.fillet(.8,es),'rim fillet')
    faders=[r for r in d['apertures'] if r[-1]==k and r[0].startswith('F')]
    for name,x,y,*_ in faders:
        w,h=(69.7,14) if name=='F05' else (14,69.7)
        p=checked(p.cut(rr(x,y,w,h,3,19,22)), 'fader '+name)
        es=edges_at(p,lambda v: top(v) and abs(v.X-x)<=w/2+1e-5 and abs(-v.Y-y)<=h/2+1e-5)
        assert es, ('fader chamfer',name)
        p=checked(p.chamfer(.8,None,es),'fader chamfer '+name)
    if k in ('R01','R04','R05','R07'):
        x=110 if k in ('R01','R05') else 490; y=165
        p=checked(p.cut(cyl(x,y,26,17,22)).cut(cyl(x,y,54,19,22)),'jog cut')
        es=edges_at(p,lambda v: top(v) and abs(math.hypot(v.X-x,-v.Y-y)-54)<1e-5)
        assert es, ('jog chamfer',k)
        p=checked(p.chamfer(.8,None,es),'jog chamfer')
    for row in rows:
        name,x,y,kind,w,h,r,_,_=row
        if not name.startswith(('B','T')): continue
        extent=7.2+1.6*math.sqrt(5)+.01 if name.startswith('T') else max(w,h)/2+.01
        es=edges_at(p,lambda v: top(v) and abs(v.X-x)<extent and abs(-v.Y-y)<extent)
        assert es, ('aperture chamfer',name)
        try: p=checked(p.chamfer(.8,None,es),'aperture chamfer '+name)
        except Exception as exc: raise RuntimeError(f'aperture chamfer {name}; selected {len(es)} edges: {exc}') from exc
    for mark in d['marks']:
        if mark['panel']==k:
            z0,z1=mark['z']; p=checked(p.fuse(poly(mark['polygon'],z0,z1-z0)),'mark '+mark['id'])
    for name,x,y,*_ in faders:
        travel=28 if name=='F05' else 41
        for j in range(11):
            u=-travel/2+j*travel/10; length=4 if j in (0,5,10) else 2
            for sign in (-1,1):
                local=[(u-.4,sign*2.4),(u+.4,sign*2.4),(u+.4,sign*(2.4+length)),(u-.4,sign*(2.4+length))]
                points=[(x+uu,y-vv) if name=='F05' else (x+vv,y+uu) for uu,vv in local]
                p=checked(p.fuse(poly(points,19,.4)),'tick '+name)
    for x,y in d['closure_axes'][k]:
        p=checked(p.cut(cyl(x,y,1.7,17,22)).cut(Solid.make_cone(1.7,3,1.3,Plane(origin=(x,-y,18.7)))),'closure')
    return p

def bounds(s):
    b=s.bounding_box(); return [[b.min.X,b.min.Y,b.min.Z],[b.max.X,b.max.Y,b.max.Z]]
def cutvol(a,b):
    op=BRepAlgoAPI_Cut(a.wrapped,b.wrapped); op.Build()
    if not op.IsDone() or op.Shape().IsNull(): raise RuntimeError('BRepAlgoAPI_Cut failed')
    props=GProp_GProps(); BRepGProp.VolumeProperties_s(op.Shape(),props)
    return abs(props.Mass())
def difference_components(a,b):
    op=BRepAlgoAPI_Cut(a.wrapped,b.wrapped); op.Build()
    if not op.IsDone() or op.Shape().IsNull(): raise RuntimeError('component cut failed')
    return [{'bounds_mm':bounds(s),'volume_mm3':s.volume} for s in Shape.cast(op.Shape()).solids()]

for key,mesh in meshes.items():
    try:
        triangles=mesh['triangles']; assert len(triangles)==mesh['triangle_count']
        raw=base64.b64decode(mesh['header_base64'],validate=True)+struct.pack('<I',len(triangles))
        assert len(raw)==84
        edges=collections.Counter(); oriented=collections.Counter(); volume=0.0; verts=[]
        for t in triangles:
            vs=t['vertices_mm']; verts.extend(vs)
            raw+=struct.pack('<12fH',*(t['normal']+sum(vs,[])),t['attribute'])
            volume+=float(np.dot(vs[0],np.cross(vs[1],vs[2])))/6
            for i in range(3):
                a,b=tuple(vs[i]),tuple(vs[(i+1)%3]); edges[tuple(sorted((a,b)))]+=1; oriented[(a,b)]+=1
        digest=hashlib.sha256(raw).hexdigest()
        release=REL/'STL'/f'{key}_Rev_B26_build123d03.stl'
        data=release.read_bytes()
        manifold=all(n==2 for n in edges.values())
        winding=all(oriented[(a,b)]==oriented[(b,a)] for a,b in oriented)
        v=np.array(verts)
        report['caps'][key]={'triangles':len(triangles),'roundtrip_sha256':digest,'documented_sha256_match':digest==mesh['source_sha256'],'release_stl_path':str(release.relative_to(ROOT)),'release_stl_byte_identical':raw==data,'watertight_edges':manifold,'consistent_edge_winding':winding,'signed_volume_mm3':volume,'local_bounds_mm':[v.min(axis=0).tolist(),v.max(axis=0).tolist()]}
    except Exception as exc: report['caps'][key]={'error':repr(exc)}; report['errors'].append('cap '+key+': '+traceback.format_exc())
    save()
for pose in poses:
    try:
        key=pose['mesh_definition']; cap=report['caps'][key]
        ex=np.array(pose['cad_x_direction']); ez=np.array(pose['cad_z_direction']); ey=np.cross(ez,ex); o=np.array(pose['cad_origin_mm'])
        assert abs(np.linalg.norm(ex)-1)<1e-9 and abs(np.linalg.norm(ez)-1)<1e-9 and abs(np.dot(ex,ez))<1e-9
        matrix=np.column_stack((ex,ey,ez,o)); ref=evidence['cap_placements'][pose['owner']+'-CAP-REF']; delta=float(np.max(np.abs(matrix-np.array(ref['world_transform']))))
        vertices=np.array([v for tri in meshes[key]['triangles'] for v in tri['vertices_mm']]); world=vertices@matrix[:,:3].T+o
        report['occurrences'].append({'owner':pose['owner'],'inventory_id':pose['inventory_id'],'definition':key,'cad_transform':matrix.tolist(),'world_bounds_mm':[world.min(axis=0).tolist(),world.max(axis=0).tolist()],'release_evidence_definition_match':ref['definition']==key,'release_evidence_transform_max_abs':delta,'release_evidence_transform_match':delta<1e-8,'release_evidence_bounds_difference_mm':ref['bounds_difference_mm'],'reference_mesh_byte_identical':cap['release_stl_byte_identical'],'status':'release STL + recorded STEP placement; direct STEP identity and BRep boolean not established'})
    except Exception as exc: report['occurrences'].append({'owner':pose['owner'],'error':repr(exc)}); report['errors'].append('pose '+pose['owner']+': '+traceback.format_exc())
    save()
try:
    step=import_step(REL/'STEP/B26-build123d03-trial-assembly.step')
    leaves=[]
    def visit(node,parent,path):
        if node.children:
            loc=parent*node.location
            for i,c in enumerate(node.children): visit(c,loc,path+[i])
        else: leaves.append((path,node.label,node.moved(parent)))
    visit(step,Location(),[])
    report['step_import']={'leaf_count':len(leaves),'solid_leaves':sum(bool(s.solids()) for _,_,s in leaves),'identity_note':'numeric tree paths; names may collapse to referred labels'}
except Exception:
    leaves=[]; report['errors'].append('STEP import: '+traceback.format_exc())
save()
for k in ('R01','R03','R04','R05','R06','R07'):
    result={'assigned_apertures':sum(r[-1]==k for r in d['apertures']),'assigned_marks':sum(m['panel']==k for m in d['marks']),'closure_axes':len(d['closure_axes'][k]),'assigned_ticks':22*sum(r[-1]==k and r[0].startswith('F') for r in d['apertures'])}
    report['panels'][k]=result
    try:
        p=panel(k); result.update({'valid':p.is_valid,'solid_count':len(p.solids()),'volume_mm3':p.volume,'bounds_mm':bounds(p)})
        matches=[(path,label,s) for path,label,s in leaves if k in label and 'PANEL' in label.upper() and len(s.solids())==1]
        result['step_label_candidates']=[{'path':path,'label':label,'bounds_mm':bounds(s)} for path,label,s in matches]
        close=[(path,label,s) for path,label,s in matches if max(abs(a-b) for ar,br in zip(bounds(p),bounds(s)) for a,b in zip(ar,br))<1e-5]
        if len(close)!=1: raise ValueError(f'STEP panel match ambiguous: {len(close)} close of {len(matches)} candidates')
        path,label,s=close[0]; result.update({'reference_path':path,'reference_label':label,'reference_volume_mm3':s.volume,'reference_valid':s.is_valid,'reconstruction_minus_step_mm3':cutvol(p,s),'step_minus_reconstruction_mm3':cutvol(s,p)})
        if k=='R06': result['reconstruction_minus_step_components']=difference_components(p,s)
    except Exception as exc: result['error']=repr(exc); result['traceback']=traceback.format_exc(); report['errors'].append(k+': '+repr(exc))
    save()
report['coverage']={'panels_attempted':len(report['panels']),'panels_completed':sum('reconstruction_minus_step_mm3' in x for x in report['panels'].values()),'mesh_definitions_attempted':len(report['caps']),'mesh_roundtrips_match':sum(x.get('documented_sha256_match',False) and x.get('release_stl_byte_identical',False) for x in report['caps'].values()),'occurrences_attempted':len(report['occurrences']),'occurrences_matched_recorded_placement':sum(x.get('release_evidence_transform_match',False) and x.get('release_evidence_definition_match',False) and x.get('reference_mesh_byte_identical',False) for x in report['occurrences']),'expected_apertures':69,'expected_marks':65,'expected_ticks':110,'expected_closures':28}
save()
print(json.dumps({'coverage':report['coverage'],'errors':report['errors']},indent=2))
