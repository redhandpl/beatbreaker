"""Incomplete nominal control envelopes and plunger tip planes from B24.

These are references, not complete purchased parts or proof of clearances.
"""
import json
from pathlib import Path

from build123d import Face, Wire
from shell import _group

ROOT = Path(__file__).resolve().parents[4]
PROOF = ROOT / "schematics/enclosure/B24/DJC_Enclosure_Rev_B24_validation.json"


def build():
    rows = json.loads(PROOF.read_text())["compiled_control_primitives"]
    rows = [row for row in rows if "retainer" not in row["id"].lower()]
    if len(rows) != 49:
        raise ValueError(f"Expected 49 control bodies; got {len(rows)}")
    result = {}
    for row in rows:
        name, transform = row["owner"], row["CSG"][1]
        cuts = []
        if name.startswith(("B", "T")):
            additions = [[0, [-6, -6, 0], [12, 12, 4.3]]]
        elif name.startswith("P"):
            additions = [[0, [-5.7, -5.5, 0], [11.4, 12.5, 6.8]]]
        elif name.startswith("F"):
            additions = [[0, [-30, -4.5, 0], [60, 9, 6]], [0, [-2, -.5, 6], [4, 1, 15]]]
        elif name == "E01":
            additions = [[0, [-5.9, -7, 0], [11.8, 14.5, 6.5]], [1, [0, 0, 6.5], [3.5, 3.5, 7]], [1, [0, 0, 13.5], [3, 3, 8]]]
            cuts = [[0, [-5, 1.5, 14.5], [10, 3.5, 7.01]]]
        else:
            raise ValueError(f"Unknown control: {name}")
        solid = _group([name, transform, additions, cuts])
        solid.label = name + " incomplete purchased control reference"
        result[name + "-BODY-REF"] = solid
        if name.startswith(("B", "T")):
            vertices = []
            for x, y in ((-1.9, -1.9), (-1.9, 1.9), (1.9, 1.9), (1.9, -1.9)):
                coords = (x, y, 7.3)
                xyz = [sum(transform[i][j]*coords[j] for j in range(3)) + transform[i][3] for i in range(3)]
                vertices.append((xyz[0], -xyz[1], xyz[2]))
            face = Face(Wire.make_polygon(vertices, close=True))
            face.label = name + " nominal free plunger tip plane reference"
            result[name + "-TIP-REF"] = face
    return result
