"""B26 control interfaces reconstructed from the approved B24 CSG.

Table coordinates are (X, Y, Z); shapes use CAD coordinates (X, -Y, Z).
Purchased controls and legacy STL caps remain incomplete/display references.
"""
import csv
import json
import math
from pathlib import Path

from build123d import Location, Plane
import caps
import controls
import reference_controls

ROOT = Path(__file__).resolve().parents[4]
PROOF = ROOT / "schematics/enclosure/B24/DJC_Enclosure_Rev_B24_validation.json"
COORDINATES = ROOT / "schematics/frontpanel/R12/DJC_frontpanel_R12_DRAFT_coordinates.csv"
MOVES = ROOT / "schematics/enclosure/B24/DJC_Enclosure_Rev_B24_definition.json"


def _source_rows():
    source = json.loads(PROOF.read_text())["compiled_control_primitives"]
    if len(source) != 98 or len({r["id"] for r in source}) != 98:
        raise ValueError("Expected 98 unique B24 fixed/retainer control groups")
    return source


def _targets(source):
    with COORDINATES.open(newline="") as stream:
        coordinates = {r["ID"]: (float(r["X_global_mm"]), float(r["Y_global_mm"]))
                       for r in csv.DictReader(stream)}
    moves = {r["id"]: r for r in json.loads(MOVES.read_text())["control_moves"]}
    targets = {}
    for row in source:
        owner = row["owner"]
        x, y = coordinates[owner]
        old = row["CSG"][1]
        if owner in moves:
            move = moves[owner]
            if not all(math.isclose(a, b, abs_tol=1e-7) for a, b in zip((x, y), move["old_XY"])):
                raise ValueError(f"R12/B24 move mismatch: {owner}")
            baseline = move["new_XY"]
        else:
            baseline = (x, y)
        if not all(math.isclose(a, b, abs_tol=1e-7) for a, b in zip((old[0][3], old[1][3]), baseline)):
            raise ValueError(f"B24 control pose mismatch: {owner}")
        if owner in ("B23", "B24"):
            target = (x, 255.0)
        elif owner in ("E01", "T01", "T02"):
            target = (x, y + 20.0)
        else:
            target = (baseline[0], y + 20.0)
        if owner in targets and targets[owner] != target:
            raise ValueError(f"Inconsistent owner target: {owner}")
        targets[owner] = target
    if len(targets) != 49:
        raise ValueError(f"Expected 49 controls, found {len(targets)}")
    return targets


def _move_fader_ends(csg):
    # B26-DETAIL-01 sheet 3: rigidly move end-side primitives, not rails.
    for primitives in csg[2:4]:
        for kind, origin, size in primitives:
            u = origin[0]
            if kind == 0:
                low, high = u, u + size[0]
                if low < 0 < high:
                    if not math.isclose(low, -high, abs_tol=1e-7):
                        raise ValueError(f"Ambiguous fader primitive: {csg[0]}")
                    continue
                center = (low + high) / 2
            else:
                center = u
            if center:
                origin[0] += math.copysign(1.5, center)


def rows():
    """Return B24-format per-owner fixed and retainer CSG rows at B26 poses."""
    source = _source_rows()
    targets = _targets(source)
    result = []
    for row in source:
        owner = row["owner"]
        csg = row["CSG"]
        csg[1][0][3], csg[1][1][3] = targets[owner]
        if owner.startswith("F"):
            _move_fader_ends(csg)
        result.append({"id": row["id"], "owner": owner, "CSG": csg})
    return result


def _deltas():
    source = _source_rows()
    targets = _targets(source)
    return {r["owner"]: (targets[r["owner"]][0] - r["CSG"][1][0][3],
                         targets[r["owner"]][1] - r["CSG"][1][1][3])
            for r in source}


def build_retainers():
    """Return 49 retainer groups as 54 separately keyed solids."""
    result = {}
    cache = {}
    for row in rows():
        if "retainer" not in row["id"].lower():
            continue
        identifier, transform, additions, cuts = row["CSG"]
        key = json.dumps([additions, cuts], separators=(",", ":"))
        if key not in cache:
            cache[key] = controls._local_retainer(row["CSG"])
        shape = cache[key]
        a, b = transform[0][:2]
        c, d = transform[1][:2]
        determinant = a * d - b * c
        if not math.isclose(abs(determinant), 1, abs_tol=1e-9):
            raise ValueError(f"Unexpected control transform: {identifier}")
        if determinant > 0:
            shape = shape.mirror(Plane.XZ)
        shape = shape.moved(Location((transform[0][3], -transform[1][3], transform[2][3]),
                                     math.degrees(math.atan2(-c, a))))
        solids = sorted(shape.solids(), key=lambda s: (s.center().X, s.center().Y, s.center().Z))
        expected = 2 if row["owner"].startswith("F") else 1
        if len(solids) != expected:
            raise ValueError(f"{identifier}: expected {expected} solids, found {len(solids)}")
        for index, solid in enumerate(solids, 1):
            name = f"{identifier}-{index}" if expected == 2 else identifier
            solid.label = f"{name} / removable control retainer / B26 review"
            result[name] = solid
    if len(result) != 54:
        raise ValueError(f"Expected 54 retainer solids, found {len(result)}")
    return result


def build_references():
    """Move the B24 nominal purchased-body and tip-plane references by owner."""
    delta = _deltas()
    result = {}
    for name, shape in reference_controls.build().items():
        owner = name.split("-", 1)[0]
        dx, dy = delta[owner]
        moved = shape.moved(Location((dx, -dy, 0)))
        moved.label = shape.label + " / B26 review"
        result[name] = moved
    return result


def build_caps():
    """Return legacy mesh references at the B26 poses, keyed by control owner."""
    source = _source_rows()
    baseline = {}
    for row in source:
        transform = row["CSG"][1]
        baseline[row["owner"]] = (transform[0][3], transform[1][3])
    delta = _deltas()
    inventory = json.loads(caps.INVENTORY.read_text())["inventory"]
    meshes = caps.build()
    result = {}
    for row in inventory:
        if row["id"] not in meshes:
            continue
        pose = row["pose"]
        x, y = pose[3] * 10, -pose[7] * 10
        owners = [owner for owner, (bx, by) in baseline.items()
                  if math.isclose(x, bx, abs_tol=1e-6) and math.isclose(y, by, abs_tol=1e-6)]
        if len(owners) != 1:
            raise ValueError(f"Cannot uniquely associate cap with owner: {row['id']}")
        owner = owners[0]
        name = owner + "-CAP-REF"
        if name in result:
            raise ValueError(f"Duplicate cap owner: {owner}")
        dx, dy = delta[owner]
        shape = meshes[row["id"]].moved(Location((dx, -dy, 0)))
        shape.label = f"{name} / immutable legacy mesh reference / B26 review"
        result[name] = shape
    if set(result) != {owner + "-CAP-REF" for owner in baseline}:
        raise ValueError("Cap references do not cover all controls")
    return result
