"""B24-build123d01 removable control retainers from approved compiled CSG."""

import json
import math
from pathlib import Path

from build123d import BuildPart, Location, Mode, Plane, RectangleRounded, Shape, Solid, extrude, insert


_ROOT = Path(__file__).resolve().parents[4]
_PROOF = _ROOT / "schematics/enclosure/B24/DJC_Enclosure_Rev_B24_validation.json"


def _primitive(spec):
    kind, origin, size = spec
    x, y, z = origin
    if kind == 0:
        return Solid.make_box(*size, plane=Plane(origin=(x, y, z)))
    if kind == 1:
        r0, r1, height = size
        plane = Plane(origin=(x, y, z))
        if r0 == r1:
            return Solid.make_cylinder(r0, height, plane=plane)
        return Solid.make_cone(r0, r1, height, plane=plane)
    if kind == 2:
        width, height, radius, depth = size
        return extrude(RectangleRounded(width, height, radius), amount=depth).moved(
            Location((x, y, z))
        )
    raise ValueError(f"Unsupported control CSG primitive: {kind}")


def _local_retainer(csg):
    _, _, additions, cuts = csg
    positive = [_primitive(spec) for spec in additions]
    negative = [_primitive(spec) for spec in cuts]
    with BuildPart() as part:
        insert(positive)
        insert(negative, mode=Mode.SUBTRACT)
    return part.part


def build_retainers() -> dict[str, Shape]:
    """Build the 49 removable groups as 54 distinguishable printed solids.

    Coordinates in the compiled proof are table coordinates; the source Fusion
    builder maps them to CAD by (X, -Y, Z). B24 moves are already compiled.
    """
    rows = json.loads(_PROOF.read_text())["compiled_control_primitives"]
    rows = [row for row in rows if "retainer" in row["id"].lower()]
    if len(rows) != 49:
        raise ValueError(f"Expected 49 removable control groups, found {len(rows)}")

    cache = {}
    result = {}
    for row in rows:
        identifier, transform, additions, cuts = row["CSG"]
        key = json.dumps([additions, cuts], separators=(",", ":"))
        if key not in cache:
            cache[key] = _local_retainer(row["CSG"])
        shape = cache[key]
        a, b = transform[0][:2]
        c, d = transform[1][:2]
        determinant = a * d - b * c
        if abs(abs(determinant) - 1) > 1e-9:
            raise ValueError(f"Unexpected control transform for {identifier}")
        # Reflection in table-to-CAD coordinates precedes the proper rotation.
        if determinant > 0:
            shape = shape.mirror(Plane.XZ)
        angle = math.degrees(math.atan2(-c, a))
        shape = shape.moved(Location((transform[0][3], -transform[1][3], transform[2][3]), angle))
        solids = sorted(shape.solids(), key=lambda s: (s.center().X, s.center().Y, s.center().Z))
        expected = 2 if row["owner"].startswith("F") else 1
        if len(solids) != expected:
            raise ValueError(f"{identifier}: expected {expected} solids, found {len(solids)}")
        for index, solid in enumerate(solids, 1):
            name = f"{identifier}-{index}" if expected > 1 else identifier
            solid.label = f"{name} / removable control retainer / B24-build123d01"
            result[name] = solid
    return result


