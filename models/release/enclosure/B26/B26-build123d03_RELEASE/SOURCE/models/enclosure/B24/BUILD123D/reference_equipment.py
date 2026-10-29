"""B24 incomplete purchased equipment envelopes and measured reference planes.

These are not vendor solids, electrical-clearance verification, or printable parts.
"""
import json
import math
import re
from pathlib import Path

from build123d import Align, Cylinder, Face, Pos, Rot, Wire
from shell import _box

ROOT = Path(__file__).resolve().parents[4]
CYL = (Align.CENTER, Align.CENTER, Align.MIN)


def _axis_y(x, y, z, radius, length):
    return Pos(x, y, z) * Rot(-90, 0, 0) * Cylinder(radius, length, align=CYL)


def build():
    b22 = json.loads((ROOT / "schematics/enclosure/B22/DJC_Enclosure_Rev_B22_definition.json").read_text())
    text = (ROOT / "models/enclosure/B15/DJC_Enclosure_Rev_B15_inputs.scad").read_text()
    data = {name: json.loads(value) for name, value in re.findall(r"^(b15_\w+) = (.*);$", text, re.M)}
    result = {}
    for dev in b22["devices"]:
        x, y = dev["centre_XY"]
        w, h = dev["size_XY"]
        z0, z1 = dev["body_Z"] if dev["id"] == "PSU" else (dev["PCB_underside_Z"]-dev["below_PCB"], dev["PCB_underside_Z"]+dev["above_PCB"])
        result[dev["id"] + "-envelope"] = _box(x-w/2, x+w/2, y-h/2, y+h/2, z0, z1)
    for name, (x, y), (w, h), (z0, z1) in data["b15_controllers"]:
        result[name + "-envelope"] = _box(x-w/2, x+w/2, y-h/2, y+h/2, z0, z1)
    result["J01-body"] = _axis_y(101, -298, 10, 4.075, 11.8) + _axis_y(101, -302.5, 10, 3, 4.5)
    result["J01-nut"] = _axis_y(101, -301.8, 10, 4, 1.8) - _axis_y(101, -301.81, 10, 3, 1.82)
    a = math.radians(49)
    c, s = math.cos(a), math.sin(a)
    cy, height = 96-40*c, 18+40*s
    points = [(300+u, -cy-c*v, height-s*v) for u, v in ((-138, -38), (-138, 38), (138, 38), (138, -38))]
    result["D01-front-plane"] = Face(Wire.make_polygon(points, close=True))
    result["RCA-front-plane"] = Face(Wire.make_polygon([(x, 0, z) for x, z in ((28.85, .05), (28.85, 19.95), (80.55, 19.95), (80.55, .05))], close=True))
    for name, part in result.items():
        part.label = name + " incomplete reference / not vendor geometry"
    return result
