"""F13 static jog, reconstructed for assembly review, not manufacture.

The T30 sweep follows the F13-STATIC-01 nominal radial profile and phase.
It requires independent geometric verification before any model approval.
Purchased items are qualified nominal reference envelopes.
"""
import math

from build123d import (
    Axis, BuildPart, CenterArc, Edge, Face, Line, Location, Mode, Plane, Pos, Shell, Solid, Wire,
    insert, loft, make_face,
)


BLOCKERS = (
    "P01 and P04/P07 T30 sweep geometry and same-Z phase require independent verification.",
    "Actual sensor components, connector and wiring, bearing internal geometry, "
    "and fastener details are not defined by the drawing; references are envelopes.",
)


def _cyl(r, z0, z1, x=0, y=0):
    return Solid.make_cylinder(r, z1 - z0, plane=Plane(origin=(x, y, z0)))


def _box(x0, x1, y0, y1, z0, z1):
    return Solid.make_box(x1 - x0, y1 - y0, z1 - z0, plane=Plane(origin=(x0, y0, z0)))


def _cone(r0, r1, z0, z1, x=0, y=0):
    return Solid.make_cone(r0, r1, z1 - z0, plane=Plane(origin=(x, y, z0)))


def _xy(r, a):
    return r * math.cos(math.radians(a)), r * math.sin(math.radians(a))


def _radial_box(a, u0, u1, v0, v1, z0, z1):
    return _box(u0, u1, v0, v1, z0, z1).rotate(Axis.Z, a)


def _hex(af, z0, z1, x, y):
    radius = af / math.sqrt(3)
    points = [(x + radius * math.cos(math.radians(30 + 60 * i)),
               y + radius * math.sin(math.radians(30 + 60 * i)), z0) for i in range(6)]
    return Solid.extrude(Face(Wire.make_polygon(points)), (0, 0, z1 - z0))


def _groove_profile(z, offset):
    outer, inner = 19.2 + offset, 16.8 - offset
    xc = 2.8
    yo = math.sqrt(18.4 ** 2 - xc ** 2)
    yi = math.sqrt(17.6 ** 2 - xc ** 2)
    ol, or_ = (-xc, yo), (xc, yo)
    il, ir = (-xc, yi), (xc, yi)

    def radial(point, radius):
        factor = radius / math.hypot(*point)
        return tuple(v * factor for v in point)

    outer_left, outer_right = radial(ol, outer), radial(or_, outer)
    inner_left, inner_right = radial(il, inner), radial(ir, inner)
    left_low, left_up = (-2 + offset, yi), (-2 + offset, yo)
    right_up, right_low = (2 - offset, yo), (2 - offset, yi)

    def arc(center, start, end, ccw=True):
        a = math.degrees(math.atan2(start[1] - center[1], start[0] - center[0]))
        b = math.degrees(math.atan2(end[1] - center[1], end[0] - center[0]))
        sweep = (b - a) % 360 if ccw else -((a - b) % 360)
        return CenterArc(center, math.dist(center, start), a, sweep)

    edges = [
        arc((0, 0), outer_left, outer_right),
        arc(or_, outer_right, right_up),
        Line(right_up, right_low),
        arc(ir, right_low, inner_right),
        arc((0, 0), inner_right, inner_left, False),
        arc(il, inner_left, left_low),
        Line(left_low, left_up),
        arc(ol, left_up, outer_left),
    ]
    return Pos(0, 0, z) * make_face(edges)


def _platter_exterior():
    # This is only the defined exterior portion, not the complete P01 rotor.
    groove = loft([_groove_profile(35.6, 0), _groove_profile(36.4, .8)], ruled=True)
    with BuildPart() as p:
        insert(_cone(55, 52.5, 21.4, 36.4))
        tool = Solid.make_cylinder(5, 9.75, plane=Plane(origin=(50.25, 0, 28.9), z_dir=(1, 0, 0)))
        start_edges = [e for e in tool.edges() if abs(e.center().X - 50.25) < 1e-7]
        tool = tool.fillet(1, start_edges)
        for a in range(0, 360, 30):
            insert(tool.rotate(Axis.Z, a), mode=Mode.SUBTRACT)
        insert(groove, mode=Mode.SUBTRACT)
    return p.part


def _thread_ridge(radial_offset):
    root = 14.725 + radial_offset
    crest = 14.975 + radial_offset
    half_root = .03125 + .25 / math.sqrt(3)
    z = 2.5
    # Ruled helical faces avoid the invalid Boolean topology of a radial pipe sweep.
    profile = [(root - .025, -half_root), (root, -half_root),
               (crest, -.03125), (crest, .03125),
               (root, half_root), (root - .025, half_root)]
    helices = [Edge.make_helix(.5, 3.5, r, center=(0, 0, z + dz))
               for r, dz in profile]
    faces = [Face.make_surface_from_curves(a, b)
             for a, b in zip(helices, helices[1:] + helices[:1])]
    for dz in (0, 3.5):
        faces.append(Face(Wire.make_polygon([(r, 0, z + offset + dz)
                                             for r, offset in profile])))
    shell = Shell(faces, tolerance=1e-5)
    if not shell.is_valid or not shell.is_manifold:
        raise ValueError("F13 helical ridge shell is not valid and closed")
    return Solid(shell) & _cyl(16, 3, 5.5)


def _rotor():
    platter = _platter_exterior()
    with BuildPart() as shaft:
        insert(_cyl(14.725, 3, 5.5))
        insert(_thread_ridge(0))
        insert(_cyl(14.975, 5.5, 21.4))
        insert(_cyl(16.1, 19.5, 21.4))
        insert(_cyl(13, 3, 21.4), mode=Mode.SUBTRACT)
    root_edges = [
        e for e in shaft.part.edges()
        if abs(e.center().Z - 19.5) < 1e-6
        and abs(e.length - 2 * math.pi * 14.975) < 1e-5
    ]
    if len(root_edges) != 1:
        raise ValueError("Cannot identify the P01 shoulder root edge")
    shaft_body = shaft.part.fillet(.2, root_edges)
    if not shaft_body.is_inside((-14.97, 0, 4.25)):
        raise RuntimeError("F13 P01 T30 Boolean lost the thread crest; full model is blocked")
    with BuildPart() as p:
        insert(shaft_body)
        insert(_cyl(6, 6.6, 21.4))
        insert(platter)
        insert(_cyl(4.1, 6.6, 10.8), mode=Mode.SUBTRACT)
    return p.part


def _collar(z0, z1):
    with BuildPart() as p:
        insert(_cyl(16.1, z0, z1))
        insert(_cyl(14.775, z0, z1), mode=Mode.SUBTRACT)
        insert(_thread_ridge(.05), mode=Mode.SUBTRACT)
        for a in (0, 120, 240):
            insert(_radial_box(a, 15.6, 16.2, -1, 1, z0, z1), mode=Mode.SUBTRACT)
    if p.part.is_inside((-15.0, 0, z0 + .25)):
        raise RuntimeError("F13 collar T30 Boolean lost the thread groove; full model is blocked")
    return p.part


def _carrier():
    with BuildPart() as p:
        insert(_cyl(23, 5.5, 19.5))
        for a in (0, 120, 240):
            x, y = _xy(23, a)
            insert(_cyl(2.5, 5.5, 9.5, x, y))
            insert(_cyl(2.5, 15.5, 19.5, x, y))
        for a in (90, 210, 330):
            x, y = _xy(31, a)
            insert(_cyl(5, 6, 9, x, y))
            insert(_radial_box(a, 22, 31, -5, 5, 6, 9))
            insert(_radial_box(a, 22, 25.7, -2, 2, 1, 3.8))
            insert(_radial_box(a, 24, 25.7, -2, 2, 3.8, 9))
        insert(_cyl(21.075, 5.5, 19.5), mode=Mode.SUBTRACT)
        for a in (0, 120, 240):
            x, y = _xy(23, a)
            insert(_cyl(.8, 5.5, 8.5, x, y), mode=Mode.SUBTRACT)
            insert(_cyl(.8, 16.5, 19.5, x, y), mode=Mode.SUBTRACT)
        for a in (90, 210, 330):
            x, y = _xy(31, a)
            insert(_cyl(1, 6, 9, x, y), mode=Mode.SUBTRACT)
    return p.part


def _cover(upper):
    z0, z1 = (19.5, 21) if upper else (4, 5.5)
    with BuildPart() as p:
        insert(_cyl(23, z0, z1))
        for a in (0, 120, 240):
            x, y = _xy(23, a)
            insert(_cyl(2.5, z0, z1, x, y))
        insert(_cyl(20, z0, z1), mode=Mode.SUBTRACT)
        for a in (0, 120, 240):
            x, y = _xy(23, a)
            insert(_cyl(1.2, z0, z1, x, y), mode=Mode.SUBTRACT)
            if upper:
                insert(_cone(1.2, 2.1, z1 - .9, z1, x, y), mode=Mode.SUBTRACT)
            else:
                insert(_cone(2.1, 1.2, z0, z0 + .9, x, y), mode=Mode.SUBTRACT)
    return p.part


def _sensor_plate():
    with BuildPart() as p:
        insert(_cyl(25, 0, 1))
        for sign in (-1, 1):
            insert(_cyl(.9, 1, 2.5, sign * 6, 0))
            insert(_box(7.6 if sign > 0 else -12.4, 12.4 if sign > 0 else -7.6, -3, 3, 1, 3))
        insert(_box(23.8, 25.1, -1.2, 1.2, 0, 1), mode=Mode.SUBTRACT)
        insert(_box(-5, 5, -26, -3, 0, 1), mode=Mode.SUBTRACT)
        for sign in (-1, 1):
            x = sign * 10
            insert(_hex(4.1, .6, 2.3, x, 0), mode=Mode.SUBTRACT)
            insert(_box(x - 2.1, x + 2.1, 0, 8, .6, 2.3), mode=Mode.SUBTRACT)
            insert(_cyl(1.1, .2, 3, x, 0), mode=Mode.SUBTRACT)
    return p.part


def _toe():
    with BuildPart() as p:
        insert(_box(6.8, 12.4, -2.5, 2.5, 3, 4.3))
        insert(_cyl(1.1, 3, 4.3, 10, 0), mode=Mode.SUBTRACT)
        insert(_cone(1.1, 1.3, 4.1, 4.3, 10, 0), mode=Mode.SUBTRACT)
    return p.part


def _board():
    with BuildPart() as p:
        insert(_cyl(9, 1, 3))
        insert(_box(-7.5, 7.5, -8.5, 8.5, 1, 3), mode=Mode.INTERSECT)
        for x in (-6, 6):
            insert(_cyl(1.1, 1, 3, x, 0), mode=Mode.SUBTRACT)
    return p.part


def _bearing(z):
    return _cyl(21, z, z + 7) - _cyl(15, z, z + 7)


def build(appearance_only=False):
    """Build full jogs, or explicitly omit unverified threads for visual review."""
    printed = {
        "P01 platter exterior only" if appearance_only else "P01 platter and threaded rotor":
            _platter_exterior() if appearance_only else _rotor(),
        "P02 carrier F13-STATIC-04": _carrier(),
        "P05 upper cover": _cover(True),
        "P06 lower cover": _cover(False),
        "sensor plate F13-STATIC-02": _sensor_plate(),
        "P08 toe right": _toe(),
        "P08 toe left": _toe().rotate(Axis.Z, 180),
    }
    if not appearance_only:
        printed["P04 threaded retaining collar"] = _collar(4, 5.5)
        printed["P07 threaded jam collar"] = _collar(3, 4)
    reference = {
        "SKF 61806-2RS1 lower simplified envelope": _bearing(5.5),
        "SKF 61806-2RS1 upper simplified envelope": _bearing(12.5),
        "D8x4 diametric magnet nominal envelope": _cyl(4, 6.6, 10.6),
        "AS5048A PCB nominal contour laminate only no components": _board(),
    }
    for sign in (-1, 1):
        x = sign * 10
        reference[f"PCB M2 nut nominal threadless {sign}"] = _hex(4, .65, 2.25, x, 0) - _cyl(1, .65, 2.25, x, 0)
        reference[f"PCB M2x4 cap screw nominal threadless {sign}"] = _cyl(1, .3, 4.3, x, 0) + _cyl(1.9, 4.3, 6.3, x, 0)
    for i, a in enumerate((90, 210, 330), 1):
        x, y = _xy(31, a)
        reference[f"floor M2.5x8 ETTINGER nominal threadless {i}"] = _cyl(1.25, .5, 8.5, x, y) + _cyl(2.25, -2, .5, x, y)
    for i, a in enumerate((0, 120, 240), 1):
        x, y = _xy(23, a)
        reference[f"upper M2x4 DIN7991 nominal threadless {i}"] = _cyl(1, 17, 20, x, y) + _cone(1, 2, 20, 21, x, y)
        reference[f"lower M2x4 DIN7991 nominal threadless {i}"] = _cyl(1, 5, 8, x, y) + _cone(2, 1, 4, 5, x, y)
    result = {"printed": {}, "reference": {}}
    for side, x in (("left", 110), ("right", 490)):
        for category, parts in (("printed", printed), ("reference", reference)):
            for name, part in parts.items():
                shape = part.rotate(Axis.Z, 60).moved(Location((x, -165, 2)))
                key = f"{side} {name}"
                shape.label = key
                result[category][key] = shape
    return result
