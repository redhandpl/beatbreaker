"""B24-build123d01 working assembly, millimetres; no fabrication exports.

Printed shell, panels, bridges, retainers and display toes are modeled with
build123d. The explicitly approved legacy cap meshes remain immutable display
references. Purchased components and fasteners are incomplete nominal references.
"""
from build123d import Compound

import bridges
import caps
import controls
import display_toes
import hardware
import panels
import reference_controls
import reference_equipment
import shell


def build():
    groups = {
        "Shells - printed PETG": shell.build(),
        "Panels and roof - printed PETG": panels.build(),
        "Bridges - printed PETG": bridges.build(),
        "Control retainers - printed PETG": controls.build_retainers(),
        "Display toes - printed PETG": display_toes.build(),
        "Caps - retained mesh references": caps.build(),
        "Control envelopes and tip planes - incomplete references": reference_controls.build(),
        "Equipment and connector envelopes - incomplete references": reference_equipment.build(),
        "Fasteners - nominal reference only": hardware.build(),
    }
    expected = (6, 8, 14, 54, 4, 49, 79, 11, 199)
    if tuple(map(len, groups.values())) != expected:
        raise ValueError(f"Unexpected B24 part counts: {[(k, len(v)) for k, v in groups.items()]}")
    return groups


def show_assembly(groups):
    from ocp_viewer import Camera, show

    assemblies = [Compound(label=name, children=list(parts.values())) for name, parts in groups.items()]
    show(*assemblies, names=list(groups), reset_camera=Camera.ISO, port=3939)


if __name__ == "__main__":
    assembly = build()
    print("B24-build123d01 DRAFT / NOT APPROVED:", [(name, len(parts)) for name, parts in assembly.items()], flush=True)
    show_assembly(assembly)
