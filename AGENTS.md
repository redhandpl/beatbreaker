# Agent guide

## Project and records

beatbreaker is a two-deck DJ/MIDI controller: an ESP32-S3 reads controls and drives indicators, and a Raspberry Pi 4 runs Mixxx. The enclosure and jog mechanisms are FDM/FFF prototypes.

- `DESIGN.md`: product facts and decisions; `TODO.md`: the only active work queue.
- `docs/APPROVALS.md`: the engineer's named decisions and their scope. `docs/ARTIFACTS.md`: historical artifact index. `docs/history/SESSION-HANDOFF.md` is dated context, not a current task list.
- The current mechanical release is [REV_A](models/release/enclosure/REV_A/REV_A_handoff.md): an unpowered trial only. Use its [drawing and data](schematics/release/enclosure/REV_A/) and handoff as the entry point; older releases and historical "current" statements are not the current release.
- Discuss work with the engineer in Polish; write code and project documentation in English.

## Artifact layout and migration

- `schematics/work/<subsystem>/<revision>/` and `models/work/<subsystem>/<revision>/` contain working and historical revision packages. Some historical approved exports remain inside mixed packages here; `work` does not revoke their scoped approval.
- REV_A packages the approved B26-CONSOLIDATED-02 drawing and unchanged B26-build123d03 model and exports; it is a package name, not a new geometry revision. Preserve its self-contained `SOURCE/` layout and use the handoff for environment and rebuild instructions.
- Older paths beginning `schematics/<subsystem>/` or `models/<subsystem>/` normally map to `schematics/work/<subsystem>/` or `models/work/<subsystem>/`, except preserved release packages. Frozen artifacts may contain obsolete paths or commands; do not rewrite their bytes or hashes to repair links. Inspect dependencies and use non-destructive staging for older generators.
- `models/work/`, `schematics/work/`, `docs/history/`, `old_case/` and `tmp/` are ignored by Git. Their locally present contents are not necessarily available in a clone; preserve approved local artifacts and distinguish an absent source from an invalid approval.
- Keep supplied references in `elements/`; leave `old_case/`, existing SVGs and legacy directories intact. Do not create SVG deliverables or alternate-format copies of drawings.

## Engineering and approval

- The responsible engineer alone decides dimensions and approves each named drawing and model revision. Do not infer dimensions from pixels, silently choose fits, or treat a concept, folder name, export or absence of objection as approval. Record sourced inputs and explicitly delegated choices; mark critical missing information `TBD` and ask grouped questions.
- For new geometry: dimensioned PDF and separate illustrative concept, explicit approval of the named drawing, build123d model, actual-model viewer review and geometric validation, explicit approval of the named model, then verified STL/STEP exports. Preserve approved snapshots; geometry changes require new revisions and affected approvals. Presentation-only corrections must not alter geometry.
- Use build123d and the locally bound standalone `ocp_viewer`; do not silently change CAD backends. Inspect the existing approved Python environment, installed versions, source and dependencies before execution. Do not install packages, change configuration, overwrite approved files or perform unrelated destructive operations without authorization. Viewer success alone is not visual proof.
- Separate printed parts from purchased, machined and incomplete reference geometry. Verify geometry, intended build orientation and clearances within documented coverage; distinguish intended contact, reference overlap and actual interference. Physical fit, strength, electrical and thermal safety, and production readiness require separate evidence.

## Current trial boundaries

- Read the REV_A handoff before using its artifacts. The C03/C05 Boolean comparison and P01 STEP volume checks did not pass; the recorded bounded exceptions apply only to the unpowered trial. Physical fit, strength, electrical and thermal safety remain unverified.
- The jogs do not press; the additional NUDGE/SCRATCH button remains TBD. Do not reuse the older two-jog-switch input allocation without reconciliation.
- Use the documented conservative 250 × 250 × 250 mm print screen, not an assumed usable bed. Orientations, supports, calibration and jog/cap materials remain open.
- Do not invent PCB mounting holes or restore rejected B25-MOUNT-01 mounts. Temporary hot glue is not a safety or structural approval; permanent board and DAC retention need measured inputs.
