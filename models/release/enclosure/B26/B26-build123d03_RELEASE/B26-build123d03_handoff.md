# B26-build123d03 — approved model, mechanical trial handoff

**Scope: APPROVED model and bounded STEP numerical exception for an unpowered mechanical trial. Not a production, physical-fit, strength, electrical or thermal approval.** The engineer approved [drawing B26-FADER-01](../../../../docs/APPROVALS.md#engineer-approval-of-b26-fader-01-drawing) and [model B26-build123d03 and the P01 STEP exception](../../../../docs/APPROVALS.md#engineer-approval-of-b26-build123d03-model-and-step-numerical-exception). Older review and preflight documents contain historical pending-approval labels; the later approval record controls. The B26-build123d02 fader STL set remains on hold and is not part of this release.

## Files and quantities

- [STL parts and per-file verification manifest](STL/B26-build123d03_STL_manifest.json): 36 distinct files, 155 printed occurrences, excluding purchased/reference hardware. STL is unitless; interpret coordinates as **mm**. File axes are assembly axes translated to positive coordinates, not approved print orientations.
- [Complete represented assembly STEP](STEP/B26-build123d03-trial-assembly.step) and [assembly evidence](STEP/assembly-evidence.json). Some purchased/electronic bodies are incomplete references, not complete vendor geometry. PCB mounts without reliable inputs were deliberately omitted; see [open work](../../../../TODO.md).
- [Editable source package](SOURCE/) and [52-file source hash manifest](SOURCE/source-manifest.json); [rebuild evidence](SOURCE/rebuild-evidence.json). Nine inherited cap definitions are meshes, not editable feature histories. STEP also does not preserve Python feature history.
- [Assembled actual-model view](VIEWS/DJC_Enclosure_Rev_B26_build123d03_isometric_build123d-view.png), [fader detail](VIEWS/DJC_Enclosure_Rev_B26_build123d03_fader-detail_build123d-view.png), and [view hashes](VIEWS/views-manifest.json).

The manifest identifies the exact STL filename, quantity and SHA-256 for each part. BOM quantities are:

| Part ID | Quantity |
|---|---:|
| C01, C02, C03, C04, C05, C06 | 1 each |
| PANEL_R01, PANEL_R03, PANEL_R04, PANEL_R05, PANEL_R06, PANEL_R07 | 1 each |
| D02L, D02R | 1 each |
| C07_bridge | 16 |
| button_retainer | 30 |
| pot_retainer | 13 |
| fader_retainer | 10 |
| encoder_retainer | 1 |
| display_toe | 4 |
| jog_P01_rotor, jog_P02_carrier, jog_P04_collar, jog_P07_collar, jog_sensor_plate | 2 each |
| jog_cover, jog_toe | 4 each |
| CAP_B | 12 |
| CAP_T | 6 |
| CAP_P | 13 |
| CAP_F | 4 |
| CAP_C, CAP_E | 1 each |
| CAP-CUE40, CAP-PP40 | 2 each |
| CAP-HC40 | 8 |

PETG is selected for the enclosure parts. Material for jogs and inherited cap meshes is not confirmed. Orientations, supports, brim, slicer settings and fit calibration remain to be determined; the export is not a ready-to-print plate.

## Export and geometry checks

Every actual released STL was decoded and checked for exact shared-edge closure, winding, triangle degeneracy, stored normals and one connected component; its checksum and measured geometry match the checked working mesh. No self-intersection or vertex-link manifold test was performed. Build123d-produced meshes use linear deflection 0.005 mm and angular deflection 5 degrees; inherited cap mesh tessellation is unknown. A mesh tolerance below the nominal 0.025 mm thread clearance does not prove a printable or functional thread.

Sections of the actual released C04/C05/C06 meshes at CAD Z 14.123 mm and two transverse offsets checked all five fader cups: F01–F04 pilot axes at ±33.95 mm, F05 at ±33.80 mm, with bosses flush with the end-wall inner faces; the sampled section tolerance was 0.0051 mm. Ten matching fader retainers are included. This is sampled geometry, not a physical fit test.

The approved model evaluation covered 395 valid non-empty BRep solids, 640 sampled fader surface/void probes, and 5,910 changed-part/assembly bounds pairs, followed by 55 BRep intersection operations. The ten positive intersections are the intended nominal screw-to-pilot engagements; no other positive intersections were found within that limited screen. Fader post-to-body gaps are 1.75 mm for F01–F04 and 1.60 mm for F05 against incomplete nominal references, not measured hardware. See the [model review](../BUILD123D03/DJC_Enclosure_Rev_B26_build123d03_review.md) for excluded pairs, assumptions and detailed evidence.

Six shells and ten changed retainer occurrences fit a nominal 250 mm cube in their current assembly axes; the largest measured axis was 220 mm. The engineer reports a 256 × 256 mm P2S bed, but chosen print orientations, usable margins, supports and brim were not checked. Do not scale parts to fit.

## STEP exception

The [final STEP fader check](STEP/fader-evidence.json) separately reopened the released STEP and passed 640 pilot/countersink probes across the ten fader ends, including the new axes, retainer alignment and sampled flush-wall/old-axis checks. The assembly evidence's `FADERS_PENDING` label records the earlier assembly check; the later fader evidence completes this scoped check without changing the STEP.

The released STEP was reopened: all 476 represented leaves match their named source counterparts and placements within the stated comparison checks; it contains 444 solid leaves and 32 non-solid reference leaves, including 49 converted faceted cap occurrences. Maximum bounding-coordinate difference was about 1e-7 mm. **The strict default-volume comparison still fails** for both P01 rotors: 0.641091522 mm³ per rotor against the 0.0001 mm³ threshold. This is the specifically accepted bounded exception, not a passed strict check.

For each rotor, adaptive integration at 1e-8 differed by 0.000001609 mm³; both directed BRep cuts returned zero volume; 264 radial phase samples and independently generated 0.005 mm / 5° meshes were compared. These checks strongly indicate a numerical integration effect after cone reparameterization, but do not prove exact surface equality. SHA-256 of the released STEP: `be226639517a5e5042979a5c78039f82f4e40c89f9d92193f8bd150e7c0c258b`. The STEP is a trial representation, not a guarantee of purchased-part completeness or physical assembly.

## Source and environment

Python 3.11.15; build123d `0.13.1.dev254+gc49a0493a`; cadquery-ocp-novtk `8.0.1.1.0`; ocp_viewer `1.2.0`; numpy 2.4.6; scipy 1.17.1. The existing repository `.venv` is an external prerequisite and is not included. All 52 packaged source and asset hashes were checked; the packaged model was rebuilt with that environment and all 476 leaves compared, with zero reported bounding-coordinate and volume differences. Bounds and volumes alone do not prove exact shape equivalence. The imported legacy cap meshes have no parametric feature history.

From the repository root, with the same environment, start the locally bound viewer and open `http://127.0.0.1:3949`:

```sh
.venv/bin/python -m ocp_viewer --host 127.0.0.1 --port 3949
```

In another terminal, send the packaged model:

```sh
.venv/bin/python -B models/enclosure/B26/B26-build123d03_RELEASE/SOURCE/models/enclosure/B26/BUILD123D03/DJC_Enclosure_Rev_B26_build123d03.py
```

## Remaining physical and safety work

Verify fader insertion and travel, actual screw seating and pilot/thread formation with coupons, jog rotation and threaded joint calibration, joints and fastener strength, layer adhesion and support removal with the selected orientation/material. Establish measurable acceptance criteria before claiming physical verification. Obtain real board-hole dimensions and design permanent mounts and DAC retention; hot glue is a temporary test proposal, not a verified structural or electrical solution. Actual cable, connector, tool access, mains insulation, thermal performance and complete purchased-part geometry remain unchecked. The approved geometry and trial exports do not authorize powered operation or certify manufacturing readiness.
