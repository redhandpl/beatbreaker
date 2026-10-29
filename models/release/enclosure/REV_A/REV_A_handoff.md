# beatbreaker — REV_A mechanical-trial handoff

**APPROVED — scoped, unpowered mechanical trial only, subject to the two recorded bounded exceptions.** `REV_A` names this release package; the retained drawing revision is B26-CONSOLIDATED-02 and the already approved model revision is B26-build123d03. No geometry was changed and no new STL or STEP was generated for this packaging. Strict C03/C05 and P01 comparisons did not pass; the accepted exceptions are not a claim of exact surface equality, physical fitness or production readiness.

## Deliverables

- [Consolidated 70-page drawing and companion JSON](../../../../schematics/release/enclosure/REV_A/beatbreaker_REV_A_drawing.pdf). Keep the `shell/`, `panel/`, `jog/`, and `reference_geometry_DRAFT.json` data with the PDF. Page 1 is the REV_A release cover; the 69 original approved B26-CONSOLIDATED-02 pages retain their historical DRAFT/NOT APPROVED labels and internal page numbers. Read their index with a +1 page offset. The cover and approval register record later decisions without altering the source drawing snapshot.
- [Printed STL files and BOM](STL/), [complete represented assembly STEP](STEP/B26-build123d03-trial-assembly.step), and [editable build123d Python source and required local assets](SOURCE/). These are byte-for-byte copies of the approved B26-build123d03 release; their original revision-bearing names and embedded historical paths are intentionally preserved.
- [Actual-model isometric view](VIEWS/DJC_Enclosure_Rev_B26_build123d03_isometric_build123d-view.png) and [fader detail](VIEWS/DJC_Enclosure_Rev_B26_build123d03_fader-detail_build123d-view.png). The [separate concept](../../../../schematics/release/enclosure/REV_A/beatbreaker_REV_A_DRAFT_concept.png) is illustrative, not an actual model view or dimensional source.
- [Independent documentation reconstruction report](VALIDATION/REV_A_reconstruction_review.md), [shell diagnostics](VALIDATION/shell_diagnostics.json), [fuzzy comparison](VALIDATION/shell_fuzzy.json), [mesh verification](VALIDATION/REV_A_mesh_check.json), [STEP reopen](VALIDATION/REV_A_step_check.json), and [source rebuild](VALIDATION/REV_A_rebuild_check.json). The reconstruction report predates the later [accepted C03/C05 trial exception](../../../../docs/APPROVALS.md#engineer-accepts-bounded-c03c05-reconstruction-exception); its blocked status is historical and the exception does not make the comparison pass.

## Printed parts

36 distinct STL definitions, 155 printed occurrences; exact filenames, quantities and checksums are in [the STL manifest](STL/B26-build123d03_STL_manifest.json). All STL coordinates are unitless and must be interpreted in millimetres.

| Part | Quantity |
|---|---:|
| C01–C06; PANEL_R01/R03/R04/R05/R06/R07; D02L/D02R | 1 each |
| C07 bridge | 16 |
| Button / potentiometer / fader / encoder retainers | 30 / 13 / 10 / 1 |
| Display toe | 4 |
| Jog P01, P02, P04, P07, sensor plate | 2 each |
| Jog cover / jog toe | 4 each |
| CAP_B / CAP_T / CAP_P / CAP_F | 12 / 6 / 13 / 4 |
| CAP_C / CAP_E / CAP-CUE40 / CAP-PP40 / CAP-HC40 | 1 / 1 / 2 / 2 / 8 |

PETG is selected for enclosure parts. Jog and cap materials, intended print orientations, supports, brim/raft, actual printer margins and fit calibration are TBD. The retained report screens parts against a conservative nominal 250 × 250 × 250 mm volume; freshly checked STL bounds have maximum single axis 220 mm in their current assembly axes, **without** supports, brim, margins or an approved print orientation. The engineer reports a Bambu P2S 256 × 256 mm bed and 0.4 mm nozzle; usable area and layer settings are not established. Do not scale parts to fit.

## Executed checks and bounded exceptions

- All 36 copied STL files were decoded and SHA-256 matched their approved manifest. Exact-vertex edge checks found one edge-connected component per file, no boundary/nonmanifold edges, inconsistent winding, degenerate triangles, zero stored normals or opposed stored normals. A 1e-12 mm² cross-product magnitude threshold was used for degeneracy and -1e-5 cosine for opposed normals. No self-intersection or vertex-link manifold test was performed. Build123d-produced meshes used 0.005 mm linear / 5° angular tessellation; inherited cap tessellation is unknown. These settings do not prove printable thread fit.
- The copied STEP was reopened: 11 groups, 476 leaves, 444 solid and 32 non-solid reference leaves. Per-occurrence bounds, volume, validity and solid counts matched its recorded released STEP evidence; maximum bound and repeat-volume differences were zero in this run. This does not prove exact surfaces or physical completeness. Both P01 source-to-STEP strict default-volume comparisons remain failed by approximately 0.641091522 mm³ per rotor; only the previously accepted bounded trial exception applies.
- Independent reconstruction from the consolidated drawing compared six panels, 18 printed jog occurrences, and 82 shell/roof/bridge/retainer/toe occurrences. All six panels had zero directed-cut volumes. Of 82 shell-related bodies, 80 met the listed strict criteria; C03/C05 reverse cuts were invalid, with order-dependent intersection results. Their 4,992 occupancy points per shell and 100 surface samples per direction agreed, but these are not continuous proof. The engineer accepted that disclosed exception only for this unpowered trial.
- The rebuilt jogs produced 36 zero-volume directed cuts and 128 matching sampled T30 phase probes. Both P01 strict volume comparisons remain failed; neither sampled points nor zero cuts prove exact surface identity. Nine cap meshes reproduce the original bytes, while all 49 cap placements were compared against recorded STEP placement evidence rather than direct STEP Boolean geometry.
- All 52 source/asset hashes matched, and the delivered source rebuilt 476 named leaves; non-mesh validity, bounds, volumes and solid counts matched recorded evidence within the declared thresholds. **All 49 imported legacy caps are triangulation-only display Faces: they reported invalid BRep, zero solids and zero BRep volume.** This expected reference representation is not editable cap geometry; the nine STL meshes were separately checked. The STEP package contains converted faceted cap occurrences.
- 90 purchased-control/equipment reference bounds and 57 analytic volumes were screened against released STEP evidence only. The 197 enclosure fastener and 34 jog purchased-reference bodies were not independently reconstructed during this documentation check. Full purchased-part geometry and connected wiring remain incomplete.

## Rebuilding and review

External prerequisite: the existing approved `.venv` with Python 3.11.15, build123d `0.13.1.dev254+gc49a0493a`, cadquery-ocp-novtk `8.0.1.1.0`, ocp_viewer `1.2.0`, numpy `2.4.6`, scipy `1.17.1`. From the repository root, this rebuilds the source assembly without a viewer or export:

```sh
.venv/bin/python -I -B -c 'import runpy,sys; p="models/release/enclosure/REV_A/SOURCE/models/enclosure/B26/BUILD123D03/DJC_Enclosure_Rev_B26_build123d03.py"; sys.path.insert(0,p.rsplit("/",1)[0]); m=runpy.run_path(p,run_name="rev_a_rebuild"); print({k:len(v) for k,v in m["build"]().items()})'
```

The retained source's `__main__` uses the standalone viewer at local port 3949; its historical `MODEL NOT APPROVED` messages describe the original review state and are superseded only by the recorded B26-build123d03 model approval. The STEP is an interchange representation, not Python feature history. Legacy cap STL geometry is not parametric.

## Physical and safety work

Establish measurable pass criteria and perform fader insertion/travel and screw-seat tests, print-fit coupons and pilot/thread checks, jog rotation and thread calibration, bearing and magnet retention checks, joint strength and layer-adhesion trials. Check cable routing, connector/tool access, board fixation, electrical insulation, thermal behavior and the complete actual purchased parts before any powered use. U1–U4 board mounts without trustworthy dimensions remain intentionally omitted; temporary hot glue is not a qualified structural or electrical solution. No physical tests were performed as part of this release.
