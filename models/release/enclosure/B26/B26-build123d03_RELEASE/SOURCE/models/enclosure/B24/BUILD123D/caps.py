"""Approved legacy cap meshes at B24-Fusion-05 positions, millimetres.

These are triangulated display references, not editable BRep solids. The
approved engineer decision preserves the original meshes; no STEP is imported.
"""
import hashlib
import json
from pathlib import Path

from build123d import Plane, import_stl

ROOT = Path(__file__).resolve().parents[4]
FUSION = ROOT / "models/enclosure/B24/FUSION"
INVENTORY = FUSION / "DJC_Enclosure_Rev_B24_Fusion05_validation.json"


def build():
    old = json.loads((ROOT / "models/enclosure/B19/FUSION/DJC_Enclosure_Rev_B19_Fusion01_BOM_and_exports.json").read_text())
    new = json.loads((FUSION / "DJC_Enclosure_Rev_B24_Fusion05_BOM_and_exports.json").read_text())
    definitions = {}
    for kind in ("CAP_B", "CAP_T", "CAP_P", "CAP_F", "CAP_C", "CAP_E"):
        row = next(row for row in old["parts"] if row["id"] == kind)
        path = (ROOT / "models/enclosure/B19/FUSION" / row["path"]).resolve()
        if not path.is_relative_to(ROOT) or hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            raise ValueError(f"Missing or changed approved cap mesh: {kind}")
        definitions[kind] = import_stl(path)
    for kind in ("CAP-CUE40", "CAP-PP40", "CAP-HC40"):
        row = next(row for row in new["parts"] if row["id"] == kind)
        path = (FUSION / row["path"]).resolve()
        if not path.is_relative_to(ROOT) or hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            raise ValueError(f"Missing or changed approved cap mesh: {kind}")
        definitions[kind] = import_stl(path)
    rows = json.loads(INVENTORY.read_text())["inventory"]
    rows = [row for row in rows if row["component"].split()[0] in definitions]
    if len(rows) != 49:
        raise ValueError(f"Expected 49 installed caps, got {len(rows)}")
    result = {}
    for row in rows:
        p = row["pose"]
        frame = Plane(origin=(p[3]*10, p[7]*10, p[11]*10), x_dir=(p[0], p[4], p[8]), z_dir=(p[2], p[6], p[10]))
        part = definitions[row["component"].split()[0]].moved(frame.location)
        part.label = row["occurrence"] + " / immutable mesh reference"
        result[row["id"]] = part
    return result
