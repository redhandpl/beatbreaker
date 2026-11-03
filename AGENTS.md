# Agent guide

## Project and records

beatbreaker is a two-deck DJ/MIDI controller: an ESP32-S3 reads controls and drives indicators, and a Raspberry Pi 4 runs Mixxx. The enclosure and jog mechanisms are FDM/FFF prototypes.

- `DESIGN.md`: product facts and decisions; `TODO.md`: the only active work queue.
- `docs/APPROVALS.md`: the engineer's named decisions and their scope. `docs/ARTIFACTS.md`: historical artifact index. `docs/history/SESSION-HANDOFF.md` is dated context, not a current task list.
- The current mechanical release is [REV_B](models/REV_B/beatbreaker_REV_B_validation.json): an unpowered trial only. Use its [complete drawing](schematics/REV_B/beatbreaker_REV_B_drawing.pdf), [standalone build123d source](models/REV_B/beatbreaker_REV_B.py) and consolidated validation/BOM/handoff JSON as the entry point; older releases and historical "current" statements are not the current release.
- Discuss work with the engineer in Polish; write code and project documentation in English.

## Artifact layout and migration

- `work/models/<subsystem>/<revision>/` and `work/schematics/<subsystem>/<revision>/` are the only destinations for new working CAD sources, drafts, studies and validation files. Existing historical inputs and approved snapshots retained there are not current release deliveries; relocation does not revoke their scoped approvals.
- `models/<release>/` and `schematics/<release>/` are release-only destinations. They currently contain only `REV_B/`; do not put working files, preparation packages or incremental amendments there.
- The preserved REV_A package is under `work/models/enclosure/REV_A/` with drawings under `work/schematics/enclosure/REV_A/`. It retains approved B26-CONSOLIDATED-02/B26-build123d03 geometry and its self-contained `SOURCE/` layout.
- Historical `models/work/` and `schematics/work/` paths map to `work/models/` and `work/schematics/`. Former `models/release/enclosure/REV_B/` and `schematics/release/enclosure/REV_B/` map to `models/REV_B/` and `schematics/REV_B/`; use the [current relocation map](docs/ARTIFACTS.md#artifact-relocation-map) for other verified historical relocations. Never rewrite frozen source, drawing, JSON or manifest bytes/hashes to fix stored paths. Inspect dependencies and use non-destructive staging for older generators.
- `.gitignore` excludes `work/`, `tmp/` and `docs/history/`. Their locally present contents are not necessarily available in a clone; preserve approved local artifacts and distinguish an absent source from an invalid approval.
- Keep supplied references in `elements/`; leave `old_case/`, existing SVGs and legacy directories intact. Do not create SVG deliverables or alternate-format copies of drawings.

## Engineering and approval

- The responsible engineer alone decides dimensions and approves each named drawing and model revision. Do not infer dimensions from pixels, silently choose fits, or treat a concept, folder name, export or absence of objection as approval. Record sourced inputs and explicitly delegated choices; mark critical missing information `TBD` and ask grouped questions.
- For new geometry: dimensioned PDF and separate illustrative concept, explicit approval of the named drawing, build123d model, actual-model viewer review and geometric validation, explicit approval of the named model, then verified STL/STEP exports. If the engineer explicitly authorizes continuous work through a draft 3D model for a defined scope, prepare and review that draft without an intermediate drawing-approval stop; this does not approve either named revision or authorize final exports. Preserve approved snapshots; geometry changes require new revisions and affected approvals. Presentation-only corrections must not alter geometry.
- Use build123d and the locally bound standalone `ocp_viewer`; do not silently change CAD backends. Inspect the existing approved Python environment, installed versions, source and dependencies before execution. Do not install packages, change configuration, overwrite approved files or perform unrelated destructive operations without authorization. Viewer success alone is not visual proof.
- Separate printed parts from purchased, machined and incomplete reference geometry. Verify geometry, intended build orientation and clearances within documented coverage; distinguish intended contact, reference overlap and actual interference. Physical fit, strength, electrical and thermal safety, and production readiness require separate evidence.

## Current trial boundaries

- REV_B is approved for an unpowered trial only. Consult its validation JSON for the scope and limitations of its computational checks; the original sharp-bearing-reference failures remain distinct from the selected-SKF nominal compatibility pass. Physical fit, strength, electrical and thermal safety remain unverified.
- The jogs do not press; the additional NUDGE/SCRATCH button remains TBD. Do not reuse the older two-jog-switch input allocation without reconciliation.
- Use the documented conservative 250 × 250 × 250 mm print screen, not an assumed usable bed. Orientations, supports, calibration and jog/cap materials remain open.
- Do not invent PCB mounting holes or restore rejected B25-MOUNT-01 mounts. Temporary hot glue is not a safety or structural approval; permanent board and DAC retention need measured inputs.
