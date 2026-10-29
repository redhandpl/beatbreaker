import hashlib
import json
import runpy
import sys
from pathlib import Path

base = Path.cwd() / 'tmp/rev-a-release/models'
source = base / 'SOURCE'
entry = source / 'models/enclosure/B26/BUILD123D03/DJC_Enclosure_Rev_B26_build123d03.py'
evidence = base / 'STEP/assembly-evidence.json'
manifest = json.loads((source / 'source-manifest.json').read_text())
for relative, expected in manifest['file_hashes'].items():
    actual = hashlib.sha256((source / relative).read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(f'Source hash mismatch: {relative}')

sys.path.insert(0, str(entry.parent))
namespace = runpy.run_path(str(entry), run_name='rev_a_rebuild_check')
groups = namespace['build']()
records = json.loads(evidence.read_text())['leaves']
expected = {(r['group'], r['key']): r for r in records}
actual = {(g, k): shape for g, parts in groups.items() for k, shape in parts.items()}
if len(expected) != 476 or len(actual) != 476 or set(expected) != set(actual):
    raise RuntimeError(f'Leaf identity/count mismatch: source {len(actual)}, release evidence {len(expected)}')
max_bound = 0.0
max_volume = 0.0
bad = []
invalid_mesh_references = []
for key, shape in actual.items():
    ref = expected[key]
    if not shape.is_valid:
        if key[0] == 'Control caps - legacy mesh references':
            invalid_mesh_references.append(key[1])
        else:
            bad.append([*key, 'invalid non-mesh BRep'])
            continue
    box = shape.bounding_box()
    bounds = [[box.min.X, box.min.Y, box.min.Z], [box.max.X, box.max.Y, box.max.Z]]
    error = max(abs(a-b) for p,q in zip(bounds,ref['source_bounds_mm']) for a,b in zip(p,q))
    max_bound = max(max_bound, error)
    if error > 1e-5:
        bad.append([*key, 'bounds', error])
    if key[0] == 'Control caps - legacy mesh references':
        if len(shape.solids()) != 0 or shape.volume != 0:
            bad.append([*key, 'unexpected mesh-only reference representation'])
        continue
    if ref['source_volume_mm3'] is not None:
        delta = abs(shape.volume - ref['source_volume_mm3'])
        max_volume = max(max_volume, delta)
        if delta > 1e-4:
            bad.append([*key, 'volume', delta])
    if len(shape.solids()) != ref['source_solids']:
        bad.append([*key, 'solid count', len(shape.solids()), ref['source_solids']])
if len(invalid_mesh_references) != 49:
    bad.append(['unexpected invalid mesh-reference count', len(invalid_mesh_references)])
if bad:
    raise RuntimeError(f'Rebuild mismatches: {bad}')
result = {'status':'scoped rebuild comparison completed; 49 STL-imported references have zero solids/volume and fail BRep validity, but their separately checked meshes are intact; no surface identity claim', 'source_file_hashes_verified':len(manifest['file_hashes']), 'leaves':len(actual), 'invalid_mesh_reference_count':len(invalid_mesh_references), 'invalid_mesh_reference_ids':invalid_mesh_references, 'mesh_reference_note':'import_stl returns a triangulated display Face; BRep validity and volume are not established by that representation. Separate STL mesh checks cover the definitions.', 'max_bound_difference_mm':max_bound, 'max_volume_difference_mm3':max_volume, 'bound_tolerance_mm':1e-5, 'volume_tolerance_mm3':1e-4, 'group_counts':{key:len(parts) for key,parts in groups.items()}}
out = base / 'VALIDATION/REV_A_rebuild_check.json'
with out.open('x') as f:
    json.dump(result,f,indent=2,allow_nan=False)
    f.write('\n')
print(json.dumps(result, indent=2))
