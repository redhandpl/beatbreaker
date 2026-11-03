# beatbreaker — Current TODO

This is the active task queue. Product specification: [DESIGN.md](DESIGN.md); current [release artifacts](docs/ARTIFACTS.md), [approval decisions](docs/APPROVALS.md), [complete REV_B drawing](schematics/REV_B/beatbreaker_REV_B_drawing.pdf) and [validation/BOM/handoff](models/REV_B/beatbreaker_REV_B_validation.json).

REV_B is the sole current release, approved for an **unpowered mechanical trial only**. Its completed computational checks do not qualify physical fit, retention, strength, print process, electrical or thermal safety, or production. The engineer owns technical decisions and physical acceptance; record failures and limitations rather than treating a print start, nominal CAD check or export as a physical pass. Any geometry change requires a separately authorized revision and affected approvals.

`READY` means preparatory work is actionable; `WAITING` names a prerequisite; `LATER` is deliberately deferred. Close each task only when its own done-when evidence is recorded. The non-pressing B26 jogs have no press switches; the additional NUDGE/SCRATCH control is TBD, and BROWSE push is unused and unconnected. F.11/F12 press, spring and switch requirements are historical, not active B26 requirements.

## Mechanical trial and interfaces

- [ ] **ENC-LAP-01 — Verify lower-shell lap joints and feet** — `WAITING: physical trial and engineer-agreed criteria; REV_B CAD delivered`.
  - Measure the actual loaded assembly mass; agree deflection/load criteria. Check joint and wall-lap fit, hardware, seam intersections, assembly order, load response, PSU and jog underside access and actual component/tool clearances. The previously used 1 kg load was provisional, not measured mass.
  - Check foot peg fit, repeated insertion/removal and retention, pad adhesion/friction, leveling and load sharing; the nominal interference zone spans only 0.3 mm of the tapered peg. Assess orientation, supports and process limits.
  - **Done when:** physical results and limitations are recorded against agreed criteria; CAD alone does not prove safe lifting or strength.

- [ ] **JOG-MOUNT-01 — Verify the non-pressing jog sensor mounting** — `WAITING: physical trial and actual bearing identity; REV_B CAD delivered`.
  - The original sharp-bearing-reference screen has **24 failed pair-poses**; the separate bounded nominal SKF 61806-2RS1 compatibility check passed. The latter neither changes those failures into passes nor qualifies physical fit or another bearing. Upper panels must be removed for installation/service.
  - **Done when:** the engineer records actual bearing identity, seating and free rotation, PCB underside/clamp/thread fit, magnetic readings and print-process results against agreed criteria; any substitute's corner and fit are independently verified.

- [ ] **JOG-MODE-01 — Resolve the additional NUDGE/SCRATCH control** — `WAITING: engineer's placement and behavior decision`.
  - Select location, behavior and actual component, establish available space, and reconcile physical controls, PCF allocation and counts. Existing placement concepts are illustrations, not dimensioned or collision-checked designs; do not assume the old two jog-switch inputs. A physical addition needs a new affected drawing/model revision and named approvals.
  - **Done when:** the engineer selects location and behavior, component/space are defined, and affected mechanical and electrical drawings and firmware contract are reconciled and approved within their respective scopes. Physical fit, wiring and powered tests remain separate.

- [ ] **MECH-01 — Assemble and test the printed jog** — `WAITING: B26 physical trial and engineer-agreed criteria`.
  - Establish actual material, orientation, supports, margins and layer settings; test rotation, bearing/shaft fit, sensor/magnet clearance and operation, and assembly/service access. F.11 press, spring and switch tests do not apply.
  - **Done when:** setup and measured results are recorded against agreed criteria, with failures and uncertainty explicit; corrections return through revision and approval gates.

- [ ] **MECH-02 — Define lower-enclosure integration inputs and interfaces** — `WAITING: actual-interface qualification; unpowered REV_B trial approved`.
  - Use the current drawing rather than historical layouts as trial authority. Identify actual installed and service envelopes, fastener/driver access and remaining critical dimensions without re-requesting closed inputs. Verify actual display body, rear/visible image, plugs, mirrored pads and toe sweep; sensor height/lands, threads and retention; Pi/DAC installation and service access; RCA/inlet body and mounting; component, wiring and service clearances. Connected fit, ventilation and mains safety remain unverified. Existing cable/plug and mains-protection responsibilities remain with the engineer, not assumed safety approval.
  - PCF/mux are selected as 2 mm boards with flat finished undersides, no headers and top-only soldered wires; ESP retains reversed headers. REV_B includes their integral holders; no physical retention is approved. DAC has plain pads without modeled screw retention; temporary hot glue is not permanent retention or safety approval. Rejected B25-MOUNT-01 geometry is not to be reused.
  - **Done when:** each installed part/interface has a trustworthy source or explicit bounded engineer selection, remaining design-critical dimensions are marked TBD, and actual-interface qualification is documented. Do not restart a blanket inventory or reopen confirmed measurements.

  - [ ] **B26-PCB-MOUNTS — Qualify controller holders and complete DAC retention** — `WAITING: physical holder trials and DAC retention decision; controller CAD/exports delivered`.
    - **Done when:** ESP-EDGE-01, PCF-EDGE-01 and MUX-EDGE-01 meet their independent criteria, and DAC retention is defined, approved in its applicable scope and physically qualified. Slicing, support removal, calibration and actual fit are not established by the release.
    - [ ] **ESP-EDGE-01 — Physically qualify the integrated ESP edge holder** — `WAITING: unpowered trial; C04 geometry approved`. Insert from smaller table Y; the opposite approach is blocked by B11. Initial 0.1 mm interference per side is uncalibrated. **Done when:** insertion/removal, plug-load retention, PCB damage, creep and print-fit results meet engineer-agreed criteria.
    - [ ] **PCF-EDGE-01 — Physically qualify both PCF edge holders** — `WAITING: unpowered trial; C04/C06 geometry approved`. Use the selected flat underside/no-header/top-only-wire configuration. **Done when:** support removal, print fit, insertion/retention, PCB/pad damage and PETG creep results meet engineer-agreed criteria for both boards.
    - [ ] **MUX-EDGE-01 — Physically qualify the mux edge holder** — `WAITING: unpowered trial; C06 geometry approved`. Use the selected flat underside/no-header/top-only-wire configuration. **Done when:** slicer/support removal, fit/retention, damage and creep results meet engineer-agreed criteria.
  - [ ] **B26-EXPORT-01 — Complete trial and cap-source limitations** — `WAITING: physical print trials and engineer's cap-history decision; REV_B STL/STEP delivered`.
    - Nine inherited cap definitions retain exact meshes without editable feature histories. [Variant B](docs/PRINT_SETTINGS.md) is the selected starting recipe for the 4 mm PETG floor; A and C are optional comparisons. The nominal 250 × 250 × 250 mm screen is not a print approval.
    - **Done when:** actual orientations, supports, calibration, jog/cap materials and physical fit/strength results are recorded, and the engineer decides whether editable cap histories are required. Controller-holder and DAC work remains independently open under B26-PCB-MOUNTS.

- [ ] **MECH-03 — Complete remaining actual interfaces and any affected drawing revisions** — `WAITING: MECH-02 actual-interface inputs and any authorized revision`.
  - The complete [REV_B drawing](schematics/REV_B/beatbreaker_REV_B_drawing.pdf) is already approved for the current unpowered trial; do not demand its re-approval or treat this task as closed. Resolve missing actual purchased-part, hardware, installed, assembly/service and tool interfaces, datums and tolerances in the appropriate scope. The modeled trial is not a complete physical installation qualification.
  - Where changes are necessary, review full installed/joint envelopes and affected floor, wall, panel, support, hardware and print-split interfaces. Do not split purchased components, scale parts to a bed or invent inlet retention/terminal guards. Preserve accepted geometry unless a new revision is explicitly authorized; include relevant approved MECH-01 corrections and obtain named engineer approval of that revision. Existing grille area does not establish airflow, touch protection or thermal safety.
  - **Done when:** remaining model-defining actual interfaces are source-backed or explicitly resolved by the engineer; any required revision is reconstructible from its PDF and sources, its applicable concept is reviewed, and the engineer approves its named scope. This does not close physical or electrical gates.

- [ ] **MECH-05 — Fit and physically verify the installed controller prototype** — `WAITING: actual interfaces, drawing review, print setup and actual parts`.
  - Verify panel/cap travel, fit coupons, pilots, threads, joints, mounting strength, jog clearances, assembly/removal/tool access, wiring, connector/cooling space and material behavior. Do not invent force, torque, deflection or lifetime thresholds.
  - **Done when:** tested build, materials and setup, measurable engineer-agreed criteria, results and accepted limitations are recorded; any geometry corrections return through drawing/model approval.

## Electrical, firmware and validation

- [ ] **ELEC-01 — Verify USB power, VBUS sensing and external-supply behavior** — `READY: source inspection; blocks unverified combined power/USB connections`.
  - Use the exact DevKit revision schematic and RS-25-5 data to resolve regulated 5 V distribution, both USB VBUS paths, isolation, host detection and common ground. Before energizing mains, define and obtain acceptance of inlet/strain relief, terminal guarding, protective-earth continuity, applicable protection/separation and ventilation. Include Pi, DAC, display, controller, 20 LEDs and transients in the whole-system budget; 5 V/5 A/25 W is a rating, not a demonstrated budget.
  - **Done when:** the mains installation and complete power arrangement are source-backed and engineer-accepted; a matrix identifies allowed, forbidden and unverified combinations, and actual tests demonstrate no back-feed or supply contention. No combined-power/native-USB bench release before this gate.

- [ ] **ELEC-02 — Reconcile actual hardware identity, stock and procurement BOM** — `READY: use MECH-02 identities rather than duplicate inventory`.
  - Identify the actual DevKit/module, PCF implementations, AS5048A boards and readable pinout, panel switch electrical variant, BROWSE A/B terminals, pot taper and fader electrical variant. BROWSE push stays unconnected. Distinguish required quantities, actual stock, prices and purchasing status from historical cart notes before ordering; do not re-request closed mechanical measurements.
  - **Done when:** relevant actual variants and sources are identified or explicitly TBD and quantities/stock are reconciled before ordering; procurement costs and unresolved purchases remain explicit.

- [ ] **ELEC-03 — Agree and verify the complete pin/input/power interface map** — `WAITING: relevant ELEC-01/ELEC-02 evidence and JOG-MODE-01; required before complete-input wiring`.
  - The earlier E01 draft is not approved wiring: its old 32-contact allocation predates non-pressing jogs and the requested mode button. Resolve E01-TBD-01…08, map actual panel/mode controls and obtain engineer acceptance. BROWSE is rotation-only.
  - Check native USB, flash/PSRAM/onboard RGB and strapping reservations, ADC capability, AS5048A implementation/levels, BROWSE A/B, mux and two master-VU data lines; GPIO34 is not ADC. Verify PCF addresses, I2C pull-ups/voltage/loading, open-drain INT sharing/clearing, initialization and regulator limits. Do not silently add GPIO or an expander.
  - Verify actual PCF/mux header labels, resistor networks, address straps, INT exposure and HC rather than HCT identity; do not infer board pin numbers. Check control end/wiper terminals, switch contact groups, strip pad direction/order, 74AHCT125 power sequencing and sensor chip-select bias. Verify the Pi–DAC 40-pin cable pin-1 orientation/continuity, display port/power variant, RCA terminals and headphone contact/detect identity before wiring.
  - **Done when:** required signals and power paths have source-checked allocations, safe wiring instructions, readable sensor pinout and explicit remaining limitations; module-pinout confirmation alone is not a GPIO allocation.

- [ ] **FW-01 — Define the stable MIDI/Mixxx contract** — `WAITING: JOG-MODE-01 and input reconciliation; validate at V0.4`.
  - Define channels, CC/Note IDs, press/release semantics, relative BROWSE rotation without push, agreed jog modes and feedback for MAIN_L/MAIN_R master VU only, 10 LEDs each. Confirm Mixxx support and input allocation before freezing IDs.
  - **Done when:** the documented table supports end-to-end browsing, both jog modes, LED feedback and reconnect verification at V0.4; subsequent ID changes require a recorded compatibility decision.

- [ ] **FW-BENCH-01 — Run the direct-input serial diagnostic on actual ESP32-S3 hardware** — `WAITING: engineer hardware identity, safe wiring and upload; source, host checks and ESP32-S3 cross-build/image validation complete`.
  - The [bench diagnostic](firmware/bench_inputs/README.md) reads one fader, pot, button and AS5048A over direct GPIO/SPI and reports serial only: no PCF, mux, MIDI, LED or mode change. Use the isolated USB-only bench; identify the board, sensor breakout, terminals and verified port before wiring. Preserve prior firmware before the engineer uploads; no automatic flashing.
  - **Done when:** actual board/flash settings, readable sensor header/supply topology and control terminals are confirmed, firmware is uploaded, and recorded serial observations demonstrate analog controls, debounced transitions, rotation/wrap and fault behavior. Host tests and cross-build alone do not close this task or V0.1/electrical gates.

- [ ] **VAL-01 — Define measurable prototype acceptance criteria** — `READY: before each corresponding sign-off`.
  - Engineer selects thresholds; record methods, units and evidence for input-to-MIDI/jog latency, angle repeatability, ADC jitter, missed/duplicate events, agreed mode behavior, browsing, reconnect and extended-run stability, plus applicable mechanical fit/retention. Do not invent force/life/strength limits or retrofit thresholds to failures.
  - **Done when:** each applicable gate has a deterministic procedure, measurable engineer-agreed threshold and recorded result/evidence.

- [ ] **VAL-02 — Measure LED power and analog/sensor behavior under representative load** — `WAITING: safe wiring from ELEC-01/03; blocks full-brightness release and final calibration`.
  - Measure both 10-LED master-VU chains, complete supply load, voltage drop/temperature and data integrity; include Pi/DAC/display/controller and RS-25-5 thermal derating. Compare ADC/mux settling and noise with LEDs and actual cables; check jog direction, wrap, noise, update rate and agreed mode behavior.
  - **Done when:** measured operating brightness/power budget and source-backed wiring/protection are documented, and settling/filter/deadband/calibration choices follow actual data and agreed criteria. Supplier estimates are not a tested complete budget.

## Prototype gates

All gates remain open. Each requires its own physical evidence and engineer-agreed VAL-01 criteria; CAD checks and the separate serial diagnostic do not close them.

| Gate | Scope | Completion evidence |
|---|---|---|
| V0.1 — WAITING on safe power/interface prerequisites and JOG-MODE-01 | Small breadboard: MCU, PCF, button, AS5048A, agreed mode control, BROWSE rotation, pot and LED; programming/logging and native USB MIDI | Real upload/enumeration; I2C/address/pull-ups/button/debounce/INT, jog direction/wrap/mode, encoder rotation, ADC and LED checks. No BROWSE push test. |
| V0.2 — LATER | Both jogs, all panel/rotary/analog controls and mux | Agreed complete input allocation; simultaneous inputs, event rate, missed/duplicate events, response and ADC noise verified. |
| V0.3 — LATER | Full level-shifted LED system | Chains/colors/brightness, integrity, measured peak current, voltage drop and thermal behavior; controlled brightness until VAL-02 passes. |
| V0.4 — LATER | Raspberry Pi/Mixxx USB MIDI in/out | Enumeration/reconnect, browsing, agreed jog modes, LED feedback, latency/dropped events and extended stability against VAL-01. |
| V0.5 — LATER | Integrated point-to-point assembly in actual packaging | Actual connectors, wiring, grounding, power/cooling and access; repeat V0.2–V0.4 including stability and fix actual wiring/layout before PCB. |

## Later

- [ ] **PCB-01 — Design/review PCB only after prototypes pass** — `LATER: V0.1–V0.5 and required mechanical integration accepted`.
  - Require frozen actual board/pin/power interfaces, complete inputs, measured power/calibration and physical installation. Review USB-C CC if selected, ESD, differential routing without stubs, shield/ground, current-rated protection/copper, analog/LED return separation, decoupling, programming and service access.
  - **Done when:** the separately named PCB scope has its own source-backed electrical/mechanical review. This queue does not authorize production or bypass prerequisites.

UFO202/version 2.0 and wireless remain outside the current build; deferral does not authorize present mounts, reserved volume or wireless resource assumptions.

## Completed and stopped historical scopes

- **REL-REV-B-01** delivered the current computationally verified release for the approved unpowered trial only. **DOC-B26-CONSOLIDATED-01** delivered the earlier REV_A trial with bounded exceptions; **DOC-REV-A-STRICT** was cancelled, not passed.
- **ENC-JOINTS-02**, **FP-KCAP-01**, **FP-KCAP-02**, **B26-FADER-STL-HOLD**, **MECH-04**, **MECH-04-LP**, **MECH-04-R**, **MECH-04-D** and **MECH-04-T** completed their respective named historical drawing/model/export scopes, not physical qualification of REV_B.
- **MECH-JOG-LP** stopped with its F12 STEP/F3D and physical gates incomplete; **MECH-06** was cancelled with F.11 withdrawal, not passed. Historical R06/F.06/B08 and F.11 approvals, JW-H05P, **VIS-01** and **DOC-01/02/03** remain limited to their recorded scopes, not new release or physical acceptance.
