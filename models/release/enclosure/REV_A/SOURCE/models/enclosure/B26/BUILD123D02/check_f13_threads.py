"""Check the approved F13 T30 profile and sampled screw motion in millimetres.

Numerical probes are geometric checks, not print or continuous-motion approval.
Run with the same approved environment as the assembly.
"""
import math

from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
from build123d import Axis, Location, Shape

import f13_jog


def check():
    rotor = f13_jog._rotor()
    collars = (('P04', f13_jog._collar(4, 5.5), (4.05, 4.25, 4.43, 4.75, 5.25, 5.45)),
               ('P07', f13_jog._collar(3, 4), (3.05, 3.25, 3.43, 3.75, 3.95)))
    for name, part in [('P01', rotor)] + [(name, part) for name, part, _ in collars]:
        if not part.is_valid or len(part.solids()) != 1:
            raise ValueError(f'{name} is not one valid solid')
    for name, collar, heights in collars:
        count = 0
        for z in heights:
            for deg in range(0, 360, 15):
                t = (z - .5*deg/360 + .25) % .5 - .25
                radius = max(14.725, 14.975 - math.sqrt(3)*max(0, abs(t)-.03125))
                angle = math.radians(deg)
                c, s = math.cos(angle), math.sin(angle)
                def inside(part, r):
                    return part.is_inside((r*c, r*s, z), 1e-6)
                if not (inside(rotor, radius-.005) and not inside(rotor, radius+.005)
                        and not inside(collar, radius+.045) and inside(collar, radius+.055)):
                    raise ValueError(f'{name} profile or phase differs at z={z}, angle={deg}')
                count += 1
        print(name, 'radial phase samples:', count, 'passed', flush=True)
    collar = collars[1][1]
    for angle in (0, 45, 90, 180, 270, 360):
        shift = .5*angle/360
        moved = collar.rotate(Axis.Z, angle).moved(Location((0, 0, shift)))
        common = BRepAlgoAPI_Common(rotor.wrapped, moved.wrapped)
        common.Build()
        if not common.IsDone() or common.Shape().IsNull():
            raise RuntimeError(f'P07 Boolean operation failed at {angle} degrees')
        volume = Shape.cast(common.Shape()).volume
        distance = rotor.distance_to(moved)
        if volume > 1e-6 or distance <= 1e-5:
            raise ValueError(f'P07 interference/contact at {angle} degrees: {volume}, {distance}')
        print('P07 pose', angle, 'degrees, axial shift', shift, 'mm, clearance', distance, 'mm', flush=True)


if __name__ == '__main__':
    check()
