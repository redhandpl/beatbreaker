import ast
import hashlib
from pathlib import Path
from build123d import Axis, Edge, Face, Plane, Shell, Solid, Wire
from ocp_viewer import show
import math

source = Path('tmp/rev-a-jog/reconstruct.py')
expected = {'C', 'K', 'B', 'RB', 'xy', 'union', 'sub', 'ridge', 'profile', 'rotor', 'carrier', 'collar', 'cover', 'plate', 'toe'}
raw = source.read_text()
tree = ast.parse(raw, filename=str(source))
functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in expected]
if {node.name for node in functions} != expected:
    raise RuntimeError('Reconstruction functions missing')
exec(compile(ast.Module(body=functions, type_ignores=[]), str(source), 'exec'))
male = ridge(0)
female = ridge(0.05)
t = toe()
parts = [rotor(male), carrier(), cover(19.5, 21, True), cover(4, 5.5, False), plate(), t, t.rotate(Axis.Z, 180), collar(4, 5.5, female), collar(3, 4, female)]
if not all(part.is_valid and len(part.solids()) == 1 for part in parts):
    raise RuntimeError('Invalid viewer reconstruction')
names = ['CHECK-02 P01 rotor', 'CHECK-02 P02 carrier', 'CHECK-02 P05 cover', 'CHECK-02 P06 cover', 'CHECK-02 sensor plate', 'CHECK-02 P08 right', 'CHECK-02 P08 left', 'CHECK-02 P04 collar', 'CHECK-02 P07 collar']
show(*parts, names=names, port=4059, reset_camera='reset')
print('Showing B26-CONSOLIDATED-02 reconstructed jog; 9 printed local parts; script SHA-256', hashlib.sha256(source.read_bytes()).hexdigest())
