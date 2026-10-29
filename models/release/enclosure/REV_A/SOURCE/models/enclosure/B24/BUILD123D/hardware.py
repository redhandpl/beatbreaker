"""B24 nominal reference fasteners, not manufacturing thread geometry.

The approved Fusion05 inventory records occurrence transforms in centimetres;
all parametric shapes and returned positions use millimetres.
"""
import json
from pathlib import Path

from build123d import Align, Cone, Cylinder, Plane, Pos

ROOT = Path(__file__).resolve().parents[4]
INVENTORY = ROOT / "models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_validation.json"


def _cylinder(radius, height, bottom):
    return Pos(0, 0, bottom) * Cylinder(radius, height, align=(Align.CENTER, Align.CENTER, Align.MIN))


def _socket_screw(radius, length, head_radius, head_height):
    return _cylinder(radius, length, -length) + _cylinder(head_radius, head_height, 0)


def _countersunk(radius, length, head_radius):
    height = head_radius - radius
    cone = Pos(0, 0, -height) * Cone(radius, head_radius, height, align=(Align.CENTER, Align.CENTER, Align.MIN))
    return _cylinder(radius, length, -length) + cone


def build():
    definitions = {
        "REF M3x8 ISO4762 source nominal outer geometry": _socket_screw(1.5, 8, 2.75, 3),
        "REF M2.5x6 supplied CHC source nominal outer geometry": _socket_screw(1.25, 6, 2.25, 2.5),
        "REF M2x6 countersunk source nominal outer geometry": _countersunk(1, 6, 2.2),
        "REF M1.6x5 countersunk source nominal outer geometry": _countersunk(0.8, 5, 1.6),
        "REF BN616 M3x6 conditional source nominal outer geometry": _countersunk(1.5, 6, 3),
        "REF BN616 1076469 M3x8 B24 complete nominal outer head": _countersunk(1.5, 8, 3),
    }
    rows = json.loads(INVENTORY.read_text())["inventory"]
    fasteners = [row for row in rows if row["occurrence"].startswith("REFERENCE FASTENERS nominal heads and shafts / threads unqualified:")]
    assert len(fasteners) == 199
    result = {}
    for row in fasteners:
        name = row["component"]
        if name not in definitions:
            raise ValueError(f"Unknown nominal fastener: {name}")
        p = row["pose"]
        frame = Plane(origin=(p[3] * 10, p[7] * 10, p[11] * 10), x_dir=(p[0], p[4], p[8]), z_dir=(p[2], p[6], p[10]))
        part = definitions[name].moved(frame.location)
        part.label = row["occurrence"]
        result[row["id"]] = part
    assert len(result) == len(fasteners)
    return result
