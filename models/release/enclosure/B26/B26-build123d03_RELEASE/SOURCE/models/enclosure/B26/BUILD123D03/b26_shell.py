"""B26-INTEGRATED-01 lower shells and C07 bridges, in CAD (X, -Y, Z).

The model is for review, not manufacturing. U1-U4 mounting and the actual
connector, wire and display-rear geometries are not specified by the drawing.
"""
import math
import re
import json

from build123d import Face, Pos, Rot, Solid, Wire

import b26_controls
from C07_Rev_B24_build123d01 import build_c07
from shell import ROOT, _attach, _box, _cut, _cyl, _edge_points, _group, _horizontal, _json, _valid


BOUNDS = {
    'C01': (0, 220, 0, 140), 'C02': (220, 380, 0, 140),
    'C03': (380, 600, 0, 140), 'C04': (0, 220, 140, 320),
    'C05': (220, 380, 140, 320), 'C06': (380, 600, 140, 320),
}
REAR_TOP = 23 + 80 * math.sin(math.radians(49))


def _joints():
    definition = _json('schematics/enclosure/B24-JOINTS-02/DJC_Enclosure_Rev_B24_JOINTS_02_definition.json')
    joints = []
    for source in definition['retained_joints'] + definition['added_joints']:
        x, y = source['centre']
        joints.append((source['id'], source['normal'], x, y + 20))
    joints.extend((('J15', 'X', 220, 14), ('J16', 'X', 380, 14)))
    assert len(joints) == 16
    return joints


def _round_shell(shape, key):
    corners = {'C01': (0, 0, 2, -2), 'C03': (600, 0, 598, -2),
               'C04': (0, -320, 2, -318), 'C06': (600, -320, 598, -318)}
    if key in corners:
        x, y, ix, iy = corners[key]
        for px, py, radius in ((x, y, 3), (ix, iy, 1)):
            edges = [e for e in shape.edges()
                     if all(abs(p.X-px) < 1e-6 and abs(p.Y-py) < 1e-6 for p in _edge_points(e))
                     and abs(_edge_points(e)[-1].Z-_edge_points(e)[0].Z) > 1]
            assert len(edges) == 1, (key, px, py, len(edges))
            shape = _valid(shape.solids()[0].fillet(radius, edges), key + ' plan fillet')

    def exterior(p):
        x, y = p.X, -p.Y
        tol = 1e-5
        if (((abs(x) < tol or abs(x-600) < tol) and 3-tol <= y <= 317+tol)
                or ((abs(y) < tol or abs(y-320) < tol) and 3-tol <= x <= 597+tol)):
            return True
        return any((x-cx)*(1 if cx == 3 else -1) <= tol
                   and (y-cy)*(1 if cy == 3 else -1) <= tol
                   and abs(math.hypot(x-cx, y-cy)-3) < tol
                   for cx, cy in ((3, 3), (597, 3), (3, 317), (597, 317)))

    edges = [e for e in shape.edges() if all(abs(p.Z) < 1e-6 and exterior(p) for p in _edge_points(e))]
    assert edges, key
    return _valid(shape.solids()[0].fillet(.8, edges), key + ' bottom fillet')


def build():
    definition = _json('schematics/enclosure/B22/DJC_Enclosure_Rev_B22_definition.json')
    proof = _json('schematics/enclosure/B22/DJC_Enclosure_Rev_B22_validation.json')
    equipment = _json(definition['sources']['equipment'])
    inlet = _json('schematics/enclosure/B24-AC01-LOW-01/DJC_Enclosure_Rev_B24_AC01_LOW_01_definition.json')['inlet']
    text = (ROOT / 'models/enclosure/B15/DJC_Enclosure_Rev_B15_inputs.scad').read_text()
    data = {name: json.loads(value) for name, value in re.findall(r'^(b15_\w+) = (.*);$', text, re.M)}

    shells = {}
    for key, (x0, x1, y0, y1) in BOUNDS.items():
        shape = _box(x0, x1, y0, y1, 0, 18) - _box(max(x0, 2), min(x1, 598), max(y0, 2), min(y1, 318), 2, 102)
        if y0 == 0:
            a, b = max(x0, 153.55), min(x1, 446.45)
            if b > a:
                shape += _box(a, b, 0, 2, 18, REAR_TOP)
        shells[key] = _round_shell(_valid(shape, key + ' envelope'), key)

    shells['C01'] -= _box(37.25, 72.15, -.01, 2.01, 2, 18)
    for x in (32.75, 76.65):
        shells['C01'] -= _horizontal(x, -.01, 9.95, 1.8, 2.02)
    for cell in proof['ventilation_cells']:
        wire = Wire.make_polygon([(x, .01, z) for x, z in cell['polygon_XZ']])
        shells['C02'] -= Solid.extrude(Face(wire), (0, -2.02, 0))
    shells['C04'] -= _horizontal(101, 317.99, 10, 3.1, 2.02)
    x, z = inlet['new_centre_XZ_mm']
    shells['C01'] -= _box(x-23.75, x+23.75, 0, 2, z-14, z+14)

    main = definition['main_body']
    posts = [p for p in equipment['panel_posts'] if p['centre_table_mm'] not in main['removed_panel_post_axes_XY']]
    assert len(posts) == 33
    for post in posts:
        x, old_y = post['centre_table_mm']
        if [x, old_y] in main['module_rear_retention_axes_XY']:
            y, top = 4, REAR_TOP
        elif [x, old_y] in main['module_front_retention_axes_XY']:
            y, top = 110, 16
        elif old_y == 4 and x in (8, 110, 490, 592):
            y, top = 8, 18
        else:
            y, top = old_y + 20, 18
        shape = _cyl(x, y, 2, 5.8, 4.5, 4) + _cyl(x, y, 2, top, 4)
        shape -= _cyl(x, y, top-10, top+.01, 1.25)
        shape &= _box(0, 600, 0, 320, 0, 100)
        _attach(shells, BOUNDS, shape, post['id'])

    for identifier, normal, x, y in _joints():
        for offset in (-9, 9):
            px, py = (x + offset, y) if normal == 'X' else (x, y + offset)
            pad = _cyl(px, py, 2, 8, 4.5) - _cyl(px, py, 2.5, 8.01, 1.25)
            _attach(shells, BOUNDS, pad, identifier)

    fixed_ids = {row[0] for row in data['b15_fixed']}
    fixed = [row for row in b26_controls.rows() if row['id'] in fixed_ids]
    assert len(fixed) == 49
    for row in fixed:
        _attach(shells, BOUNDS, _group(row['CSG']), row['id'])

    for device in definition['devices']:
        for x, old_y in device['mount_axes_XY']:
            y = old_y + 20
            radius, top = (5, 3) if device['id'] == 'PSU' else (3.5, 6)
            _attach(shells, BOUNDS, _cyl(x, y, 2, top, radius), device['id'])
            if device['id'] == 'PI':
                _cut(shells, BOUNDS, _cyl(x, y, 1, 6.01, 1), 'PI pilot')
            elif device['id'] == 'PSU':
                tool = _cyl(x, y, -.01, 3.01, 1.7) + _cyl(x, y, 0, 1.3, 3, 1.7)
                _cut(shells, BOUNDS, tool, 'PSU countersink')

    # F13 local O is on the floor top; the whole jog is clocked +60 degrees in table XY.
    for cx in (110, 490):
        cy = 165
        for angle in (150, 270, 30):
            x = cx + 31 * math.cos(math.radians(angle))
            y = cy - 31 * math.sin(math.radians(angle))
            _attach(shells, BOUNDS, _cyl(x, y, 2, 8, 5), 'jog mounting boss')
            _cut(shells, BOUNDS, _cyl(x, y, -.01, 2.5, 2.4), 'jog head counterbore')
            _cut(shells, BOUNDS, _cyl(x, y, 2.5, 8.01, 1.45), 'jog screw clearance')
        for angle in (60, 180, 300):
            x = cx + 26.2 * math.cos(math.radians(angle))
            y = cy - 26.2 * math.sin(math.radians(angle))
            _attach(shells, BOUNDS, _cyl(x, y, 2, 3.5, 1), 'sensor locator')
        key = Pos(cx, -cy, 2) * Rot(0, 0, 60) * _box(24, 26, -1, 1, 0, 1)
        _attach(shells, BOUNDS, key, 'sensor anti-rotation key')

    for key, shape in shells.items():
        _valid(shape, key)
        shape.label = key + ' lower shell PETG B26-INTEGRATED-01 review'
    return shells


def build_bridges():
    base = build_c07()
    result = {}
    for identifier, normal, x, y in _joints():
        part = Pos(x, -y, 8) * Rot(0, 0, 0 if normal == 'X' else -90) * base
        part.label = f'C07 {identifier} printed B26-INTEGRATED-01 review'
        result[identifier] = part
    return result
