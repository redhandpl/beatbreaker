# Artifact Register — Current Release

This register describes the published mechanical release, not an engineering approval grant. See the [product design](../DESIGN.md), the [work queue](../TODO.md), the [approval register](APPROVALS.md) and [print settings](PRINT_SETTINGS.md).

## Current REV_B trial and artifact layout

REV_B is the current release for an **unpowered mechanical trial only**. The engineer accepted the controller holders and authorized the complete geometry11 update for that trial. The jogs do not press. Neither publication nor computational verification qualifies the design for powered use, production or physical safety.

### Artifact relocation map

Older path names are historical and may require locally retained archives. Relocation does not grant or revoke a scoped approval.

| Former release path | Published release path |
|---|---|
| `models/release/enclosure/REV_B/` | `models/REV_B/` |
| `schematics/release/enclosure/REV_B/` | `schematics/REV_B/` |

### REV_B — minimal standalone mechanical release, approved and verified

- [Complete 341-page drawing](../schematics/REV_B/beatbreaker_REV_B_drawing.pdf)
- [Standalone editable Python](../models/REV_B/beatbreaker_REV_B.py)
- [Consolidated validation, BOM, environment, hashes and handoff](../models/REV_B/beatbreaker_REV_B_validation.json)
- [37 STL definitions](../models/REV_B/STL/) for 169 printed pieces
- [Complete assembly STEP](../models/REV_B/beatbreaker_REV_B_assembly.step)
- Actual-model views: [isometric](../models/REV_B/beatbreaker_REV_B_isometric_build123d-view.png) and [holder inspection](../models/REV_B/beatbreaker_REV_B_holders_build123d-view.png)

The minimal release contains 43 files: one Python source, 37 STLs, one assembly STEP, two PNGs, one validation JSON and one drawing PDF. It has no historical drawing appendices, runtime geometry-input files, source tree or separate manifest/report. C04 contains the ESP/U2 holders; C06 contains the U3/mux holders.

Final-PDF-only reconstruction and independent source replay matched all 565 accepted geometry11 occurrences using complete oriented boundary/mesh signatures. All 37 STLs passed recorded topology, normals and bounds checks and the nominal 250 mm screen. The assembly STEP reopened with 13 groups, 565 leaves, 533 solid leaves and 32 datums. The [validation JSON](../models/REV_B/beatbreaker_REV_B_validation.json) records the checks, hashes, differences and their scope.

**Limits:** The original 24 sharp-bearing-reference failures and the separate selected-SKF nominal compatibility pass remain distinct; the latter does not erase the former. Purchased geometry is incomplete and nine cap meshes have no recovered analytic history. PCF/mux require flat undersides, no headers and top-only wires. Print orientation, support removal and calibration, physical retention and strength, PETG creep, and electrical and thermal qualification remain open. No physical fit, manufacturing, electrical safety or production qualification is implied.
