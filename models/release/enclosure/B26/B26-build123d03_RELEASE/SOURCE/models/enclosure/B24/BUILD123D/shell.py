"""B24-build123d01 lower shells; millimetres, CAD coordinates (X, -Y, Z).

Reconstructs the B22 native shell and retained B15 CSG, then applies the
approved B24 layout, AC01-LOW-01 and JOINTS-02 changes. This model is unapproved
and does not establish printability or physical fastener fit.
"""
from __future__ import annotations

import json
import math
import re
from pathlib import Path

from build123d import Align, Box, Cone, Cylinder, Face, Location, Plane, Pos, Rot, Solid, Wire

ROOT = Path(__file__).resolve().parents[4]
MIN = (Align.MIN, Align.MIN, Align.MIN)
CYL = (Align.CENTER, Align.CENTER, Align.MIN)


def _json(path):
    return json.loads((ROOT / path).read_text())


def _box(x0, x1, y0, y1, z0, z1):
    return Pos(x0, -y1, z0) * Box(x1-x0, y1-y0, z1-z0, align=MIN)


def _cyl(x, y, z0, z1, r0, r1=None):
    r1 = r0 if r1 is None else r1
    obj = Cylinder(r0, z1-z0, align=CYL) if r0 == r1 else Cone(r0, r1, z1-z0, align=CYL)
    return Pos(x, -y, z0) * obj


def _horizontal(x, y, z, radius, length):
    return Pos(x, -y, z) * Rot(90, 0, 0) * Cylinder(radius, length, align=CYL)


def _primitive(p):
    kind, (x, y, z), size = p
    if kind == 0:
        w, h, d = size
        return Pos(x, y, z) * Box(w, h, d, align=MIN)
    if kind == 1:
        r0, r1, h = size
        return Pos(x, y, z) * (Cylinder(r0, h, align=CYL) if r0 == r1 else Cone(r0, r1, h, align=CYL))
    assert kind == 2, p
    w, h, r, height = size
    assert 0 < r <= min(w, h)/2
    pieces = []
    if w > 2*r:
        pieces.append(Pos(x-w/2+r, y-h/2, z) * Box(w-2*r, h, height, align=MIN))
    if h > 2*r:
        pieces.append(Pos(x-w/2, y-h/2+r, z) * Box(w, h-2*r, height, align=MIN))
    for sx in (-1, 1):
        for sy in (-1, 1):
            pieces.append(Pos(x+sx*(w/2-r), y+sy*(h/2-r), z) * Cylinder(r, height, align=CYL))
    result = pieces[0]
    for piece in pieces[1:]:
        result = result + piece
    return result


def _group(csg):
    name, transform, additions, cuts = csg
    assert additions, name
    result = _primitive(additions[0])
    for p in additions[1:]:
        result = result + _primitive(p)
    for p in cuts:
        result = result - _primitive(p)
    # Map table Y to CAD Y without applying a non-rigid reflection as a location.
    a, b = transform[0][:2]
    c, d = transform[1][:2]
    determinant = a*d - b*c
    assert math.isclose(abs(determinant), 1, abs_tol=1e-9), name
    if determinant > 0:
        result = result.mirror(Plane.XZ)
    angle = math.degrees(math.atan2(-c, a))
    result = result.moved(Location((transform[0][3], -transform[1][3], transform[2][3]), angle))
    assert result.is_valid and result.volume > 0, name
    return result


def _valid(shape, label):
    assert shape is not None and shape.is_valid and len(shape.solids()) == 1 and shape.volume > 0, label
    return shape


def _attach(shells, bounds, solid, label):
    original = solid.volume
    attached = 0.0
    for key, (x0, x1, y0, y1) in bounds.items():
        bb = solid.bounding_box()
        if bb.max.X <= x0 or bb.min.X >= x1 or bb.max.Y <= -y1 or bb.min.Y >= -y0:
            continue
        piece = solid & _box(x0, x1, y0, y1, -100, 200)
        if piece is None or piece.volume < 1e-8:
            continue
        attached += piece.volume
        shells[key] = _valid(shells[key] + piece, label + ' / ' + key)
    assert math.isclose(attached, original, rel_tol=1e-7, abs_tol=1e-5), (label, original, attached)


def _cut(shells, bounds, cutter, label):
    owners = []
    bb = cutter.bounding_box()
    for key, (x0, x1, y0, y1) in bounds.items():
        if bb.max.X <= x0 or bb.min.X >= x1 or bb.max.Y <= -y1 or bb.min.Y >= -y0:
            continue
        intersection = shells[key] & cutter
        if intersection is None or intersection.volume < 1e-8:
            continue
        shells[key] = _valid(shells[key] - cutter, label + ' / ' + key)
        owners.append(key)
    assert owners, label


def _edge_points(edge):
    return [edge.position_at(t) for t in (0, .25, .5, .75, 1)]


def _exterior(p):
    x, y = p.X, -p.Y
    tol = 1e-5
    if ((abs(x) < tol or abs(x-600) < tol) and 3-tol <= y <= 297+tol) or ((abs(y) < tol or abs(y-300) < tol) and 3-tol <= x <= 597+tol):
        return True
    return any((x-cx)*(1 if cx == 3 else -1) <= tol and (y-cy)*(1 if cy == 3 else -1) <= tol and abs(math.hypot(x-cx, y-cy)-3) < tol for cx, cy in ((3, 3), (597, 3), (3, 297), (597, 297)))


def _round_shell(shape, key):
    corners = {'C01': (0, 0, 2, -2), 'C03': (600, 0, 598, -2), 'C04': (0, -300, 2, -298), 'C06': (600, -300, 598, -298)}
    if key in corners:
        x, y, ix, iy = corners[key]
        for px, py, radius in ((x, y, 3), (ix, iy, 1)):
            edges = [e for e in shape.edges() if all(abs(p.X-px) < 1e-6 and abs(p.Y-py) < 1e-6 for p in _edge_points(e)) and abs(_edge_points(e)[-1].Z-_edge_points(e)[0].Z) > 1]
            assert len(edges) == 1, (key, px, py, len(edges))
            shape = _valid(shape.solids()[0].fillet(radius, edges), key + ' plan fillet')
    edges = [e for e in shape.edges() if all(abs(p.Z) < 1e-6 and _exterior(p) for p in _edge_points(e))]
    assert edges, key
    return _valid(shape.solids()[0].fillet(.8, edges), key + ' bottom fillet')


def build():
    definition = _json('schematics/enclosure/B22/DJC_Enclosure_Rev_B22_definition.json')
    proof = _json('schematics/enclosure/B22/DJC_Enclosure_Rev_B22_validation.json')
    b24 = _json('schematics/enclosure/B24/DJC_Enclosure_Rev_B24_validation.json')
    equipment = _json(definition['sources']['equipment'])
    inlet = _json('schematics/enclosure/B24-AC01-LOW-01/DJC_Enclosure_Rev_B24_AC01_LOW_01_definition.json')['inlet']
    joints = _json('schematics/enclosure/B24-JOINTS-02/DJC_Enclosure_Rev_B24_JOINTS_02_definition.json')
    text = (ROOT / 'models/enclosure/B15/DJC_Enclosure_Rev_B15_inputs.scad').read_text()
    data = {name: json.loads(value) for name, value in re.findall(r'^(b15_\w+) = (.*);$', text, re.M)}
    rear_u = 20 + 80*math.sin(math.radians(49))
    bounds = {identifier: (xs[0], xs[1], ys[0], ys[1]) for identifier, xs, ys in data['b15_segments']}
    assert set(bounds) == {'C01', 'C02', 'C03', 'C04', 'C05', 'C06'}
    shells = {}
    for key, (x0, x1, y0, y1) in bounds.items():
        shape = _box(x0, x1, y0, y1, 0, 18) - _box(max(x0, 2), min(x1, 598), max(y0, 2), min(y1, 298), 2, 102)
        if y0 == 0:
            a, b = max(x0, 153.55), min(x1, 446.45)
            if b > a:
                shape = shape + _box(a, b, 0, 2, 18, rear_u-2)
        shells[key] = _valid(shape, key + ' envelope')
    shells['C01'] -= _box(37.25, 72.15, -.01, 2.01, 2, 18)
    for x in (32.75, 76.65):
        shells['C01'] -= _horizontal(x, -.01, 9.95, 1.8, 2.02)
    # The old rear J01 hole is closed in B24, so only its front cut is needed.
    cells = proof['ventilation_cells']
    assert len(cells) == 48
    for cell in cells:
        wire = Wire.make_polygon([(x, .01, z) for x, z in cell['polygon_XZ']])
        shells['C02'] -= Solid.extrude(Face(wire), (0, -2.02, 0))
    main = definition['main_body']
    posts = [p for p in equipment['panel_posts'] if p['centre_table_mm'] not in main['removed_panel_post_axes_XY']]
    assert len(posts) == 33
    for post in posts:
        x, y = post['centre_table_mm']
        top = rear_u-2 if [x, y] in main['module_rear_retention_axes_XY'] else 16 if [x, y] in main['module_front_retention_axes_XY'] else 18
        shape = _cyl(x, y, 2, 5.8, 4.5, 4) + _cyl(x, y, 2, top, 4)
        shape -= _cyl(x, y, top-10, top+.01, 1.25)
        shape &= _box(0, 600, 0, 300, 0, 100)
        _attach(shells, bounds, shape, post['id'])
    for identifier, normal, (cx, cy) in data['b15_bridge_instances']:
        for offset in (-9, 9):
            x, y = (cx, cy+offset) if normal == 'Y' else (cx+offset, cy)
            pad = _cyl(x, y, 2, 8, 4.5) - _cyl(x, y, 2.5, 8.01, 1.25)
            _attach(shells, bounds, pad, identifier)
    fixed_ids = {row[0] for row in data['b15_fixed']}
    fixed = [row for row in b24['compiled_control_primitives'] if row['id'] in fixed_ids]
    assert len(fixed) == 49
    for row in fixed:
        _attach(shells, bounds, _group(row['CSG']), row['id'])
    for device in definition['devices']:
        for index, (x, y) in enumerate(device['mount_axes_XY']):
            radius, top = (5, 3) if device['id'] == 'PSU' else (3.5, 6)
            _attach(shells, bounds, _cyl(x, y, 2, top, radius), device['id'])
            if device['id'] == 'PI':
                _cut(shells, bounds, _cyl(x, y, 1, 6.01, 1), 'PI pilot')
            elif device['id'] == 'PSU':
                tool = _cyl(x, y, -.01, 3.01, 1.7) + _cyl(x, y, 0, 1.3, 3, 1.7)
                _cut(shells, bounds, tool, 'PSU countersink')
    for x, y in proof['old_jog_axes_XY']:
        _attach(shells, bounds, _cyl(x, y, 2, 8, 5) - _cyl(x, y, 3, 8.01, 1), 'jog boss')
    for key in shells:
        shells[key] = _round_shell(shells[key], key)
    shells['C04'] = _valid(shells['C04'] - _horizontal(101, 297.99, 10, 3.1, 2.02), 'front J01')
    x, z = inlet['new_centre_XZ_mm']
    shells['C01'] = _valid(shells['C01'] - _box(x-23.75, x+23.75, 0, 2, z-14, z+14), 'lowered AC01')
    counts = {key: 0 for key in shells}
    for joint in joints['added_joints']:
        for x, y in joint['screw_axes_XY_mm']:
            owners = [key for key in joint['pair'] if bounds[key][0] < x < bounds[key][1] and bounds[key][2] < y < bounds[key][3]]
            assert len(owners) == 1, (joint['id'], x, y)
            key = owners[0]
            shells[key] = _valid(shells[key] + _cyl(x, y, 2, 8, 4.5), joint['id'] + ' pad')
            shells[key] = _valid(shells[key] - _cyl(x, y, 2.5, 8.01, 1.25), joint['id'] + ' pilot')
            counts[key] += 1
    assert counts == joints['changed_shell_pad_counts']
    for key, shape in shells.items():
        _valid(shape, key)
        shape.label = key + ' lower shell PETG B24-build123d01 DRAFT'
    return shells
