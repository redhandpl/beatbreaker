import hashlib, json, math, traceback
from pathlib import Path
from build123d import Axis, Edge, Face, Plane, Shell, Solid, Wire, import_step

ROOT = Path.cwd()
PDF = ROOT / 'schematics/work/enclosure/B26-CONSOLIDATED-02/B26_CONSOLIDATED_02_complete_DRAFT.pdf'
DATA = ROOT / 'schematics/work/enclosure/B26-CONSOLIDATED-02/jog/jog_data.json'
STEP = ROOT / 'models/release/enclosure/B26/B26-build123d03_RELEASE/STEP/B26-build123d03-trial-assembly.step'
EVIDENCE = ROOT / 'models/release/enclosure/B26/B26-build123d03_RELEASE/STEP/assembly-evidence.json'
OUT = ROOT / 'tmp/rev-a-jog/results-retry.json'
EXPECTED = ['left P01 platter and threaded rotor', 'left P02 carrier F13-STATIC-04', 'left P05 upper cover', 'left P06 lower cover', 'left sensor plate F13-STATIC-02', 'left P08 toe right', 'left P08 toe left', 'left P04 threaded retaining collar', 'left P07 threaded jam collar']
KEYS = ['P01','P02','P05','P06','plate','toe_right','toe_left','P04','P07']
R = {'units': {'length':'mm','volume':'mm3','angle':'degrees'}, 'coverage_denominator':18, 'results':[], 'errors':[], 'phase':[], 'input_sha256':{}, 'limits':'Purchased jog references are incomplete nominal envelopes; no physical, safety, manufacturing or new model approval. P01 strict release comparison failed 0.641091522 mm3 per rotor against 0.0001 mm3; its bounded exception is unpowered trial only, not surface identity.', 'tolerances':{'bounds_mm':0.0001,'volume_mm3':0.0001,'point_classification_mm':0.000001}}
def save():
    OUT.write_text(json.dumps(R, indent=2, allow_nan=False) + '\n')
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576), b''): h.update(b)
    return h.hexdigest()
def err(name):
    R['errors'].append({'operation':name,'traceback':traceback.format_exc()})
    save()
def C(r,z0,z1,x=0,y=0): return Solid.make_cylinder(r,z1-z0,Plane(origin=(x,y,z0)))
def K(r0,r1,z0,z1,x=0,y=0): return Solid.make_cone(r0,r1,z1-z0,Plane(origin=(x,y,z0)))
def B(x0,x1,y0,y1,z0,z1): return Solid.make_box(x1-x0,y1-y0,z1-z0,Plane(origin=(x0,y0,z0)))
def RB(a,*args): return B(*args).rotate(Axis.Z,a)
def xy(r,a): return (r*math.cos(math.radians(a)),r*math.sin(math.radians(a)))
def union(a,b):
    out=a.fuse(b)
    if out is None: raise RuntimeError('Fuse returned None')
    return out
def sub(a,b):
    out=a.cut(b)
    if out is None: raise RuntimeError('Cut returned None')
    return out
def ridge(d):
    root=14.725+d; crest=14.975+d; h=0.03125+0.25/math.sqrt(3)
    v=[(root-0.025,-h),(root,-h),(crest,-0.03125),(crest,0.03125),(root,h),(root-0.025,h)]
    helices=[Edge.make_helix(0.5,3.5,r,center=(0,0,2.5+z)).edges()[0] for r,z in v]
    faces=[Face.make_surface_from_curves(helices[i],helices[(i+1)%6]) for i in range(6)]
    faces += [Face(Wire.make_polygon([(r,0,2.5+z+dz) for r,z in v])) for dz in (0,3.5)]
    shell=Shell(faces)
    if not shell.is_manifold: raise RuntimeError('T30 shell is not manifold')
    body=Solid(shell)
    if not body.is_valid: raise RuntimeError('T30 solid invalid before trim')
    result=body.intersect(C(16,3,5.5))
    if len(result) != 1 or not result[0].is_valid or len(result[0].solids()) != 1: raise RuntimeError(f'T30 trim invalid or non-single-solid: {len(result)} results')
    return result[0]

def profile(d,z):
    yo=math.sqrt(18.4**2-2.8**2); yi=math.sqrt(17.6**2-2.8**2)
    ol=(-2.8,yo); or_=(2.8,yo); il=(-2.8,yi); ir=(2.8,yi)
    def rad(p,r): return (p[0]*r/math.hypot(*p),p[1]*r/math.hypot(*p))
    pts=[rad(ol,19.2+d),rad(or_,19.2+d),(2-d,yo),(2-d,yi),rad(ir,16.8-d),rad(il,16.8-d),(-2+d,yi),(-2+d,yo)]
    def arc(i,j,c,ccw):
        a,b=pts[i],pts[j]; start=math.atan2(a[1]-c[1],a[0]-c[0]); end=math.atan2(b[1]-c[1],b[0]-c[0]); delta=(end-start)%(2*math.pi) if ccw else -((start-end)%(2*math.pi)); r=math.dist(a,c); m=start+delta/2
        return Edge.make_three_point_arc((*a,z),(c[0]+r*math.cos(m),c[1]+r*math.sin(m),z),(*b,z))
    def line(i,j): return Edge.make_line((*pts[i],z),(*pts[j],z))
    return Wire([arc(0,1,(0,0),True),arc(1,2,or_,True),line(2,3),arc(3,4,ir,True),arc(4,5,(0,0),False),arc(5,6,il,True),line(6,7),arc(7,0,ol,True)])

def rotor(male):
    platter=K(55,52.5,21.4,36.4)
    cutter=Solid.make_cylinder(5,9.75,Plane(origin=(50.25,0,28.9),z_dir=(1,0,0)))
    edge=[e for e in cutter.edges() if abs(e.center().X-50.25)<1e-5]
    assert len(edge)==1, ('finger start edge',len(edge))
    cutter=cutter.fillet(1,edge)
    for a in range(0,360,30): platter=sub(platter,cutter.rotate(Axis.Z,a))
    platter=sub(platter,Solid.make_loft([profile(0,35.6),profile(0.8,36.4)],ruled=True))
    shaft=union(C(14.725,3,5.5),male)
    shaft=union(shaft,C(14.975,5.5,21.4)); shaft=union(shaft,C(16.1,19.5,21.4)); shaft=sub(shaft,C(13,3,21.4))
    edges=[e for e in shaft.edges() if abs(e.length-2*math.pi*14.975)<1e-4 and abs(e.center().Z-19.5)<1e-5]
    assert len(edges)==1, ('shaft root',len(edges))
    shaft=shaft.fillet(0.2,edges)
    return sub(union(union(shaft,C(6,6.6,21.4)),platter),C(4.1,6.6,10.8))

def carrier():
    p=C(23,5.5,19.5)
    for a in (0,120,240):
        x,y=xy(23,a)
        p=union(p,C(2.5,5.5,9.5,x,y)); p=union(p,C(2.5,15.5,19.5,x,y))
    for a in (90,210,330):
        x,y=xy(31,a)
        for s in (C(5,6,9,x,y),RB(a,22,31,-5,5,6,9),RB(a,22,25.7,-2,2,1,3.8),RB(a,24,25.7,-2,2,3.8,9)): p=union(p,s)
    p=sub(p,C(21.075,5.5,19.5))
    for a in (0,120,240):
        x,y=xy(23,a); p=sub(p,C(.8,5.5,8.5,x,y)); p=sub(p,C(.8,16.5,19.5,x,y))
    for a in (90,210,330):
        x,y=xy(31,a); p=sub(p,C(1,6,9,x,y))
    return p

def collar(z0,z1,female):
    p=sub(sub(C(16.1,z0,z1),C(14.775,z0,z1)),female)
    for a in (0,120,240): p=sub(p,RB(a,15.6,16.2,-1,1,z0,z1))
    return p

def cover(z0,z1,upper):
    p=C(23,z0,z1)
    for a in (0,120,240):
        x,y=xy(23,a); p=union(p,C(2.5,z0,z1,x,y))
    p=sub(p,C(20,z0,z1))
    for a in (0,120,240):
        x,y=xy(23,a); p=sub(p,C(1.2,z0,z1,x,y)); p=sub(p,K(1.2,2.1,20.1,21,x,y) if upper else K(2.1,1.2,4,4.9,x,y))
    return p

def plate():
    p=C(25,0,1)
    for s in (-1,1):
        p=union(p,C(.9,1,2.5,6*s,0)); p=union(p,B(-12.4,-7.6,-3,3,1,3) if s==-1 else B(7.6,12.4,-3,3,1,3))
    p=sub(sub(p,B(23.8,25.1,-1.2,1.2,0,1)),B(-5,5,-26,-3,0,1))
    for x in (-10,10):
        r=4.1/math.sqrt(3)
        wire=Wire.make_polygon([(x+r*math.cos(math.radians(30+60*i)),r*math.sin(math.radians(30+60*i)),.6) for i in range(6)])
        p=sub(p,Solid.extrude(Face(wire),(0,0,1.7))); p=sub(p,B(x-2.1,x+2.1,0,8,.6,2.3)); p=sub(p,C(1.1,.2,3,x,0))
    return p

def toe(): return sub(sub(B(6.8,12.4,-2.5,2.5,3,4.3),C(1.1,3,4.3,10,0)),K(1.1,1.3,4.1,4.3,10,0))
def bounds(s):
    b=s.bounding_box(); return [[b.min.X,b.min.Y,b.min.Z],[b.max.X,b.max.Y,b.max.Z]]
def maxdiff(a,b): return max(abs(a[i][j]-b[i][j]) for i in range(2) for j in range(3))
def clean(s): return s.translate(str.maketrans(' .()','____'))

def main():
    assert not OUT.exists(), 'Refusing to overwrite results'
    for p in (PDF,DATA,STEP,EVIDENCE): R['input_sha256'][str(p.relative_to(ROOT))]=sha(p)
    assert R['input_sha256'][str(PDF.relative_to(ROOT))]=='35ab5a40ae0051ec4080cb6cfb287782c482859d1a6f666e9a8b0ccca00226c2'
    assert R['input_sha256'][str(DATA.relative_to(ROOT))]=='fb522c07afe6be372b6833ceae93182ed7592ea97a30b85345ae3f6800f34e4d'
    assert R['input_sha256'][str(STEP.relative_to(ROOT))]=='be226639517a5e5042979a5c78039f82f4e40c89f9d92193f8bd150e7c0c258b'
    data=json.loads(DATA.read_text()); assert len(data['parts'])==6 and len(data['t30'])==4
    save(); parts={}; ridges={}
    for key,d in [('male',0),('female',.05)]:
        try: ridges[key]=ridge(d)
        except Exception: err('construct T30 '+key)
    for key,fn in [('P01',lambda:rotor(ridges['male'])),('P02',carrier),('P05',lambda:cover(19.5,21,True)),('P06',lambda:cover(4,5.5,False)),('plate',plate),('toe_right',toe),('toe_left',lambda:parts['toe_right'].rotate(Axis.Z,180)),('P04',lambda:collar(4,5.5,ridges['female'])),('P07',lambda:collar(3,4,ridges['female']))]:
        try:
            p=fn(); assert p.is_valid and len(p.solids())==1, (key,'invalid or non-single solid',len(p.solids()))
            parts[key]=p
        except Exception: err('construct '+key)
    ev=json.loads(EVIDENCE.read_text())
    def walk_json(v):
        if isinstance(v,dict):
            if v.get('group')=='Static jogs - printed' and 'step_bounds_mm' in v: yield v
            for child in v.values(): yield from walk_json(child)
        elif isinstance(v,list):
            for child in v: yield from walk_json(child)
    evidence={x['name']:x for x in walk_json(ev)}
    assert len(evidence)==18, ('evidence identities',len(evidence))
    assembly=import_step(STEP)
    def walk(node,anc,path):
        loc=anc*node.location
        if not node.children:
            yield path,node,loc
        else:
            for i,ch in enumerate(node.children): yield from walk(ch,loc,path+[i])
    from build123d import Location
    leaves=list(walk(assembly,Location(),[]))
    R['import_leaf_count']=len(leaves)
    assert len(assembly.children) > 9 and len(assembly.children[9].children) == 18, 'Printed jog group does not have expected 18 numeric occurrences'
    R['identity_note']='STEP import uses referred-shape labels, collapsing left/right identities; numeric printed-group child index and independently recorded world bounds and solid count establish occurrence mapping, not the imported label.'
    for side,xc in [('left',110),('right',490)]:
        for index,key in enumerate(KEYS):
            name=EXPECTED[index].replace('left ',side+' ',1); record={'operand_reconstructed':side+' '+key,'operand_step_evidence_name':name,'numeric_ordinal':index+(0 if side=='left' else 9)}; R['results'].append(record)
            try:
                expected=evidence[name]; ordinal=record['numeric_ordinal']
                candidates=[(path,node,loc) for path,node,loc in leaves if path==[9,ordinal]]
                if len(candidates)!=1: raise RuntimeError('Expected numeric STEP occurrence not unique')
                path,node,loc=candidates[0]; actual=node.located(loc)
                record['imported_label']=node.label
                record['step_numeric_path']=path
                record['evidence_bounds_max_delta_mm']=maxdiff(bounds(actual),expected['step_bounds_mm'])
                record['step_solid_count']=len(actual.solids())
                if record['evidence_bounds_max_delta_mm']>=.0001 or record['step_solid_count']!=expected['step_solids']: raise RuntimeError('Numeric occurrence does not match release evidence world bounds and solid count')
                actual=actual.solids()[0]; record['step_valid']=actual.is_valid
                if key not in parts: raise RuntimeError('Reconstruction failed; see construct errors')
                model=parts[key].rotate(Axis.Z,60).translate((xc,-165,2))
                record.update(reconstructed_solid_count=len(model.solids()),reconstructed_valid=model.is_valid, reconstructed_bounds_mm=bounds(model),step_bounds_mm=bounds(actual),bounds_max_abs_delta_mm=maxdiff(bounds(model),bounds(actual)),reconstructed_volume_mm3=model.volume,step_volume_mm3=actual.volume,volume_abs_delta_mm3=abs(model.volume-actual.volume))
                for direction,a,b in [('reconstruction_minus_step',model,actual),('step_minus_reconstruction',actual,model)]:
                    try:
                        difference=a.cut(b)
                        if difference is None: raise RuntimeError('Boolean returned None, cannot classify as empty')
                        if not difference.is_valid: raise RuntimeError('Boolean difference invalid')
                        record[direction+'_mm3']=difference.volume
                    except Exception: record[direction+'_error']=traceback.format_exc()
                if key in ('P01','P04','P07'):
                    for a in (30,90,150,210,270,330):
                        for n in ((2,3,4) if key=='P01' else ((4,5) if key=='P04' else (2,3))):
                            z=2.5+0.5*(a/360+n)
                            if not (3.05<z<(5.45 if key!='P07' else 3.95)) or (key=='P04' and z<=4.05): continue
                            for offset in (0,.25):
                                z2=z+offset
                                if not (3.02<z2<5.48) or (key=='P04' and not 4.02<z2<5.48) or (key=='P07' and not 3.02<z2<3.98): continue
                                r=14.9 if key=='P01' else 15.0; x,y=xy(r,a); wx=xc+x*.5-y*math.sqrt(3)/2; wy=-165+x*math.sqrt(3)/2+y*.5
                                expected_inside=(offset==0) if key=='P01' else (offset!=0)
                                R['phase'].append({'operand':name,'local_angle_deg':a,'local_z_mm':z2,'radius_mm':r,'phase_offset_mm':offset,'ideal_expected_inside':expected_inside,'reconstruction_inside':model.is_inside((wx,wy,z2+2),1e-6),'step_inside':actual.is_inside((wx,wy,z2+2),1e-6)})
            except Exception: record['error']=traceback.format_exc(); R['errors'].append({'operation':'compare '+name,'traceback':record['error']})
            save()
    R['summary']={'constructed_local_parts':list(parts),'occurrences_compared':sum('volume_abs_delta_mm3' in v for v in R['results']),'occurrence_denominator':18,'phase_samples':len(R['phase']),'phase_model_ideal_mismatches':sum(x['reconstruction_inside']!=x['ideal_expected_inside'] for x in R['phase']),'phase_step_ideal_mismatches':sum(x['step_inside']!=x['ideal_expected_inside'] for x in R['phase']),'boolean_errors':sum(sum(k.endswith('_error') for k in v) for v in R['results'])}
    save()
try: main()
except Exception:
    err('top-level'); raise
