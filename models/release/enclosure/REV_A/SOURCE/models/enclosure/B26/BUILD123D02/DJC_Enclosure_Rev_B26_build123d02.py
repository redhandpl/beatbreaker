"""B26-build123d02 review assembly. No manufacturing exports or model approval.

Build123d geometry is in millimetres, in global CAD coordinates (X,-Y,Z).
Legacy cap meshes and incomplete purchased bodies are labelled references.
"""
from pathlib import Path
import sys

from build123d import Compound, Pos

BASELINE = Path(__file__).resolve().parents[2] / "B24" / "BUILD123D"
sys.path.insert(0, str(BASELINE))

import b26_controls
import b26_equipment
import b26_fasteners
import b26_panels
import b26_shell
import display_toes
import f13_jog


def build(appearance_only=False):
    jog = f13_jog.build(appearance_only=appearance_only)
    groups = {
        "Lower shells - printed PETG": b26_shell.build(),
        "Flat panels and screen roof - printed PETG": b26_panels.build(),
        "Shell bridges - printed PETG": b26_shell.build_bridges(),
        "Control retainers - printed PETG": b26_controls.build_retainers(),
        "Display toes - printed PETG": {name: Pos(0, 0, 5) * shape for name, shape in display_toes.build().items()},
        "Control caps - legacy mesh references": b26_controls.build_caps(),
        "Controls - incomplete purchased references": b26_controls.build_references(),
        "Equipment - incomplete purchased references": b26_equipment.build(),
        "Enclosure fasteners - nominal purchased references": b26_fasteners.build(),
        "Static jogs - printed": jog["printed"],
        "Static jogs - purchased references": jog["reference"],
    }
    return groups


def show_assembly(groups, inspect_panels=False):
    from ocp_viewer import Camera, show
    visible = {}
    palette = {}
    colors = {
        "Lower shells - printed PETG": "#365340",
        "Flat panels and screen roof - printed PETG": "#c6b49b",
        "Shell bridges - printed PETG": "#365340",
        "Control retainers - printed PETG": "#365340",
        "Display toes - printed PETG": "#365340",
        "Controls - incomplete purchased references": "#8a8a8a",
        "Equipment - incomplete purchased references": "#8a8a8a",
        "Enclosure fasteners - nominal purchased references": "#8a8a8a",
        "Static jogs - printed": "#594337",
        "Static jogs - purchased references": "#8a8a8a",
    }
    for group_name, parts in groups.items():
        if inspect_panels and group_name == "Static jogs - printed":
            parts = {name: part for name, part in parts.items() if "P01" not in name}
        if group_name == "Flat panels and screen roof - printed PETG":
            roof = {k: v for k, v in parts.items() if k.startswith("D02")}
            parts = {k: v for k, v in parts.items() if k not in roof}
            visible["Screen roof - printed PETG"] = Compound(label="Screen roof", children=list(roof.values()))
            palette["Screen roof - printed PETG"] = "#365340"
        if group_name == "Control caps - legacy mesh references":
            red = {k: v for k, v in parts.items() if k.startswith("F") or k[:3] in {f"B{i:02d}" for i in range(11, 23)}}
            parts = {k: v for k, v in parts.items() if k not in red}
            visible["Red caps - legacy mesh references"] = Compound(label="Red caps", children=list(red.values()))
            palette["Red caps - legacy mesh references"] = "#b63b39"
            palette[group_name] = "#594337"
        else:
            palette[group_name] = colors[group_name]
        if parts:
            visible[group_name] = Compound(label=group_name, children=list(parts.values()))
    show(*visible.values(), names=list(visible), colors=[palette[name] for name in visible],
         reset_camera=Camera.TOP if inspect_panels else Camera.ISO, port=3949)


if __name__ == "__main__":
    appearance_only = "--appearance-only" in sys.argv
    assembly = build(appearance_only=appearance_only)
    print("B26-build123d02 APPEARANCE ONLY / MODEL NOT APPROVED:" if appearance_only else "B26-build123d02 REVIEW / MODEL NOT APPROVED:",
          [(name, len(parts)) for name, parts in assembly.items()], flush=True)
    show_assembly(assembly, inspect_panels="--panels" in sys.argv)
