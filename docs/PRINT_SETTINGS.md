# Print settings

## Variant B — 4 mm PETG lower enclosure

**Status: selected starting recipe for an unpowered trial; applied slicer settings and physical results are not verified.**

Source: discussion on 2026-10-31 about stiffening the 4 mm enclosure floor in Bambu Studio. The engineer selected variant B with “Zacznę od B”. Recorded here on 2026-11-02. This is a settings note, not an importable Bambu Studio preset or a qualified manufacturing profile.

### Basis and scope

- Printer: Bambu Lab P2S; nozzle: 0.4 mm.
- Material: PETG; assumed constant layer height: **0.20 mm**.
- Scope: the **4 mm lower-enclosure floor**, not a default for every part, jog, cap or spring.
- Preserve the project's conservative **250 × 250 × 250 mm** print screen. Usable margins, orientation, supports and calibration remain separate checks.

### Bambu Studio settings

| Setting | Variant B |
|---|---|
| Wall loops | **3** |
| Top surface pattern | Monotonic |
| Top shell layers | **6** |
| Top shell thickness | **1.2 mm** |
| Bottom surface pattern | Monotonic |
| Bottom shell layers | **6** |
| Bottom shell thickness | **1.2 mm** |
| Internal solid infill pattern | Rectilinear |
| Sparse infill density | **50%** |
| Sparse infill pattern | **Gyroid** |
| Fill multiline | 1 |
| Embedding the wall into the infill | Disabled |
| Top paint penetration layers | Keep the existing profile value; no new numeric value selected |
| Bottom paint penetration layers | Keep the existing profile value; no new numeric value selected |

At a nominal 0.20 mm layer height, a flat 4 mm floor has about 20 layers. Six full layers on each side leave approximately **1.6 mm / eight layers of core**. First-layer height, local geometry and slicer rules can change the actual result; inspect the sliced layers rather than assuming this division everywhere.

### Before printing

1. Verify the actual PETG filament/process profile and 0.20 mm layer height. Temperatures, speeds, cooling, flow and pressure-advance calibration were not selected in this discussion; do not invent them from this note.
2. Inspect the floor centre, lap joints, holes and feet in the layer preview. Confirm the solid shells, chosen infill pattern/density and continuous wall paths. Check orientation, supports and support removal independently, including the integral PCB-holder cantilevers in model11; these recipes do not establish support-free printing.
3. Review estimated material/time. Assess stiffness on the assembled lower shell under an engineer-agreed support/load arrangement; infill selection alone does not prove safe lifting, joint strength or adequate rigidity.

No Bambu Studio profile, 3MF, sliced preview or physical result was verified when recording this recipe. Drawing/model approvals and existing STL validation do not qualify these print settings.

## Variants A and C — optional comparisons

**Status: candidates to test; neither replaces the selected starting variant B.** Both were proposed in the same 2026-10-31 discussion. Inherit all variant B assumptions, settings and checks above, changing only these two infill fields:

| Variant | Sparse infill density | Sparse infill pattern | Intended comparison |
|---|---|---|---|
| A — lighter | **25%** | **Gyroid** | Lower-density core with the same full outer shells; compare material use and assembled-floor deflection. Adequate rigidity is not established. |
| C — nominally solid | **100%** | **Rectilinear** | Full-fill reference; inspect dense paths in the preview. It may increase mass, material use and print time, without guaranteeing gap-free extrusion or adequate stiffness. |

Keep geometry, orientation, filament and all other process settings unchanged when comparing variants. Record slicer material/time estimates and compare the assembled lower shell under the same support/load arrangement. Thin lap regions can become fully solid even with partial infill. Neither alternative has a verified saved slicer profile, sliced preview or physical result.
