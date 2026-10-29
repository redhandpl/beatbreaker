import hashlib
import json
from pathlib import Path
from build123d import Location, import_step

base=Path('tmp/rev-a-release/models')
step=base/'STEP/B26-build123d03-trial-assembly.step'
evidence=base/'STEP/assembly-evidence.json'
expected_hash='be226639517a5e5042979a5c78039f82f4e40c89f9d92193f8bd150e7c0c258b'
if hashlib.sha256(step.read_bytes()).hexdigest()!=expected_hash:
    raise RuntimeError('STEP hash mismatch')
data=json.loads(evidence.read_text())
assemblies=data['assemblies'][1:]
expected_groups=[a['path'][1] for a in assemblies]
root=import_step(step)
if len(root.children)!=len(expected_groups):
    raise RuntimeError(f'STEP group count {len(root.children)}')
def walk(node,acc):
    world=acc*node.location
    if not node.children:
        yield node.located(world)
    else:
        for child in node.children:
            yield from walk(child,world)
max_bounds=0.0
max_volume=0.0
count=solids=0
exceptions=[]
for index,(group,branch) in enumerate(zip(expected_groups,root.children)):
    observed=list(walk(branch,root.location))
    reference=[r for r in data['leaves'] if r['group']==group]
    if len(observed)!=len(reference):
        raise RuntimeError(f'{group}: STEP leaf count {len(observed)} versus {len(reference)}')
    for n,(shape,ref) in enumerate(zip(observed,reference)):
        bounds=shape.bounding_box()
        got=[[bounds.min.X,bounds.min.Y,bounds.min.Z],[bounds.max.X,bounds.max.Y,bounds.max.Z]]
        delta=max(abs(a-b) for row,other in zip(got,ref['step_bounds_mm']) for a,b in zip(row,other))
        max_bounds=max(max_bounds,delta)
        actual_solids=len(shape.solids())
        if delta>1e-5 or actual_solids != ref['step_solids'] or shape.is_valid != ref['step_valid']:
            raise RuntimeError(f'{group} ordinal {n}: bounds/solid-count/validity mismatch {delta}, {actual_solids}, {shape.is_valid}')
        if ref['step_volume_mm3'] is not None:
            dv=abs(shape.volume-ref['step_volume_mm3']); max_volume=max(max_volume,dv)
            if dv>1e-4:
                raise RuntimeError(f'{group} ordinal {n}: STEP repeat-volume mismatch {dv}')
        if ref.get('volume_difference_mm3',0) and ref['volume_difference_mm3']>1e-4:
            exceptions.append({'group':group,'key':ref['key'],'strict_source_step_volume_difference_mm3':ref['volume_difference_mm3']})
        solids += 1 if actual_solids else 0
        count+=1
    print(f'{group}: {len(observed)} leaves verified',flush=True)
if count!=476 or solids!=444 or len(exceptions)!=2:
    raise RuntimeError(f'Unexpected counts: {count} leaves, {solids} solid leaves, {len(exceptions)} existing exceptions')
result={'status':'reopened identical released STEP; bounds, volumes, validity and solid counts match recorded STEP evidence; P01 source-vs-STEP exceptions still fail', 'step_sha256':expected_hash,'groups':len(expected_groups),'leaves':count,'solid_leaves':solids,'non_solid_leaves':count-solids,'max_bound_difference_mm':max_bounds,'max_repeat_step_volume_difference_mm3':max_volume,'strict_p01_exceptions':exceptions,'limits':['Numeric branch/occurrence order and world bounds used, not potentially shared imported labels.', 'Recorded counts and bounds do not prove exact surfaces, physical fit, complete purchased geometry or safety.']}
with (base/'VALIDATION/REV_A_step_check.json').open('x') as f:
    json.dump(result,f,indent=2,allow_nan=False); f.write('\n')
print(json.dumps(result,indent=2))
