"""Check B24 working geometry against the recorded approved native inventory.

Numerical comparisons are not manufacturing tolerances or collision checks.
"""
import json
from pathlib import Path

from DJC_Enclosure_Rev_B24_build123d01 import build

ROOT = Path(__file__).resolve().parents[4]
INVENTORY = ROOT / "models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_validation.json"


def bounds(shape):
    box = shape.bounding_box()
    return [[box.min.X, box.min.Y, box.min.Z], [box.max.X, box.max.Y, box.max.Z]]


def delta(a, b):
    return max(abs(x-y) for ar, br in zip(a, b) for x, y in zip(ar, br))


def check():
    groups = build()
    rows = json.loads(INVENTORY.read_text())["inventory"]
    results = []

    def compare(name, shapes, row, mesh=False):
        if not shapes:
            raise ValueError(f"Missing geometry: {name}")
        if not mesh and not all(s.is_valid for s in shapes):
            raise ValueError(f"Invalid BRep: {name}")
        boxes = [bounds(s) for s in shapes]
        actual = [[min(b[0][i] for b in boxes) for i in range(3)],
                  [max(b[1][i] for b in boxes) for i in range(3)]]
        bd = delta(actual, row["bounds_mm"])
        vd = None if mesh else abs(sum(s.volume for s in shapes) - row["volume_mm3"])
        if bd > (0.001 if mesh else 0.0001) or (vd is not None and vd > 0.0001):
            raise ValueError(f"{name}: bound difference {bd} mm, volume difference {vd} mm³")
        results.append((name, bd, vd))

    for group, prefix in (("Shells - printed PETG", ""), ("Panels and roof - printed PETG", "")):
        for name, shape in groups[group].items():
            row = next(r for r in rows if r["component"].startswith(prefix + name + " "))
            compare(name, [shape], row)

    expected_bridges = [r for r in rows if r["component"] == "C07 retained bolted bridge PETG"]
    for name, shape in groups["Bridges - printed PETG"].items():
        candidates = [r for r in expected_bridges if delta(bounds(shape), r["bounds_mm"]) < 0.0001]
        if len(candidates) != 1:
            raise ValueError(f"C07 {name}: expected exactly one matching placement")
        compare("C07 " + name, [shape], candidates[0])

    retainers = groups["Control retainers - printed PETG"]
    for row in rows:
        if "retained removable PETG" not in row["component"]:
            continue
        name = row["component"].split()[0]
        pieces = [retainers[k] for k in (name, name+"-1", name+"-2") if k in retainers]
        compare(name, pieces, row)

    toes = [r for r in rows if r["component"].startswith("D01 B22 removable frame toe")]
    for name, shape in groups["Display toes - printed PETG"].items():
        candidates = [r for r in toes if delta(bounds(shape), r["bounds_mm"]) < 0.0001]
        if len(candidates) != 1:
            raise ValueError(f"{name}: expected exactly one matching placement")
        compare(name, [shape], candidates[0])

    by_id = {row["id"]: row for row in rows}
    for name, shape in groups["Caps - retained mesh references"].items():
        compare(name, [shape], by_id[name], mesh=True)
    for name, shape in groups["Fasteners - nominal reference only"].items():
        compare(name, [shape], by_id[name])

    references = groups["Control envelopes and tip planes - incomplete references"]
    for row in rows:
        if row["role"] == "reference_control":
            key = row["component"].split()[0] + "-BODY-REF"
            compare(key, [references[key]], row)
        elif row["role"] == "reference_surface" and "free plunger TIP PLANE" in row["component"]:
            key = row["component"].split()[0] + "-TIP-REF"
            compare(key, [references[key]], row)

    equipment = groups["Equipment and connector envelopes - incomplete references"]
    equipment_names = {
        "PI-envelope": "PI B22 source envelope REF", "DAC-envelope": "DAC B22 source envelope REF",
        "PSU-envelope": "PSU B22 source envelope REF", "ESP32-envelope": "ESP32 retained controller REF / retention TBD",
        "PCF8575-1-envelope": "PCF8575-1 retained controller REF / retention TBD",
        "PCF8575-2-envelope": "PCF8575-2 retained controller REF / retention TBD",
        "CD74HC4067-envelope": "CD74HC4067 retained controller REF / retention TBD",
        "J01-body": "J01 source body and thread envelope REF", "J01-nut": "J01 source nut envelope REF",
        "D01-front-plane": "D01 measured LCD FRONT PLANE REF / rear unknown",
        "RCA-front-plane": "RCA known face plane REF / actual rear body unknown",
    }
    for name, component in equipment_names.items():
        compare(name, [equipment[name]], next(r for r in rows if r["component"] == component))

    print(f"Matched {len(results)} B24 source body/face instances; 5 retainer bodies each contain two solids.")
    print(f"Maximum bounds difference: {max(r[1] for r in results):.9g} mm")
    print(f"Maximum non-mesh volume difference: {max(r[2] for r in results if r[2] is not None):.9g} mm³")
    print("Caps are triangulated references; no mesh-volume, collision, clearance, motion or physical checks were performed.")


if __name__ == "__main__":
    check()
