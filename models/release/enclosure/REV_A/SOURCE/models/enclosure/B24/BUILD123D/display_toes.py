"""Four removable B22/B24 display toes, in the assembled CAD frame."""
from itertools import product
from math import cos, radians, sin

from build123d import Align, Box, Cylinder, Plane, Pos

MIN = (Align.MIN, Align.MIN, Align.MIN)
CYL = (Align.CENTER, Align.CENTER, Align.MIN)


def build():
    toe = Pos(136.5, 20, -21) * Box(7.7, 8, 3, align=MIN)
    toe += Pos(136.5, 20, -18) * Box(1, 8, 1, align=MIN)
    toe -= Pos(140.7, 24, -21.1) * Cylinder(1.7, 3.2, align=CYL)
    angle = radians(49)
    c, s = cos(angle), sin(angle)
    cy, height = 96 - 40*c, 18 + 40*s
    result = {}
    for side, row in product((-1, 1), repeat=2):
        local = toe.mirror(Plane.XZ) if side*row > 0 else toe
        frame = Plane(origin=(300, -cy, height), x_dir=(side, 0, 0), z_dir=(0, -s, c))
        part = local.moved(frame.location)
        key = f"D01-toe-{side}-{row}"
        part.label = key + " printed B24-build123d01 DRAFT"
        result[key] = part
    return result
