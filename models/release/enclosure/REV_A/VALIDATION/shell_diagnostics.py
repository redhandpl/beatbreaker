import importlib.util, itertools, json, math, sys, traceback
from pathlib import Path
from build123d import Shape, Compound
from OCP.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Common

ROOT=Path.cwd()
SPEC=importlib.util.spec_from_file_location('independent_shell_evaluator', ROOT/'tmp/rev-a-shell/evaluate-checked.py')
e=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(e)
OUT=ROOT/'tmp/rev-a-shell/shell-diagnostics.json'

def operation(cls,a,b):
    op=cls(a.wrapped,b.wrapped)
    record={'done':bool(op.IsDone()),'warning_status':'unavailable' if not hasattr(op,'HasWarnings') else bool(op.HasWarnings()),'error_status':'unavailable' if not hasattr(op,'HasErrors') else bool(op.HasErrors())}
    if not record['done'] or record['error_status'] is True: return record
    s=Shape.cast(op.Shape())
    record.update({'valid':s.is_valid,'volume_mm3':s.volume,'solids':len(s.solids()),'empty':s.is_empty})
    return record

def surface(source,target):
    vertices,triangles=source.tessellate(0.1,0.1)
    assert vertices
    step=max(1,len(vertices)//100)
    selected=vertices[::step][:100]
    faces=Compound(list(target.faces()))
    distances=[faces.distance_to(p) for p in selected]
    return {'mesh_deflection_mm':0.1,'angular_tolerance_rad':0.1,'vertex_count':len(vertices),'triangle_count':len(triangles),'sample_count':len(selected),'max_vertex_to_other_surface_mm':max(distances),'mean_vertex_to_other_surface_mm':sum(distances)/len(distances)}

def occupancy(a,b,domain):
    x0,x1,y0,y1=domain
    xs=[x0+(x1-x0)*(i+.5)/24 for i in range(24)]
    ys=[-y0-(y1-y0)*(j+.5)/16 for j in range(16)]
    zs=[.25,1,1.75,2.25,5,8,12,17,19,25,40,60,80]
    count=0; disagreements=[]; inside_a=inside_b=0
    for p in itertools.product(xs,ys,zs):
        ia=a.is_inside(p,1e-6); ib=b.is_inside(p,1e-6); count+=1; inside_a+=ia; inside_b+=ib
        if ia!=ib: disagreements.append({'point_cad_mm':p,'reconstructed_inside':ia,'step_inside':ib})
    return {'sampling':'24 x 16 XY cell centres by 13 fixed Z levels, not a coverage proof','classifier_tolerance_mm':1e-6,'tested_points':count,'reconstructed_inside':inside_a,'step_inside':inside_b,'disagreements':disagreements}

def main():
    assert not OUT.exists()
    hashes={p:e.sha(p) for p in e.EXPECTED}; assert hashes==e.EXPECTED
    data=json.loads(e.DATA.read_text()); sc=data['schedules']; domains=data['operations']['shell_domains_XY']
    rows=[r for r in sc['controls'] if 'FIXED' in r['id'] or r['id']=='E01-fixed_cage']
    assert len(rows)==49
    fixed=[(r,e.csg(r)) for r in rows]
    root=e.import_step(e.STEP); leaves=list(e.walk(root)); bypath={tuple(p):s for p,label,s in leaves}
    out={'input_sha256':hashes,'notes':['Numeric STEP path is an assembly occurrence, not a unique imported label. Both solids are in global CAD coordinates.','Invalid Boolean outputs and unavailable warning flags are not interpreted as empty results or actual geometric differences. Surface and occupancy samples are not proof of exact equality.'],'parts':{}}
    for n,path in [('C03',(0,2)),('C05',(0,4))]:
        try:
            a=e.build_shell(n,domains[n],sc,fixed); b=bypath[path]; assert len(a.solids())==len(b.solids())==1
            d={'step_numeric_leaf_path':path,'step_label':b.label,'reconstructed_valid':a.is_valid,'step_valid':b.is_valid,'reconstructed_solids':len(a.solids()),'step_solids':len(b.solids()),'reconstructed_bounds_mm':e.bounds(a),'step_bounds_mm':e.bounds(b),'reconstructed_volume_mm3':a.volume,'step_volume_mm3':b.volume,'reconstructed_faces':len(a.faces()),'step_faces':len(b.faces()),'operations':{}}
            for name,cls,x,y in [('reconstruction_minus_STEP',BRepAlgoAPI_Cut,a,b),('STEP_minus_reconstruction',BRepAlgoAPI_Cut,b,a),('intersection_reconstruction_STEP',BRepAlgoAPI_Common,a,b),('intersection_STEP_reconstruction',BRepAlgoAPI_Common,b,a)]:
                try: d['operations'][name]=operation(cls,x,y)
                except Exception as ex: d['operations'][name]={'error':repr(ex),'traceback':traceback.format_exc()}
            d['surface_samples']={}
            for name,x,y in [('reconstruction_to_STEP',a,b),('STEP_to_reconstruction',b,a)]:
                try: d['surface_samples'][name]=surface(x,y)
                except Exception as ex: d['surface_samples'][name]={'error':repr(ex),'traceback':traceback.format_exc()}
            try: d['occupancy_samples']=occupancy(a,b,domains[n])
            except Exception as ex: d['occupancy_samples']={'error':repr(ex),'traceback':traceback.format_exc()}
            out['parts'][n]=d
        except Exception as ex: out['parts'][n]={'error':repr(ex),'traceback':traceback.format_exc()}
        with open(OUT,'w') as f: json.dump(out,f,indent=2,allow_nan=False)
        print(n,flush=True)
    print('diagnostics complete',flush=True)

if __name__=='__main__': main()
