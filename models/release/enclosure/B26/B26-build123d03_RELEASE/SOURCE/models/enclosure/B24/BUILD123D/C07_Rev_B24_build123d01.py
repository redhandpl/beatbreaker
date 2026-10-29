"""B24 C07 bridge, working model from the approved B24-JOINTS-02 drawing.

Millimetres; local origin at the bridge centre on the bottom face.
This is one printed part, not the complete B24 enclosure.
"""
from math import isclose, pi

from build123d import Align, Box, Cylinder, Pos

LENGTH = 28.0
WIDTH = 10.0
THICKNESS = 3.0
HOLE_DIAMETER = 3.4
HOLE_PITCH = 18.0


def build_c07():
    part = Box(LENGTH, WIDTH, THICKNESS, align=(Align.CENTER, Align.CENTER, Align.MIN))
    for x in (-HOLE_PITCH / 2, HOLE_PITCH / 2):
        part -= Pos(x, 0, 0) * Cylinder(
            HOLE_DIAMETER / 2, THICKNESS, align=(Align.CENTER, Align.CENTER, Align.MIN)
        )
    part.label = "C07 B24-build123d01 DRAFT"
    return part


def check_c07(part):
    size = part.bounding_box().size
    assert part.is_valid and len(part.solids()) == 1
    assert all(isclose(actual, expected, abs_tol=1e-7) for actual, expected in zip(size, (LENGTH, WIDTH, THICKNESS)))
    expected_volume = (LENGTH * WIDTH - 2 * pi * (HOLE_DIAMETER / 2) ** 2) * THICKNESS
    assert isclose(part.volume, expected_volume, abs_tol=1e-7)


if __name__ == "__main__":
    from ocp_viewer import Camera, show

    c07 = build_c07()
    check_c07(c07)
    print(f"C07: valid; one solid; {LENGTH:g} x {WIDTH:g} x {THICKNESS:g} mm; volume {c07.volume:.6f} mm^3")
    show(c07, names=["C07 B24-build123d01 DRAFT - not full enclosure"], reset_camera=Camera.ISO)
