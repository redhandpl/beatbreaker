"""B26 installed nominal purchased fastener references, not manufacturing parts.

Coordinates are CAD (X, -Y, Z), in millimetres. Threads and drive recesses
are absent. Jog hardware is owned by f13_jog, not this module. U1-U4
fasteners are not specified by B26.
"""
from itertools import product
from math import cos, radians, sin

from build123d import Plane, Pos

import b26_controls
import b26_shell
import hardware


def build():
    """Return stable IDs mapped to installed, incomplete reference solids."""
    result = {}
    joint = hardware._socket_screw(1.5, 8, 2.75, 3)
    closure = hardware._countersunk(1.5, 8, 3)
    control_m2 = hardware._countersunk(1, 6, 2.2)
    control_m16 = hardware._countersunk(.8, 5, 1.6)

    def add(identifier, shape):
        if identifier in result:
            raise ValueError(f"Duplicate fastener ID: {identifier}")
        shape.label = f"{identifier} / purchased nominal reference / incomplete"
        result[identifier] = shape

    for identifier, normal, x, y in b26_shell._joints():
        for side in (-1, 1):
            px = x + 9 * side if normal == 'X' else x
            py = y + 9 * side if normal == 'Y' else y
            add(f"C07-{identifier}-{'A' if side < 0 else 'B'}-M3x8",
                Pos(px, -py, 11) * joint)

    panels = {
        'R01': ((8, 8), (110, 8), (8, 132), (160, 132), (212, 132)),
        'R03': ((228, 110), (372, 110)),
        'R04': ((490, 8), (592, 8), (388, 132), (440, 132), (592, 132)),
        'R05': ((8, 148), (212, 148), (8, 230), (212, 230), (8, 312), (212, 312)),
        'R06': ((228, 148), (372, 148), (228, 312), (372, 312)),
        'R07': ((388, 148), (592, 148), (388, 230), (592, 230), (388, 312), (592, 312)),
    }
    for panel, axes in panels.items():
        for index, (x, y) in enumerate(axes, 1):
            add(f"{panel}-closure-{index}-BN616-M3x8", Pos(x, -y, 20) * closure)
    for index, x in enumerate((210, 230, 300, 370, 390), 1):
        add(f"roof-rear-{index}-BN616-M3x8", Pos(x, -4, b26_shell.REAR_TOP + 2) * closure)
    for index, y in enumerate((18, 24), 1):
        add(f"roof-lap-{index}-BN616-M3x8", Pos(340, -y, b26_shell.REAR_TOP + 2) * closure)
    for index, x in enumerate((361.5, 416.5), 1):
        frame = Plane(origin=(x, -54.35, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))
        add(f"PSU-{index}-BN616-M3x6", hardware._countersunk(1.5, 6, 3).moved(frame.location))


    for row in b26_controls.rows():
        if 'retainer' not in row['id'].lower():
            continue
        owner = row['owner']
        _, transform, _, cuts = row['CSG']
        screw = control_m16 if owner.startswith('P') else control_m2
        head_radius = 1.6 if owner.startswith('P') else 2.2
        number = 0
        for kind, origin, size in cuts:
            if kind != 1 or abs(size[1] - head_radius) > 1e-7 or size[0] == size[1]:
                continue
            u, v, w = origin
            x = transform[0][0] * u + transform[0][1] * v + transform[0][3]
            y = transform[1][0] * u + transform[1][1] * v + transform[1][3]
            z = transform[2][3] + w + size[2]
            number += 1
            add(f"{owner}-retainer-{number}-{'M1.6x5' if owner.startswith('P') else 'M2x6'}",
                Pos(x, -y, z) * screw)
        expected = 4 if owner.startswith('P') else 2
        if number != expected:
            raise ValueError(f"{owner}: expected {expected} retainer screw axes, found {number}")

    # B10 specifies ISO4762 under the B22 toe, with the shaft pointing inward.
    shaft = joint.moved(Plane(origin=(140.7, 24, -21), x_dir=(1, 0, 0),
                              z_dir=(0, 0, -1)).location)
    angle = radians(49)
    c, s = cos(angle), sin(angle)
    cy, height = 96 - 40*c, 23 + 40*s
    for side, row in product((-1, 1), repeat=2):
        local = shaft.mirror(Plane.XZ) if side * row > 0 else shaft
        frame = Plane(origin=(300, -cy, height), x_dir=(side, 0, 0), z_dir=(0, -s, c))
        add(f"display-toe-{side}-{row}-ISO4762-M3x8", local.moved(frame.location))

    if len(result) != 197:
        raise ValueError(f"Expected 197 enclosure fastener references, found {len(result)}")
    return result
