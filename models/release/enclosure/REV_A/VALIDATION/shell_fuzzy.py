import importlib.util, json, time, traceback
from pathlib import Path
from build123d import Shape
from OCP.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Common
from OCP.collections import List_TopoDS_Shape

ROOT=Path.cwd()
SPEC=importlib.util.spec_from_file_location('independent_shell_evaluator',ROOT/'tmp/rev-a-shell/evaluate-checked.py')
e=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(e)
OUT=ROOT/'tmp/rev-a-shell/fuzzy-shells.json'

def compare(cls,a,b,tol):
    op=cls(); args=List_TopoDS_Shape(); tools=List_TopoDS_Shape()
    args.Append(a.wrapped); tools.Append(b.wrapped)
    op.SetArguments(args); op.SetTools(tools); op.SetFuzzyValue(tol); op.SetNonDestructive(True)
    start=time.monotonic(); op.Build()
    result={'requested_fuzzy_tolerance_mm':tol,'actual_fuzzy_tolerance_mm':op.FuzzyValue(),'non_destructive':True,'done':bool(op.IsDone()),'elapsed_s':time.monotonic()-start,'warnings':'unavailable' if not hasattr(op,'HasWarnings') else bool(op.HasWarnings()),'errors':'unavailable' if not hasattr(op,'HasErrors') else bool(op.HasErrors())}
    if result['done'] and result['errors'] is not True:
        shape=Shape.cast(op.Shape())
        result.update({'valid':shape.is_valid,'empty':shape.is_empty,'solids':len(shape.solids()),'volume_mm3':shape.volume})
    return result

def main():
    assert not OUT.exists()
    hashes={p:e.sha(p) for p in e.EXPECTED}; assert hashes==e.EXPECTED
    data=json.loads(e.DATA.read_text()); sc=data['schedules']; domains=data['operations']['shell_domains_XY']
    rows=[r for r in sc['controls'] if 'FIXED' in r['id'] or r['id']=='E01-fixed_cage']; assert len(rows)==49
    fixed=[(r,e.csg(r)) for r in rows]
    root=e.import_step(e.STEP); leaves={tuple(path):shape for path,label,shape in e.walk(root)}
    ev={'input_sha256':hashes,'strict_evidence':'tmp/rev-a-shell/shell-diagnostics.json','limitations':['Additional fuzzy tolerance affects numerical comparison only; no construction dimensions or files are changed.','Strict C03/C05 comparison failed due to invalid reverse cut and contradictory common operations; a fuzzy result does not replace or waive it.','OCCT warning and error status is unavailable if not exposed by the installed binding.'],'parts':{}}
    for name,path in [('C03',(0,2)),('C05',(0,4))]:
        a=e.build_shell(name,domains[name],sc,fixed); b=leaves[path]
        assert len(a.solids())==1 and len(b.solids())==1
        out={'step_numeric_leaf_path':path,'step_label':b.label,'reconstructed_valid':a.is_valid,'step_valid':b.is_valid,'reconstructed_volume_mm3':a.volume,'step_volume_mm3':b.volume,'reconstructed_bounds_mm':e.bounds(a),'step_bounds_mm':e.bounds(b),'fuzzy':{}}
        ev['parts'][name]=out
        for tol in (1e-7,1e-6):
            record={}; out['fuzzy'][str(tol)]=record
            for op,cls,x,y in [('reconstruction_minus_STEP',BRepAlgoAPI_Cut,a,b),('STEP_minus_reconstruction',BRepAlgoAPI_Cut,b,a),('intersection_reconstruction_STEP',BRepAlgoAPI_Common,a,b),('intersection_STEP_reconstruction',BRepAlgoAPI_Common,b,a)]:
                try: record[op]=compare(cls,x,y,tol)
                except Exception as ex: record[op]={'error':repr(ex),'traceback':traceback.format_exc()}
                print(name,tol,op,flush=True)
                with open(OUT,'w') as f: json.dump(ev,f,indent=2,allow_nan=False)
    print('fuzzy diagnostics complete',flush=True)

if __name__=='__main__': main()
