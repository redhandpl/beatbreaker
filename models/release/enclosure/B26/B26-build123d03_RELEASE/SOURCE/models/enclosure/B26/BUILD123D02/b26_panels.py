"""B26-INTEGRATED-01 panel and roof geometry, in global CAD coordinates, mm.

Drawing coordinates (X, Y, Z) map to (X, -Y, Z). This is a review model,
not a manufacturing release; physical fit and the display interfaces are unverified.
"""
import math

from build123d import Cone, Plane, Pos, RectangleRounded, extrude, fillet
from panels import (CMIN, box, cap_edge, chamfer_edges, cylinder, edge_points,
                    load_data, polygon, profile, section, top_edges)

FRONT = 96 + 5 / math.tan(math.radians(49))
AXES = {
    'R01': [(8, 8), (110, 8), (8, 132), (160, 132), (212, 132)],
    'R03': [(228, 110), (372, 110)],
    'R04': [(490, 8), (592, 8), (388, 132), (440, 132), (592, 132)],
    'R05': [(8, 148), (212, 148), (8, 230), (212, 230), (8, 312), (212, 312)],
    'R06': [(228, 148), (372, 148), (228, 312), (372, 312)],
    'R07': [(388, 148), (592, 148), (388, 230), (592, 230), (388, 312), (592, 312)],
}


def owner(x, y):
    if x < 220:
        rear = y < (165 if 75 <= x <= 145 else 140)
        return 'R01' if rear else 'R05'
    if x < 380:
        return 'R03' if y < 140 else 'R06'
    rear = y < (165 if 455 <= x <= 525 else 140)
    return 'R04' if rear else 'R07'


def exterior(x, y):
    y = -y
    t = 1e-5
    if ((abs(x) < t or abs(x-600) < t) and 3-t <= y <= 317+t or
            (abs(y) < t or abs(y-320) < t) and 3-t <= x <= 597+t):
        return True
    return any((x-cx)*(1 if cx == 3 else -1) <= t and
               (y-cy)*(1 if cy == 3 else -1) <= t and
               abs(math.hypot(x-cx, y-cy)-3) < t
               for cx, cy in ((3, 3), (597, 3), (3, 317), (597, 317)))


def outer_rounds(part, identifier):
    corners = {'R01': (0, 0), 'R04': (600, 0),
               'R05': (0, -320), 'R07': (600, -320)}
    if identifier in corners:
        x, y = corners[identifier]
        edges = [e for e in part.edges() if e.length > 1 and
                 all(abs(p.X-x) < 1e-6 and abs(p.Y-y) < 1e-6 for p in edge_points(e))]
        if len(edges) != 1:
            raise ValueError((identifier, 'corner edges', len(edges)))
        part = fillet(edges, 3)
    edges = top_edges(part, exterior)
    if edges:
        part = fillet(edges, .8)
    return part


def panel(identifier, data, b19, proof, moves):
    if identifier == 'R03':
        part = box(220, 380, -140, -FRONT, 18, 20)
    elif identifier == 'R06':
        part = box(220, 380, -320, -140, 18, 20)
    else:
        left = identifier in ('R01', 'R05')
        rear = identifier in ('R01', 'R04')
        x0, x1 = (0, 220) if left else (380, 600)
        a, b = (75, 145) if left else (455, 525)
        if rear:
            part = box(x0, x1, -140, 0, 18, 20)
            part += box(a, b, -165, -140, 18, 20)
            cut0, cut1 = (153.55, 220) if left else (380, 446.45)
            part -= box(cut0, cut1, -FRONT, 0, 17, 21)
        else:
            part = box(x0, x1, -320, -140, 18, 20)
            part -= box(a, b, -165, -140, 17, 21)

    rows = []
    for original in data['b15_panel_apertures']:
        row = list(original)
        name = row[0]
        if not (name.startswith(('B', 'T', 'P', 'F', 'L')) or name == 'E01'):
            continue
        if name in moves and name not in ('E01', 'T01', 'T02'):
            row[1:3] = moves[name]
        row[2] += 20
        if name in ('E01', 'T01', 'T02'):
            row[2] = 125
        if name in ('B23', 'B24'):
            row[2] = 255
        if owner(row[1], row[2]) == identifier:
            rows.append(row)
            part -= profile(row)
    part = outer_rounds(part, identifier)

    wells = [r for r in b19['fader_recesses']['instances'] if r['panel'] == identifier]
    for r in wells:
        x, y = r['table_xy']
        w, h = (69.7, 14) if r['id'] == 'F05' else (14, 69.7)
        part -= Pos(x, -(y+20), 19) * extrude(RectangleRounded(w, h, 3), amount=3)
    if wells:
        def on_well(x, y):
            for r in wells:
                cx, cy = r['table_xy']
                w, h = (69.7, 14) if r['id'] == 'F05' else (14, 69.7)
                qx, qy = abs(x-cx)-(w/2-3), abs(y+cy+20)-(h/2-3)
                if abs(math.hypot(max(qx, 0), max(qy, 0))+min(max(qx, qy), 0)-3) < 1e-5:
                    return True
            return False
        part = chamfer_edges(part, on_well)

    jog = {'R01': 110, 'R05': 110, 'R04': 490, 'R07': 490}.get(identifier)
    if jog is not None:
        part -= cylinder(jog, -165, 17, 26, 5)
        part -= cylinder(jog, -165, 19, 54, 3)
        part = chamfer_edges(part, lambda x, y: abs(math.hypot(x-jog, y+165)-54) < 1e-5)
    caps = [r for r in rows if r[0].startswith(('B', 'T'))]
    if caps:
        part = chamfer_edges(part, lambda x, y: any(cap_edge(r, x, y) for r in caps))

    for mark in proof['P_marks']:
        name = mark['id'].split('-')[0]
        if name in ('P01', 'P02', 'P03'):
            continue
        points = mark['polygon_XY']
        cx = sum(p[0] for p in points)/4
        cy = sum(p[1] for p in points)/4 + 20
        if owner(cx, cy) == identifier:
            part += polygon([(x, -y-20) for x, y in points], 20, .4)
    if identifier == 'R04':
        patterns = [r['polygon_XY'] for r in proof['P_marks'] if r['id'] == 'P04']
        for target_y in (41, 69, 97):
            for points in patterns:
                part += polygon([(x-244+559, -(y-131+target_y)) for x, y in points], 20, .4)
    for name, x, y, *_ in data['b15_fader_poses']:
        y += 20
        if owner(x, y) != identifier:
            continue
        travel = 28 if name == 'F05' else 41
        for j in range(11):
            u = -travel/2 + j*travel/10
            length = 4 if j in (0, 5, 10) else 2
            for sign in (-1, 1):
                points = [(uu, sign*vv) for uu, vv in
                          ((u-.4, 2.4), (u+.4, 2.4), (u+.4, 2.4+length), (u-.4, 2.4+length))]
                points = [(x+uu, -(y-vv)) if name == 'F05' else (x+vv, -(y+uu))
                          for uu, vv in points]
                part += polygon(points, 19, .4)
    for x, y in AXES[identifier]:
        part -= cylinder(x, -y, 17, 1.7, 5)
        part -= Pos(x, -y, 18.7) * Cone(1.7, 3, 1.3, align=CMIN)
    return part


def roof(identifier):
    left = identifier == 'D02L'
    x0, x1 = (153.55, 335) if left else (335, 446.45)
    a = math.radians(49)
    c, s = math.cos(a), math.sin(a)
    cy, h, j, u = 96-40*c, 23+40*s, 96-80*c, 25+80*s
    part = section(x0, x1-x0, [(0, u-2), (-j, u-2), (-FRONT, 18),
                                (-FRONT, 20), (-j, u), (0, u)])
    part += section(153.55 if left else 444.45, 2,
                    [(-2, 18), (-FRONT, 18), (-FRONT, 20), (-j, u), (-2, u)])

    def place(shape, side, row):
        if side*row > 0:
            shape = shape.mirror(Plane.XZ)
        frame = Plane(origin=(300, -cy, h), x_dir=(side, 0, 0), z_dir=(0, -s, c))
        return shape.moved(frame.location)

    part -= place(box(-136, 136, -36, 36, -5, 5), 1, 1)
    for x in (210, 230, 300, 370, 390):
        if x0 < x < x1:
            part -= cylinder(x, -4, u-2.01, 1.7, 2.02)
            part -= Pos(x, -4, u-1.3) * Cone(1.7, 3, 1.3, align=CMIN)
    if left:
        part += box(325, 345, -29, -13, u-10, u-2)
        for y in (18, 24):
            part -= cylinder(340, -y, u-9, 1.25, 7.01)
    else:
        for y in (18, 24):
            part -= cylinder(340, -y, u-2.01, 1.7, 2.02)
            part -= Pos(340, -y, u-1.3) * Cone(1.7, 3, 1.3, align=CMIN)
    x = 228 if left else 372
    part += section(x-5, 10, [(-95, 16), (-116, 16), (-116, 18),
                              (-FRONT, 18), (-95, 23+math.tan(a))])
    part -= cylinder(x, -110, 15.99, 1.7, 2.02)
    for row in (-1, 1):
        support = box(138.5, 144.2, 18, 30, -21.2, 0)
        support += box(138.25, 140, 20, 39.797470349551496, -21, -.25)
        support += box(130, 140, 38.297470349551496, 39.797470349551496, -21, -.25)
        support -= box(136, 146, 19.9, 28.1, -21.2, -18)
        support -= cylinder(140.7, 24, -18.1, 1.25, 7.1)
        support -= cylinder(140.7, 24, -60, 4, 39)
        part += place(support, -1 if left else 1, row)
    edges = top_edges(part, exterior, u)
    return fillet(edges, .8) if edges else part


def build():
    data, _, b19, proof, moves = load_data()
    parts = {'PANEL_'+i: panel(i, data, b19, proof, moves) for i in AXES}
    parts.update({i: roof(i) for i in ('D02L', 'D02R')})
    for key, part in parts.items():
        part.label = key + ' B26-INTEGRATED-01 review'
    return parts
