"""B24-JOINTS-02 C07 bridge occurrences in the enclosure CAD frame."""
import json
from pathlib import Path

from build123d import Pos, Rot

from C07_Rev_B24_build123d01 import build_c07

ROOT = Path(__file__).resolve().parents[4]
DEFINITION = ROOT / "schematics/enclosure/B24-JOINTS-02/DJC_Enclosure_Rev_B24_JOINTS_02_definition.json"


def build():
    definition = json.loads(DEFINITION.read_text())
    joints = definition["retained_joints"] + definition["added_joints"]
    assert len(joints) == definition["bridge"]["quantity_after"] == 14
    base = build_c07()
    result = {}
    for joint in joints:
        identifier = joint["id"]
        assert identifier not in result
        x, y = joint["centre"]
        normal = joint["normal"]
        assert normal in ("X", "Y")
        angle = 0 if normal == "X" else -90
        part = Pos(x, -y, definition["bridge"]["assembled_Z_mm"][0]) * Rot(0, 0, angle) * base
        part.label = f"C07 {identifier} printed"
        result[identifier] = part
    return result
