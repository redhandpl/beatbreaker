# REV_A documentation reconstruction review

**Status: CHANGES REQUIRED — release blocked pending resolution or explicit scoped engineering decision.** B26-CONSOLIDATED-02 was approved for control reconstruction, not as proof of standalone completeness or as a new model approval. `REV_A` is the requested release-package name, not a new geometry revision. No new final STL or STEP was created.

## Inputs and environment

- Drawing: `schematics/work/enclosure/B26-CONSOLIDATED-02/B26_CONSOLIDATED_02_complete_DRAFT.pdf`, SHA-256 `35ab5a40ae0051ec4080cb6cfb287782c482859d1a6f666e9a8b0ccca00226c2`, plus the approved seven JSON data files recorded in `B26_CONSOLIDATED_02_validation_DRAFT.json`.
- Reference STEP: `models/release/enclosure/B26/B26-build123d03_RELEASE/STEP/B26-build123d03-trial-assembly.step`, SHA-256 `be226639517a5e5042979a5c78039f82f4e40c89f9d92193f8bd150e7c0c258b`. Evidence reference: `STEP/assembly-evidence.json`.
- Existing `.venv` Python 3.11.15, build123d `0.13.1.dev254+gc49a0493a`, cadquery-ocp-novtk `8.0.1.1.0`, ocp_viewer `1.2.0`, numpy `2.4.6`, scipy `1.17.1`.
- Construction scripts use the drawing schedules and JSON; the packaged source model was not used as a source of missing construction operations. Reference STEP and its evidence were used for matching and comparison. The reconstructed control geometry is not an approved deliverable.

## Results

- **Enclosure, roof, bridges and retainers:** 82 printed occurrences covered: six shells, 16 bridges, 54 retainer solids, two roof halves, four display toes. Of these, 80 met valid, two-direction Boolean and bounds/volume comparison criteria. C03 and C05 have unresolved reverse Boolean failures; see below. Bounds threshold 0.00001 mm; volume and directed-difference thresholds 0.0001 mm³. `shell_evidence.json` and `shell_evaluator.py` record the detailed evidence.
- **Six front panels:** six valid single solids, each checked against its placed STEP counterpart; both directed Boolean differences returned zero volume. `panel_evidence.json` records the panel data and thresholds. A first R06 mismatch was traced to an evaluator omission of the specified exterior fillet; the evaluator was corrected, and its residual is preserved in `panel_initial_R06_residual.json`.
- **Caps:** nine meshes reproduced the documented hashes and were byte-identical to the released STL files; 49 placements matched recorded release STEP placement evidence. Cap occurrences were not compared as direct STEP BRep operands. Nine faceted definitions do not imply parametric feature histories.
- **Jogs:** all 18 printed occurrences rebuilt and checked against STEP; each operand was a valid single solid and all 36 directed cuts returned zero volume. The 16 non-P01 volume differences were below 5.2e-10 mm³. Both P01 strict volume comparisons failed by approximately 0.641091522 mm³ each against 0.0001 mm³; the earlier bounded exception for the unpowered mechanical trial remains in force. Zero cut volume does not prove exact surface identity. 128 sampled T30 phase probes matched the ideal expectation for both reconstruction and STEP, with 1e-6 mm point-classification tolerance. This is sampled phase coverage, not continuous-motion or physical-fit certification. See `jog_evidence.json`.
- **Incomplete purchased references:** 90 of 90 bounds and 57 analytic solid volumes agree with the released STEP evidence within 2e-6 mm and 1e-5 mm³ respectively; this is a bounds/volume screen, not an independent BRep equality check. See `reference_evidence.json`. The 197 enclosure fastener reference bodies and 34 jog purchased-reference bodies were not independently reconstructed or compared in this work.

## Blocking C03 / C05 Boolean results

Both reconstructed and STEP operands are valid, single solids and have matching face counts; their volume deltas are approximately 2.2e-9 and 2.0e-8 mm³. Reconstruction-minus-STEP is a valid empty cut, but STEP-minus-reconstruction returns an **invalid** result for each. Intersection results contradict each other depending on operand order. Increasing the numerical fuzzy tolerance to 1e-7 and 1e-6 mm did not resolve this. OCCT operation completion was reported, but warning/error flags were unavailable; an invalid result is not an empty cut and its reported volume is not evidence of real missing material.

For each shell, 4,992 fixed-grid occupancy points agreed at 1e-6 mm classifier tolerance, and 100 tessellation vertices per direction were checked for point-to-surface distance. These are sampled corroboration only; they do not prove exact equality. `shell_diagnostics.json` and `shell_fuzzy.json` preserve operand IDs, thresholds, measured values and operation validity. Do not relabel strict comparison as passed.

## Visual scope

The local standalone ocp_viewer was bound to 127.0.0.1:4059. A browser actually displayed nine reconstructed local jog solids. [Assembled jog](B26_CONSOLIDATED_02_CHECK_jog_build123d-view.png) and [carrier with the rotor hidden](B26_CONSOLIDATED_02_CHECK_jog_open_build123d-view.png) were saved and opened; the rotor visibility was restored. These are only jog review images, not a complete assembly review or model approval. The historical 02 concept PNG was absent when drawing approval was recorded; it was not silently restored.

## Executed commands and evidence

From repository root, isolated task scripts were executed with `.venv/bin/python -I -B`: `tmp/rev-a-shell/evaluate-checked.py`, `diagnose-shells.py`, `fuzzy-shells.py`, `tmp/rev-a-panel/evaluate.py`, and `tmp/rev-a-jog/reconstruct.py`. `ruby tmp/rev-a-reference/check.rb` screened reference bounds/volumes; `.venv/bin/python -I -B tmp/rev-a-viewer/show_jog.py` sent the actual reconstructed jog to the local viewer. Scripts and resulting JSON have been preserved in this directory with explicit filenames. They retain the original `tmp/rev-a-*` input/output paths and refuse to overwrite results; replay requires recreating the task-local layout and selecting fresh output names. No network access or installation was required.

For replay, `shell_evaluator.py`, `shell_diagnostics.py` and `shell_fuzzy.py` correspond to `tmp/rev-a-shell/evaluate-checked.py`, `diagnose-shells.py` and `fuzzy-shells.py`; `panel_evaluator.py`, `jog_evaluator.py`, `reference_evaluator.rb`, and `show_jog.py` correspond to the other commands above.

## Limits and next action

Do not publish REV_A as a complete verified documentation release until the C03/C05 comparison is resolved or the responsible engineer explicitly accepts a bounded, trial-only exception with the missing strict evidence disclosed. Preserve the accepted drawing snapshots. No claims of physical fit, strength, print orientation, printer margins, complete purchased geometry, wiring, electrical or thermal safety, or production readiness are made. No physical tests were performed.
