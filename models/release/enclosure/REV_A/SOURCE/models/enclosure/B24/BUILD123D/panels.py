"""B24-build123d01 upper panels and display roofs, in CAD coordinates, mm.

Source: B22_panels.py and B24_changes.py, with B24-R04-MARKS-01.
This unapproved reconstruction requires geometric validation against Fusion-05.
"""
import json
import math
import re
from pathlib import Path

from build123d import (Align, Box, Cone, Cylinder, Plane, Polygon, Pos,
                       Rectangle, RectangleRounded, SlotOverall, chamfer, extrude, fillet)

ROOT = Path(__file__).resolve().parents[4]
MIN = (Align.MIN, Align.MIN, Align.MIN)
CMIN = (Align.CENTER, Align.CENTER, Align.MIN)


def source(path):
    return json.loads((ROOT / path).read_text())


def box(x0, x1, y0, y1, z0, z1):
    return Pos(x0, y0, z0) * Box(x1-x0, y1-y0, z1-z0, align=MIN)


def cylinder(x, y, z, radius, height):
    return Pos(x, y, z) * Cylinder(radius, height, align=CMIN)


def polygon(points, z, height):
    return Pos(0, 0, z) * extrude(Polygon(*points, align=None), amount=height, dir=(0, 0, 1))


def profile(row, z=17, height=5):
    name, x, y, kind, w, h, r, _ = row
    if name.startswith('T'):
        a = 7.2 + 1.6 * math.sqrt(5)
        sign = 1 if int(name[1:]) % 2 else -1
        return polygon([(x+sign*u, -y+sign*v) for u, v in
                        [(-a, 0), (4, (a+4)/2), (4, -(a+4)/2)]], z, height)
    if kind == 'circle':
        return cylinder(x, -y, z, w/2, height)
    if kind == 'rect':
        sketch = Rectangle(w, h)
    elif kind == 'slot':
        sketch = SlotOverall(max(w, h), min(w, h), rotation=90 if h > w else 0)
    else:
        sketch = RectangleRounded(w, h, r)
    return Pos(x, -y, z) * extrude(sketch, amount=height)


def edge_points(edge):
    return [edge.position_at(t) for t in (0, .25, .5, .75, 1)]


def top_edges(part, predicate, z=20):
    return [e for e in part.edges() if all(abs(p.Z-z) < 1e-5 and predicate(p.X, p.Y)
                                           for p in edge_points(e))]


def chamfer_edges(part, predicate):
    edges = top_edges(part, predicate)
    if edges:
        return chamfer(edges, .8)
    raise ValueError('Expected top chamfer edges not found')


def cap_edge(row, x, y):
    name, cx, cy, kind, w, h, r, _ = row
    u, v = x-cx, y+cy
    if name.startswith('T'):
        sign = 1 if int(name[1:]) % 2 else -1
        u, v = sign*u, sign*v
        a = 7.2 + 1.6*math.sqrt(5)
        distances = [u-4, (-u+2*v-a)/math.sqrt(5), (-u-2*v-a)/math.sqrt(5)]
        return max(distances) <= 1e-5 and min(abs(d) for d in distances) < 1e-5
    if kind == 'circle':
        return abs(math.hypot(u, v)-w/2) < 1e-5
    qx, qy = abs(u)-(w/2-r), abs(v)-(h/2-r)
    return abs(math.hypot(max(qx, 0), max(qy, 0))+min(max(qx, qy), 0)-r) < 1e-5


def exterior(x, y):
    y = -y
    tol = 1e-5
    if ((abs(x) < tol or abs(x-600) < tol) and 3-tol <= y <= 297+tol or
        (abs(y) < tol or abs(y-300) < tol) and 3-tol <= x <= 597+tol):
        return True
    return any((x-cx)*(1 if cx == 3 else -1) <= tol and
               (y-cy)*(1 if cy == 3 else -1) <= tol and
               abs(math.hypot(x-cx, y-cy)-3) < tol
               for cx, cy in ((3, 3), (597, 3), (3, 297), (597, 297)))


def rounds(part, identifier, top=20):
    corners = {'R01': (0, 0), 'R04': (600, 0), 'R05': (0, -300), 'R07': (600, -300)}
    if identifier in corners:
        x, y = corners[identifier]
        edges = [e for e in part.edges() if all(abs(p.X-x) < 1e-6 and abs(p.Y-y) < 1e-6
                                                  for p in edge_points(e)) and e.length > 1]
        if len(edges) != 1:
            raise ValueError((identifier, 'corner edges', len(edges)))
        part = fillet(edges, 3)
    edges = top_edges(part, exterior, top)
    if edges:
        part = fillet(edges, .8)
    elif identifier != 'R03':
        raise ValueError((identifier, 'missing exterior edge'))
    return part


def load_data():
    text = (ROOT / 'models/enclosure/B15/DJC_Enclosure_Rev_B15_inputs.scad').read_text()
    data = {name: json.loads(value) for name, value in re.findall(r'^(b15_\w+) = (.*);$', text, re.M)}
    b22 = source('schematics/enclosure/B22/DJC_Enclosure_Rev_B22_definition.json')
    b19 = source('schematics/enclosure/B19/DJC_Enclosure_Rev_B19_definition.json')
    proof = source('schematics/enclosure/B22/DJC_Enclosure_Rev_B22_validation.json')
    moves = {r['id']: r['new_XY'] for r in source('schematics/enclosure/B24/DJC_Enclosure_Rev_B24_definition.json')['control_moves']}
    return data, b22, b19, proof, moves


def overlaps(row, bounds):
    name, x, y, _, w, h, _, _ = row
    if name.startswith('T'):
        w, h = 30, 16
    x0, x1, y0, y1 = bounds
    return x+w/2 > x0 and x-w/2 < x1 and y+h/2 > y0 and y-h/2 < y1


def flat(identifier, data, b22, b19, proof, moves):
    _, x0, x1, y0, y1 = next(r for r in b19['panel_regions'] if r[0] == identifier)
    if identifier == 'R03':
        y0 = 96
    bounds = (x0, x1, y0, y1)
    part = box(x0, x1, -y1, -y0, 18, 20)
    if identifier == 'R01':
        part -= box(153.55, 220, -96, 0, 17, 22)
    if identifier == 'R04':
        part -= box(380, 446.45, -96, 0, 17, 22)
    if identifier == 'R03':
        for x in (228, 372):
            part -= box(x-5, x+5, -98, -96, 17, 22)
    rows = []
    removed = b22['main_body']['removed_panel_post_axes_XY']
    for original in data['b15_panel_apertures']:
        row = list(original)
        name, x, y = row[:3]
        if name in ('D01', 'J01') or row[7] and ([x, y] in removed or 153.55 < x < 446.45 and y < 96):
            continue
        if name in moves:
            row[1:3] = moves[name]
        if overlaps(row, bounds):
            rows.append(row)
            part -= profile(row)
    part = rounds(part, identifier)
    wells = [r for r in b19['fader_recesses']['instances'] if r['panel'] == identifier]
    for row in wells:
        x, y = row['table_xy']
        w, h = (69.7, 14) if row['id'] == 'F05' else (14, 69.7)
        part -= Pos(x, -y, 19) * extrude(RectangleRounded(w, h, 3), amount=3)
    if wells:
        def on_well(x, y):
            for row in wells:
                cx, cy = row['table_xy']
                w, h = (69.7, 14) if row['id'] == 'F05' else (14, 69.7)
                qx, qy = abs(x-cx)-(w/2-3), abs(y+cy)-(h/2-3)
                if abs(math.hypot(max(qx, 0), max(qy, 0))+min(max(qx, qy), 0)-3) < 1e-5:
                    return True
            return False
        part = chamfer_edges(part, on_well)
    jogs = [x for x in (110, 490) if x+54 > x0 and x-54 < x1 and 204 > y0 and 96 < y1]
    for x in jogs:
        part -= cylinder(x, -150, 19, 54, 3)
    if jogs:
        part = chamfer_edges(part, lambda x, y: any(abs(math.hypot(x-j, y+150)-54) < 1e-5 for j in jogs))
    caps = [r for r in rows if r[0].startswith(('B', 'T'))]
    if caps:
        part = chamfer_edges(part, lambda x, y: any(cap_edge(r, x, y) for r in caps))
    for mark in proof['P_marks']:
        name = mark['id'].split('-')[0]
        if identifier == 'R04' and name in ('P01', 'P02', 'P03'):
            continue
        poly = mark['polygon_XY']
        cx, cy = (sum(p[i] for p in poly)/4 for i in (0, 1))
        if x0 < cx < x1 and y0 < cy < y1:
            part += polygon([(x, -y) for x, y in poly], 20, .4)
    if identifier == 'R04':
        patterns = [r['polygon_XY'] for r in proof['P_marks'] if r['id'] == 'P04']
        for target_y in (21, 49, 77):
            for poly in patterns:
                part += polygon([(x-244+559, -(y-131+target_y)) for x, y in poly], 20, .4)
    for name, x, y, *_ in data['b15_fader_poses']:
        if not (x0 < x < x1 and y0 < y < y1):
            continue
        travel = 28 if name == 'F05' else 41
        for j in range(11):
            u = -travel/2+j*travel/10
            length = 4 if j in (0, 5, 10) else 2
            for sign in (-1, 1):
                points = [(uu, sign*vv) for uu, vv in ((u-.4, 2.4), (u+.4, 2.4), (u+.4, 2.4+length), (u-.4, 2.4+length))]
                points = [(x+uu, -(y-vv)) if name == 'F05' else (x+vv, -(y+uu)) for uu, vv in points]
                part += polygon(points, 19, .4)
    return part


def section(x, width, points):
    return extrude(Plane.YZ.offset(x) * Polygon(*points, align=None), amount=width, dir=(1, 0, 0))


def roof(identifier, b22):
    left = identifier == 'D02L'
    x0, x1 = (153.55, 335) if left else (335, 446.45)
    a = math.radians(49)
    c, s = math.cos(a), math.sin(a)
    cy, h, j, u = 96-40*c, 18+40*s, 96-80*c, 20+80*s
    part = section(x0, x1-x0, [(0, u-2), (-j, u-2), (-96, 18), (-96, 20), (-j, u), (0, u)])
    part += section(153.55 if left else 444.45, 2, [(-2, 18), (-96, 18), (-96, 20), (-j, u), (-2, u)])
    def place(shape, side, row):
        if side*row > 0:
            shape = shape.mirror(Plane.XZ)
        frame = Plane(origin=(300, -cy, h), x_dir=(side, 0, 0), z_dir=(0, -s, c))
        return shape.moved(frame.location)
    opening = place(box(-136, 136, -36, 36, -5, 5), 1, 1)
    part -= opening
    for x, y in b22['main_body']['module_rear_retention_axes_XY']:
        if x0 < x < x1:
            part -= cylinder(x, -y, u-2.01, 1.7, 2.02)
    if left:
        part += box(325, 345, -29, -13, u-10, u-2)
        for y in (18, 24):
            part -= cylinder(340, -y, u-9, 1.25, 7.01)
    else:
        for y in (18, 24):
            part -= cylinder(340, -y, u-2.01, 1.7, 2.02)
    x = 228 if left else 372
    upper95 = 20 + math.tan(a)
    part += section(x-5, 10, [(-95, 16), (-98, 16), (-98, 20), (-96, 20), (-95, upper95)])
    part += box(x-5, x+5, -116, -95, 16, 18)
    part -= cylinder(x, -112, 15.99, 1.7, 2.02)
    for row in (-1, 1):
        support = box(138.5, 144.2, 18, 30, -21.2, 0)
        support += box(138.25, 140, 20, 39.797470349551496, -21, -.25)
        support += box(130, 140, 38.297470349551496, 39.797470349551496, -21, -.25)
        support -= box(136, 146, 19.9, 28.1, -21.2, -18)
        support -= cylinder(140.7, 24, -18.1, 1.25, 7.1)
        support -= cylinder(140.7, 24, -60, 4, 39)
        part += place(support, -1 if left else 1, row)
    return rounds(part, identifier, u)


def build():
    data, b22, b19, proof, moves = load_data()
    parts = {'PANEL_'+i: flat(i, data, b22, b19, proof, moves) for i in ('R01', 'R03', 'R04', 'R05', 'R06', 'R07')}
    parts.update({i: roof(i, b22) for i in ('D02L', 'D02R')})
    # Source post axes identify all 33 closure screws; two lap axes complete the 35.
    rear = b22['main_body']['module_rear_retention_axes_XY']
    removed = b22['main_body']['removed_panel_post_axes_XY']
    a = math.radians(49)
    u = 20+80*math.sin(a)
    for _, xy, *_ in data['b15_posts']:
        x, y = xy
        if xy in removed:
            continue
        top = u if xy in rear else 20
        tool = Pos(x, -y, top-1.3) * Cone(1.7, 3.01, 1.31, align=CMIN)
        for key, part in parts.items():
            if (part & tool).volume > 1e-6:
                parts[key] = part - tool
                break
        else:
            raise ValueError(('No panel for countersink', x, y))
    for y in (18, 24):
        parts['D02R'] -= Pos(340, -y, u-1.3) * Cone(1.7, 3.01, 1.31, align=CMIN)
    for key, part in parts.items():
        part.label = key + ' B24-build123d01 DRAFT'
    return parts
