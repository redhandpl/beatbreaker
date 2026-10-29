import copy, hashlib, json, math, sys, time, traceback
from pathlib import Path
from build123d import Solid, Shape, Plane, Matrix, Wire, Face, import_step
from OCP.BRepAlgoAPI import BRepAlgoAPI_Cut

ROOT = Path.cwd()
DATA = ROOT / 'schematics/work/enclosure/B26-CONSOLIDATED-02/shell/shell_dataset_DRAFT.json'
PDF = ROOT / 'schematics/work/enclosure/B26-CONSOLIDATED-02/B26_CONSOLIDATED_02_complete_DRAFT.pdf'
STEP = ROOT / 'models/release/enclosure/B26/B26-build123d03_RELEASE/STEP/B26-build123d03-trial-assembly.step'
OUT = ROOT / 'tmp/rev-a-shell/evidence-checked.json'
EXPECTED = {str(PDF): '35ab5a40ae0051ec4080cb6cfb287782c482859d1a6f666e9a8b0ccca00226c2', str(DATA): '1687a23e7c45b43ed2a21ff8acc0567f4d053a37da6891892131f3a0b2b30f57', str(STEP): 'be226639517a5e5042979a5c78039f82f4e40c89f9d92193f8bd150e7c0c258b'}

def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''): h.update(chunk)
    return h.hexdigest()

def box(x0,x1,y0,y1,z0,z1):
    assert x1 > x0 and y1 > y0 and z1 > z0, (x0,x1,y0,y1,z0,z1)
    return Solid.make_box(x1-x0,y1-y0,z1-z0,Plane(origin=(x0,y0,z0)))

def cyl(x,y,z0,z1,r0,r1=None):
    assert z1 > z0 and r0 > 0
    p = Plane(origin=(x,y,z0))
    return Solid.make_cylinder(r0,z1-z0,p) if r1 is None or r0 == r1 else Solid.make_cone(r0,r1,z1-z0,p)

def polygon(points, direction):
    return Solid.extrude(Face(Wire.make_polygon(points, close=True)), direction)

def section(x0,width,yz):
    return polygon([(x0,y,z) for y,z in yz], (width,0,0))

def rr(x,y,z,w,h,r,d):
    parts = [box(x-w/2+r,x+w/2-r,y-h/2,y+h/2,z,z+d), box(x-w/2,x+w/2,y-h/2+r,y+h/2-r,z,z+d)]
    parts += [cyl(x+sx*(w/2-r),y+sy*(h/2-r),z,z+d,r) for sx in (-1,1) for sy in (-1,1)]
    return fuse(parts)

def fuse(items):
    assert items
    a = items[0]
    for b in items[1:]: a = a.fuse(b)
    return a

def primitive(p):
    kind,(x,y,z),s = p
    if kind == 0: return box(x,x+s[0],y,y+s[1],z,z+s[2])
    if kind == 1: return cyl(x,y,z,z+s[2],s[0],s[1])
    if kind == 2: return rr(x,y,z,*s)
    raise ValueError(('unknown primitive',kind))

def csg(row):
    _,m,adds,cuts = row['CSG']
    a = fuse([primitive(p) for p in adds])
    for p in cuts: a = a.cut(primitive(p))
    # Compose the table-to-CAD reflection with the documented local-to-table matrix.
    t = [[m[0][j] for j in range(4)],[-m[1][j] for j in range(4)],[m[2][j] for j in range(4)],[0,0,0,1]]
    det = t[0][0]*t[1][1]-t[0][1]*t[1][0]
    assert abs(abs(det)-1) < 1e-9
    if det < 0:
        a = a.mirror(Plane.XZ)
        for i in range(3): t[i][1] = -t[i][1]
    return a.transform_shape(Matrix(t))

def table_to_cad(a): return a.mirror(Plane.XZ)

def bounds(a):
    b=a.bounding_box()
    return [[b.min.X,b.min.Y,b.min.Z],[b.max.X,b.max.Y,b.max.Z]]

def delta_bounds(a,b):
    x,y=bounds(a),bounds(b)
    return max(abs(x[i][j]-y[i][j]) for i in range(2) for j in range(3))

def overlapping(a,b):
    x,y=bounds(a),bounds(b)
    return all(x[0][i] < y[1][i]-1e-7 and y[0][i] < x[1][i]-1e-7 for i in range(3))

def clip_attach(shell, feature, clip):
    if not overlapping(feature,clip): return shell
    pieces=feature.intersect(clip)
    solids=[s for p in pieces for s in p.solids()]
    if not solids: return shell
    return shell.fuse(*solids)

def line_edge(e, x=None, y=None, vertical=False, bottom=False):
    b=e.bounding_box(); eps=1e-5
    if x is not None and (abs(b.min.X-x)>eps or abs(b.max.X-x)>eps): return False
    if y is not None and (abs(b.min.Y-y)>eps or abs(b.max.Y-y)>eps): return False
    if vertical and (b.max.Z-b.min.Z < 1 or b.max.X-b.min.X>eps or b.max.Y-b.min.Y>eps): return False
    if bottom and (abs(b.min.Z)>eps or abs(b.max.Z)>eps): return False
    return True

def shell_base(name, domain, sc):
    x0,x1,y0,y1=domain
    a=box(x0,x1,y0,y1,0,18).cut(box(max(x0,2),min(x1,598),max(y0,2),min(y1,318),2,102))
    if y0==0 and min(x1,446.45)>max(x0,153.55): a=a.fuse(box(max(x0,153.55),min(x1,446.45),0,2,18,23+80*math.sin(math.radians(49))))
    if name in ('C01','C03','C04','C06'):
        x=0 if x0==0 else 600; y=0 if y0==0 else 320
        es=[e for e in a.edges() if line_edge(e,x,y,vertical=True)]
        assert len(es)==1,(name,'outer edge',len(es))
        a=a.fillet(3,es)
        es=[e for e in a.edges() if line_edge(e,2 if x==0 else 598,2 if y==0 else 318,vertical=True)]
        assert len(es)==1,(name,'inner edge',len(es))
        a=a.fillet(1,es)
    es=[]
    for e in a.edges():
        b=e.bounding_box()
        if not line_edge(e,bottom=True): continue
        on_external = (abs(b.min.X)<1e-5 and abs(b.max.X)<1e-5) or (abs(b.min.X-600)<1e-5 and abs(b.max.X-600)<1e-5) or (abs(b.min.Y)<1e-5 and abs(b.max.Y)<1e-5) or (abs(b.min.Y-320)<1e-5 and abs(b.max.Y-320)<1e-5)
        corner = (b.max.X-b.min.X>1e-5 and b.max.Y-b.min.Y>1e-5 and ((b.min.X<3.01 or b.max.X>596.99) and (b.min.Y<3.01 or b.max.Y>316.99)))
        if on_external or corner: es.append(e)
    if es: a=a.fillet(.8,es)
    if name=='C01':
        a=a.cut(box(37.25,72.15,-.01,2.01,2,18))
        for x in (32.75,76.65): a=a.cut(Solid.make_cylinder(1.8,2.02,Plane(origin=(x,-.01,9.95),z_dir=(0,1,0))))
        ac=sc['inlet_definition']; xx=ac['cutout_X_mm']; zz=ac['cutout_Z_mm']; a=a.cut(box(xx[0],xx[1],0,2,zz[0],zz[1]))
    if name=='C02':
        for v in sc['ventilation_cells_original']:
            a=a.cut(polygon([(x,-.01,z) for x,z in v['polygon_XZ']],(0,2.02,0)))
    if name=='C04': a=a.cut(Solid.make_cylinder(3.1,2.02,Plane(origin=(101,317.99,10),z_dir=(0,1,0))))
    return table_to_cad(a)

def build_shell(name,domain,sc,fixed):
    x0,x1,y0,y1=domain; clip=table_to_cad(box(x0,x1,y0,y1,0,102)); a=shell_base(name,domain,sc)
    for p in sc['posts']:
        x,y=p['centre_XY']; foot=p['foot']; core=p['core']; pilot=p['pilot']
        q=cyl(x,y,*foot['z'],foot['bottom_radius'],foot['top_radius']).fuse(cyl(x,y,*core['z'],core['radius'])).cut(cyl(x,y,*pilot['z'],pilot['radius']))
        a=clip_attach(a,table_to_cad(q),clip)
    for j in sc['joints']:
        for d in (-9,9):
            x,y=j['centre']; x+=d if j['normal']=='X' else 0; y+=d if j['normal']=='Y' else 0
            q=cyl(x,y,2,8,4.5).cut(cyl(x,y,2.5,8.01,1.25))
            a=clip_attach(a,table_to_cad(q),clip)
    for row,q in fixed: a=clip_attach(a,q,clip)
    for device in sc['device_mount_axes_original_table_XY']:
        for x,y in device['axes']:
            y+=20
            if not (x0 <= x <= x1 and y0 <= y <= y1): continue
            kind=device['id']; q=cyl(x,y,2,3 if kind=='PSU' else 6,5 if kind=='PSU' else 3.5)
            a=a.fuse(table_to_cad(q))
            if kind=='PI': a=a.cut(table_to_cad(cyl(x,y,1,6.01,1)))
            if kind=='PSU': a=a.cut(table_to_cad(cyl(x,y,-.01,3.01,1.7))).cut(table_to_cad(cyl(x,y,0,1.3,3,1.7)))
    for cx in (110,490):
        if not (x0 <= cx <= x1 and y0 <= 165 <= y1): continue
        for deg in (150,270,30):
            t=math.radians(deg); x=cx+31*math.cos(t); y=165-31*math.sin(t)
            a=a.fuse(table_to_cad(cyl(x,y,2,8,5))).cut(table_to_cad(cyl(x,y,-.01,2.5,2.4))).cut(table_to_cad(cyl(x,y,2.5,8.01,1.45)))
        for deg in (60,180,300):
            t=math.radians(deg); a=a.fuse(table_to_cad(cyl(cx+26.2*math.cos(t),165-26.2*math.sin(t),2,3.5,1)))
        a=a.fuse(box(24,26,-1,1,0,1).rotate(__import__('build123d').Axis.Z,60).translate((cx,-165,2)))
    return a

def bridge(j):
    x,y=j['centre']
    if j['normal']=='X': a=box(x-14,x+14,y-5,y+5,8,11); axes=[(x-9,y),(x+9,y)]
    else: a=box(x-5,x+5,y-14,y+14,8,11); axes=[(x,y-9),(x,y+9)]
    for px,py in axes: a=a.cut(cyl(px,py,7.99,11.01,1.7))
    return table_to_cad(a)

ang=math.radians(49); sn=math.sin(ang); cs=math.cos(ang); F=96+5/math.tan(ang); J=96-80*cs; U=25+80*sn; CY=96-40*cs; H=23+40*sn

def placed(a,side,row):
    if side*row>0: a=a.mirror(Plane.XZ)
    # x=(side,0,0), y=z cross x, z=(0,-sin49,cos49).
    m=Matrix([[side,0,0,300],[0,side*cs,-sn,-CY],[0,side*sn,cs,H],[0,0,0,1]])
    return a.transform_shape(m)

def toe(side,row):
    a=box(136.5,144.2,20,28,-21,-18).fuse(box(136.5,137.5,20,28,-18,-17))
    a=a.cut(cyl(140.7,24,-21.1,-17.9,1.7))
    return placed(a,side,row)

def roof(name):
    left=name=='D02L'; x0,x1=(153.55,335) if left else (335,446.45)
    a=section(x0,x1-x0,[(0,U-2),(J,U-2),(F,18),(F,20),(J,U),(0,U)])
    rx0,rx1=(153.55,155.55) if left else (444.45,446.45)
    a=a.fuse(section(rx0,rx1-rx0,[(2,18),(F,18),(F,20),(J,U),(2,U)]))
    a=table_to_cad(a).cut(placed(box(-136,136,-36,36,-5,5),1,1))
    for x in (210,230,300,370,390):
        if x0<x<x1: a=a.cut(table_to_cad(cyl(x,4,U-2.01,U+.01,1.7))).cut(table_to_cad(cyl(x,4,U-1.3,U,1.7,3)))
    if left: a=a.fuse(table_to_cad(box(325,345,13,29,U-10,U-2)))
    for y in (18,24):
        if left: a=a.cut(table_to_cad(cyl(340,y,U-9,U-1.99,1.25)))
        else: a=a.cut(table_to_cad(cyl(340,y,U-2.01,U+.01,1.7))).cut(table_to_cad(cyl(340,y,U-1.3,U,1.7,3)))
    x=228 if left else 372
    a=a.fuse(table_to_cad(section(x-5,10,[(95,16),(116,16),(116,18),(F,18),(95,23+math.tan(ang))]))).cut(table_to_cad(cyl(x,110,15.99,18.01,1.7)))
    side=-1 if left else 1
    for row in (-1,1):
        q=fuse([box(138.5,144.2,18,30,-21.2,0),box(138.25,140,20,39.797470349551496,-21,-.25),box(130,140,38.297470349551496,39.797470349551496,-21,-.25)])
        q=q.cut(box(136,146,19.9,28.1,-21.2,-18)).cut(cyl(140.7,24,-18.1,-11,1.25)).cut(cyl(140.7,24,-60,-21,4))
        a=a.fuse(placed(q,side,row))
    es=[e for e in a.edges() if abs(e.bounding_box().min.Z-U)<1e-5 and abs(e.bounding_box().max.Z-U)<1e-5 and abs(e.bounding_box().min.Y)<1e-5 and abs(e.bounding_box().max.Y)<1e-5]
    if es: a=a.fillet(.8,es)
    return a

def walk(node,path=()):
    if node.children:
        for i,ch in enumerate(node.children): yield from walk(ch,path+(i,))
    else:
        shape=copy.copy(node); shape.parent=None; shape.locate(node.global_location)
        yield path,node.label,shape

def snapshot(evidence):
    temp=OUT.with_suffix('.json.tmp')
    with open(temp,'w') as f: json.dump(evidence,f,indent=2,allow_nan=False)
    temp.replace(OUT)

def checked_cut(a,b):
    op=BRepAlgoAPI_Cut(a.wrapped,b.wrapped)
    if not op.IsDone(): raise RuntimeError('OCCT BRepAlgoAPI_Cut IsDone is false')
    if hasattr(op,'HasErrors') and op.HasErrors(): raise RuntimeError('OCCT BRepAlgoAPI_Cut reports errors')
    out=Shape.cast(op.Shape())
    if not out.is_valid: raise RuntimeError('OCCT BRepAlgoAPI_Cut produced invalid shape')
    return out, bool(op.HasWarnings()) if hasattr(op,'HasWarnings') else None

def compare(id,shapes,candidates,ev):
    expected=[s for s in shapes if not s.is_empty]
    records=[]; used=set()
    for index,a in enumerate(expected):
        ranked=sorted((delta_bounds(a,b),i,path,label,b) for i,(path,label,b) in enumerate(candidates) if i not in used and len(b.solids())==1)
        if not ranked: records.append({'body':index,'error':'no unused single-solid STEP candidates'}); continue
        d,i,path,label,b=ranked[0]
        if d>0.001: records.append({'body':index,'error':'no STEP candidate within bounding tolerance','nearest_numeric_path':path,'nearest_label':label,'nearest_bound_delta_mm':d,'reconstructed_bounds_mm':bounds(a)}); continue
        ties=[r for r in ranked if abs(r[0]-d)<1e-7]
        if len(ties)>1: records.append({'body':index,'error':'ambiguous equal bounds','numeric_paths':[r[2] for r in ties],'bound_delta_mm':d}); continue
        used.add(i)
        result={'body':index,'step_numeric_path':path,'step_label':label,'reconstructed_bounds_mm':bounds(a),'step_bounds_mm':bounds(b),'bound_delta_mm':d,'reconstructed_volume_mm3':a.volume,'step_volume_mm3':b.volume,'volume_delta_mm3':abs(a.volume-b.volume),'reconstructed_valid':a.is_valid,'step_valid':b.is_valid}
        try:
            ab,wab=checked_cut(a,b); ba,wba=checked_cut(b,a)
            result['reconstructed_minus_step_mm3']=ab.volume
            result['step_minus_reconstructed_mm3']=ba.volume
            result['boolean_done_and_valid']=True
            result['boolean_warnings']=[wab,wba]
            result['difference_volume_conservation_error_mm3']=abs((ab.volume-ba.volume)-(a.volume-b.volume))
            if result['difference_volume_conservation_error_mm3']>1e-4:
                result['boolean_error']='two-way differences violate volume conservation'
            result['matches_test_tolerances']=d<=1e-5 and abs(a.volume-b.volume)<=1e-4 and ab.volume<=1e-4 and ba.volume<=1e-4 and result['difference_volume_conservation_error_mm3']<=1e-4 and a.is_valid and b.is_valid
        except Exception as ex: result['boolean_error']=repr(ex)
        records.append(result)
    ev['results'][id]={'body_count':len(expected),'bodies':records}
    snapshot(ev)

def main():
    assert not OUT.exists(), 'Evidence exists; do not overwrite'
    hashes={p:sha(p) for p in EXPECTED}
    assert hashes==EXPECTED, hashes
    data=json.loads(DATA.read_text()); sc=data['schedules']; ops=data['operations']
    controls=sc['controls']; fixedrows=[r for r in controls if 'FIXED' in r['id'] or r['id']=='E01-fixed_cage']; ret=[r for r in controls if r not in fixedrows]
    assert len(fixedrows)==49 and len(ret)==49 and len(sc['joints'])==16 and len(sc['posts'])==33
    assert abs(F-100.346433689)<1e-8 and abs(U-85.3767664178)<1e-8
    ev={'input_sha256':hashes,'criteria':{'bounds_mm':1e-5,'absolute_volume_mm3':1e-4,'each_direction_boolean_volume_mm3':1e-4,'comparison_candidate_bound_mm':0.001},'denominator':{'shells':6,'bridges':16,'retainer_groups':49,'retainer_solids':54,'roof_halves':2,'display_toes':4},'results':{},'errors':[],'notes':['Numeric STEP tree paths and global_location are used; labels alone are not assumed unique. Matching requires unique 0.001 mm bounds; boolean exceptions are errors.','The reconstruction is documentation review only, not a print or safety approval.']}
    snapshot(ev)
    root=import_step(STEP); leaves=list(walk(root)); ev['import_leaf_count']=len(leaves); ev['import_single_solid_leaves']=sum(len(s.solids())==1 for _,_,s in leaves)
    # Restrict matching by release assembly branch and split multi-solid retainer leaves.
    cats={}
    for path,label,s in leaves:
        anc=root
        for i in path[:-1]: anc=anc.children[i]
        branch=anc.label.lower()
        if any(w in branch for w in ('lower_shells','shell_bridges','control_retainers','display_toes','flat_panels')):
            parts=list(s.solids())
            for si,part in enumerate(parts): cats.setdefault(branch,[]).append((list(path)+[si],label,part))
    ev['candidate_branch_counts']={k:len(v) for k,v in cats.items()}; snapshot(ev)
    def candidates(substr): return [v for k,ls in cats.items() if substr in k for v in ls]
    def run(id,fn,cand,expected):
        try:
            a=fn(); shapes=list(a.solids()); assert len(shapes)==expected, (id,'solid count',len(shapes),expected)
            compare(id,shapes,cand,ev)
        except Exception as ex:
            ev['results'][id]={'error':repr(ex),'traceback':traceback.format_exc()}; snapshot(ev)
        print(id,flush=True)
    for j in sc['joints']: run(j['id'],lambda j=j:bridge(j),candidates('shell_bridges'),1)
    for row in ret: run(row['id'],lambda row=row:csg(row),candidates('control_retainers'),2 if row['owner'].startswith('F') else 1)
    for side in (-1,1):
        for r in (-1,1): run(f'toe_{side}_{r}',lambda side=side,r=r:toe(side,r),candidates('display_toes'),1)
    for n in ('D02L','D02R'): run(n,lambda n=n:roof(n),candidates('flat_panels'),1)
    fixed=[]
    for row in fixedrows:
        try: fixed.append((row,csg(row)))
        except Exception as ex: ev['errors'].append({'id':row['id'],'error':repr(ex),'traceback':traceback.format_exc()})
    snapshot(ev)
    for n,domain in ops['shell_domains_XY'].items():
        if len(fixed)!=49:
            ev['results'][n]={'error':'blocked: one or more fixed CSG groups failed; see errors'}; snapshot(ev)
        else: run(n,lambda n=n,domain=domain:build_shell(n,domain,sc,fixed),candidates('lower_shells'),1)
    ev['completed']=True; snapshot(ev)
    print(json.dumps({'completed':True,'results':len(ev['results']),'errors':len(ev['errors'])}),flush=True)

if __name__=='__main__': main()
