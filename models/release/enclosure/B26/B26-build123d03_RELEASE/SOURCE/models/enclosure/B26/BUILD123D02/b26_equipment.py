"""B26 incomplete purchased-equipment envelopes, in the assembled CAD frame.

These are measured or documented envelopes, not vendor solids or fit proof.
B25 board mounting was deliberately deferred; no mounting geometry is added.
"""
import json
from pathlib import Path

from build123d import Pos

import reference_equipment
from shell import _box

ROOT = Path(__file__).resolve().parents[4]
BOARD_SOURCE = ROOT / "schematics/enclosure/B25-ELEC-02/DJC_Enclosure_Rev_B25_ELEC_02_definition.json"


def build():
    old = reference_equipment.build()
    result = {}
    for name in ("PI-envelope", "DAC-envelope", "PSU-envelope", "J01-body", "J01-nut"):
        result[name] = Pos(0, -20, 0) * old[name]
    result["D01-front-plane"] = Pos(0, 0, 5) * old["D01-front-plane"]
    result["RCA-front-plane"] = old["RCA-front-plane"]
    boards = json.loads(BOARD_SOURCE.read_text())["boards"]
    if {row["id"] for row in boards} != {"U1", "U2", "U3", "U4"}:
        raise ValueError("Unexpected B25 board set")
    for row in boards:
        x, y = row["centre_XY"]
        y += 20
        width, depth = row["plan_size_XY"]
        z0, z1 = row["reference_Z"]
        name = row["id"] + "-envelope"
        result[name] = _box(x-width/2, x+width/2, y-depth/2, y+depth/2, z0, z1)
    for name, shape in result.items():
        shape.label = name + " incomplete purchased reference, not vendor geometry"
    return result
