# Drawing and model approval register

This is a chronological decision/approval/evidence log, not the current product specification or a live session report. Earlier “pending”, “unapproved”, “current” and Fusion-state statements describe their own point in history and may be superseded by later explicit entries. Start with the [current artifact/status register](ARTIFACTS.md), [product design](../DESIGN.md) and [single TODO](../TODO.md). The index summarizes evidence; only the engineer's recorded decisions grant the stated approval scope. The engineer-authorized hierarchy migration moved the single active log to `docs/APPROVALS.md`; its [original text and path provenance](history/hierarchy-migration/README.md) remain preserved. Historical inline paths, quotes and hashes retain their original context; navigation-only link updates do not alter approval scope.

## R06 frontpanel: layout approved

The responsible engineer explicitly approved the frontpanel presented as R06. Approval covers the retained R05 layout, USB/AUX opening, panel split, matched deck button positions and retirement of the six jog-to-panel mounting holes.

The engineer also stated a condition for installed-assembly acceptance: pressing the jog into SCRATCH must not drive the platter into the frontpanel. This condition is **not yet a physical verification or a model approval**. The revised mounting drawings must demonstrate the full platter-envelope clearance, including the inclined rear panel region, and identify tolerance/deflection limits.

The existing R06 files are preserved byte-for-byte. Their original `DRAFT` filenames and printed draft markings are retained; this register records the later approval of the layout scope without overwriting an approved artifact or silently claiming manufacturing release.

| Preserved artifact | SHA-256 |
|---|---|
| `DJC_frontpanel_R06_DRAFT.pdf` | `8cceff50ece65808f636b70b082d107f5cc0530d4e466d780e47f729b398d55c` |
| `DJC_frontpanel_R06_DRAFT.png` | `0189a511613d48c0f8201a1306387b29964bb8c0565edf33d6cc56fdd33c4ba1` |
| `DJC_frontpanel_R06_DRAFT.svg` | `0d2989dd6b5b714bca9cbe3ed423ac63629428310da3038c8ad93ff10f9ecbea` |
| `DJC_frontpanel_R06_DRAFT_coordinates.csv` | `2d5ef776126340ae0c7948712bd67a3e3bb89e9504131c1781b235c82a817ef5` |
| `DJC_frontpanel_R06_DRAFT_coordinates.svg` | `88d2f9a099a24bac3448168777176c1d8e1f3d1b52331a0418b7fd38e251ef95` |

## Jog and enclosure scope

The responsible engineer selected Jog Rev E as the mechanism reference, required mounting its fixed body to the enclosure floor rather than the frontpanel, and authorized adapting the enclosure while preserving that mechanism. Work remains schematics-only.

Jog Rev F and case B03 were unapproved integration drafts. The B03 calculation considered clearance at the jog axis only. Its nominal SCRATCH platter envelope reaches the inclined panel at the rear rim; this is a blocking integration finding, not a change to the approved R06 layout. The new mounting proposal uses the next draft identifiers **Jog Rev F.02 / Case B04** and preserves earlier drafts as historical references. Approval of either new draft has not been granted.

## Model approvals and save authority

No new Fusion model revision is approved. Fusion has not been modified or saved in this drawing work. No STL, STEP or F3D export is authorized by these layout decisions or conditional assembly acceptance.

## Subsequent direction: lower ears and direct M3 fastening

The responsible engineer rejected the tall-column mounting concept of Rev F.02. That proposal and its B04 integration remain historical, unapproved documents. No approval of their proposed whole-jog rotation is inferred.

The engineer requested moving the fixed-body mounting ears to the bottom and replacing captive nuts with short integral floor bosses carrying M3 pilot holes. Preserve the internal Rev E mechanism and the approved R06 frontpanel layout. The next concept draft identifiers are **Jog Rev F.03 / Case B05**; these are not yet approved.

Confirmed materials are **PLA for the test prototype** and **PETG for the intended final version**. The operating scope is gentle normal jog use; nobody is expected to lean on it. No numerical force, tightening torque, acceptable deflection or thread durability threshold was supplied. Record those as unverified rather than assigning an estimated load.

A standard metric M3 screw is not automatically a thread-forming screw for plastics. Pilot fit, direct screw-forming versus post-print tapping, screw geometry and physical thread retention must be verified separately for PLA and PETG. This material/direction decision does not approve a finished mounting revision, certify strength or authorize CAD exports.

## Authorized selection: boss height, tip reserve and layer height

The responsible engineer explicitly delegated the final short-boss height/tip reserve for the candidate M3 x 8 mounting and asked the agent to select layer height. The operator identified a **Bambu Lab P2S with a 0.4 mm nozzle**. Delegation is limited to those choices; it does not approve a named drawing/model revision, the proposed whole-jog rotation, other geometry, print-fit compensation or CAD save/export.

Chosen values for **Jog Rev F.04 / Case B06 DRAFT**:

- Boss height **6 mm**; inherited diameter **10 mm** remains unchanged.
- Nominal blind pilot **diameter 2.5 x depth 5 mm**. Diameter is the existing B02 input, still subject to separate PLA/PETG fit verification.
- M3 x 8 through the inherited 4-mm ear gives **4 mm nominal penetration**. A 5-mm blind depth leaves **1 mm tip reserve**.
- The 6-mm boss leaves **1 mm material below the hole**, plus the complete inherited **2-mm floor**: total nominal bottom ligament **3 mm**. No hole enters the floor.
- Selected nominal layer height **0.20 mm**, half the confirmed nozzle diameter. The 1/2/4/5/6-mm mounting dimensions are integer nominal layer multiples; this is not a claim that the uninspected slicer or physical print achieves those dimensions. PLA and PETG fit must be verified separately.

The height and reserve are authorized engineering selections, not strength-sized or physically verified values. With the inherited geometry, the new jog base is Z8, flat/rear panel tops Z52/Z58 and nominal rear-rim platter gaps 2.5/1.0 mm at NUDGE/SCRATCH. The assembled heights include the 2-mm panel; nominal bare-case mating planes are Z50/Z56. Case integration and named drawing/model approval remain pending.

Historical M3-based draft, superseded for the floor fasteners: [Jog Rev F.04 / Case B06 PDF](../schematics/jog-mounting/F04/Jog_mounting_Rev_F04_drawing_DRAFT.pdf), [review](../schematics/jog-mounting/F04/Jog_mounting_Rev_F04_review.md) and [validation](../schematics/jog-mounting/F04/Jog_mounting_Rev_F04_validation.json). This was a mounting-change package, not the complete Case B06 manufacturing release or BOM. Its files are preserved; no revision approval was recorded.

The earlier session image-model catalog was empty. No separate LLM `_concept.png` was produced, and no SVG or rasterized PDF was substituted. Existing SVGs and earlier preview files are preserved. New drawing delivery remains PDF only, with separate review/validation records.

## Latest input: M2.5 x 6 and accepted whole-jog +60-degree pose

The responsible engineer supplied [m25x6.png](../elements/m25x6.png) for the actual floor screws: **CHC/socket-head M2.5 x 6**, head diameter **4.5 mm MAX**, head height **2.5 mm MAX**, hex key **2 mm**. These are supplied nominal/max dimensions; pitch, minimum bearing diameter/underside geometry, socket depth and supplier SKU are not specified. Change only the **six floor fixings**; preserve the internal Rev E M3 fasteners/nuts and the approved R06 layout.

The engineer explicitly stated acceptance of **whole-jog +60 degrees about CAD-Z**. This preserves local ear/wire relationships while mapping local90/210/330 to global150/270/30. Rotation acceptance does **not** approve a named drawing/model revision, prove the wiring/service envelope or authorize Fusion changes/save/export.

Historical hardware-update draft before dimensional delegation: **Jog Rev F.05 / Case B07**, [PDF](../schematics/jog-mounting/F05/Jog_mounting_Rev_F05_drawing_DRAFT.pdf), [review](../schematics/jog-mounting/F05/Jog_mounting_Rev_F05_review.md), [validation](../schematics/jog-mounting/F05/Jog_mounting_Rev_F05_validation.json). **CHANGES REQUIRED / CRITICAL TBD / NOT APPROVED.** Retain boss10 x6, ear4 with hole3.4 under review, blind depth5, floor2 and layer0.20. The supplied6-mm screw gives **2 mm nominal penetration**, with **3 mm derived tip reserve**; boss base1 plus floor2 remains3. Body baseZ8 and assembled panel tops52/58 remain unchanged.

In that historical draft the old diameter2.5 pilot was retired and the replacement pilot was TBD. For nominal concentric axes, head diameter4.5 MAX over hole3.4 gives a max-reference radial seat0.55; actual support/strength was not verified. The subsequent authorization and current choices are recorded below.

## Authorized M2.5 mounting-interface selection

The responsible engineer answered **"Choose"** to the explicit request to select pilot diameter, ear clearance hole and, if needed, mounting-ear thickness. Scope is limited to those printed mounting interfaces for the supplied M2.5 x6. Preserve the internal Rev E mechanism, boss10 x6, floor2, enclosure heights52/58, accepted whole-jog +60 CAD-Z pose and R06 layout. Delegation does not approve a named revision, uncertain head support, physical strength or Fusion save/export.

Published mounting revision: **Jog Rev F.06 / Case B08**, [PDF](../schematics/jog-mounting/F06/Jog_mounting_Rev_F06_drawing_DRAFT.pdf), [review](../schematics/jog-mounting/F06/Jog_mounting_Rev_F06_review.md), [validation](../schematics/jog-mounting/F06/Jog_mounting_Rev_F06_validation.json). The subsequent named drawing approval and its limited scope are recorded below; the complete B08 assembly remains not model-ready.

- Lower ears/bridges: **3 mm**, localZ0..3. Choice increases nominal penetration2 to3 while retaining more section than ear2; it is a geometric prototype tradeoff, not strength sizing.
- Through hole: **diameter2.9** through3. Authorized transfer of inherited diametral clearance: old3.4-M3major3=0.4; newM2.5major2.5+0.4=2.9.
- Blind pilot: **diameter2.0 x depth5**, a starting trial. Authorized transfer of B02's prior0.5 undersize: major3-pilot2.5=0.5; major2.5-0.5=2.0. This is neither manufacturer tap-drill data nor an assumption about the unknown pitch; calibrate separately in PLA and PETG.
- Supplied screw6 through selected ear3 gives **3 mm nominal penetration**, not verified effective threads. Depth5 leaves **2 mm tip reserve**. Boss6 leaves base1 plus the intact floor2: total3 below the hole.
- Body base remainsZ8; ear top becomesZ11; nominal tipZ5; max-head topZ13.5. Assembled panel tops52/58 and nominal rear-rim gaps2.5/1.0 NUDGE/SCRATCH remain unchanged. Layer0.20/nozzle0.4 retained.

For nominal concentric axes, head4.5 MAX over hole2.9 gives a max-reference radial seat0.8 and contact annulus about9.30 mm². Neither is a minimum actual support or strength guarantee. Actual bearing face, thread operation/fit, useful engagement and retention remain unverified; explicit engineer acceptance is needed where support is uncertain. No mounting nuts/inserts/washers or unrelated geometry are added; internal Rev E M3 hardware stays unchanged.

## Named drawing approval: Jog Rev F.06 / Case B08 mounting scope

The responsible engineer explicitly approved the revision in direct response to the **F.06 / B08** drawing handoff: **"I approve the revision"** (English translation). **APPROVED: the nominal mounting drawing scope of the linked F.06 / B08 PDF**, including ear3, through hole2.9, trial pilot2.0 x5 and the retained geometry/pose documented above. This is an approval of the presented mounting revision, not merely dimensional delegation.

**The full B08 enclosure/installed assembly is not model-ready or approved.** Unresolved design-critical PCB/connectors, original support connectivity, assembly/tool/service route and wall/carrier/joint integration still block approval and final modeling of that wider scope. General drawing approval is not evidence of strength, calibrated fit, verified effective threads, loaded platter clearance or explicit acceptance of uncertain head support. No new engineering choices or geometry changes are authorized by this approval.

The PDF and its review/validation snapshots are preserved byte-for-byte. Their `DRAFT`, `NOT APPROVED`, pending-approval flags and pre-approval findings remain historical markings; this register records the later approval and controls its scope. No Fusion model revision, physical-test pass, cloud save or STL/STEP/F3D export is approved by this drawing acceptance.

| Preserved approval package artifact | SHA-256 |
|---|---|
| `Jog_mounting_Rev_F06_drawing_DRAFT.pdf` | `13d69c7d7ab93c8929df11787109162707b11fd97000ce834f9f06c17dc3162c` |
| `Jog_mounting_Rev_F06_review.md` | `b21ff982f8130d4dd82829f0bd4169e862efefeb4ef8153513856d3216ffed32` |
| `Jog_mounting_Rev_F06_validation.json` | `9ccb116c139386241c1e2a83ea7c40e532d3044d67af81afea57f91c2e27e188` |

## Next approval gate

The named F.06 / B08 nominal mounting drawing approval is recorded. The responsible engineer must resolve the wider critical installation/integration inputs above before complete enclosure modeling. Confirm the target Fusion document and existing unsaved changes before any CAD mutation; Fusion was not accessed or changed in this approval-record task. Actual bearing/thread-fit acceptance, material-specific calibration, printer margins/supports/settings and measurable physical no-contact/retention criteria remain outstanding. Any dimensional/geometric correction requires a new drawing revision and explicit approval of the affected scope; obtain named model approval before exports. Keep drawing approval, prototype approval and physical verification separate.

## Control population confirmation: 2026-10-13

The responsible engineer requested retaining the controls shown in `DJC_frontpanel_R06_DRAFT.pdf`: five faders, thirteen potentiometers, three rotary channels and their three press inputs, plus the panel buttons. In response to the explicit count clarification, the engineer selected **"30 total: 24 B + 6 T"** (English translation). Thus B01-B24 and T01-T06 are all populated; the six arrow buttons are included in the thirty panel buttons, not added to thirty.

The existing architecture identifies the three rotary channels as E01 BROWSE and JA/JB jog sensing (one incremental A/B encoder plus two AS5048A sensors). The three press inputs comprise the BROWSE push switch and the two jog switches; do not count the jog switches again. The resulting requirement is **33 button inputs**, exceeding the existing two-PCF8575 capacity by one. The complete electrical allocation remains TBD; this confirmation does not select an additional GPIO or expander.

**Confirmed scope: control population only.** R06 artifacts and the approved nominal F.06 / B08 mounting package remain unchanged. In preserved R06, T01-T06 are REFERENCE cap symbols, not panel cut definitions. Actual arrow-button cut profiles, mounting and other unresolved integration dimensions require a new drawing revision and explicit approval before geometry changes. No new drawing/model revision, physical-test pass, Fusion mutation/save or STL/STEP/F3D export is approved by this population decision.

## Consolidated jog drawing: Rev F.07 DRAFT / 2026-10-14

The responsible engineer requested updating `schematics/Jog_Wheel_Rev_F_DRAFT.pdf` to include all information from `schmatics/Jog_Wheel_rysunki_do_CAD_Rev_E.pdf` in one Fusion-reconstruction document. The explicitly requested, previously unapproved one-page Rev F selected section is replaced at that path by a **12-sheet A3 Rev F.07 DRAFT**. This publication is not approval of the new revision.

The PDF includes the Rev E JW-E00..JW-E08 topics, complete scoped part/hardware BOM, local/global datums, motion/height chain, assembly order, source checks and current nominal F.06 / B08 floor mounting. Five unchanged mechanism-detail sheets retain their source vector views and annotations; revised sheets replace obsolete upper ears and panel fixings with the approved lower-ear/floor interface. A precedence table explicitly retires the former panel4 / upper-ear / panel-nut information and the early Rev F constant-height section. Internal JW-E references map to the corresponding F.07 sheets within the same PDF.

**CHANGES REQUIRED / NOT MODEL-READY FOR THE COMPLETE INSTALLED ASSEMBLY.** The source does not fully dimension the PCB support ribs: width4 is given but endpoints, attachment path and Z limits are missing. The source post envelopes lie inside the electronics cavity; no connecting material is selected or added. Actual sensor PCB/IC/connectors, magnet diameter/thickness conflict, switch variant, spring, complete fastener details and the B08 pre-closure assembly/driver/service route remain unresolved. Source reference envelopes and historical sampled core-part checks are not full purchased-part geometry, native all-body validation or physical verification.

The existing R06 and approved nominal F.06 / B08 packages remain byte-for-byte unchanged. Their approvals are not extended to F.07 or the complete enclosure. No Fusion document was accessed, changed or saved; CAD body/BRep/physical-test coverage in this drawing task is zero. No STL, STEP or F3D was generated. PLA prototype / PETG intended final and the confirmed P2S nozzle0.4 / mounting layer0.20 remain recorded inputs, not new print-strength or full build-volume checks.

Reproducible native PDF drawing source: `schematics/Jog_Wheel_Rev_F_DRAFT.swift`; run from the repository root with an explicit output PDF argument. It uses installed macOS AppKit/PDFKit/CoreGraphics without new dependencies. The existing `Jog_Wheel_Rev_F_DRAFT.svg` and `.png` are preserved legacy selected-section artifacts, **not companions of the updated F.07 PDF**; no SVG or alternate-format technical drawing is delivered.

A separate preliminary LLM illustration is published as `schematics/Jog_Wheel_Rev_F07_concept.png`, marked DRAFT CONCEPT. An initial image with incorrect screw heads was rejected; the corrected illustration was opened, actually converted from WebP to PNG with `sips`, reopened and checked as PNG1402x1122. It is not a Fusion model, dimensional source or validation view; simplified features are illustrative only.

Executed verification: the delivered PDF opens with native PDFKit, all12 A3 landscape sheets render and were visually inspected across the final layout and unchanged-source views; all searchable detail text from the five retained source sheets is present. Generator guards check page/table overflow, mounting penetration/reserve and the rear-rim SCRATCH height calculation. All eight protected R06/F.06 approval-package SHA-256 values match this register. Temporary generator-inspection scripts, staging PDFs and readability renders are removed after publication; the permanent PDF generator, final PDF, concept PNG and this record remain.

Publication fingerprints:

- Rev E input SHA-256: `466d964366e7373cbb1d9862deb19bd8cb2b68366563e497734e7152b8d63ec6`.
- Superseded unapproved one-page Rev F PDF SHA-256: `725d94c2d9d4e3bc238bc6737e255d929d1e46f8dfe848a1dc7bdeb755493726`.
- Published F.07 PDF SHA-256: `d6abd8ab557f14426bcbcac8fc9e1c7f4b5435e2d974f1014f945df9269954d4`.
- Permanent drawing source SHA-256: `2091ddfc679e8b56d16dc1ef819c304bc9de7d9f865d259b3021fbe0eedcbefd`.
- Illustrative PNG SHA-256: `bdf21cbaca35c4eebb65563ea9de27dc0a1183186f169b2d43eddf032aeac61f`.

Next owner: the responsible engineer is compiling actual-part dimensions. Close the listed source-geometry and purchased-part inputs, then explicitly review/approve the resulting named drawing revision before Fusion geometry work; model approval and export/save gates remain separate.

## Purchased jog parts and proposed AS5048A module: 2026-10-14

The responsible engineer specified that the shaft, bearings, spring and switch will be purchased and the remaining custom mechanical parts printed. This resolves the spacer manufacturing role as **printed**; a purchased steel shaft may still require the two source-defined clamp flats and final-length machining. The existing purchased magnet, sensor/electronics and metal-fastener roles are not replaced with printed equivalents. F.07's former machined-shaft / spacer-role-TBD labels are superseded by this sourcing decision, not by an approved geometry revision.

The engineer reported available diametrically magnetized, Ni-coated magnets: diameter10 x4, N40, listed holding force10.4N; and diameter8 x4, N35, listed holding force8.0N. The latter is the mechanically matching candidate for the retained diameter8.20 x4.2 pocket. No magnetic-performance approval or final selection is inferred from asking which is better; holding force is not the sensor-plane magnetic field.

The engineer identified this intended AS5048A module listing: https://www.fruugo.pl/2x-as5048a-enkoder-magnetyczny-interfejs-pwmspi-wysokiej-precyzji-14-bitowy-silnik-bezszczotkowy-enkoder-as5048a/p-532477684-1079695071 .

Supplied dimension image: https://img.fruugo.com/product/0/23/2626346230_max.jpg . Its original JPEG bytes are retained at `schematics/AS5048A_Fruugo_2626346230_dimensions.jpg`, SHA-256 `a7ff17113971a51b986c0f656416e9362aff76fec9a15c70a15ca89f8fb47dcb` (69,861 bytes, decoded image1700x1700). Static reads failed certificate verification; the image was successfully opened in an already-installed Chrome with normal certificate validation, downloaded without transcoding and reopened locally. The product-page browser navigation was blocked; its full description, delivery contents, stock and electrical claims were not verified.

Explicit source annotations, not pixel-derived dimensions:

| Feature | Source annotation / interpretation |
|---|---|
| Overall planar width / height | 15 / 17 |
| Mounting holes | 2 x diameter2.2 |
| Hole-centre pitch | 12, symmetric about the drawn centre axis; derived offsets +/-6 along the hole line |
| Upper/lower contour arcs | R9, referenced to the drawn central intersection |
| Side-view dimension | 2 from the PCB back face to the outer IC face; NOT a separately specified bare-PCB thickness or a wired-module envelope |
| Unit notation / tolerances | Not explicitly stated on the supplied graphic. The project uses mm; confirm source units and tolerances before final dimensional approval. |

At the mounting-hole line, the source width/pitch/hole annotations imply a nominal remaining side ligament `(15-12)/2 - 2.2/2 = 0.4` in source units. This is a dimensional derivation only, not verification of PCB or fastener support/strength.

The proposed two-hole module is not the F.07 placeholder30x30x1.6 with four diameter3.2 holes at (+/-12,+/-12). A future drawing must replace that placeholder and explicitly define the new mounting, actual PCB thickness/IC stack, populated terminals and wire route. Do not copy the old four M3 supports, select new screw/pilot sizes or infer rib geometry. The shaft/magnet/sensor axis and installed Z position must be established from confirmed module data and the required full-stroke magnetic check.

The delivered F.07 PDF/generator and approved R06/F.06 packages are intentionally unchanged in this source-identification task. The supplied drawing is a proposed-part reference, not proof of the delivered module's identity or permission for Fusion mutation. New mounting geometry and the resulting named drawing/model revisions still require explicit engineer approval.

## Confirmed AS5048A inputs and lower-enclosure option: 2026-10-14

The responsible engineer explicitly confirmed **millimetres** for the supplied module drawing and supplied canonical inputs `elements/AS5048A.jpg` and `elements/AS5048A_pinouts.jpg`. The selected module is the Fruugo model at https://www.fruugo.pl/2x-as5048a-enkoder-magnetyczny-interfejs-pwmspi-wysokiej-precyzji-14-bitowy-silnik-bezszczotkowy-enkoder-as5048a/p-532477684-1079695071 . This exact model URL must appear in the drawing and project documents.

The engineer confirms the pinout **by reference to the supplied pinout image** and authorizes assuming the working diameter8 x4 N35 diametric magnet/module combination operates throughout the 1.5-mm jog travel. This closes the functional assumption for the drawing discussion, **not** physical magnetic, electrical, accuracy or reliability verification. No AGC/MAG measurements or electrical-level tests are claimed. The 100x100 pinout file is not sufficiently legible for reliable transcription; the engineer's reference confirmation is retained without inventing signal labels or wire colours. A readable original remains necessary before producing a wiring instruction.

Confirmed module dimensions: width15, height17, two diameter2.2 holes on12 pitch, R9 contour arcs and total PCB-back-to-IC-face height2, all in mm. Drawing-derived hole offsets are +/-6 along the hole line. With the shown shared R9 centre, the bottom edge is9 below the source centre and the top straight edge is17-9=8 above it. No bare-PCB thickness, solder thickness, terminal geometry, wire diameter, bend radius or dimensional tolerances are inferred.

The engineer permits attaching the module to the lower enclosure. The working **proposal** uses two floor-supported fixing axes rather than the obsolete four housing PCB posts/ribs; it does not change the approved six jog-floor fixings. Support diameter, fastener/thread/pilot details and final clocking remain unselected. These are engineering choices, not dimensions deducible from the supplied picture.

| Derived placement | Calculation / condition |
|---|---|
| Sensor top, body-local | Retain the existing nominal source datum Z9.5; not a new measured die datum |
| PCB underside / support contact, body-local | 9.5-2=Z7.5 |
| PCB underside / support top, global | Jog base8 +7.5=Z15.5 |
| Support height above existing floor top | 15.5-floorTop2=13.5 |
| Screw-head clearance constraint | Magnet-holder underside at full press is12-1.5=10.5; over the mounting-hole region, actual PCB thickness plus hardware height above PCB must be less than10.5-7.5=3, before any separately agreed clearance margin |

These conditional height deductions use the supplied overall2 and existing nominal datums only; they do not require guessing the laminate/IC split. They are not a complete fastener/support definition, a collision test or permission to round13.5 for the0.20 layer setting. Actual clamping hardware must clear the moving holder, support the PCB at its0.4 nominal edge ligament and have an accepted load/contact path. Cable exit localZ3..7 remains inherited; the proposed PCB undersideZ7.5 does not prove a usable solder/wire route through it.

Source hashes: `elements/AS5048A.jpg` SHA-256 `a7ff17113971a51b986c0f656416e9362aff76fec9a15c70a15ca89f8fb47dcb`; `elements/AS5048A_pinouts.jpg` SHA-256 `3cd26abae32687fa6a720f496ceccb3e3394351581b72d6ee480abe349e3b1e7`. The supplied originals are not changed. The earlier published F.07 PDF is preserved at `schematics/Jog_Wheel_Rev_F07_DRAFT.pdf` with its recorded SHA-256 `d6abd8ab557f14426bcbcac8fc9e1c7f4b5435e2d974f1014f945df9269954d4` before preparing the next draft.

No F.08 drawing/model approval, floor-support dimension selection, Fusion mutation/save or export is authorized by these input confirmations. Approved R06 and nominal F.06 / B08 mounting remain unchanged; the proposed sensor-to-floor interface needs explicit drawing approval before modeling.

## Published jog drawing: Rev F.08 DRAFT / 2026-10-14

Published the13-sheet A3 `schematics/Jog_Wheel_Rev_F_DRAFT.pdf` as **Rev F.08 DRAFT / CHANGES REQUIRED / NOT APPROVED**. This is a drawing/input update only. The module footprint is reconstructed from the confirmed15/17/R9 and2 xdiameter2.2 on12-pitch source annotations; no unspecified terminal/slot geometry or laminate thickness is estimated from pixels. The old four-M3 PCB placeholder and its housing supports are explicitly retired in the precedence table, current housing/module sheets and BOM. The source Rev E details remain in the same consolidated document.

Sheet12 includes the actual `elements/AS5048A.jpg` and the100x100 `elements/AS5048A_pinouts.jpg`, the engineer's mm/pinout confirmations, magnetic-operation assumption, conditional Z7.5/Z15.5/H13.5 derivation and the necessary clamp-stack constraint. It contains the **full exact Fruugo model URL both as searchable text and as a clickable PDF link**, not just a generic AS5048A family link. Pin labels are not invented from the low-resolution image.

The two floor-supported sensor axes are a proposal, not fully specified or approved new floor geometry. Height is derived while retaining the prior nominal IC-face datum; support diameter, footprint, fastener/thread/pilot, final clocking, hardware bearing/contact and cable route remain open. The two fixing positions per module replace the obsolete four-M3 PCB allocation in the current BOM; no new screw type/length or support cross-section is silently selected. Printed spacer and purchased-shaft roles now match the engineer's sourcing decision. The approved six jog-floor fixings, R06, source images and F.06 / B08 approval packages remain unchanged.

Verified the actual delivered PDF with native PDFKit: all13 A3 pages open and render; every sheet was visually inspected across the staged final layout, including the supplied graphics and module outline. The full supplier URL is present and its link annotation resolves to the exact requested string. All five unchanged source-detail sheets retain their searchable source text. Numerical guards pass for retained mounting/height arithmetic, PCB underside7.5, floor support13.5 and source-derived edge ligament0.4; these are document/arithmetic checks, not engineering tolerances or a BRep collision analysis.

All eight protected approval artifacts, the two canonical supplied images and preserved F.07 PDF match their recorded SHA-256 values. The F.08 preliminary illustration was generated separately from the prior exterior concept with only a revision-label edit requested; it omits undefined sensor supports/wiring, was opened, genuinely converted from WebP to PNG and reopened. It is not a Fusion-model validation view.

Publication fingerprints:

- F.08 PDF SHA-256: `d6452684095f4b2578fb0eaace791568453997748a79ee8a2a030a5c50c28e85`.
- Current drawing generator SHA-256: `b5dab4a53edd3cf70dff981bf573bb8334eb4488177d76ba9787e8d46d3bed88`.
- `schematics/Jog_Wheel_Rev_F08_concept.png` SHA-256: `89d053688848a95ad4bfc71cd5cf43208443c756723930891de707f3605eb77b`, actual PNG1402x1122.
- Preserved `schematics/Jog_Wheel_Rev_F07_DRAFT.pdf` SHA-256 remains `d6abd8ab557f14426bcbcac8fc9e1c7f4b5435e2d974f1014f945df9269954d4`.

`DESIGN.md`, `DESIGN-TODO.md` and `TODO.md` are synchronized with the confirmed inputs and explicitly distinguish assumptions from physical checks. No Fusion access/mutation/save, native body/interference/motion test, physical test or STL/STEP/F3D export occurred. No new SVG or alternate-format technical drawing was created. Task-owned staging/verification scripts and page renders under `tmp/jog-f08-inputs/` are removed after publication; the permanent generator and named deliverables remain. The engineer still owns local dimensional choices and named drawing/model approval; a mounting option or functional assumption does not approve a revision or waive actual clamping/service checks.

## Enclosure-stage boundary and supplied control and LED inputs: 2026-10-14

The responsible engineer clarified the workflow: supports, pilot/thread details, fastener lengths/heads, solder/wire envelopes and routing will be designed during **lower-enclosure design and integration**, adapting the enclosure to the known jog mechanism and chosen controls. This applies to all installed elements, not just the AS5048A. These are case-design deliverables, not a demand to provide all mounting dimensions before starting that phase. R06 supplies the retained layout and F.08 supplies the documented nominal jog construction; this statement is not explicit named F.08 drawing approval, a full installed-assembly approval or a physical-test pass.

The current F.08 PDF/generator remain intentionally unchanged in this inventory task. Its full-installation items B1/B2/B5 are carried into the enclosure phase under the clarified scope; they must not be treated as missing purchased-part dimensions that prevent inventory or enclosure planning. Actual part-variant omissions, nominal jog fits, final integration checks and approval gates remain distinct.

The following canonical `elements/` images were opened. Only printed annotations are used; no dimension is estimated from pixels. Mounting/support geometry and printed caps/knobs will be designed with the enclosure, not silently selected here.

| Source / part | Readable dimensional information | Part-definition limits |
|---|---|---|
| `elements/encoder_browse.png` | Body width11.8; axial6.5 callout to the shown base; bushing M7x0.75 and length7; shaft diameter6 with D-flat dimension4.5; SW travel0.4+/-0.2; source PCB terminal patterns | Shaft dimensions L and A are symbolic with no supplied values. Exact variant/shaft extension and printed knob envelope are not determined. |
| `elements/knob_potencjometr.png` | L=30 from the drawing's indicated rear datum to shaft end, not30 of exposed shaft; axial6.8 and4.5 callouts; transverse9.7/11.4 callouts; outer terminal spacing5; PCB locating features shown | Shaft diameter, bushing/thread designation and actual resistance/taper are not supplied by this image. The file depicts the potentiometer, not a dimensioned knob. Do not combine unrelated view dimensions into an invented bounding box. |
| `elements/przycisk.png` | Shared source drawing lists B3F-4050/4055/5050/5051; body12+/-0.2 square; overall top height7.3+0.2/-0.3; projected terminal span13.8+/-0.5; plunger square3.8+/-0.1; reference PCB drill/locating pattern | Exact family variant, force/travel and cap geometry are not selected by the image. The PCB t1.6 note is a button mounting reference, not AS5048A PCB thickness. Do not read the unlabelled1.8 height callout as switch travel. This panel-button source does not replace the jog's D2F-01FL3 reference. |
| `elements/fader.png` | Longitudinal body annotation60mm; body-width annotation9mm; exposed lever height15mm from the shown top face; visible blade-width annotation4mm | No actual slider travel, mounting-hole pitch/thread, body depth below its upper face, transverse blade thickness, pinout or electrical variant is dimensioned. The4mm blade width is not a stated across-slot thickness. Do not reuse the historical B02 body9x80x13 or treat60 as the travel. |

### Arrow-button candidate screening

The engineer considers the supplied button possibly too large for T01-T06, but has not excluded it if it fits. The R06 triangles10x10 remain REFERENCE symbols, not cut profiles or maximum purchased-body sizes. A raw switch can be wider below the panel than its eventual printed cap/plunger opening.

A script read the actual R06 coordinate CSV and checked the three T pairs in a source-axis-aligned 2D arrangement. Body maximum is12+0.2=12.2; projected terminal-span maximum is13.8+0.5=14.3.

| Pair | Centre spacing mm | Body-envelope gap mm | Terminal-span gap mm |
|---|---:|---:|---:|
| T01/T02 LOAD | 46 | 33.8 | 31.7 |
| T03/T04 FX A | 18 | 5.8 | 3.7 |
| T05/T06 FX B | 18 | 5.8 | 3.7 |

The raw switch is therefore not rejected merely for its size. Coverage is **three pairs / six candidate switches in 2D only**. Caps, BROWSE knob, other complete installed bodies, PCB/supports, solder/wires, Z positions, tool access, force and native BRep pairs were not validated. This is not an all-controls fit or collision-free claim, and no final T switch, cap or cut size is chosen.

### Selected cut-to-length LED strip

The engineer selected https://botland.com.pl/paski-led-adresowane/12486-pasek-led-rgbw-sk6812-cyfrowy-adresowany-ip65-144-ledm-432wm-5v-1m-5904422319373.html . The product page was successfully read in installed Chrome with normal HTTPS validation after the static reader's certificate failure. It confirms SK6812 RGBW SMD5050,5V,144LED/m,12mm width, IP65 silicone cover, quoted43.2W/m and approximately9A/m, and cutting after each LED. The user's approximate2mm spacing is also retailer wording; it must not be used as centre pitch.

Nominal centre pitch from density is1000/144=6.944444mm. Around a nominal5mm package, this corresponds to approximately1.944mm edge gap, consistent with the wording “about2mm”; actual pitch/encapsulation tolerances were not measured. R06 L01-L10 and L11-L20 each have7mm centre pitch and63mm first-to-last-centre span. Ten consecutive strip LEDs nominally span9*(1000/144)=62.5mm between their first/last centres, a0.5mm span difference. Do not silently shift approved windows or assume a continuous10-LED strip exactly matches them. Individual cuts/placement, diffusers, the mapping of four10-LED electrical chains to20 windows, supports, solder and wire paths are enclosure-design work.

The electrical baseline remains40LEDs in four chains of10. Scaling the quoted approximately9A/m gives9*40/144=approximately2.5A and5*2.5=approximately12.5W for those LEDs alone. This is a planning estimate, not a measured or guaranteed maximum and not a complete controller/Pi power budget. The retailer's43.2W/m and rounded9A/m are retained as separate approximate claims; no new PSU or brightness limit is selected. Strip thickness including silicone/adhesive, terminal/solder envelope and assembly waterproofing are not established by IP65 alone; cutting/soldering does not automatically preserve an IP65 assembly rating.

Input fingerprints:

- `elements/encoder_browse.png`: SHA-256 `441ea3f57ef14fa9d158efba5ca909498f37dd10a783e1e0fb12321eafb70a50`,202046 bytes.
- `elements/knob_potencjometr.png`: SHA-256 `b8f73f5f2302d4e070a9ea94fb5b8142fc8c0ba214bf1122a5bf263c173fcdd2`,207153 bytes.
- `elements/przycisk.png`: SHA-256 `fa9b8f6d9a3e420d12064af567827387a4052c2670f5f48699f4f0f8da2069b1`,258740 bytes.
- `elements/fader.png`: SHA-256 `df937c697ed032ce6dfe7ddea1eed5638fc783adf8d9da2c6cab86db3d6f40d3`,78563 bytes.

No supplied image, approved geometry, R06 coordinates, jog PDF/source, Fusion document or export is changed by this inventory/stage clarification. The temporary fader magnification is a readability aid only, not a new drawing or dimensional source, and is removed before handoff.

Verification completed: SHA-256 comparison passed for all8 registered R06/F.06 artifacts, the current F.08 PDF/generator/concept, preserved F.07 PDF and all6 supplied AS5048A/control images. The new stage-reference anchors resolve to this record and referenced component/drawing files exist. The R06-coordinate calculations above were executed; coverage remains the stated three T pairs and two VU columns, not full installed geometry. `TODO.md`, `DESIGN.md` and `DESIGN-TODO.md` are synchronized. Task-owned `tmp/component-inputs/` was removed. No Fusion, full-assembly collision, physical fit, electrical load test or export was performed.

## Legacy control references and confirmed variants: 2026-10-14

The responsible engineer supplies BROWSE dimensions A=7mm and L=15mm for `elements/encoder_browse.png`; these resolve the previously symbolic shaft-variant inputs without changing the supplied drawing. The potentiometer is confirmed as10kOhm with stated shaft length23mm; its actual knob is `old_case/knob.stl`. Preserve the image's separately based L=30 annotation; do not replace it with23 or infer a datum conversion by rounding30-6.8. Taper and a precise installed shaft-length datum are not established by the knob mesh.

The engineer confirms the old enclosure used exactly the current fader model, supplies `old_case/tempo-fader.stl` and `old_case/crossfader.stl` as the matching caps, and selects `old_case/performance-pad.stl` as the panel-button cap baseline. Retain its mechanical interface and change top markings for the B buttons; develop a triangular derivative for T01-T06 in the enclosure/drawing phase. This is source/part-selection authority, not approval of new cut profiles, invented triangular dimensions, an installed assembly or a named drawing/model revision. No existing model is modified by this record.

### Legacy source preservation and mesh checks

The repository is confirmed as `/Users/krzysztof.pedrys/Projects/OWN/GIT/redController`. Inspection is read-only for all supplied geometry; Fusion is not accessed and its active-document/save state remains uninspected. The native FreeCAD thumbnail was extracted for inspection under task-owned `tmp/legacy-controls/parent/`; it is an existing legacy-model preview, not a new drawing, concept or Fusion validation view.

| Supplied file | SHA-256 at inspection start |
|---|---|
| `old_case/case.stl` | `b6fc3659b7641a4b95275cacd79f8b25e4d03e5d4da46c3fd6612efde4182ea6` |
| `old_case/front-panel.FCStd` | `dcfee959c2e054ae152cd183e39a70429d402a613931f4274380fdbfeb236e18` |
| `old_case/front-panel.stl` | `5cedac9e49ae3b4a8b03005ee2c1cceec8d350a9235577c7f60fe218b136c9cd` |
| `old_case/tempo-fader.stl` | `13162e64c43d38c626b1425eaa22c4e90ed775c208e042e82f436b194f785a6d` |
| `old_case/crossfader.stl` | `c7d864b2908f8304e0f00e41a7e1111164eaf96696754c8835d2196cc82fec46` |
| `old_case/knob.stl` | `fa96654a5aa5c10a89864c4de4fb8a8e20842d8cc148bf176ed7efe8615998e4` |
| `old_case/performance-pad.stl` | `3ce7ede980638c21904d4a174e8813e1bc26c1091880e3aaca1b7772c3ebcf25` |

A binary-STL analysis checked the four supplied caps: correct byte/triangle counts, finite coordinates, no degenerate triangles, no boundary edges and one vertex-connected component each. Exact-coordinate edge incidence found four nonmanifold edges in `tempo-fader.stl`; the other three caps had none. This does not test self-intersection, physical fit, printability or strength. Preserve the tempo source and resolve its mesh topology in the approved editable reconstruction before manufacturing; do not silently repair or certify it as a valid solid.

### Knob and performance-cap geometry

Numeric readings retain source XY sections and axial Z coordinates. FreeCAD base `Sketch` spans X=−87.5…87.5/Y=−60…60 with native mm lengths, and its `Pad` thickness agrees with the 175×120×2.4 panel STL. This supports the legacy project's millimetre interpretation, but STL has no unit metadata and no editable cap source independently confirms each cap's export scale. Keep native scale unchanged; the following are geometric source readings, not measured purchased hardware or a manufacturing release.

| Source feature | Native-coordinate geometry |
|---|---|
| Knob envelope | Actual faceted X/Y/Z size 12.064535×12.082254×19; nominal widest ring radius 6.05 / diameter 12.10 recovered from circular vertices, not the faceted bounding-box width |
| Knob socket entry | Mouth at Z=0, nominal Ø6.90 tapering over 0.4 to Ø6.10 |
| Knob circular socket | Nominal Ø6.10, Z=0.4…7.6 |
| Knob D socket | Same circular radius 3.05 with flat at Y=+1.85, Z=7.6…17; blind ceiling Z=17, total socket depth 17 |
| Knob exterior/marking | Source mesh retains the scalloped/tapered grip, base transitions and positive-Y indicator; top indicator recess is 0.4 deep, separate from the shaft socket |
| Performance-cap head | Z=0…4; widest 14×14 R3 at Z=0.6…3.2; underside 12.8×12.8 R2.4; top 12.4×12.4 R2.2 |
| Performance-cap stem | Z=−4.6…0; main outer section 6.8×6.8 R1; bottom 0.4 lead-in ends at 6×6 R0.6 |
| Performance-cap socket | Main cavity 4.4×4.4 R1 at Z=−4.2…0; entry 5.2×5.2 R1.4 at Z=−4.6; total engagement depth 4.6 |
| Performance-cap markings | Top annular rounded-square recess depth 0.4; cosmetic modifications must preserve the approved eventual mechanical interface |

The user identifies these as the actual legacy knob/cap for the selected components, so reuse their source geometry rather than inventing replacements. Socket Ø6.10 and flat Y=1.85 do not prove actual shaft diameter, flattening or clearance; do not calculate installed projection as23−17 without matching datums. Similarly, pad socket width4.4 alone does not prove B3F fit: rounded cavity corners and actual plunger corners/tolerances matter. A hypothetical sharp square3.9 does not fit the sampled cavity; no claim is made that the actual purchased plunger is sharp or incompatible. Physical fit remains to be checked on the chosen hardware.

R06 B11/B12/B17/B18 retain Ø15 circular openings. Sampled cap-head radial maxima are 8.046252 at Z=0, 8.644519 at Z=1 and 7.846888 at Z=4, exceeding opening radius7.5; head traversal is therefore not a valid assumption. The narrower stem has maximum sampled radius4.389253, so a stem-through/head-above arrangement is not ruled out, but installed Z levels, clearance and press travel are unvalidated. No panel opening is changed. The Z=0 shoulder is not evidence of an independently positioned below-panel flange.

Execution evidence: helper analysis checked closed degree-two section loops, socket shoulders/ceilings and circle-fit residuals; parent independently intersected knob sections at Z=2/10 and pad sections at Z=−2/1 and confirmed the Ø6.10/D-flat Y=1.85 cavity, knob ceiling Z=17 and pad socket width4.4. Coverage is these two source meshes and sampled sections, not a full installed assembly. Existing knob/pad sources remain unchanged; task-owned helper section scripts were removed.

### Recovered fader installation geometry

The FreeCAD document explicitly records `UnitSystem=0`, `Standard (mm, kg, s, °)`. Base sketch constraints17/18 are175/120; `Pad.Length=2`, with later raised details reaching panel-mesh Z=2.4. This establishes the panel XML/STL scale, not independent cap/case unit metadata. `[INFERENCE]` case/panel XY registration is panel+(130,130), matching all three legacy fader sites; no assembly Z transform is established.

| Feature | Source and measured geometry | Meaning / limit |
|---|---|---|
| Tempo through-slots | `front-panel.FCStd`, `Sketch002` geometry44–51 /54–61: 41.5×2, cornerR0.75; centers(−36.5,−26.75)/(74.5,−26.75); `Pocket001.Length=2` | Printed cuts, not measured mechanical travel |
| Cross through-slot | `Sketch002` geometry70–77: 30×2, cornerR0.75, center(0,−46.5) | Printed cut, not travel |
| Tempo upper reliefs | `Sketch003`, 49.5×14 R3, nominal depth1; final chamfered upper opening50.9×15.4 atZ1.9 | Printed relief/clearance, not actual metal body envelope |
| Tempo end seats | Case transverse gap9; axial inner boundariesY71.998/132.5, separation60.502 | Open-centered printed cups, not a modeled purchased fader or mounting-hole pitch |
| Cross end seats | Case transverse gap9; axial inner boundariesX99.899/160.099, separation60.200; printed end-wall centersX99/161 | The62 wall-center spacing is not screw-hole pitch |
| Central supports | Case topZ7; tempo footprint approximately9×30.002, cross30.002×9; end-seat topsZ14 | Printed support levels; their7 height difference is not body depth |
| Tempo cap | Envelope12×10×10.6; socket1.2×4.8 R≈0.4, entry lead-in0.4, blind depth10 | Printed cap interface; actual blade dimensions/engagement remain distinct |
| Cross cap | Faceted envelope15×7.933612×12; socket1.2×4.8 R≈0.4, entry lead-in0.4, blind depth9.4 | Printed cap interface, not purchased blade thickness |

Inspection covered the complete FreeCAD feature inventory (one printed-panel Body, no purchased-fader object), both tempo sites and the cross site in the case, sections through Z0.5…17.5 and both cap cavities. The case contains printed end cups and central pedestals with open space between them, not complete metal fader bodies. The supplied image remains the source for body60×9, exposed lever15 and visible blade width4. True travel/end positions, body depth, blade thickness/insertion geometry, mounting-hole pitch/diameter/thread/flanges and electrical variant remain unresolved; solder/wire routing is deferred enclosure work, not an immediate inventory demand.

The final panel mesh corroborates tempo throat41.5×2 and cross throat30×2; top chamfers do not change their interpretation as printed apertures. Do not transfer those lengths as travel or silently modify R06's provisional61.7-long slots. Parent independently checked both cap cavities at two depths and their ceiling planes Z10/Z9.4.

Tempo mesh warning localized: duplicate opposite-winding facet pairs172/173,208/209,850/851,852/853 (zero-based) occur at the outer shoulder nearX±5.600005/Z2.001414, not in the central socket. Parent verified equal vertex sets for all four pairs; envelope/socket dimensions remain useful as source evidence. No repair, rescaling or geometry mutation was performed. Helper analysis script `tmp/legacy-controls/fader/analyze.py` is task-owned and removed before handoff.

Final inventory verification passed: all7 supplied `old_case/` files and all8 registered R06/F.06 artifacts match their recorded SHA-256 values; current F.08 PDF/generator/concept and all4 component-reference images also remain unchanged. `TODO.md`, `DESIGN.md` and `DESIGN-TODO.md` link this evidence record and retain the confirmed control population. Task-owned `tmp/legacy-controls/` and its scripts/thumbnail were removed. Changed artifacts are only these three project records and this register. No Fusion access/save, geometry change, new drawing/model approval, CAD export, physical fit/load/strength test or full installed-assembly interference analysis occurred. Complete enclosure integration remains CHANGES REQUIRED; nominal R06 and F.06/B08 approval scopes are unchanged.

## Confirmed fader data, native seats and jog trial components: 2026-10-14

This update supersedes the earlier active inventory requests for fader travel/depth/blade thickness/mounting-hole data, potentiometer threaded mounting and button force. It records engineer inputs and read-only source analysis, not a new drawing/model approval. R06, approved F.06/B08 and the F.08 jog PDF/generator remain unchanged; incorporate these sourcing/integration decisions into the next applicable drawing revision before its approval.

### Confirmed faders and native mounting references

Engineer inputs: crossfader travel28 mm; tempo/volume travel41 mm; NO mounting holes; blade thickness1 mm; body depth6 mm excluding protruding terminals. Combined with the supplied image, nominal body is60×9×6, blade4×1 and exposed lever height15. Terminal projection/solder/routing are future enclosure work, not an omitted dimension silently assigned here. Existing cap socket1.2×4.8 implies nominal total geometric differences0.2/0.8 relative to the stated blade; those are source differences, not newly authorized fit tolerances.

New native source `old_case/case.FCStd`: SHA-256 `8eddeaaaeda52707c15587d149373fb05c2130e018242a35a28b463bef3c80e7`,1983305 bytes, UnitSystem0 `Standard (mm, kg, s, °)`. No editable document was opened/saved or regenerated. XML/sketch parameters and final mesh sections were read directly; native XY plus(130,130) matches the exported case mesh at the inspected features. This is a source/mesh registration, not an established assembly Z transform.

| Interface | Native source features and dimensions | Mounting interpretation |
|---|---|---|
| Fader lower supports | `Sketch004` geometries32–43 / `Pad003`: two9×30 pads and one30×9 pad, Z2…7 | Lower support, no fader screw holes |
| Tempo end cups | `Sketch006` geometries0–30 plus revised closing lines189–201 / `Pad005`: nominal inner width9, longitudinal clearance60.5, walls primarily2 thick, topZ14 | Open-ended side/end capture around the body; legacy external wall contributes to one end. No purchased mounting-hole pattern |
| Cross end cups | `Sketch006` geometries31–44 plus closing lines202–203 / `Pad005`: inner width9 and axial clearance60.2, topZ14 | Lower central support plus end cups, not screws through the fader |
| Potentiometer lower supports | `Sketch004` geometries52–67 / `Pad003`: four10×12 pads, Z2…7 | Support underneath the control body |
| Potentiometer side guides | `Sketch006` geometries45–140 / `Pad005`: four L-shaped corners per control, central opening10.4×12.4, outer envelope14.4×16.4, wall thickness2, topZ14 | Cradle/corner guidance, not threaded bushing/nut mounting or an evidenced snap latch |
| Potentiometer registration | Native centres(−11.5,17),(−11.5,44),(11.5,17),(11.5,44); matching Ø8.5 panel holes in `front-panel.FCStd/Sketch002`, geometries64–67 | Confirms which four native cradles correspond to the rotary controls |

Numeric checks covered all four pot cradles at meshZ10.5, lower pad topsZ7 and corner topsZ14, plus all three fader central supports atZ7. Final mesh gaps approximately10.4/12.4 agree with native pot parameters within export offsets/tessellation; exact feature values come from XML, not mesh rounding. Sketch line loops were checked closed with degree2. The native case thumbnail was inspected. The source establishes support and lateral/end capture; final axial retention, panel closing/contact levels, terminal spaces, insertion and service sequence in the new enclosure still require design/verification. Do not call these cavities complete clamping or assume that a body6 plus supportZ7 sets an approved panel height. Reuse the mounting principle without demanding a nonexistent fader screw interface or an unnecessary potentiometer thread measurement.

### Panel-button scope

The engineer accepts `elements/przycisk.png` for the panel-button geometry and explicitly states operating force is irrelevant. Remove force as an inventory blocker. The shared B3F-4050/4055/5050/5051 drawing specifies body12±0.2, top height7.3+0.2/−0.3, body height4.3±0.2, plunger□3.8±0.1 and the PCB pattern. Its1.8±0.2 vertical callout is not labelled actuation travel; do not invent a stroke from it. Keep the selected legacy cap and test actual press travel/return and panel alignment during integration, without requesting a new force selection. This does not replace the separate jog microswitch.

### Omron jog-switch trial

Canonical engineer-supplied local source: `elements/en-d2f.pdf`,850668 bytes, SHA-256 `d3f2ed08101cf7ec6f57577643225f73faa5475026dda0072bcddf2d99fb04db`. Manufacturer URL: https://omronfs.omron.com/en_US/ecb/products/pdf/en-d2f.pdf . The local six-page PDF is byte-identical to the normal-HTTPS Chrome download and the inspected manufacturer page4 render; no certificate bypass was used. The temporary download is not a second project deliverable.

The engineer proposes trying the D2F family. Retain the existing drawing's **D2F-01FL3** R1.3 simulated-roller lever as the compatible trial candidate, rather than silently substituting a pin-plunger or generic tactile switch. Page1 lists terminal variants; the blank suffix is standard straight PCB terminals. Exact ordered suffix/terminal envelope and the real contact point must match the installed model before validation.

Page4 gives D2F-01FL3 operating force max0.39 N, releasing force min0.02 N, overtravel min0.5 mm, movement differential max0.45 mm, free position max13 mm and operating position8.5±1.2 mm, for operation at the maker's A-direction/contact point. Existing drawing nominal body-bottomZ13.4 plus OP8.5 givesZ21.9, consistent with targetON at jog stroke1.1; remaining stroke1.5−1.1=0.4 is below OTmin0.5 only under that contact/adjustment condition. This is nominal arithmetic, not a tolerance/deflection/clearance pass; hard stops, not the switch, must take full press load. Page5 calls for M2 mounting screws/washers and torque0.08…0.1 N·m; this is a manufacturer requirement to assess, not authorization to select lengths or assume adequate printed support. Its micro-load cautions also require checking actual3.3 V/input current, not assuming the contact is validated merely because it is the01 series.

### Spring procurement and proposed printed trial

Existing criteria are retained from Rev E page7/JW-E06, also retained in F.08 sheet07. They define a purchased compression spring, not a winding/manufacturing drawing.

| Parameter | Existing criterion / recorded derivation |
|---|---|
| Quantity | One per jog, two total |
| Inner diameter |28 mm nominal; source does not state a tolerance |
| Outer diameter |≤31 mm |
| Free length |Approximately10 mm; not a finalized tolerance |
| Stiffness target |0.4…0.8 N/mm |
| Working lengths |7.0 mm NUDGE,5.5 mm full press/SCRATCH |
| Solid height |≤5.0 mm |
| Axial motion |1.5 mm; fixed spring seatZ14 to moving lower-cover undersideZ21 in NUDGE |
| Nominal linear force at7.0 |For assumed L0=10: compression3.0, force1.2…2.4 N |
| Nominal linear force at5.5 |Compression4.5, force1.8…3.6 N |
| Nominal coil-bind margin |At full press,5.5−5.0≥0.5 mm before tolerance/deflection |

Executable arithmetic verified the seat-height chain and both force ranges. These forces use the approximate free length as exactly10 solely for illustration; they are not measured return force or user-approved feel. Moving weight, guide friction, actual spring tolerances/end seating and desired force/cycle acceptance remain unmeasured. Obtain the supplier's force-at-length data, dimensional tolerances, solid height, end form and material before accepting a specific spring; no wire diameter or coil count is selected here.

A printed spring may be investigated as a separate preliminary return/click demonstrator, not a calibrated or durable metal-equivalent part. ID28/OD≤31 leaves at most1.5 mm radial section for a simple annular winding; PLA/PETG layer orientation, creep, hysteresis and fatigue therefore require actual sample testing. Do not scale a steel coil or assume its0.4…0.8 stiffness transfers to plastic. No printable winding/flexure geometry, material-specific dimensions or new print settings are selected. A trial requires its own dimensioned/approved geometry before Fusion modeling/export and measured return/permanent-set results against agreed criteria; the purchased spring remains the final baseline. Initial carrier-guidance checks can be performed without a spring as the existing drawing already requires.

Verification/handoff: native XML line-loop and source/mesh section checks, source-PDF extraction/render inspection and spring/switch arithmetic were executed. SHA-256 preservation passed for all8 registered R06/F.06 artifacts,7 earlier legacy models, the newly supplied case.FCStd, canonical en-d2f.pdf,3 relevant component images and F.08 PDF/generator/concept. The three current project records link this update. Task-owned `tmp/control-seat-review/` was removed, including temporary supplier download, scripts, extracted text and PNG inspection renders; supplied originals remain. Only `TODO.md`, `DESIGN.md`, `DESIGN-TODO.md` and this register changed. No Fusion operation/save, new geometry, approval or export, full-assembly interference test, spring manufacture or physical/electrical test occurred. Complete installed-assembly status remains CHANGES REQUIRED; the completed scope is input clarification, native seat evidence and trial-component criteria, not manufacturing approval.

## Published F.09 and JW-SP01 Rev A trial drawings: 2026-10-14

The engineer requests the jog-drawing update and spring selection/drawing before modeling. Equipment is now explicitly display on top of the upper panel, Raspberry Pi,DAC,Anker supply and controller boards. Behringer UFO202 is excluded now and deferred to version2.0; no present mounting/reserved geometry is authorized. The33-input/32-port allocation is deferred to electronics connection, not a mechanical-design/approved-fabrication blocker. No electrical connection or power-safety gate is waived.

### Supplier check and authorized trial route

Lee Spring's real dimensional search returned “No Stock Springs Match Your Selection” for OD28…31,ID27.8…29,free length8…12; a broader ID27.2…29.5/free length up to20 also returned no stock. Source: https://www.leespring.com/compression-springs/1 . Gutekunst's actual form with De min28/max31 and L0 min8/max12 returned “Unfortunately no suitable item was found in the catalog.” Source: https://www.federnshop.com/en/products/compression_springs.html . These are two observed catalog searches, not proof of worldwide unavailability; no purchase, quotation submission or supplier contact was made.

The engineer explicitly chose **“Najpierw drukowana próbka”** from the offered routes rather than custom steel or mechanism changes. This authorizes development of a separate printed trial within the current envelope, not assignment of steel properties to PETG or approval of its finished revision. Forma selects the trial's proposed geometry/material under that delegation; all unrelated jog/enclosure dimensions remain unchanged.

### JW-SP01 Rev A / PETG trial geometry

The selected concept is a circumferential three-wave flexure between flat annular end rings, not a scaled steel-wire helix. Part material is PETG for the trial; it does not change the PLA baseline for other prototype parts. One initial sample; two if later adopted for both jogs.

| Dimension / construction | Chosen value / source and reason |
|---|---|
| Through bore |Ø28, retained jog criterion; finish-cut through the complete union |
| Outer diameter |Ø30.4, chosen below the retained≤31 envelope, leaving0.3 radial envelope reserve |
| Free height |10.0, explicit trial nominal chosen from the prior approximately10 criterion |
| Bearing rings |R14…15.2, Z0…1 and9…10;1.0 axial height, flat end faces |
| Wave band |Three equally spaced waves;0.8 vertical section height, same R14…15.2 construction interval |
| Section centres |Zc=5.0+4.4 cos(3θ); gives0.6…9.4 and positive material joins into both rings |
| CAD construction |72 radial rectangular sections at5° increments; ruled loft matching corners between adjacent pairs, close loop, union with both rings, then cutØ28 through |
| Why final bore cut |Straight chord interpolation intrudes inside R14 between angular sections; the explicit final cut preserves the governing bore instead of silently delivering an undersize polygon |
| Existing installed references |NUDGE7.0 and full-press5.5 from unchanged seatZ14 / moving-coverZ21 with1.5 travel |

No PETG modulus, force curve, stiffness0.4…0.8, solid-height≤5 or fatigue acceptance is claimed. The previous metal-spring criteria remain a future procurement baseline, not trial results. The complete part can now be reconstructed from its two-page technical drawing without choosing missing geometry; physical return, deformed clearance, permanent set and print/support behavior remain experimental. Existing0.4 nozzle/0.20 mounting-layer data are not a released spring-print process.

### Published artifacts and actual verification

`schematics/Jog_Wheel_Rev_F_DRAFT.pdf` is now **F.09 DRAFT**,16 searchable A3 sheets. It retains all five Rev E detail sheets, approved nominal F.06/B08 interfaces and exact AS module source, updates Omron/stage/BOM decisions, and embeds the full JW-SP01 Rev A two-page drawing. `schematics/Jog_Spring_Rev_A_DRAFT.pdf` is the separate two-page model-defining part drawing; no alternate-format technical drawing or SVG was created. Both remain unapproved at publication. Preserved F.08 PDF/generator are `Jog_Wheel_Rev_F08_DRAFT.pdf/.swift`, matching the previously published fingerprints.

Native Swift/PDFKit generators ran successfully. All16+2 pages opened/rendered as A3 with searchable text; page grids and changed/spring sheets were visually inspected for readable annotations/layout. A body-region raster comparison at1800-pixel page width passed for all five retained detail sheets versus preserved F.08, excluding intentionally replaced headers/footers. Full-page extracted-text comparison was unsuitable because current/source headers interleave during extraction; no source geometry was changed to satisfy that check. Page-count/reference/source-link guards pass, including the exact Fruugo URL, explicit UFO202 version2.0 deferral and complete spring construction.

F.09 and JW-SP01 Rev A concept PNGs were LLM-generated separately, returned as actual images, opened, genuinely converted from WebP to PNG and opened again. They are illustrative drafts, not Fusion views or dimensional evidence. No spring model was created before drawing approval. A read-only Fusion document-list query reported zero open documents; no unsaved document was closed, geometry altered or cloud save performed.

Publication fingerprints:

- F.09 PDF: SHA-256 `b1e7988dfb9534e837d0b7dc662fce5154f55b4ab77cf64786f66640a778f9c0`,508104 bytes.
- F.09 generator: SHA-256 `2f2307fdb143e109d0e989ea82f845ffd3ea8a438ec85920db71515ba1c53297`,46823 bytes.
- F.09 concept PNG: SHA-256 `201391c9ab1eae0068b00247c81eaf4e87cdb9bbf9c732ae0824efbd48c3e272`,1603978 bytes.
- JW-SP01 Rev A PDF: SHA-256 `341457fcff97846b359cdf31ddf64513ff9b03e6d453a68385e25e509f2e5bfc`,86156 bytes.
- JW-SP01 Rev A generator: SHA-256 `042383a9cd555cc123811173d44feb315816c693e68a3285eba26c6da51be158`,15264 bytes.
- JW-SP01 Rev A concept PNG: SHA-256 `a58a55ff4dc9ffcd9d4188ccb2218b60b8edfa42180a174d1f3ae483421af0ee`,1840058 bytes.

All8 registered R06/F.06 artifacts,7 earlier legacy inputs,new native case and local Omron PDF retain their recorded fingerprints. No spring/assembly physical, force, fatigue, printability, current full-body BRep/motion analysis or STL/STEP/F3D export is claimed. Status at publication: **CHANGES REQUIRED / NAMED DRAWING APPROVAL PENDING**, not model/manufacturing approval. Next approval may be scoped to JW-SP01 Rev A geometry/material for modeling only; it does not approve the entire installed jog, save to cloud, or manufacture an unapproved model.

Task-owned `tmp/jog-f09/` was removed after publication and verification, including supplier-search snapshots, staged PDF, temporary verifier, extracted text and all page/grid renders. Permanent drawing generators and published PDFs/concept PNGs remain. At the review handoff there is no spring Fusion model and no save/export authority; the next operation is the engineer's explicit named drawing decision.

### Engineer approval: JW-SP01 Rev A geometry/material for modeling

The engineer explicitly selected **“Zatwierdzam JW-SP01 Rev A do modelowania”** after receiving the published two-page PDF and the limited approval scope. Approved source: `schematics/Jog_Spring_Rev_A_DRAFT.pdf`, SHA-256 `341457fcff97846b359cdf31ddf64513ff9b03e6d453a68385e25e509f2e5bfc`. Approval covers its exact trial geometry and PETG material for creation in a NEW Fusion document only. It does not approve the complete F.09 jog/installed assembly, physical force/fit/durability, model revision, printing, cloud save or STL/STEP/F3D export. The approved PDF/source are retained without rewriting their publication-time DRAFT labels; this dated approval record governs the limited geometry scope.

### Actual Fusion model: JW-SP01 Model Rev A

Following the limited drawing approval, Forma created the NEW Fusion document `JW-SP01_Rev_A_TRIAL` and the native editable component/body `JW-SP01_Rev_A_PETG_TRIAL`. The document remains open, modified and UNSAVED; no cloud save, close/discard or STL/STEP/F3D export occurred. Shared filesystem access was verified against the approved drawing hash. No existing jog assembly was changed.

The completed uncompressed model has one closed solid body,227 faces,9 user parameters,76 sketches,72 construction planes,72 two-profile corner-railed lofts and3 extrusions, including the governing Ø28 finish cut. All224 timeline items are healthy. Measured bounds are30.4×30.400000000000006×10 mm, within0.0001 mm of the approved overall dimensions. The native bore face has radius14.000000000000002 mm; occurrence transform is identity. During construction all72 driven section corners matched their approved coordinates within0.00001 mm.

Read-only native-body verification passed456 point-containment checks at every sector midpoint,5° spacing/2.5° phase, covering band interiors, clear exterior band probes, finished bore and both end rings. Native volume285.89322918038164 mm³ agrees with independent integration of the approved ruled-sector/ring/bore union285.89329078585195 mm³; absolute difference0.00006160547030731323 mm³ is below0.02 mm³. These are numerical check thresholds, not manufacturing tolerances. Coverage is the entire ONE standalone part, zero inter-body pairs; no installed-jog collision or compressed-motion claim follows.

The construction request exceeded the MCP response timeout. It was not blindly replayed: subsequent read-only inspection found the completed72 lofts and final bore cut, then the independent health/geometry checks above passed. Earlier API/solver diagnostics were task-local and left no extra probe geometry in the final document. No configuration or dependency was changed.

Actual model review image: `models/JW-SP01_Rev_A_fusion-view.png`, native Fusion viewport,1600×1200 PNG, SHA-256 `45254be7ff7f0dd3106f89f9bbd51f4f5c7250d9a32053b1138d96b140df5ff2`. File existence/PNG encoding were checked on the repository filesystem and the image was opened for visual inspection. Sketches/construction planes are hidden; the isolated free-state model is left in its isometric review view. This is separate from the LLM concept. Detailed check scope/risks: `models/JW-SP01_Rev_A_validation.md`.

**Model approval remains pending.** PETG is the selected trial material, not a calibrated native material/stiffness model. No force, compression/solid-height, return, stress, fatigue, creep, installed fit or physical test was performed. Its nominal free-state box is smaller than250×250×250 mm, but print orientation, supports and usable margins are unresolved; no final print-fit or printing approval is claimed. One initial sample is specified, two only if adopted for both jogs. Next owner: responsible engineer reviews and explicitly approves or requests corrections to **JW-SP01 Model Rev A**. Full F.09 jog approval remains separate; cloud saving still requires an explicit request/destination. Status: **CHANGES REQUIRED**, pending these gates, not an identified standalone-geometry defect.

## Read-only jog documentation and native-model readiness review: 2026-10-14

The engineer requests review/preparation and identifies existing **`Jog Wheel - Rev E`** as the Fusion baseline. This request does not approve F.09, new geometry, cloud copying/saving or exports. The [readiness report](../schematics/jog-wheel/F09/Jog_Wheel_Rev_F09_modeling_review.md) recommends an independent native document copy preserving Rev E, not a full rebuild or another cloud version under the source lineage.

Observed source: Default Project, cloud version5, lineage `urn:adsk.wipprod:dm.lineage:F1uxEN30QRKxKmfpRlmCbQ`, mm, saved/unmodified;34 occurrences,35 closed solid bodies including hidden bodies,134 healthy timeline items,48 component features of which31 are BaseFeatures,16 sketches and zero user parameters/external referenced components. Slider limits−1.5…0 mm, unrestricted revolute joint and4 rigid groups were inspected structurally, not exercised. Native source geometry includes useful retained scallop/C-groove and retainer corrections; a whole rebuild would discard useful work without a demonstrated need.

Two related findings require resolution: existing housing feature `M3 retention head clearance - D5.7, seat Y13.5` is not dimensioned in either source Rev E PDF or consolidated F.09, and its reference screw head is only partially supported. Native flat seat face area7.582607603440975 mm², X18.65…21.04162541257965, compared with reference under-head face16.689710972195783 mm², X18.75…24.25 at the sameY13.5 plane; axisX21.5 lies outside the housing circular boundary there. These face areas are NOT a contact-overlap area or strength result. Do not silently delete the feature, copy it as approved, or infer acceptance of partial support. Record its retain/change decision in a new named drawing issue; proposed F.10 is not created or approved. Retained sheet05's metal-spacer advice should also be reconciled with the governing printed role without dimensional changes.

The cutover report identifies exactly what to retain/replace: preserve the mechanism; replace upper ears with approved lower mounting, retire old PCB posts/ribs/panel hardware/references, use the actual selected sensor's documented REF geometry, and keep the free-state spring distinct from any installed working-space envelope. Sensor support/hardware/wiring decisions remain lower-enclosure work, not a blanket ban on approved core modeling. No arbitrary spring scaling/compression or completed vendor geometry is authorized.

**Save-state update:** before opening Rev E, the host reported the spring `JW-SP01_Rev_A_TRIAL` already saved as version1, unmodified, in Default Project, lineage `urn:adsk.wipprod:dm.lineage:LpBCjRY2RGCCDQ33Xsrc6A`. This supersedes earlier creation-time unsaved warnings. No assistant save occurred in this review and no model approval is inferred from the observed saved state.

Actual checks: all16+9+2 PDF pages opened/rendered, searchable A3 media verified; F.09 pages2/6/7/9/12/14 visually inspected, as was the existing native viewport without camera/visibility/pose edits. Current F.09, Rev E source and approved spring PDF fingerprints remain unchanged at the values recorded in the report. Native interfaces/seat/structure were measured read-only. No595-pair interference, new motion/insertion, contact-overlap, physical, compressed-spring, slicer/build-margin or export check was performed. No new geometry/copy/rename/save/export was executed; the clean source is checked before restoring the original session document. The engineer retains all approval/dimensional authority. Status: **CHANGES REQUIRED** for the recorded retainer decision/documentation and later named approvals.

Session restoration executed: Rev E was confirmed saved/unmodified at version5 with the same35 bodies/134 timeline items, then only the clean document opened for this inspection was closed. The original `JW-SP01_Rev_A_TRIAL` is again the sole open/active document, saved/unmodified. No changes were discarded. The task-local scripts, API capture, inventories and PDF renders under `tmp/jog-f09-readiness/` are removed at handoff; the retained readiness report contains the source identities, measured findings, cutover plan and check limits.

## Retention-strategy discussion and spacer precedence: 2026-10-15

1. **Retainer:** the responsible engineer explains that the original screw was intended to prevent pulling the jog out, questions whether it is necessary and requests alternatives. No removal or replacement is selected. The retained F.09 sheet08 specification also makes the carrier-slot/screw contact the upper-return/NUDGE stop, so deleting it without a replacement stop would leave that position undefined by the present mechanism.
2. **Head support:** the engineer explicitly makes the partial-head-support issue dependent on the retention decision. Treat the two review findings together; do not independently repair/preserve the current head seat or infer acceptance of partial support. The review now records candidate concepts: a headless M3 stop using the existing nut/slot, a separate fixed-housing retainer ring, or a properly defined headed-screw seat. Forma's minimal-change recommendation is the headless concept; it is NOT engineer selection or approval. No lengths, end forms, projections, ring dimensions, fastenings, locking method or housing changes have been selected.
3. **Spacer:** the engineer explicitly reconfirms the printed bearing spacer as the governing baseline. Metal is a future fallback only if the printed part proves inadequate. Retain the existing nominal Ø10.5/Ø8.10×3 geometry and inner-race-only/no-preload intent; this does not select metal stock/part, fit changes or quantitative pass thresholds. Reflect the printed-first/conditional-metal wording in the next drawing issue rather than treating the retained metal preference as current.

Only the existing review/checklist and this decision record are updated. No PDF revision, Fusion geometry/session/save/copy or STL/STEP/F3D export operation occurs in this discussion. Drawing/model approvals and engineer dimensional authority remain unchanged.

## Selected headless M3 retainer concept: 2026-10-15

The responsible engineer explicitly selects **“Spróbujmy z wariantem ze śrubą bezłbową”**. This selects development of the headless M3 retainer using the existing captive metal nut/carrier-slot principle, serving anti-withdrawal and the upper-return/NUDGE stop. Do not ask again which concept to use or independently repair the old headed-interface support.

Retained source inputs are axisY atX21.5/Z35, housing boreØ3.2, captive-nut pocketAF5.7/Y8.5…11, carrier slotX19.8…23.2/Y1.5…3/Z33.5…38.4 inNUDGE and source tip approximatelyY1.7. The nominal distance11−1.7=9.3 mm to the outer pocket plane is derivable, but it does not determine a stock screw length, complete end/socket geometry, effective thread engagement or locking method. Those remain TBD; the concept choice is not explicit dimensional/component-selection delegation.

The next action is to obtain the engineer's hardware/locking specification or bounded selection authority, then prepare a named drawing. No arbitrary stock-length rounding, threadlocker, locking patch, nut change, retainer preload or housing geometry is silently selected. No named drawing/model, Fusion mutation, cloud copy/save or export is approved or executed by this concept-selection record. Printed-spacer precedence/conditional-metal fallback remains unchanged.

## Delegated retainer selection and published F.10 DRAFT: 2026-10-15

The engineer explicitly selected **“Dobierz w obecnych interfejsach”** in the bounded selection question. Authority covers screw length, end, drive, projection and anti-loosening method while preserving the existing axes, captive nut, carrier slot and1.5-mm stroke; no clamping the carriage. Outside-scope changes require returning to the engineer. This is dimensional/component-selection delegation, NOT named F.10/model approval or Fusion copy/save/export authority.

Selected H05: **KIPP K0707.03X12**, uncoated steel hardness45H black, M3x0.5x12, flat pointD2=2, SW1.5, one/jog/two total. Actual KIPP5-page manufacturer datasheet is preserved as `elements/KIPP_K0707_datasheet.pdf`; nominal length/point/drive are from its p1, pitch0.50 cross-checked against Böllhoff's ISO4026 M3 reference. No assumed socket depth, full threads or vendor tolerances are fabricated.

Retained axisX21.5/Z35,Ø3.2 bore,AF5.7 captive-nut pocketY8.5…11, carrier slot and1.5 travel remain unchanged. Selected nominal flat-tipY1.7 retains the source approximate setting; nominal socket endY13.7 gives about0.943 centreline projection beyond the original Ø50 wall. The planned model retires only the obsolete Ø5.7 head recess atY13.5; no new boss/ring or accepted partial-head-bearing interface. Useful thread engagement, actual contact/wear and holding strength remain unverified.

Anti-loosening selection: **VC-3 fully dried acrylic friction film**, not wet anaerobic glue in the assembled printed body. Maker TDS (`elements/Vibra_Tite_VC3_TDS.pdf`,May2018) specifies1.5×D coating length,30–50% thread-root fill and≥30min drying before assembly. ForD3 the4.5-mm film is centred on the existing nut pocket:5.8…10.3 from tip, bodyY7.5…12. Wet solvent-containing product is applied to the screw outside plastic and fully dried; follow SDS/ventilation/ignition precautions and verify actual PLA/PETG dried-film compatibility/fit/holding before a physical PASS. No coating thickness/retention torque is invented.

Rejected the nominal stock nylon position of KIPP K0707.203X12: makerL1=4±0.5,L2≈2p≈1 from tip gives nominal bodyY2.7…6.7, not the captive nutY8.5…11. A self-locking label is not sufficient evidence at this installed position. No purchase, quote/contact or stock-availability claim.

Published `schematics/Jog_Wheel_Rev_F_DRAFT.pdf` as **F.10 DRAFT**,18 searchable A3 pages, with dedicated retainer geometry/process sheets16/17 and a corrected printed-spacer sheet05. Cover/spacer nominal dimensions and threading/fit calibration requirements are retained; printed spacer governs, metal only if it proves inadequate. The original F.09 PDF/source are preserved byte-for-byte as `Jog_Wheel_Rev_F09_DRAFT.pdf/.swift`. New [F.10 review](../schematics/jog-wheel/F10/Jog_Wheel_Rev_F10_review.md) contains selection derivations, source links, scope and fingerprints. Separate `Jog_Wheel_Rev_F10_concept.png` is an LLM exterior illustration, actually converted from WebP and opened as PNG; hidden retainer intentionally not shown. It is NOT a Fusion view.

Executed verification: real native Swift generator;18 searchable A3 pages opened/rendered; page groups and changed sheets visually inspected. Corrected a long source-link gutter overrun/XY heading placement, regenerated and verified the corrected pages. Retained-body raster equality passes on PDF pages3/4/5/8/15/16, excluding changed headers/footers; the re-expressed cover/spacer sheet is not claimed raster-identical. Retainer/film arithmetic and source-link guards pass. All8 registered R06/F.06 artifacts, both F.09 archives, spring PDF/source and Rev E input retain fingerprints:13 files checked. Final concept decodes as1402×1122 PNG. No new CAD/BRep pairs/motion/physical/locking/strength/print/export test occurred.

Final publication fingerprints:
- F.10 PDF523323 bytes: `90c2750382d48e2b5dba8fad13644f27f7610d13aaac2c63f9346e7c9fcd896c`.
- F.10 Swift61810 bytes: `bcf551089373e36d1e63f50adab4fc0617550382bf978f35f6b7020db7288d0b`.
- Concept PNG1563144 bytes: `974039172439b7d4e61b0445a64c53b9cc89431d5ddb6a83d3125e0c55266a58`.
- KIPP PDF197424 bytes: `4cddce29b7a21f8fd36f6a76aa563322213d521ab85d45d88c4c67000991deee`.
- VC-3 TDS68743 bytes: `4db9ec3f2ad9a5a8519fac511e6f7970d10f9f77f6667db5276b82572aff7d94`.

Status: **CHANGES REQUIRED / Jog Rev F.10 nominal mechanical/core and headless-retainer drawing approval pending**. Full enclosure supports/wiring/service and physical verification remain separate; spring Model Rev A approval is still pending. Original R06/F.06/JW-SP01 drawing approvals are unchanged. The only Fusion operation read clean saved spring-document metadata; no source geometry, pose/visibility, copy, cloud save or export was changed. Native Rev E copying still requires an explicit request and destination. Task-owned research/browser profile, staged PDF, render/verifier scripts and captures under `tmp/jog-f10/` are removed after publication.

## Printed retainer trial requested: 2026-10-15

The engineer interrupts Polish-market sourcing with **“Hm... A zamodelujmu ją do druku”**. Stop procurement research and develop a printed headless M3x0.5x12 trial, proposed part identifier **JW-H05P Rev A**, retaining the metal captive nut, retainer axis, housing bore, carrier slot and1.5-mm stroke. The previous steel KIPP/VC-3 definition in F.10 is preserved as a reference, not silently republished as a printed-part specification or approval.

The existing project baseline is PLA for the initial prototype and PETG for the intended final version; the printer is a Bambu Lab P2S with a0.4-mm nozzle. No screw-specific layer height, fit compensation, allowable assembly torque, holding load or durability criterion is selected. Exact printed-thread/drive details require bounded authorization and a new named drawing; the prior steel selection is not approval of the printed part.

Read-only Fusion inspection observed the active **Jog Wheel - Rev E** document with **isModified=true**. Preserve those unsaved changes: no save, close, source mutation or cloud copy is authorized. Plan a separate new document for the printed trial after its named drawing is approved. No geometry or session-state mutation was executed.

Fusion2705.1.30 exposes the native ISO Metric profile M3x0.5 external6g definition: major2.927, minor2.3555 and pitch diameter2.6175 mm. These are queried candidate library values, not an approved printed fit or invented FDM offset. With an SW1.5 hex socket, the nominal minimum radial ligament would be2.3555/2−1.5/sqrt(3)=0.3117246 mm; this arithmetic flags a print/strength risk, not a slicer or physical result. Drive form/depth and complete end details are not yet selected for JW-H05P.

VC-3 is not selected for the printed trial: its MEK-containing wet application and the steel-screw process cannot be transferred to PLA/PETG without compatibility evidence. Functional anti-loosening remains unresolved. First obtain bounded printed-detail authority, then publish the dimensioned PDF and separate illustrative concept for explicit drawing approval. Modeling, actual Fusion views, model approval and verified STL/STEP/F3D follow in that order. No existing drawing/model approval or export permission changes.

## Printed-detail delegation and JW-H05P Rev A drawing publication: 2026-10-15

The engineer explicitly selects **“Dobierz detale pod druk”**. Authorized scope: choose the M3x0.5 thread profile/class, drive and end details within M3x0.5x12 for a PLA trial, without arbitrary fit compensation. Replacing the hex drive is permitted; the existing metal nut, axis, housing interface and stroke remain unchanged. This is bounded dimensional delegation, NOT named drawing/model approval, source-document mutation, cloud saving or export approval.

Selected **JW-H05P Rev A**: PLA, native Fusion ISO Metric profile M3x0.5 external6g/right-hand/physically modeled, queried diameters2.927/2.6175/2.3555; total length12. Flat tipØ2 with45-degree flank to the major diameter gives cone height(2.927−2)/2=0.4635. Thread covers the cylindrical faceZ0.4635…12. A centered through-width straight slot, width0.8/depth1.0, occupiesY−0.4…+0.4/Z11…12 and replaces SW1.5. No head, added relief, fillets, drive-end chamfer, scaling or fit offset. Choices use two nozzle diameters for slot width and two thread pitches for depth; these are geometric choices, not proven process settings. Nominal root radius minus half-slot width is0.77775; actual print/strength/driver fit remain unverified.

Retained installed mapping: jogX=21.5+partX, jogY=1.7+partZ, jogZ=35−partY. The metal-nut pocket lies at partZ6.8…9.3, clear of cone/drive cuts; pocket length is not verified useful engagement. Slot/bore/1.5 stroke and the anti-withdrawal/upper-return-stop function are unchanged. No chemical locking is selected for the initial fit trial; anti-loosening/holding qualification is unresolved and no functional release follows.

Published [JW-H05P Rev A DRAFT technical drawing](../schematics/jog-retainer/A/Jog_Retainer_H05P_Rev_A_DRAFT.pdf),2 searchable A3 sheets, with orthographic/section views, complete nominal native-feature definition, datums/axes, assembly mapping, role/BOM, sources and explicit trial/approval limits. The editable native Swift generator is retained. Separate [Rev A concept PNG](../schematics/jog-retainer/A/Jog_Retainer_H05P_Rev_A_concept.png) is LLM-generated, labeled illustrative/not a Fusion model. It shows the straight-slot headless concept, not dimensional proof.

Executed checks: actual Swift generator and its pitch/profile/slot/nut-zone/source-gap guards; final PDF opens with2 searchable A3 pages; both sheets rendered2400×1697 and visually inspected. Removed a leader crossing annotations, regenerated and inspected the corrected geometry sheet. Final PDF semantic checks cover thread diameters, cone extent, slot Z limits, retained interfaces and trial warnings. Generated WebP opened, converted with sips to real PNG, final PNG opened; signature and1536×1024 dimensions verified. F.10 PDF/source and the approved spring drawing retain their recorded fingerprints. No Fusion geometry/session-state/save change, nut-fit/strength/locking, slicing, actual print or export occurred.

Publication fingerprints:
- JW-H05P Rev A PDF36564 bytes: `00839f25dcc0e2b89e04d63b99bbc250366fbb0cff5c01408feb9bf92e5aa540`.
- Swift15898 bytes: `3fe35e4f5de105e73eba054a775901c230635c16a7db9d5be758f0ba04263b7c`.
- Concept PNG1864135 bytes: `a45a5b8dc35952f03bf1b25738ce7ae8b0cbe5f8b53d499876fe802bd71c29c5`.

Status: **CHANGES REQUIRED / explicit JW-H05P Rev A drawing geometry/material approval pending**. Next: approve that named drawing for a separate new editable Fusion trial, preserving the active modified Rev E; then validate actual geometry/view and request model approval before exports. Cloud save is not requested or authorized. F.10/JW-SP01 approvals remain separate. Task-owned staged PDF, render script and sheet previews under `tmp/jog-h05p/` are removed after publication; the final PDF, generator, concept and this record are retained.

## Engineer approval: JW-H05P Rev A drawing geometry/material for modeling

The engineer explicitly selects **“Zatwierdzam JW-H05P Rev A”** in the named drawing gate. Approved scope: the published2-sheet drawing, SHA256 `00839f25dcc0e2b89e04d63b99bbc250366fbb0cff5c01408feb9bf92e5aa540`, PLA trial, M3x0.5 external6g/right-hand x12, flatØ2/45deg tip and straight slot0.8x1.0. The accepted option authorizes a separate new editable, unsaved Fusion trial with physically modeled threads, preserving Rev E. It does NOT approve the resulting model, exports, cloud saving, functional retention/locking or physical printability. No amendment to F.10/JW-SP01 approvals.

Immediately before modeling, actual read-only inspection found BOTH existing documents saved but modified: `Jog Wheel - Rev E`134 timeline items/35 bodies, and `JW-SP01_Rev_A_TRIAL`224 items/1 body. Both must remain open with their unsaved changes preserved. Source geometry/occurrence-pose snapshot SHA256 values are respectively `38d0e3c6e9e1da6d4450c71b7efd3500a1b5d56ac78c02848fd505ba0a33e04a` and `d33e04cc809f1ca6658e9d46bf329732581a6129384d9395591fc54c94d03230`. Default Select command only; no interactive dialog blocks mutation. Fusion host reads the agreed repository PDF at its exact path and matches its SHA256, proving shared filesystem visibility before model-view/export writes.

## JW-H05P Model Rev A completed and validated for review

Created the separate **JW-H05P_Rev_A_TRIAL**, unsaved/open/modified, after the named drawing approval. One named printed component/body, native revolve + physically modeled M3x0.5 external6g/right-hand thread + straight-slot cut;6 user parameters,2 fully constrained sketches,7 healthy timeline items. No geometry deviation from approved Rev A was required. No cloud save or existing-document close/copy occurred.

Actual standalone checks pass: bounds2.927×2.927×12 mm within0.00001 mm,63.039701334708475 mm3,1 closed solid/28 faces/74 edges, flatØ2 tip areaπ mm2, identity transform and1111 BRep containment checks. All281 axial comparisons repeat at0.5 mm and differ at0.25; sampled physical right-hand quarter-turn/0.125-mm correspondence passes80/80. Slot/cone probes use0.01 mm and axial thread sampling0.025 mm; this is sampled geometry, not physical nut-fit/strength/continuous-contact certification. Coverage is1 standalone body/zero inter-part pairs, not the installed assembly.

Actual [Fusion view](../models/jog-retainer/A/JW-H05P_Rev_A_fusion-view.png) was saved directly from the native viewport, opened/visually inspected and independently verified as1800×1400 PNG,560911 bytes, SHA256 `7562e51bd9633d2aefc8c541ab9b0bd0a726f69051572770771c8866d260bffd`. [Validation report](../models/jog-retainer/A/JW-H05P_Rev_A_validation.md) records all checks, thresholds, preserved-source snapshots and limits. Reviewed model geometry/pose snapshot SHA256 `cdae6439fc9e958d8da2d0543daf874b932ae10bc6e866323a1a0b4ee8d50752`.

Both pre-existing modified documents remain open; before/after geometry/pose snapshots and save states agree with the preceding approval entry. No source geometry/pose/visibility was changed. Initial failed API transactions rolled back; final native history has only the7 intended items and no extra bodies. The new retainer remains active in its review view, with construction geometry hidden. Explicit **JW-H05P Model Rev A** approval is pending before STL/STEP/F3D. PLA/PETG fit, locking/holding, print settings/envelope and physical strength remain unverified.

## Engineer approval: JW-H05P Model Rev A for standalone trial exports

The engineer explicitly selects **“Zatwierdzam Model JW-H05P Rev A”** after the actual Fusion view and validation report. Approved scope: the reviewed single PLA-trial screw, snapshot `cdae6439fc9e958d8da2d0543daf874b932ae10bc6e866323a1a0b4ee8d50752`, for **STL in mm, STEP and editable F3D archive in `models/`**, without cloud-saving the active document. Drawing geometry/material approval remains as recorded. This does not approve the full jog, slicing/print process, physical nut-fit/strength or anti-loosening/functional use. Both pre-existing modified documents must remain untouched.

## JW-H05P Rev A verified export handoff and accepted STEP limitation

Actual exports after model approval: `models/JW-H05P_Rev_A.stl`, `.step`, `.f3d`, alongside the actual Fusion PNG and validation report. Binary STL explicitly uses mm/native High;27790 triangles,1 connected closed oriented manifold,0 invalid edges/degenerates/facet normals, Euler2, bounds2.926999568939209×2.927000045776367×12 mm. No triangle self-intersection/slicer/physical claim.

F3D28-entry CRC passes; actual Fusion reimport preserves7 healthy native timeline items,6 parameters,2 fully constrained sketches,1 named solid, physical right-hand M3x0.5-6g and native geometry/volume, with0 external references. STEP actual reimport retains component identity,1 closed solid,12-mm scale and565 thread/slot containment checks. STEP transverse bounds differ from native by+0.003730697179464393/+0.0024044569561993967 mm; the strict native-dimensional check did not pass and was not re-pinned as a silent PASS. The engineer explicitly selects **“Akceptuję STEP do próby”**, accepting the disclosed bounding-size difference for this trial only, not a maximum whole-surface error or production tolerance.

Repository/host byte counts and SHA256 match for all3 files:
- STL1389584 bytes: `5af9eb68e71c9fd38d2c906fcb78d041405f3487034aecff8e590d5857b53acf`.
- STEP444987 bytes: `612e713467a1c2b746d1350fdf8158c1bc3bf6cb6f8bd2780ce068fee704cc49`.
- F3D407209 bytes: `bef844277fa4bea66908d83afd0528741902f2c582dfed36f9f23d91c5e13940`.

Save-state chronology: all3 original documents were externally observed saved/clean immediately before export; retainer lineage `urn:adsk.wipprod:dm.lineage:1ytOtKlaQwOkwDA1qpFIkQ`. No assistant cloud-save call occurred. Existing source geometry/pose snapshots remained unchanged; retainer agrees with its approved snapshot when only the save-time root-label change is normalized. The full1111-check native smoke passed again after that state change.

The engineer explicitly chooses **“Zostaw kopie otwarte”** for the two unsaved/modified verification imports. They were not closed/saved by the assistant; the proper retainer was reactivated. A subsequent native document query reports0 open documents. The actor/cause is unobserved; do not infer user intent or reopen documents to undo it. Export files remain present and verified; no final cloud version number was retrieved. Task-controlled previews/scripts/staged drawing were removed; final drawing/source, concept, actual view, exports and report remain.

Status: **APPROVED for JW-H05P Rev A standalone nominal CAD/trial exports only**, including the expressly accepted STEP bounding-size limitation. No whole-jog/F.10/JW-SP01-model approval, physical fit/locking/holding/strength or complete print-process/build-envelope certification. Next owner: responsible engineer for slicing and PLA nut/driver/retention trials with agreed measurable criteria; PETG separately if adopted.

## Full jog modeling requested after retainer print handoff

The engineer reports **“Model idzie do druku”** for JW-H05P and requests the jog assembly modeled in Fusion, allowing reuse of the previous model or a rebuild. Record a reported print handoff, not a measured print/fit/strength result. The request does not explicitly approve a named consolidated jog drawing or provide a cloud-copy/save destination.

Repository remains `/Users/krzysztof.pedrys/Projects/OWN/GIT/redController`, drawings in `schematics/`, model views/deliverables in `models/`. Initial native query reports0 open documents. Opened only the known `Jog Wheel - Rev E` lineage for inspection; no geometry/camera/pose/visibility/save change. Current source is **version6**, saved/unmodified, Default Project folder `urn:adsk.wipprod:fs.folder:co.6dztQHPaTrCjgNI5HVOikA`,35 closed-body inventory/34 occurrences/134 healthy timeline items/2 as-built joints/4 rigid groups/0 external references. Fresh snapshot SHA256 `3cf69c643c9e59d97688820ab9794c70dff174f46bfccb24d9aaa01d00bbb9b3` is current evidence; do not assume historical version5 or treat order-sensitive snapshot differences as proven geometric changes.

Decision: reuse an independent native copy of the current Rev E rather than rebuilding unchanged geometry. Preserve source history/components/joints; adapt only documented changed interfaces. Proposed working revision **Jog Rev F.11**, reconciling the existing F.10 steel reference with the approved JW-H05P Rev A printed retainer and the existing JW-SP01 Rev A free-state spring definition. No arbitrary compressed-spring shape, vendor hardware detail, enclosure supports or fit compensation is authorized. Publish the synchronized complete drawing, obtain its explicit named core-scope approval and explicit cloud-copy destination before copying/mutating Fusion. No model approval/export permission follows from this task-start entry.

## F.11 preparation: printed-retainer upper-stop discrepancy — decision TBD

Read-only native Rev E v6 inspection confirms the carrier slot's horizontal faces atZ33.5/Z38.4, X19.8…23.2/Y1.5…3, with identity carrier transform. The obsolete housing feature `M3 retention head clearance - D5.7, seat Y13.5` remains present. No source geometry/pose/save was changed.

The approved printed JW-H05P has actual native majorØ2.927, not the old reference's nominalØ3 cylinder. With retained screw axisZ35, its lowest possible crest is35−2.927/2=**33.5365**, leaving **0.0365 mm** above the existing slot lower faceZ33.5 at nominal NUDGE. The new screw therefore cannot define the original upper-return contact at that pose. Do not hide this by retaining a software slider limit and claiming the physical stop/stroke is unchanged.

The F.11 working draft marks the upper-return decision **TBD**; no full drawing/model approval or copy has occurred. Proposed minimal correction for engineer selection: raise ONLY the carrier-slot lower face toZ33.5365 (carrierZL10.5365), preserving upperZ38.4, X/Y bounds, retainer/bore/nut axes and nominal1.5 travel. This is derived from approved inputs, not an FDM fit offset, and requires explicit geometric authority outside the previous retainer delegation. Alternative: explicitly accept the original slot and increased nominal mechanical travel1.5365, with no physical print/tolerance certification. JW-H05P already sent to print remains unchanged.

## Engineer selection: corrected carrier slot and Default Project copy destination

The engineer selects **“Popraw dolną krawędź rowka”**: change ONLY carrier-slot lower faceZ33.5→33.5365 (part-localZL10.5→10.5365), retaining topZ38.4/ZL15.4, X19.8…23.2/Y1.5…3, screw/bore/nut axis and nominal1.5-mm stroke. Derived opening height is15.4−10.5365=4.8635. JW-H05P already sent to print stays unchanged. This authorizes that exact drawing correction, not unbounded geometry changes or F.11 drawing/model approval.

The engineer also selects **“Default Project”** for **`Jog Wheel - Rev F11 - WIP`**, explicitly authorizing one independent native cloud copy in the current Rev E source folder after named drawing approval. Original lineage must remain unchanged. This does NOT authorize subsequently cloud-saving model edits. Preserve the approved standalone source parts/exports; perform the full assembly's own drawing/model gates.

## Published consolidated Jog Rev F.11 DRAFT for named drawing review

Published `schematics/Jog_Wheel_Rev_F11_DRAFT.pdf`, **18 searchable A3 pages**, and its editable Swift generator. F.10 PDF/source remain untouched as historical steel-process references. F.11 contains the complete retained mechanism/mounting, re-expressed carrier geometry with only the authorized lower-slot correction, current printed-retainer mapping, exact approved JW-H05P geometry and complete2-sheet JW-SP01 free-state construction. H05P's old standalone assembly-mapping page is not duplicated: current corrected mapping is on16, part geometry on17, so obsolete slot values are not carried as current instructions. Native source remains Rev E v6.

Executed checks: real generator, all18 pages open/render/searchable A3,11 exact body-region raster comparisons for unchanged/source-approved pages,5 protected source fingerprints, and nominal interface/slot-volume arithmetic guards. Current carrier PDF5, retention/sensor PDF9, BOM PDF11, build-order/limits PDF12 and corrected stop PDF17 were visually inspected; scope/axial/part-geometry pages and the complete layout were also reviewed. Carrier redraw uses the retained JW-E03 dimensions and the selected33.5365 edge only; original PDFs are not overwritten. No new geometric/model or physical-validation claim.

Separate `schematics/Jog_Wheel_Rev_F11_concept.png` is an LLM exterior label revision, not a Fusion view. Returned WebP opened; genuinely converted with sips, final PNG opened; signature and1402×1122 dimensions checked. Hidden retainer/spring are not invented or shown.

Publication fingerprints:
- F.11 PDF530409 bytes: `95b46910f1fc66fdb68e12f1d1a218b3c9eb15ffd0626802a2c20af8b75867ce`.
- Swift63004 bytes: `5f15ffc85fab50a4dbe3b2d4fa55ecdb7abe0823235c1dedec5cd50478677a2a`.
- Concept1540552 bytes: `b04c84e3778f039058ed54f0a085553b62011ad654f5e87a9c45cc87a041801d`.

Status: **CHANGES REQUIRED / named F.11 mechanical/core drawing approval pending**. Copy destination/name and exact carrier correction are already authorized; do not ask again for either. Enclosure supports, unspecified vendor fastener detail, actual switch behavior and deformed spring remain declared limits. The CAD must preserve the actual10-mm free spring instead of scaling it to the7/5.5-mm working gap; free-state overlaps are explicit state exceptions, not a collision-free physical assembly claim. Named model approval remains separate. No cloud copy/save, new assembly geometry or assembly export yet. Task-owned staged drafts/render scripts/images under `tmp/jog-f11/` are retained only during the ongoing modeling task and removed at its final handoff.

## Engineer approval: Jog Rev F.11 nominal mechanical/core drawing

The engineer explicitly selects **“Zatwierdzam rysunek Jog F.11”** for the published18-page PDF, SHA256 `95b46910f1fc66fdb68e12f1d1a218b3c9eb15ffd0626802a2c20af8b75867ce`. Approved modeling scope: retained Rev E mechanism with F.06 lower mounting, exact selected carrier-slot lowerZ33.5365, unchanged approved JW-H05P retainer and actual JW-SP01 free-state source without guessed deformation. Incomplete purchased geometry remains REF; sensor supports/wiring/enclosure and physical behavior are not approved.

The earlier explicit Default Project destination/name authority is now actionable: create one independent native `Jog Wheel - Rev F11 - WIP` copy of current Rev E v6, preserve the original and do not automatically cloud-save subsequent geometry edits. This is drawing approval only; the resulting named model and exports need their separate gates.

## Jog Model Rev F.11 created and validated — named model review pending

After named F.11 drawing approval, created the expressly authorized independent native copy **`Jog Wheel - Rev F11 - WIP`**, Default Project source folder, lineage `urn:adsk.wipprod:dm.lineage:J4sJMFovTt-NcLXXgyhdPw`. Initial native copy exactly matched Rev E v6. Source lineage `urn:adsk.wipprod:dm.lineage:F1uxEN30QRKxKmfpRlmCbQ` remains saved/unmodified, version6; canonical geometry/pose/history inventory before/after SHA256 `52c9d8cfb1ab9b6a8f1151e9e527ad1160202060ee71694c45f8930b1308410c`.

**Current copy edits are OPEN/UNSAVED. Cloud version1 is only the initial copied baseline, not the completed F.11 model.** No subsequent save authority was granted; do not save, close or discard automatically. Source remains separately open. Current review inventory fingerprint `680c6080820bc8e6dba017cb4f56767e7e7467d5426914171b153b7aa3ffd675` is not an F3D hash.

Implemented only approved nominal drawing scope: carrier floor raised0.0365 toZ33.5365 with0.186150-mm³ added volume; F.06 lower ears/holes, old upper ears/PCB posts/ribs/head recess retired in the copy; obsolete panel/hardware/reference components removed.21 retained non-root component geometry/feature inventories match source exactly, with only carrier/housing altered. Existing two joints/four rigid groups preserved.

JW-H05P Rev A source version1 and JW-SP01 Rev A observed source version2 were inserted with independent full native histories/parameters, no external links or flattening. Retainer is unchanged at approved mapping; spring stays actual10-mm free-state atZ14…24, not guessed deformation. Added exact supplied AS5048A whole-module envelope (supplier UV clocking reference only) and three approved floor boss regions/three maximum-envelope M2.5x6 instances. No full enclosure floor, sensor supports, guessed vendor details, four unspecified sensor/switch fasteners or wires are modeled.

Final computeAll/health:33 physical instance bodies/31 unique definition bodies, all solid;32 user parameters;123 root timeline entries/354 healthy leaf entries traversing two imported groups;0 unhealthy,0 external references. Native all-body interference scope528 candidate pairs at48 poses (s0/0.5/1/1.5 mm, rotation0…330 every30°),25344 pair-pose combinations, solid threshold1e-6 mm³. No unexplained positive pair. Explicit exceptions: six cover-screw/pilot engagements, three floor-screw/pilot engagements, five real free-state spring/working-carriage overlaps, and static lever/carrier overlap at pressed samples. These are NOT physical collision-free or spring/switch operation claims.

Ten independent temporary-BRep critical intersections at s0/1.5 all0 mm³. Native distances show retainer contact0 atNUDGE, lower-cover/housing stop contact0 at full1.5 press, minimum holder/module-envelope clearance1.0 mm and carrier/housing clearance0.3 mm.165 temporary-BRep pair-offset checks for11 unloaded carriage bodies versus housing/two switch reference bodies at+2/+8/+15/+25/+45 mm all0; excluded rotor, retainer, spring, enclosure and tools.288 nominal screw-seat boundary checks passed; source lower-countersink edge ligament1 mm and actual supplier minimum bearing/strength remain explicit limits.

Four actual Fusion PNGs in `models/`: assembled isometric, native Y0 sections atNUDGE/SCRATCH with free-state spring, and X21.5 retainer detail. Opened/visually reviewed; independently decoded in repository as PNG1400x1100 with signatures/hashes. Thus shared filesystem/file availability is observed. Role colors distinguish printed/purchased/machined/reference; section hatch colors are not a role legend. All visibility/pose restored to complete assembled isometricNUDGE/rotation0; temporary analyses removed, no inspection bodies remain.

Full results,33-body inventory coverage/omissions, positive-pair classification, nine printed-part quantities/materials/raw bounds, seat ligaments, fingerprints, actual paths and physical-test backlog: [`models/Jog_Wheel_Rev_F11_validation.md`](../models/jog-wheel/F11/Jog_Wheel_Rev_F11_validation.md). Raw boxes fit250mm, but no final orientation/support/margin/slicer build-volume PASS or physical/strength/function approval. Approved F.11 PDF fingerprint remains unchanged. Task-owned `tmp/jog-f11/` staging is removed before handoff; permanent evidence is the PDF/concept, four native PNGs and validation report.

**CHANGES REQUIRED / named Model Rev F.11 review pending.** No assembly STL/STEP/F3D export. No model, spring standalone or physical approval is inferred. Next authority: engineer to review the named nominal model and separately authorize saving current WIP in its existing Default Project folder; enclosure/support/hardware integration and physical trials remain declared downstream work.

## Engineer acceptance: Jog Wheel Model Rev F.11 nominal mechanical/core scope

The engineer replies **“Akceptuję”** to the explicit request to approve **Jog Wheel Model Rev F.11 in the presented nominal mechanical/core scope**. This approves the reviewed assembly geometry and its included printed-part definitions, including the unchanged free-state spring and retainer, with the documented static/reference exceptions and physical/integration limitations. Review inventory SHA256 `680c6080820bc8e6dba017cb4f56767e7e7467d5426914171b153b7aa3ffd675`; governing approved drawing SHA256 `95b46910f1fc66fdb68e12f1d1a218b3c9eb15ffd0626802a2c20af8b75867ce`.

Fresh pre-export inspection confirms that exact current inventory,33 physical bodies/32 parameters, active `Jog Wheel - Rev F11 - WIP`, modified/open, cloud version1. Rev E v6 remains separately open/unmodified. The generic acceptance is not treated as the separately requested explicit cloud-save instruction; no active-document save/close/discard. Export approved F.11 part copies and complete nominal assembly to agreed `models/` without overwriting existing artifacts. F3D archive export is permitted separately from cloud save.

Scope does not approve deformed-spring behavior, strength, print settings/orientations, complete enclosure assembly or physical function. It does not retroactively approve the separate standalone JW-SP01 source document/release; the included unchanged spring geometry is accepted as part of Model F.11 and its revision-matched part export. Export verification follows before marking delivery complete.

## Approved Jog F.11 export handoff — verification complete

Exported eleven NEW revision-matched files to `/Users/krzysztof.pedrys/Projects/OWN/GIT/redController/models/`: nine individual printed-part binary STLs explicitly in mm, complete nominal assembly `Jog_Wheel_Rev_F11.step`, editable `Jog_Wheel_Rev_F11.f3d`. No approved file overwritten, no cloud save or source geometry mutation. One transport response timed out; fresh inspection verified completed files and unchanged model rather than repeating writes.

Independent parser with five positive/negative tetrahedron self-checks validates all nine real meshes:1199198 triangles total; one connected component/positive signed volume each;0 boundary/nonmanifold/winding-invalid edges, nonmanifold vertex fans, duplicate/degenerate triangles or opposing/zero normals. Maximum native-bound coordinate difference0.000499725 mm. No global triangle self-intersection or slicer certification. Surface-deviation setting0.005 mm, normal deviation5°; STL interpretation must be mm. All eleven repository byte counts/SHA256 independently match the Fusion host.

STEP actually reimported:33 closed physical bodies/31 unique definitions,32 occurrences/31 components; component names/hierarchy retained, body labels become Body1/2/3. Centimetre declaration interpreted at correct mm scale.32 bodies match native precise bounds within1e-6 mm; corrected carrier floorZ33.5365/X19.8..23.2/Y1.5..3/area5.1 survives. Static STEP33-body/528-pair NUDGE check retains the same14 explained pilot/free-spring overlaps and retainer contact0, no new unexplained pair.

H05P-only STEP exception reproduces the earlier explicitly accepted standalone trial: installed bounds2.930730697×12×2.929404457 versus native2.927×12×2.927, transverse extent differences+0.003730697/+0.002404457 mm. Disclosed conversion/reimport difference, not a nominal design change, blanket assembly tolerance or strength/fit pass. STEP/F3D VeryHigh physical-properties comparisons are documented with their API±0.01% accuracy. Exact native F3D remains authoritative.

F3D82-entry archive CRC passes; actually reopened native inventory fingerprint exactly matches approved `680c6080820bc8e6dba017cb4f56767e7e7467d5426914171b153b7aa3ffd675`,33 bodies/32 parameters/123 root entries/354 healthy leaves/two joints/four groups/zero external references. Reopened slider−1.5 mm and rotor30° exercised, actual view inspected, carrier minZ21.5/platter maxZ58 confirmed, pose restored0/0 and354 healthy leaves retained. Main/source fingerprints unchanged; Rev E v6 still unmodified.

STEP SHA256 `7031fcee68d8885475aa89c0931854cca2c8cde9ec68a57f5dffdd5355cec5f5`; F3D `2ad796d52794efc6ab9e34b8a93bfe5b8ffedaf8e6d47d4ebd46eb3a8d6e710a`. Full eleven-file paths/bytes/hashes, mesh metrics, quantities/materials, round-trip evidence and remaining risks are in [`models/Jog_Wheel_Rev_F11_validation.md`](../models/jog-wheel/F11/Jog_Wheel_Rev_F11_validation.md).

Current model is persistently retained in the verified F3D, but active WIP remains modified and cloud version1 is still initial baseline. Two new modified/unsaved Untitled round-trip copies (F3D32 parameters/STEP0) are deliberately left open without save/close/discard authority. Main WIP reactivated, source preserved. Only task-owned file staging under `tmp/jog-f11-export/` is removed before handoff; existing final PNGs/drawing/concept/exports/report retained.

**APPROVED — Model F.11 nominal mechanical/core CAD and verified9-STL/STEP/F3D delivery, with the carried H05P-only STEP trial exception.** No physical, spring-deflection/force, final print-process/build-volume or full-enclosure approval. Next owner: engineer for slicing/setup, measurable fit/function trials and optional explicit cloud-save/verification-copy close instructions. Separate standalone JW-SP01 source/release approval is not silently inferred; included geometry is delivered under accepted Model F.11.

## Documentation consolidation and preservation — no engineering revision

The engineer requests one factual product-design document, one current TODO and clear drawing/status history without deleting files. Implemented `README.md` navigation, consolidated `DESIGN.md`, one `TODO.md` and `docs/ARTIFACTS.md`. Original DESIGN/TODO snapshots and retired DESIGN-TODO/DANE are preserved byte-for-byte under `docs/history/pre-consolidation/`, with original paths/hashes and source-to-task mapping documented there. Historical checklists are not active blockers.

`schematics/APPROVALS.md` stays at its existing path because retained generators/drawings and hash-pinned reviews cite it. Only a chronological-context/navigation introduction and this new entry are added; prior evidence and approval text are retained. Artifact lifecycle (CURRENT/SUPERSEDED/REJECTED/REFERENCE/UNKNOWN), approval scope and artifact role are separate. F.02 tall-column rejection is explicit; no other rejection or approval is invented from filenames. F.10's generic PDF filename and the historical one-page-PDF preservation gap are disclosed.

Actual documentation smoke: four source snapshots match their original byte counts/SHA256; all152 pre-existing artifact files outside this intentionally updated log retain aggregate path/content fingerprints (schematics59, schmatics53, models23, elements9, old_case8). Index covers all153 current files including this administrative log; no unregistered artifact.17 non-frozen Markdown documents/278 local links and anchors checked,0 broken; twelve unique actionable TODO IDs with acceptance criteria. The four frozen source snapshots retain their original root-relative link context as explicitly documented, not silently rewritten history.

No existing drawing/model/SVG/image/datasheet/export is moved, renamed, deleted, regenerated or numerically changed. No Fusion access/mutation/save/close, new engineering approval, geometry/physical/electrical test or manufacturing claim. The engineer reports beginning prints, not a passed physical trial. Future decision entries should be concise: named revision/artifact hash, engineer/source decision, approved scope, exclusions and evidence reference; detailed calculations/check output belong in the revision's report, not duplicated in this log.

## Authorized subsystem/revision filing migration — no engineering revision

Engineer instruction: “Odnotuj jak grupować nowe rewizje i gdzie je trzymać. Dodatkowo możesz poprzenosić pliki do nowej hierarchii.” Recorded filing/naming/package rules in the [project README](../README.md#package-and-naming-rules), preserving separate factual DESIGN, single TODO, artifact register and this single chronological log.

Relocated139 files from the old drawing/model locations into subsystem/revision packages, `elements/` or migration history; the single active log is now `docs/APPROVALS.md`. Retained118 moved payloads byte-for-byte, three macOS metadata files,23 original text snapshots and21 stationary source/history files. No destination was overwritten; the139 mapped source paths and empty `schmatics/` hierarchy are retired. The expanded legacy B02 bundle retains its original internal layout. [Exact path map, original snapshots and verification](history/hierarchy-migration/README.md) preserve historical references and original text hashes.

Working Markdown destinations and six Swift filesystem inputs/run instructions are adapted; drawing content, report technical text and historical approval decisions retain their original scope. Actually ran all six native drawing generators into temporary new files:69 pages match the retained PDFs in page bounds, searchable text, annotations and exact1684×1191 rendered pixels. Register coverage includes all153 engineering/governance artifacts; local navigation, original fingerprints and path-only source checks are recorded in the migration evidence. Temporary generated PDFs/checkers are not new releases.

This authorizes file organization only: no new drawing/model approval, dimensions, geometry, exports or manufacturing claim. No Fusion access, mutation, save, close or discard occurred. Historical inline paths and old JSON/PDF citations resolve through the map rather than being rewritten; original report/log text remains available in the frozen snapshots.

## Jog F.11 exploded Fusion PNG — 2026-10-16, presentation only

The engineer explicitly requests the agreed vertically exploded actual-Fusion PNG. Captured [Jog_Wheel_Rev_F11_exploded_fusion-view.png](../models/jog-wheel/F11/Jog_Wheel_Rev_F11_exploded_fusion-view.png),2200×3300 with transparent background, from the existing F.11 WIP lineage `urn:adsk.wipprod:dm.lineage:J4sJMFovTt-NcLXXgyhdPw`. Live cloud version2 was saved/unmodified at task start; this is a fresh observation, not an edit to earlier version1/unsaved historical reports. PNG SHA256 `02ae4f0879dc95e4d8337aa479c7424c7c50aa63bc3b7d17e28b730b87b3cb3f`,287271 bytes.

Used native temporary BRep copies/custom graphics for all33 instance bodies, preserving orientations and source appearances; main parts separated on Z, transverse hardware on its mounting axis, switch bodies kept together. Original body geometry, component transforms and joints were not moved. All32 parameters/123 root timeline entries/354 healthy leaves, body volumes/bounds/topology, joint positions and prior occurrence visibility passed before/after checks; camera/style restored and custom graphics removed. The successful capture-state fingerprint is `24ed7a351ed72eb8c0a92b362cce095042288a49b99fbe3b4838265f76483101` before and after; it is a new presentation-check schema, not the earlier engineering-review inventory schema. [Exact display translations and check scope](../models/jog-wheel/F11/Jog_Wheel_Rev_F11_exploded-view.json).

Fusion nevertheless marks the document modified after temporary custom-graphics creation/deletion. That dirty flag remains; no cloud save, close, discard or permission-reset action was performed. Geometric/parameter comparison against the initial read-only inventory passes. Spring remains the free-state shape; switch/sensor/hardware and floor-boss reference limitations persist. The floor boss regions do not become separate printable parts. This PNG is a presentation of the already approved model, not a new geometry revision, validated insertion sequence, spring simulation or physical function/strength approval.

## Rev A spring fracture report and selected PETG repeat — 2026-10-16

The engineer reports good Rev A spring dimensions and brief jog operation/travel before the spring broke apart. Actual failed print: Bambu PLA, Bambu Lab P2S, 0.20 mm layers, 2 wall loops, reported standard PLA nozzle-temperature setting. Numeric nozzle temperature, exact PLA variant, print orientation, cycle count and measured travel are not supplied. The [supplied fracture photograph](../broken_spring.png) is retained at its original repository path. The photograph does not establish a bulk-material versus interlayer failure mechanism; this is not a physical acceptance of the complete jog or a PETG test.

After reviewing material-repeat versus new-geometry routes, the engineer explicitly selects **“Rev A w PETG”**. Scope: repeat the unchanged spring geometry in its already specified PETG, using the existing approved F.11 [C02 spring STL](../models/jog-wheel/F11/Jog_Wheel_C02_Spring_Rev_F11.stl), interpreted in mm. Retain nominal jog travel 1.5 mm and all interfaces. No new spring drawing/model revision, geometry change, standalone source-release approval, export, cloud save or overwrite is authorized or performed by this choice.

The next physical trial belongs to the engineer. Record actual PETG grade/profile, orientation, settings, observed return, measured travel and any permanent set/fracture; force, lifetime and pass thresholds are not invented. PETG durability remains unverified and the reported PLA failure does not prove its cause.

## Rev A PETG accepted for tests and final metal spring required

The engineer first reports that Rev A appears to be okay in PETG, then explicitly states **“Trwałość na testy jest wystarczająca. Natomiast docelowo trzeba będzie użyć sprężyny metalowej.”** Accepted scope: the printed Rev A PETG spring has sufficient durability for the current tests. Do not reopen that limited durability acceptance as a prerequisite to continuing those tests. No cycle count, force curve, measured travel, production lifetime or complete-jog physical acceptance is inferred.

The final spring must be **metal**; the printed PETG part remains a test substitute. No particular metal/alloy, manufacturer part, dimensions, force curve or mounting change is selected by this requirement. Actual component data and any affected drawing/model approvals are required before final integration. This does not authorize treating the current wave-flexure geometry as a metal manufacturing drawing, changing the approved Rev A/F.11 source, exporting a changed model or cloud-saving/overwriting anything.

## Enclosure selections and bounded local mounting delegation

The engineer reduces the current lighting scope to **20 LEDs,2 × 10, master VU only**. Keep MAIN_L/MAIN_R for the two retained R06 columns; remove the former deck-VU chains from the current functional/BOM/interface scope. The approved coordinate/PDF bytes and historical records are preserved; this decision does not move panel windows or approve a new aperture/diffuser.

The engineer explicitly confirms **Raspberry Pi DAC Pro** and selects the supply described by [elements/05839_datasheet.pdf](../elements/05839_datasheet.pdf), replacing Anker. [Catalog item5839](https://botland.store/built-in-power-supplies/5839-mean-well-rs-25-5-power-supply-5v5a25w-4711287433578.html) identifies **Mean Well RS-25-5,5 V /5 A /25 W**; supplied manufacturer p1–2 gives case78 × 51 × 28 and mounting/terminal/derating data. The family sheet includes other voltages; they are not selected. [DAC Pro manufacturer brief](https://datasheets.raspberrypi.com/audio/dac-pro-hat-product-brief.pdf), pp2–4, gives58 × 65, GPIO-header power and the mounting drawing; installed Pi/cooler/spacer height remains open.

Supply selection does not demonstrate full-load adequacy or release an exposed-terminal mains installation. RS-25-5 has AC/L, AC/N and FG: terminal protection, safe input/strain relief, protective earth, applicable protection/separation, ventilation and complete power/USB behavior remain to be defined/accepted. The20-LED current estimate is about1.25 A from the approximate retailer9 A/m claim, not a measurement or a full-system budget.

The selected USB/AUX is [Keple ASIN B0CJFR6BKW](https://www.amazon.pl/dp/B0CJFR6BKW), USB3.0 Type-A plus3.5 mm AUX, listed1 m. The engineer requests **the enclosure hole only** and handles cable routing. Preserve the approved nominal R06 U01 Ø27/location; no tailored cable ducts or new hole diameter are selected. The accessible product text and seven inspected gallery images did not provide dimensional mounting callouts; physical barrel/nut/clamping fit is not certified or estimated from pixels.

In response to the explicit request to delegate dimensions of new local printed supports, control axial retention and sensor/switch fastening while preserving approved interfaces, the engineer answers **“Tak”**. Basia may choose those local support/retention/fastener dimensions, record values and sources/derivations, and submit them in the next drawing. This does not authorize changes to retained R06/F.06/F.11 interfaces or purchased geometry, mains electrical design, a new named drawing/model approval, cloud save/overwrite or exports.

For the cap/optical group the engineer asks for an explanation; no new triangular-cap dimensions, aperture or diffuser are approved or delegated by that question. Current source interfaces remain. No Fusion operation, approved drawing rewrite or changed-model export was performed for these decisions.

Executed selection-update checks: the two10-LED chains cover all20 retained window IDs exactly once; the source-derived centred-strip proposal has maximum nominal centre offset0.25 mm. Retailer-scaled LED arithmetic gives1.25 A /6.25 W and a nominal3.75 A remainder from the rated5 A, not complete-load adequacy. Local-link smoke passed252 targets/33 anchors across five current canonical files plus this new log section; governing R06 PDF/CSV and F.11 PDF hashes are unchanged. Supplied PSU PDF SHA256 is `0bd509932f53c2d2b772018fc7c6d083624d867bdc0e42a2b423b2cd0920bba0`. The datasheet p2 PNG preview under task-owned `tmp/enclosure-choices-20261016/` was inspected and removed along with that directory; the product-inspection browser tab was released. No mains energization, module-fit, thermal, full-load or live Fusion test was performed.

## T-button head selection delegated and diffuser-first VU trial selected

The engineer explicitly answers **“Tak”** to Basia choosing the **T-button heads and their panel apertures**, while retaining the selected mating interface and R06 positions. Scope: choose the external triangular-head/aperture geometry and associated local fit/clearance, record the chosen values and source/derivation, and present them in the next named drawing. Preserve the source socket/stem interface, actual purchased switch geometry and retained control axes. The source R06 triangle symbols are not promoted to final cuts by this delegation; no specific new dimensions or drawing/model revision are approved yet.

For the master VU the engineer states **“spróbujmy wpierw z dyfuzorem”**: the first optical trial will use a diffuser for the existing20 LEDs/two10-LED master columns. This selects the trial route, not an optical material, thickness, LED-to-diffuser gap, fixture dimensions, measured uniformity or brightness acceptance. Keep the retained window positions; do not invent the unresolved optical stack or infer material availability.

Earlier local-mount authority and accepted PETG spring durability for tests remain unchanged. This is bounded selection authority and an optical trial choice, not permission to overwrite approved artifacts, modify Fusion before the drawing gate, cloud-save, approve a model or export changed geometry.

## Pi4 DAC Pro direct-header stack without cooling

The engineer confirms **Pi4 + DAC Pro without added cooling**, with DAC Pro directly seated on the normal Pi GPIO header. Existing DAC support spacers prevent bending; they do not raise the card above its connector-seated position. The Pi currently has no attached lower standoffs for enclosure mounting, to keep the assembly low. This does not select zero PCB-to-floor clearance or waive positive retention, underside-feature clearance, passive ventilation or thermal verification.

Supplied actual-component INPUTS: [IQaudio v32 guide](../elements/20201209%20IQaudIO_v32.pdf), DAC Pro p8 and assembly pp12–13; [Pi4 mechanical drawing](../elements/RP-008343-DS-1-raspberry-pi-4-mechanical-drawing.pdf), p1. Guide p12 normally supplies four9 mm support spacers/eightM2.5 screws for low-profile boards; do not count this as an additional9 mm lift or infer the user's actual spacer/assembled-height measurements. No software/configuration instructions in that guide were executed.

The identified existing Assets source `raspberry-pi-4-model-b`, lineage `urn:adsk.wipprod:dm.lineage:BrawI1P5TLKeZvG3oRxX-g`, version1, was inspected without copying, saving, modifying geometry or inserting it into an enclosure. It contains109 solid BRep instances/19 occurrences/19 component definitions including root and no mesh bodies. Native PCB85 × 56 × 1.6; fourØ2.7 mounting axes on58 × 49 agree with the supplied plan drawing. All109 modeled bodies contribute to source bounds(−42.5,−2.9,−28)…(46.49,17,30.4) mm; PCB lies inXZ with+Y up. Derived projection below PCB is2.1 mm; it is not a selected clearance and excludes added DAC/fastener/cable geometry. Native axis conversion for future use must be a proper rotation, not a Y/Z reflection. No source transform was applied.

Live session at task start: only `Jog Wheel - Rev F11 - WIP` was open/active, saved/unmodified, cloud version3, unitsmm, default Select command. Its33-body inventory/bounds/volumes matched before/after (`e7c72fbc8d41fe4d60ba009004e0b14194c34a93a323c90f296b8e45bf755619`); counts remained123 root timeline entries/32 user parameters, without a new parameter-value or feature-health audit. This is a new preservation schema/observation, not proof that cloud version3 is byte-identical to the delivered archive or a new geometry approval. The earlier version2 dirty-flag report is historical; no assistant save cleared it.

The asset was opened **invisibly** for inspection, preserving the active jog. The open request timed out; fresh document inspection verified that the saved/read-only asset had opened, so the write was not repeated and no timeout/configuration/permission change was made. Read-only PCB verification distinguished the four manufacturer-size mounting holes from47Ø1 pin holes after an initial overly broad classification assertion. The source stayed unmodified; after inspection it was closed only while saved/unmodified. Final session: original F11 WIP alone, active/saved/unmodified. No user-modified document was closed/discarded.

Coverage: native envelopes for all109 modeled Pi bodies, PCB scale and mounting cylinders; no BRep pair/interference, complete DAC-stack, plugged-equipment, physical fit, force or thermal test. Searches for DAC/IQaudio source geometry in Assets/across projects returned no matching files. Actual seated DAC maximum height and hardware interfaces remain explicit TBDs. Retain full purchased source geometry where available; no new enclosure/model approval, geometry mutation, cloud save or changed-model export is granted by these configuration inputs.

Final source/datum smoke passed: observed58 × 49 mounting pitch and2.1 underside arithmetic; proposed Rx(+90°) is orthonormal/right-handed and was not applied.263 local links/39 anchors passed across current canonical files plus this new record, and governing R06 PDF/CSV/F.11 PDF hashes are unchanged. Supplied Pi mechanical PDF:22819 bytes, SHA256 `a5c88057563016631ebca26666fd672614fc9aaa1c59128a541612c7798e9809`; IQaudio v32:2136960 bytes, SHA256 `bdb71b78ec1af3f14f1c5e0d6d81d133e6716a46c8451d3b4ad9243091fbae31`. Pi p1 and IQaudio pp8/12/13 were rendered/read for source annotations, not measured from pixels. All four task-owned PNG previews and `tmp/pi-dac-integration-20261016/` were removed after inspection; no temporary artifact is retained.

## Existing DAC spacer studs and rear ventilation request

The engineer clarifies that the existing DAC-to-Pi support spacers **terminate in male threads below the Pi**, intended to screw into supports in the enclosure. This is the case-mounting interface, not a request for an additional lower metal spacer stack. Actual thread designation/pitch and exposed length below the Pi PCB remain TBD; the generic IQaudio kit is not evidence of the user's exact hardware. Preserve the connector-seated DAC height and actual purchased parts.

Record an assembly constraint, not a validated sequence: four fixed male studs on a rigid board assembly cannot be simultaneously screwed into four fixed case threads by rotating the whole assembly. Candidate, subject to actual hardware/access: position Pi, screw each existing spacer individually into its case support, then seat/fasten DAC. Verify shoulders, engagement, underside clearance, tool access and reverse disassembly in the next drawing/model review.

The engineer will measure **Pi/DAC assembly dimensions and display geometry**. These inputs are pending with the engineer, not newly assumed geometry. Include spacer thread designation and exposed length below the Pi PCB when defining case-support engagement; remaining plugged/service envelopes must also be resolved.

The engineer requests a **rear ventilation opening with a decorative grille**. Basia proposes an **integral honeycomb grille** in the printed rear wall, without a separate frame/fastener assembly. This is a preliminary style/drawing-scope choice; opening position/size, cell/web/wall dimensions, perimeter and open area remain TBD. The existing no-added-cooler/fan choice remains in force. Verify the actual unobstructed passive air path; no additional inlet or fan is silently selected.

Keep ventilation access away from exposed RS-25-5 mains terminals/wiring; the decorative grille does not replace terminal guarding or establish touch protection. No thermal/throttling, structural, electrical or assembly-fit pass is claimed. These requirements enter [the integration definition](../DESIGN.md#rear-passive-ventilation-and-grille) and the next model-ready drawing; they do not approve a drawing/model revision or authorize Fusion geometry, save/overwrite or exports. No Fusion operation or deliverable export was performed for this clarification.

Documentation smoke for this clarification passed264 local targets/42 Markdown anchors across the five current canonical navigation/specification files and this new log section. Governing R06 PDF/CSV and F.11 PDF hashes remain unchanged. No task temporary files were created; checks did not exercise CAD geometry, assembly fit, airflow, thermal behavior or electrical protection.

## Pi/DAC and display measurements — 2026-10-17

Engineer-supplied measurements: **Pi4 + DAC Pro maximum height36 mm; projecting spacer thread length4 mm; display external276 × 76 mm; display intrusion into the enclosure17 mm**. The4 mm projection answers the previous request for exposed thread below the Pi PCB; actual thread diameter/pitch remain unknown. The36 mm lower measurement datum and inclusion/exclusion of the projecting studs are not specified, so no support/floor Z or thread engagement is derived from them yet.

The engineer requests a display opening “2 mm smaller than its dimensions.” Literal subtraction from the overall width/height gives274 × 74, with1 mm nominal centred overlap per edge; retained R06 D01 is272 × 72, with2 mm per edge. Record the discrepancy and obtain the intended size rather than silently selecting one. Preserve D01 centre (300,46.25) and approved R06 PDF/CSV; any changed opening belongs to the next named drawing revision, not an overwrite.

These are component inputs and an unresolved opening instruction, not approval of a named enclosure drawing/model. Display17 mm is its stated enclosure intrusion, not a complete rear/plug/mount profile. No Fusion operation, save, revised drawing artifact or model export was performed for this measurement update.

Executed measurement-update smoke:265 local link targets/43 Markdown anchors passed; R06 CSV D01 remains272 × 72 at (300,46.25), and both alternative opening/overlap calculations agree. Governing R06 PDF/CSV and F.11 PDF hashes are unchanged. No CAD/physical/thermal/electrical check or temporary file was involved.

## Pi/DAC height datum and spacer designation clarified — 2026-10-17

The engineer explicitly confirms **36 mm from the lower surface of the Pi PCB laminate to the highest DAC Pro element** and supplies spacer designation **M2.5×10+6**. Retain the earlier measured **4 mm exposed thread below the Pi PCB**; do not silently replace it with nominal “+6” or add the spacer body length again above the connector-seated DAC. No new spacer or hole geometry is selected by this clarification.

For PCB underside datum Zb, the highest DAC point is Zb+36 and the measured stud tip is Zb−4:40 mm between those points. This is a derived reference, not a selected support height, full installed-body validation or a40 mm free-space requirement above the supports; the stud enters its support.

For the display opening the engineer requests an explanation, not a selection. The overall2 mm reduction is shared by opposite edges:274 × 74 gives1 mm overlap per edge, while retained272 × 72 gives2 mm per edge. Neither proves rear-body passage, active-image visibility, retention or strength. Keep both as alternatives pending the intended overlap; preserve R06. Current records close the height-datum/spacer-designation questions only. No named drawing/model approval, Fusion operation, save or export occurred.

Clarification smoke passed265 local targets/43 anchors, centred opening-overlap arithmetic and36-above/4-below/40-endpoint-span calculations under translated PCB datums. R06 PDF/CSV and F.11 PDF hashes are unchanged. Coverage is documentation/source arithmetic only, not CAD, assembly fit, thermal or electrical validation; no temporary file was created.

## Display overlap confirmed — 2026-10-17

The engineer explicitly confirms **2 mm overlap on every display edge**. With external276 × 76 mm, the derived opening is **272 × 72 mm**, matching retained R06 D01 at (300,46.25). The alternative274 × 74 interpretation is not selected; the opening-choice blocker is closed. Preserve R06 artifacts unchanged. This confirms the dimensional input only, not rear-body passage, active-image visibility, retention, complete enclosure drawing/model approval or permission to save/export. No Fusion operation or artifact export was performed.

Verification:266 local targets/44 anchors passed; confirmed overlap arithmetic matches the unchanged R06 CSV opening/centre. R06 PDF/CSV and F.11 PDF hashes are unchanged. Documentation/source checks only; no physical fit, active-image or retention test.

## Preliminary installation layout L01 — 2026-10-17

The engineer requests proceeding with the **2D installation arrangement**. This authorizes the preliminary diagram scope, not new Fusion geometry or approval of a complete enclosure drawing/model. Delivered [three-sheet A3 L01 PDF](../schematics/enclosure/L01/DJC_Installation_Layout_L01_DRAFT.pdf), [editable source](../schematics/enclosure/L01/DJC_Installation_Layout_L01_DRAFT.swift) and [verification evidence](../schematics/enclosure/L01/DJC_Installation_Layout_L01_validation.json). L01 is **CHANGES REQUIRED / NOT APPROVED / NOT MODEL-READY**.

Source-derived position proposals: Pi PCB centre table(100.25,50), midpoint from U01 opening right edge38.5 to display exterior left162 and rearY0 to platter rearY100; PSU case centre(519,50), midpoint of display exterior right438/panel right600, supplier terminal side rotated toward+X. These are review proposals, not selected safety/cable allowances or validated actual-equipment envelopes.

Under existing local-mount selection authority, Basia proposes reusing6 mm support height above floor-top referenceZ2 for Pi: PCB undersideZ8, measured DAC maximumZ44, existing4 mm stud tipZ4. Actual support widths/threads and effective engagement remain undefined; the nominal bare-Pi underside/floor budget3.9 is not strength/fit acceptance. The2 mm floor continuation is a study reference, not a newly released shell.

Review finding: nominal B01–B05 body projections overlap bare-Pi bounds; B06–B10 overlap PSU/terminal bounds.48 nominal B-body projection pairs and3 equipment/display-front box pairs were checked, not all bodies. The7.98 Pi maximum-level/panel-underside budget excludes actual control/support/terminal/wire geometry; no solid collision or assembly-fit pass is claimed. Preserve all R06 controls, both full jog poses and6 existing floor axes. Unknown DAC/display/controller/guard/service geometry stays TBD, with no made-up purchased body dimensions.

Executed: Swift/CoreGraphics generation, native PDFKit reopen as3 A3 pages and rendering, all-sheet visual review, independent datum/coordinate/height/projection arithmetic, source hash preservation and page-bounds assertions. Corrected the plotted panel transition atY120 before final review. Temporary CSV-column assertion failure was corrected against the14-column source without changing inputs or suppressing checks. Final PDF SHA256 `0c88bfea5e22b6f53603f4fb4a2f10722d450527bc07fbf4bd3a74a328c8dbc0`. Five pinned inputs remained unchanged. All task-owned inspector/source-page/readability previews and `tmp/enclosure-layout-l01/` were removed; retained artifacts are PDF, editable Swift and evidence JSON.

No Fusion access or current save-state inspection, geometry/pose/camera mutation, cloud save, model export or physical/thermal/electrical test occurred. No SVG, duplicate-format drawing PNG or illustrative3D concept was generated for this2D-only stage. This does not waive the later complete drawing/concept, named drawing/model approval or verified-export gates.

Final registration smoke passed286 local targets/48 Markdown anchors. L01 contains exactly PDF, Swift and JSON; final PDF hash matches the reviewed evidence, all five pinned inputs remain unchanged, and the task temporary directory/previews are absent. No new approval is inferred.

## L01 rejected and internal rotation study L02 — 2026-10-18

The engineer rejects the L01 Pi/PSU positions beneath B01–B10 and requires relocating equipment so nothing from the top overlaps it in projection. Do not continue the old vertical-stacking argument or re-run it to dispute the engineer's observation. After the footprint tradeoff question, the engineer explicitly requires **first searching rotations inside the existing outline**; enlargement is only a possible later discussion after internal options are evaluated. No enlargement is authorized.

Delivered [L02 two-sheet A3 PDF](../schematics/enclosure/L02/DJC_Installation_Layout_L02_DRAFT.pdf), [editable source](../schematics/enclosure/L02/DJC_Installation_Layout_L02_DRAFT.swift) and [evidence](../schematics/enclosure/L02/DJC_Installation_Layout_L02_validation.json). **L02 is NOT APPROVED / CHANGES REQUIRED**, with the full mounted DAC/RCA outline unverified. L01 PDF/source/evidence are preserved byte-for-byte as REJECTED history, not overwritten.

Sampled rotations found a better internal bare-Pi candidate than the initial narrow rear strip: native bounding-box centre table(412,171.3),76.3° clockwise, between right jog and mixer. PCB centre is(412.693367,169.077554); native Rx(+90) followed by CAD-Z−76.3 would give the plan pose, but no Fusion transform was applied. Source body dimensions are unchanged. PSU combined92 ×51 case/14-max-terminal reference is rotated90° at(569.75,58), case centre(569.75,65), terminals toward rear−Y. This centre balances the known B08/right-edge references and rear mount-row datums; it does not choose guard/wire/thermal clearances.

Final checks cover121 published reference obstacles from108 R06 rows plus13 knob projections: display exterior, two fullØ100 platters, pot/cradle/knob references, B head/body/opening boxes, T source-cap/switch references, fader body/cap-travel bounds and35 mount-opening references. **0 overlaps in242 equipment/top-reference pairs plus1 mutual equipment pair**, all vertices inside600 ×300. Minimum nominal separating-axis bounds: Pi1.528931 to B17, PSU4.75 to B08/panel edge. These are not print allowances or complete physical clearances; actual fastener heads, final support footprints, final T heads/encoder knob, guard, wiring/plugs and service are not all defined.

The [manufacturer DAC Pro brief](https://datasheets.raspberrypi.com/audio/dac-pro-hat-product-brief.pdf) pp3–4 was read and p4 rendered for annotations. Board/form-factor dimensions do not dimension the RCA overhang, so no complete DAC envelope was inferred from them or from pixels. **Required before accepting Pi/DAC placement: actual mounted DAC/RCA plan extents registered to Pi PCB.** Existing36 mm height, M2.5×10+6 designation and4 mm exposed thread remain closed inputs. The bare-Pi-only zero-overlap result is explicitly not certification of the complete stack.

Executed coarse search: integer angles0…179°/2 mm position samples,4664008 Pi and4747318 PSU samples; local0.1 mm/0.1° refinement,1030301 samples per neighbourhood. This is sampled candidate discovery, not a global optimality/impossibility proof. Final T/encoder reference envelopes were stronger than initial search inputs and still passed. Native Swift/CoreGraphics generation and PDFKit reopen/rendering produced2 A3 sheets; both were visually inspected with readable plan/detail/limit annotations. Independent polygon-edge/circle-distance validation confirmed242 pairs plus1 mutual pair. Final PDF SHA256 `e67ec3919380c817f48b37633d3e9b0e5175b43857d9950d785c462c6fa6049e`;7 pinned current/history files remained unchanged.

Task-owned C++ search/compiled binary, search JSONs, inspector, manufacturer-PDF preview and readability PNGs under `tmp/enclosure-layout-l02/` were removed; retained artifacts are L02 PDF/Swift/evidence. Native TLS download succeeded without changing certificate validation/configuration after the Python TLS client failed; no dependency, permission or runtime-configuration change was made. No Fusion access/geometry/pose/camera/save, model export, physical fit/strength or thermal/electrical test occurred. No new SVG, alternate-format drawing PNG or illustrative concept was delivered for this2D-only stage.

Final registration smoke passed291 local targets/50 Markdown anchors. L02 contains exactly PDF/Swift/JSON, reviewed PDF hash matches evidence, all7 pinned current/history files remain unchanged, and the owned temporary directory is absent. Existing600 ×300 reference is retained; no enlargement or full installed-fit approval is inferred.

## Rear-button relocation R07 and reclaimed-left installation L03 — 2026-10-18

The engineer requests B01–B05 rightward toward the display, matching P01–P03 distance on the other side, and B06–B10 slightly leftward away from the PSU. This explicitly authorizes the relocation scope; it does not approve the resulting named R07/L03 drawings or any complete enclosure/model.

Assessment: mechanical design, Standard complexity, Medium criticality for the changed panel interface. Scope approval covers only these ten button axes; no enlargement, further control relocation or Fusion mutation. Basia owns drawing preparation/integration; the engineer retains dimensional/named acceptance. Dependency order: R06 source → R07 panel/complete CSV → L03 reference projection. Validation uses native PDF generation/reopen/render, all-sheet inspection, independent coordinate/projection checks and history preservation. Rollback is selection of preserved R06/L02 artifacts, not rewriting them.

Delivered [R07 two-sheet A3 panel PDF](../schematics/frontpanel/R07/DJC_frontpanel_R07_DRAFT.pdf), [complete coordinate CSV](../schematics/frontpanel/R07/DJC_frontpanel_R07_DRAFT_coordinates.csv), [Swift source](../schematics/frontpanel/R07/DJC_frontpanel_R07_DRAFT.swift) and [evidence](../schematics/frontpanel/R07/DJC_frontpanel_R07_validation.json). B01–B05 translate+37 X: top105/125/145 at Y43, lower115/135 at Y67. Nearest B03 X145 mirrors P-column X455 about display X300:17 mm from exterior or19 mm from opening. These are axis-to-edge distances; cap/cradle edge gaps differ. B06–B10 translate−17 X: top475/495/515 at Y43, lower485/505 at Y67; B06=455+existing20 mm pitch is the explicit draft choice. Both groups retain20 mm pitch,10 mm stagger and24 mm row separation.

Only global/local/Fusion X fields change in ten records; all98 other records, non-X fields and statuses retain source bytes. CSV `LEGACY` profiles remain provisional; placements are proposed. Panel600 ×300, D01 geometry, all other controls/splits, jog poses and floor axes remain unchanged. The generator's first run stopped at an LF-only assumption before publication; the parser was corrected to preserve the actual CRLF source separator. Final native generation and independent byte/hash checks passed without changing R06.

Delivered [L03 two-sheet A3 installation PDF](../schematics/enclosure/L03/DJC_Installation_Layout_L03_DRAFT.pdf), [Swift source](../schematics/enclosure/L03/DJC_Installation_Layout_L03_DRAFT.swift) and [evidence](../schematics/enclosure/L03/DJC_Installation_Layout_L03_validation.json). Reclaimed rear-left candidate: bare-Pi box centre(56,80),160° clockwise; PCB centre(58.285111,80.445301). Reference bounds are4.591838 to B01,5.047571 to JA platter and4.201389 to panel-left. PSU pose remains L02 centre(569.75,58),90°; B08 reference gap increases4.75→21.75 mm, panel-right margin remains4.75. These do not select manufacturing, wall, electrical or service clearances.

Executed Swift/CoreGraphics generation and native PDFKit reopen/render: two A3 pages per revision, all four visually inspected at2381 ×1684. Independent CSV checks confirmed ten X-only changes and98 byte-identical records with CRLF retained. Independent polygon/circle checks confirmed all242 equipment/top-reference pairs plus1 mutual pair, zero overlaps, panel containment and recorded gap bounds. Current PDF/CSV/source and all recorded R06/F.06/F.11/L01/L02 history fingerprints match. Self-review: APPROVED for this bounded draft publication and evidence, not engineer drawing/model acceptance or complete installed fit.

| Reviewed artifact | SHA256 |
|---|---|
| R07 PDF | `30ae294c542463522005f44fc2401ed008d31b06d23845e59995a3c65c7000ec` |
| R07 complete CSV | `50f510bf60eda4ea7b7b47fe656f29fa3a44e48e30fbf5d94b284160d844b368` |
| L03 PDF | `0fc60ff5656f3334bb812c2228c8f8f73812bce9832bf0e1d317def87b00cb65` |

R07/L03 remain NOT APPROVED / NOT FOR MANUFACTURE; R06 remains the unchanged approved baseline, L02 is superseded as a proposal, L01 positions stay rejected. The full mounted DAC/RCA XY envelope remains unknown: bare-Pi separation is not complete stack certification. Heads/supports/guards/plugs/service, final T/encoder geometry, physical strength/fit and electrical/thermal acceptance remain open. No new Fusion geometry/pose/camera inspection or mutation, cloud save, model export, new SVG, alternate-format drawing PNG or illustrative concept occurred. All four task-owned PDF-review rasters and `tmp/r07-l03/` were removed.

## Raised button layout R08 and horizontal Pi study L04 — 2026-10-18

The engineer requests four changes: raise B01–B05 until upper head edges align with the display top; align B04/B05 with B02/B03; exchange B06–B10 with P01–P03 and apply the same raised/column-aligned pattern; try horizontal Pi below U01. No screen lift or enlargement. This authorizes bounded draft scope, not named R08/L04 acceptance, manufacture or complete installed fit.

Assessment: mechanical design/documentation, Standard complexity, Medium panel-interface criticality. Integration/verification owner is Tadzio; engineering/named acceptance remains with the engineer. Dependency order: preserved R07 → R08 complete CSV/PDF → L04 projection study. Validation covers native PDF generation/reopen/render, all-sheet review, independent coordinate/reference geometry and immutable history. Rollback selects preserved R07/L03 without rewriting them; R06/F.06/F.11 approvals stay closed.

Delivered [R08 two-sheet A3 PDF](../schematics/frontpanel/R08/DJC_frontpanel_R08_DRAFT.pdf), [complete CSV](../schematics/frontpanel/R08/DJC_frontpanel_R08_DRAFT_coordinates.csv), [Swift](../schematics/frontpanel/R08/DJC_frontpanel_R08_DRAFT.swift) and [evidence](../schematics/frontpanel/R08/DJC_frontpanel_R08_validation.json). Selected14 ×14 R3 HEADs, rather than retained15 mm apertures, align to display exterior topY8.25: upper axesY15.25, lowerY39.25. Left columns105/125/145; lower125/145. Right columns455/475/495; lower475/495. P column515 retains Y21/49/77. Only thirteen coordinate rows change;95 other CRLF records and all IDs/functions/Parts/profiles/statuses remain byte-preserved.

Delivered [L04 two-sheet A3 PDF](../schematics/enclosure/L04/DJC_Installation_Layout_L04_DRAFT.pdf), [Swift](../schematics/enclosure/L04/DJC_Installation_Layout_L04_DRAFT.swift) and [evidence](../schematics/enclosure/L04/DJC_Installation_Layout_L04_validation.json). Horizontal bare-Pi box centre(47.6,70.8),CW0°, bounds X3.105…92.095/Y41.6…100; PCB centre(45.605,69.6). Nominal reference gaps3.1 to U01,3.109218 to JA and3.105 to panel-left. PSU pose unchanged. These are geometric reference gaps, not accepted wall/support/plug/service allowances.

Executed native generation and PDFKit reopen/render; all four sheets visually inspected at2381 ×1684. Independent checks passed thirteen coordinate rows/95 exact retained records,242 equipment/top+1 mutual pair,1797 moved-control/neighbour pairs, containment and all source/history fingerprints. Source inspection corrected one duplicate dictionary comma and removed publication-stale manual-review wording before the successful generator run. Self-review: APPROVED for bounded draft publication, not engineer revision or installed-fit acceptance. Four task-owned review PNGs and `tmp/r08-l04/` were removed.

| Reviewed artifact | SHA256 |
|---|---|
| R08 PDF | `a13ae4dc87645e9c3a995a93a3941de7dacf56477aeeb4adf9d08e9c6ba37760` |
| R08 complete CSV | `1b0bdd780f04d1432351dd5d1bea240384b9a1d76d5d7ce290c0e62354f47f29` |
| L04 PDF | `e31505bfbc30b24ee7dcd493a3408187677d4a6fc31e8335469dd9224179eff1` |

R08/L04 remain NOT APPROVED; R07/L03/L02 are superseded proposals, not newly rejected/approved. All predecessors remain unchanged. Full mounted DAC/RCA XY and connected U01/display, final supports/heads/fasteners/walls/guards/service remain unverified. Existing36 mm height, M2.5×10+6 designation and4 mm exposed thread remain closed. No Fusion access/mutation/save, model export, physical fit/strength, thermal/electrical test, SVG, alternate drawing PNG or illustrative concept occurred.

## U01 removal R09 and rearward Pi study L05 — 2026-10-18

The engineer requests five changes: remove U01 for now; move horizontal Pi rearward while retaining the panel-to-floor screw; shift B01–B05 by half B01 length toward the front; exchange B06–B10 back with P01–P03; apply the same forward shift to B06–B10. This authorizes the bounded draft, not named R09/L05 acceptance, manufacture or complete installed fit.

Assessment: mechanical design/documentation, Standard complexity, Medium interface criticality. Tadzio owns integration/final checks; engineer owns engineering/named acceptance. Dependency: preserved R08 → R09 CSV/PDF → L05 study. Prior local-support authority covers the proposed planar reserve; rollback selects preserved R08/L04 without rewriting any predecessor. No screen lift, enlargement or replacement U01 is authorized.

Delivered [R09 two-sheet A3 PDF](../schematics/frontpanel/R09/DJC_frontpanel_R09_DRAFT.pdf), [107-record CSV](../schematics/frontpanel/R09/DJC_frontpanel_R09_DRAFT_coordinates.csv), [Swift](../schematics/frontpanel/R09/DJC_frontpanel_R09_DRAFT.swift) and [evidence](../schematics/frontpanel/R09/DJC_frontpanel_R09_validation.json). U01 alone is removed; Keple installation is deferred. Both B groups shift+7 Y, half the selected14 mm HEAD rather than half the15 mm legacy opening: upper/lower axes22.25/46.25. Right B columns475/495/515 with lower495/515; P returnsX455 at retainedY21/49/77. Thirteen coordinate rows change;94 other CRLF records, all retained non-coordinate fields and all35Ø3.4 panel-screw holes/axes remain unchanged.

Delivered [L05 two-sheet A3 PDF](../schematics/enclosure/L05/DJC_Installation_Layout_L05_DRAFT.pdf), [Swift](../schematics/enclosure/L05/DJC_Installation_Layout_L05_DRAFT.swift) and [evidence](../schematics/enclosure/L05/DJC_Installation_Layout_L05_validation.json). Pi retainsX47.6/CW0°, moves32.1 mm rearward to centre(47.6,38.7), boundsX3.105…92.095/Y9.5…67.9; PCBcentre(45.605,37.5). S1-M1 remains(8,4). ProposedØ9 planar post/foot references use only B02 source line215 R4/R4.5, not old heights or installed-body approval. Chosen1 mm study gap gives rear edge4+4.5+1=9.5; another0.1 rearward leaves0.9, failing that allowance. This is a fixed-X bound, not a global optimum or certified head/tool clearance. PSU pose is unchanged.

Executed native generation/PDFKit reopen/render and all-four-sheet visual review at2381 ×1684. Corrected R09 detail text overlapping P03, regenerated only owned R09 outputs and reviewed the final sheets. Independent checks passed deletion/coordinate/byte preservation,310 equipment/reference pairs(240 base+70 proposed support)+1 mutual,2341 moved-neighbour pairs, containment, the chosen reserve bound and all source/history hashes. Self-review: APPROVED for bounded draft publication only. Four review PNGs and `tmp/r09-l05/` removed; no temporary artifacts retained.

| Reviewed artifact | SHA256 |
|---|---|
| R09 PDF | `213248c24a35c90eada40edb16ddd769bdaa5f7770269f0dba79701a8d215a09` |
| R09 complete CSV | `450c817f06eb3604d7a651698f797eaa082739277084aeb93b15b249050d9245` |
| L05 PDF | `2db4c9a69b759c345f142de24a08084e0597b01954dbf457f3d05c53ca047263` |

R09/L05 remain NOT APPROVED; R08/L04 are superseded proposals, not engineer-rejected. Approved R06/F.06/F.11 and all predecessor artifacts remain unchanged. Full DAC/RCA XY, plugged display, final installed supports/heads/tools/threads/walls/guards/service and physical/electrical/thermal acceptance remain open. The1 mm allowance is a new study choice, not a measured tolerance. No Fusion access/mutation/save, model export, physical fit/strength or thermal/electrical test, new SVG, alternate drawing PNG or illustrative concept occurred.

## Centred identifiers R10 and matched jog-edge alignment L06 — 2026-10-18

The engineer requests centred component IDs and rightward B06–B10 placement matching B01–B05 relative to each jog's right edge. This explicitly authorizes the bounded revision, not named R10/L06 drawing acceptance, manufacture or complete installed fit.

Assessment: mechanical design/documentation, Standard complexity, Medium panel-interface criticality. Tadzio owns integration, validation and self-review; engineer retains dimensional/named acceptance. Dependency order: preserved R09 → R10 CSV/PDF → synchronized L06 study. Rollback selects preserved R09/L05. No new supports, aperture selection, screen lift, enlargement, equipment relocation or Fusion mutation is in scope.

Delivered [R10 two-sheet A3 panel PDF](../schematics/frontpanel/R10/DJC_frontpanel_R10_DRAFT.pdf), [107-record CSV](../schematics/frontpanel/R10/DJC_frontpanel_R10_DRAFT_coordinates.csv), [Swift source](../schematics/frontpanel/R10/DJC_frontpanel_R10_DRAFT.swift) and [evidence](../schematics/frontpanel/R10/DJC_frontpanel_R10_validation.json); [L06 two-sheet A3 installation PDF](../schematics/enclosure/L06/DJC_Installation_Layout_L06_DRAFT.pdf), [Swift source](../schematics/enclosure/L06/DJC_Installation_Layout_L06_DRAFT.swift) and [evidence](../schematics/enclosure/L06/DJC_Installation_Layout_L06_validation.json).

B06–B10 translate+10 X only: upper485/505/525, lower505/525; Y22.25/46.25 retained. Only global/local/Fusion X fields in five records change;102 other CRLF records remain byte-identical. Right edges of fullØ100 JA/JB platters are X160/540. All five left/right pairs repeat the same signed edge offsets with translation(380,0), without reflection; nearest14 mm HEAD edge gaps are8 mm, legacy15 mm aperture gaps7.5 mm. All other geometry, U01 absence and Pi/PSU poses remain unchanged.

Existing component IDs are centred in both axes on overview/detail sheets; tiny LED/mounting-hole IDs remain unlabelled and Hn/Kn axis callouts remain offset. PI06 anchors to the reference envelope, PS06 to its physical case. Native Swift/CoreGraphics generation and PDFKit reopen/render passed. Parent inspected all four final2381×1684 sheets. A separate PDFKit process independently measured122 actual text-selection centres against CSV/equipment/page anchors: maximum deviation0.136913 mm, below the0.5 mm presentation threshold; this is not a mechanical tolerance.

Independent consumer checks passed all five X-only changes/102 exact retained records,310 equipment/reference pairs(240 base+70 proposed support)+1 mutual,760 moved-control/neighbour pairs, containment and all current/source/history hashes. PSU/B08 represented separation decreases21.75→11.75 mm and remains positive. L05 Pi/PCB/PSU geometry, mounting axes and35 proposedØ9 reserves are unchanged; the inherited1 mm Pi reserve remains a study allowance. Self-review: **APPROVED for this bounded draft publication and evidence only**. Four task-owned review PNGs and `tmp/r10-l06/` were removed; no temporary artifacts remain.

| Reviewed artifact | SHA256 |
|---|---|
| R10 PDF | `f5420c7321ce19c8c5a8170115d601225e178a73dae4b33358f9a1669188584d` |
| R10 complete CSV | `8a44c5dc687a4d1770ab917aa137ec2bd2db41ee3946a8237126952266d0b588` |
| L06 PDF | `64bfaee7a7c3fa5981ef414efda94b74b4ba61521d83d1126b19ce762ab79ff0` |

R10/L06 remain NOT APPROVED; R09/L05 are superseded proposals, not engineer-rejected. All predecessor artifacts and approved R06/F.06/F.11 remain unchanged. Full mounted DAC/RCA XY, plugged display, installed supports/heads/tools/threads/walls/guards/service and physical/electrical/thermal acceptance remain unverified. No Fusion access/mutation/save, model export, physical test, new SVG, alternate drawing PNG or illustrative concept occurred.

## Installed jog outlines L07 — 2026-10-18

The engineer identifies L06's JA/JB circles as platter projections and explicitly requests the proposed correction: distinguish the dashedØ100 platter from the installed housing, lower ears and floor bosses. Scope authorizes this drawing correction only; no equipment relocation, panel change, support redesign or Fusion operation.

Assessment: App/drawing documentation, Standard complexity, Medium mounting-interface criticality; explicit scope approval is present. Tadzio owns source integration, validation and self-review; engineer retains named drawing/model acceptance. Inputs are unchanged R10 coordinates, L06 equipment/reference poses and approved F.11 housing/mounting dimensions. Output is a new L07 PDF/editable Swift/evidence package. Dependency: verified F.11 local geometry and+60° CAD-Z transform → L07 projection → native generation, independent geometry checks and sheet review. Rollback selects preserved L06; R10, L06 and approved baselines must remain byte-identical.

Delivered [L07 two-sheet A3 PDF](../schematics/enclosure/L07/DJC_Installation_Layout_L07_DRAFT.pdf), [editable Swift](../schematics/enclosure/L07/DJC_Installation_Layout_L07_DRAFT.swift) and [verification evidence](../schematics/enclosure/L07/DJC_Installation_Layout_L07_validation.json). Solid dark silhouettes include theØ50 core, switch shelf, bridges and lower ear caps; the full-height local housing projection is67.046788 ×61 mm. Dashed greyØ100 remains the platter-only conservative reference. Dashed blueØ10 floor bosses, solidØ2.9 ear holes and dottedØ2 trial pilots share the six retained F.11 named axes. Whole-jog+60° applies to all features, including the switch shelf; tableY reverses CADY.

Executed native Swift/CoreGraphics generation, PDFKit reopen/render and parent visual review of both2381 ×1684 sheets. Independent source-derived checks passed16 circle/rectangle part envelopes, six F.11 mounting axes and32 Pi/PSU-to-part pairs, minimum represented separation31.762169 mm. Every part envelope stays inside its retainedØ100 reference. L06 equipment/PCB/terminal geometry,155 reference obstacles,35 proposed panel-post reserves and310+1/760 check records match exactly. All current/source/history hashes match.

Final-PDF surface checks passed57 actual text-selection centres(max0.081984 mm versus0.5 mm presentation threshold),15 physical-boundary raster probes and3 exterior probes. Independent native curved-path bounds use0.01 mm drawing-comparison allowance only; no mechanical tolerance is inferred. Six canonical documents passed410 local targets/64 anchors before adding these three delivered-file links. Two owned review PNGs and `tmp/l07/` were removed; no temporary artifacts remain.

| Reviewed artifact | SHA256 |
|---|---|
| L07 PDF | `c936eeb0684feee7936447882e3772a8dc5bdb85a73fbbf7a17130d8acf5c5a8` |
| L07 Swift source | `01e3145b95e3804bf5df71153f373ccdefadc317fbbdbe808e4862f770efd17d` |

Self-review: **APPROVED for this bounded drawing publication and evidence only**. L07/R10 remain NOT APPROVED by the engineer; L06 is superseded presentation history, not newly engineer-rejected. R10, L06, all predecessors and approved R06/F.06/F.11 remain unchanged. Full DAC/RCA, plugged display, final installed supports/heads/threads/tools/wires/guards/service and physical/electrical/thermal acceptance remain open. No Fusion access, model mutation/save/export, new support selection or physical test occurred.

## Uniform button colours R11 and L08 — 2026-10-18

The engineer explicitly requests matching B06–B10 colours to the other buttons on both current drawings. Scope is presentation only: remove obsolete move highlighting from component outlines/IDs; preserve role colours for dimensions, HEAD/aperture references, equipment and warnings. No physical geometry, coordinates, mounting interfaces or equipment/support positions may change.

Assessment: App/drawing documentation, Standard complexity, Low criticality, reversible presentation-only scope. Tadzio owns integration/verification; engineer retains named drawing/model acceptance. Publish R11 panel and L08 installation from preserved R10/L07, updating only colour selection and revision/scope annotations. R11's complete CSV must be byte-identical to R10; L08 consumes that same schedule and retains L07 geometry. Validation: native PDF generation/reopen/render, all-four-sheet inspection, independent final-PDF colour checks and geometry/byte/history preservation. Rollback selects preserved R10/L07; no Fusion/model/export or physical operations.

Delivered [R11 two-sheet A3 panel PDF](../schematics/frontpanel/R11/DJC_frontpanel_R11_DRAFT.pdf), [complete CSV](../schematics/frontpanel/R11/DJC_frontpanel_R11_DRAFT_coordinates.csv), [Swift](../schematics/frontpanel/R11/DJC_frontpanel_R11_DRAFT.swift), [evidence](../schematics/frontpanel/R11/DJC_frontpanel_R11_validation.json), and [L08 two-sheet A3 installation PDF](../schematics/enclosure/L08/DJC_Installation_Layout_L08_DRAFT.pdf), [Swift](../schematics/enclosure/L08/DJC_Installation_Layout_L08_DRAFT.swift), [evidence](../schematics/enclosure/L08/DJC_Installation_Layout_L08_validation.json). B06–B10 now use the same component stroke/ID colours as the other buttons; both panel-detail groups retain identical blue HEAD/amber dashed LEGACY aperture roles. Current legends/revision labels identify the colour-only scope; the R09 comparison remains explicitly historical.

Executed native Swift/CoreGraphics generation and PDFKit reopen/render; parent visually inspected all four2381 ×1684 sheets. Independent final-PDF checks passed122 component-label centres(max0.136913 mm,0.5 mm presentation-only threshold),15 paired neutral ID-colour comparisons and20 overview button regions with neutral component-edge strokes and no obsolete warm highlighting. R11 CSV is byte-identical to all107 R10 records, including all fields/order/profiles/CRLF. Panel dimensions/label anchors and every L07 installed geometry/reference/check record match, including32 equipment/jog-part,310+1 reference and760 neighbour checks. All recorded current/source/history hashes match; R10/L07 and approved baselines remain unchanged.

Six canonical documents passed423 local targets/67 anchors before adding the seven delivered-file links above. Four task-owned review PNGs and `tmp/r11-l08/` were removed; no temporary artifacts remain.

| Reviewed artifact | SHA256 |
|---|---|
| R11 PDF | `6c0d4b651b6c8b98c27f47ccafd1071bda6e491a80ddb1faebfbbdc470e59d55` |
| R11 complete CSV | `8a44c5dc687a4d1770ab917aa137ec2bd2db41ee3946a8237126952266d0b588` |
| L08 PDF | `75e2c3fcff1a924c8144628712af28987276b49c6b07abdb22d1e62a87039818` |

Self-review: **APPROVED for this bounded presentation-only publication and evidence**. R11/L08 remain NOT APPROVED by the engineer; R10/L07 are superseded presentation packages, not engineer-rejected geometry. Full DAC/RCA, plugged display, installed supports/threads/tools/wires/guards/service and physical/electrical/thermal acceptance remain open. No physical geometry/position, Fusion/model/save/export, dependency or electrical behavior changed; no physical tests occurred.

## Corner headphone jack R12 and Pi relocation L09 — 2026-10-18

The engineer requests the supplied panel-mounted3.5 mm headphone jack above Pi in the left/rear corner, with equal offsets from the left/rear outer edges, retaining and clearing the corner screw; move Pi toward+tableY to make room. This authorizes the bounded interface/layout proposal, not named R12/L09 acceptance, complete installed fit or Fusion/model operations.

Assessment: App/mechanical drawing documentation, Standard complexity, Medium panel-interface criticality; the concrete addition/relocation scope is explicitly authorized. Tadzio owns integration, validation and self-review; engineer retains dimensional/named acceptance. Inputs: preserved R11/L08, supplied jack image, F.11 jog geometry and retained screw/post references. Dependency: verified dimensions/plan proposal → R12 panel/108-record CSV → L09 equipment study → native PDFs, independent geometry/byte checks and all-sheet review. Rollback selects preserved R11/L08; never overwrite predecessors or approved baselines.

Proposal contract: new J01 centre(14,14), axis normal to the rear upper panel, equal14 mm from left/rear outer edges; nominalØ6.2 trial aperture for M6×0.5. Supplied filename says PJ-392; drawing title block says PJD-035-77D. Use that supplied nominal geometry without asserting complete vendor/actual-part identification. BodyØ8.0±0.15 → maximumØ8.15; thread length4.5, shoulder/body length11.8, terminal extension6.5, nutØ8×1.8. With retained panel2, nominal residual thread is4.5−2−1.8=0.7; below-panel body/terminal reach18.3, giving terminal endZ37.7 from rear undersideZ56. No washer, extra spacer or invented cable envelope is selected; actual thread/chamfer/tolerance/plug/solder fit remains unverified.

Chosen planar study reserve is3 mm between known reference envelopes, not a manufacturing/tool/wire allowance. S1-M1 stays(8,4), nominalØ3.4 hole and inherited proposedØ9 foot: centre distance√136 gives J01-body/foot gap3.086904; equal13 mm offset would leave1.720630, so14 is the first integral-mm candidate meeting this chosen reserve. Pi retains X47.6/CW0°/88.99×58.4 and shifts+12 Y to centre(47.6,50.7), rear/frontY21.5/79.9; PCB centre(45.605,49.5), all four axes+12 Y. J01-body/Pi gap3.425; an11 mm shift would leave2.425. PSU, all107 existing panel rows,35 screw axes, jogs and all other equipment/support geometry remain unchanged. Full mounted DAC/RCA XY, actual screw heads/tools, plug/wire/service and electrical/thermal acceptance remain open.

Delivered: [R12 PDF](../schematics/frontpanel/R12/DJC_frontpanel_R12_DRAFT.pdf), [coordinate CSV](../schematics/frontpanel/R12/DJC_frontpanel_R12_DRAFT_coordinates.csv), [editable generator](../schematics/frontpanel/R12/DJC_frontpanel_R12_DRAFT.swift), [validation evidence](../schematics/frontpanel/R12/DJC_frontpanel_R12_validation.json); [L09 PDF](../schematics/enclosure/L09/DJC_Installation_Layout_L09_DRAFT.pdf), [editable generator](../schematics/enclosure/L09/DJC_Installation_Layout_L09_DRAFT.swift), [validation evidence](../schematics/enclosure/L09/DJC_Installation_Layout_L09_validation.json). R12/L09 are current DRAFT proposals, NOT APPROVED; R11/L08 are preserved, superseded proposals, not rejected baselines.

Executed checks: both native Swift generators completed successfully and PDFKit reopened/rendered both two-page A3 PDFs. Parent inspected all four final sheets; one overlapping R12 dimension label was corrected before final regeneration and review. Independent consumer checks confirmed the exact107-record R11 byte prefix plus the sole J01 addition, unchanged predecessor fingerprints and all retained geometry, and Pi-only translation(0,+12). Independent signed planar checks passed312 equipment/reference pairs plus one mutual pair,155 jack/neighbour pairs and32 equipment/jog-part pairs; candidate13/14 offsets and11/12 Pi shifts exercise the chosen3 mm bound. Independent final-PDF checks passed113 identifier centres(maximum error0.128684 mm, presentation threshold0.5 mm),14 raster boundary probes and20 button regions without obsolete warm highlights. Nominal mounting-chain arithmetic passed; these checks do not certify physical fit, tolerances or strength.

Self-review: APPROVED for publication of the bounded2D proposal, without blocking findings. Named engineer drawing acceptance remains pending; no Fusion/model access, mutation, save or export was performed. Actual jack identity, print/thread fit, screw-head/tool access, complete mounted DAC/RCA outline, plug/solder/wire/service envelopes, wiring/function, strength and thermal acceptance remain unverified. All four task-owned review PNGs and the empty `tmp/r12-l09/` tree were removed; no task temporary artifacts remain.

| Published artifact | SHA-256 |
|---|---|
| R12 PDF | `39c65af0b6ab1713600defacd1b1056da2e5a14c5806596d3672234ca1b9ffec` |
| R12 coordinate CSV | `13a9926564f874d7f20e2aff74f90b460e42c0f264cfaa15fac10c6c1432559e` |
| L09 PDF | `5e02df1260de63594ffd9258f2c40aaea851310e9c3750c044e414225665913e` |

## Engineer acceptance of R12 and L09; B09 height sections authorized

The engineer explicitly states “Akceptuję L09 i R12. Zrób przekroje wysokościowe i mocowania spodu.” This approves the published R12 panel layout/J01 proposal and L09 planar equipment placement, with their recorded reference-envelope, trial-hole and installed-fit limitations. Preserve the accepted PDF/CSV/source/evidence bytes and their existing DRAFT markings; this later decision supersedes historical pending-acceptance labels without rewriting them.

| Accepted artifact | SHA-256 |
|---|---|
| [R12 PDF](../schematics/frontpanel/R12/DJC_frontpanel_R12_DRAFT.pdf) | `39c65af0b6ab1713600defacd1b1056da2e5a14c5806596d3672234ca1b9ffec` |
| [R12 coordinates](../schematics/frontpanel/R12/DJC_frontpanel_R12_DRAFT_coordinates.csv) | `13a9926564f874d7f20e2aff74f90b460e42c0f264cfaa15fac10c6c1432559e` |
| [L09 PDF](../schematics/enclosure/L09/DJC_Installation_Layout_L09_DRAFT.pdf) | `5e02df1260de63594ffd9258f2c40aaea851310e9c3750c044e414225665913e` |

Assessment/contract: App/mechanical drawing plus documentation, Standard planning with cross-component coupling, Medium interface criticality; explicit authority covers the new B09 section/local-mount proposal. Tadzio owns design integration, validation and self-review; bounded helpers execute control and sensor definition slices, not maintenance/acceptance ownership. Engineer retains named B09 drawing and subsequent model acceptance. Inputs are accepted R12/L09, retained F.06/F.11 datums and existing purchased/native sources. Outputs are a new dimensioned PDF, editable generator, numerical mounting definitions and scoped evidence under `schematics/enclosure/B09/`. Dependency order: source/height chains and helper definitions → integrated sections/mounts → native generation/render, independent checks and all-sheet self-review → documentation. Rollback selects the unchanged earlier artifacts; no approved package is overwritten.

Retain floorZ0…2, jog baseZ8 and rear-panel slope: panel underside `50 + max(0,120−tableY)×0.05`, top+2. Z56/58 describe the rear edge, not every point of the upper panel. New local mounting dimensions may be selected under the previously recorded I3 authority; incompatible accepted apertures or missing purchased-part datums must be surfaced rather than silently changed or invented. Drawing work does not grant Fusion/model/save/export authority, mains design or an electrical/thermal/physical/strength pass. The complete-enclosure drawing gate remains separate from this section/local-mount package.

## B09 height sections and lower mounts published

Delivered the new six-file [B09 package](ARTIFACTS.md#enc-b09--current-height-sections-and-lower-mounts): [14-sheet A3 PDF](../schematics/enclosure/B09/DJC_Enclosure_Rev_B09_sections_DRAFT.pdf), [editable Swift](../schematics/enclosure/B09/DJC_Enclosure_Rev_B09_sections_DRAFT.swift), [equipment/post definitions](../schematics/enclosure/B09/DJC_Enclosure_Rev_B09_equipment.json), [control geometry/Z schedule](../schematics/enclosure/B09/DJC_Enclosure_Rev_B09_controls.json), [sensor/switch definitions](../schematics/enclosure/B09/DJC_Enclosure_Rev_B09_sensors.json) and [executed evidence](../schematics/enclosure/B09/DJC_Enclosure_Rev_B09_validation.json). This implements the authorized section/local-support drawing work; it does not close the complete installed enclosure gate. R12/L09 acceptance is recorded above and all accepted/predecessor files remain unchanged.

New selections under retained local-mount/I4 authority:35 slope-topped panel posts, Pi PCB/pad topZ8 with existing studs, PSU bottom pads/recesses at8.2,30 switch cups/retainers,13 fixed source-based asymmetric pot cradles,5 fader mounts, E01 cage/knob, four sensor support assemblies/conditional toe clamps and relieved switch saddles. Parent corrected a16mm T head that did not cover its aperture, selecting18.2/8x8R1.4 with0.537926 nominal cover. Parent directly inspected the pot image, enlarged the undersized legacy pocket to contain its asymmetric supplied-view union and removed side adjustment/towers/26 side screws and their obstructed approaches. New T cuts are pending B09 definitions; accepted R12 REFERENCE symbols are not rewritten. Retain source sockets, F.11 core/pose/six floor axes and U01 absence.

Executed evidence: native Swift generation and PDFKit reopen/render of14 A3 sheets; sheet review and corrected-sheet reinspection. Independent49 control chains,35 panel posts, eight sensor axes and six retained floor axes passed.809 conservative additive primitives across100 owners have no unexplained intersection in322239 cross-owner pairs;124 verticalD4 driver reserves clear98504 support-reference pairs.4013 equipment/jog-reference and65930 cap/source-motion pairs pass within declared coverage. Actual final-PDF checks cover49 rows/245 numeric cells and21 geometric features(19 outline probes plus four material/void samples). Source/reference thresholds and intentional same-owner/cavity/mount exclusions are recorded in evidence; none is a manufacturing tolerance or full BRep/connected/physical pass.

Self-review: **APPROVED for bounded section/local-mount publication only**. B09 named engineer acceptance remains pending. **CHANGES REQUIRED before complete installed/model-ready release:** actual display rear/retention/plug contacts, sensor laminate and clean contact lands, control mating/stroke/return/grip/terminals, complete DAC/RCA/electronics/connected geometry, real service tools, final shell/joints/splits/optics/ventilation and safe mains/USB/power definition. No unknown purchased geometry, default laminate, physical force/torque/strength or thermal acceptance is invented. No Fusion operation, model mutation, save or export occurred.

Preservation/cleanup: all220 earlier files under schematics/models/elements/old_case match their initial SHA-256 values, including all accepted R12/L09 source/evidence. Removed14 internal sheet PNGs, the supplied-PSU review PNG and empty `tmp/b09-sections/`; helpers left no temporary files. No new concept or alternate-format technical drawing is substituted for the incomplete full-enclosure/concept gate.

Final coverage addition: sheet04 also shows the retained jog/core/panel height references at NUDGE/SCRATCH, with nominal rear minimum gaps2.5/1.0. Parent inspected the final render and rechecked its three earlier boss/pilot pixel probes. Independent native-render hashes confirm all13 other sheets are exactly pixel-identical to the versions already reviewed/consumer-tested. Final source/PDF fingerprints below include this addition; final review previews were removed.

| B09 artifact | SHA-256 |
|---|---|
| PDF | `3ab67c4c913234afff870fa935fe88a4c80712acdef58ad30f95325871b76f80` |
| Swift | `d20d512d7e984671f83982b078e04f022f3335051ca1bb432905a015067266d1` |

## Engineer acceptance of B09 section and local-mount drawing

The engineer explicitly states: “Podoba mi się rysunek B09. Akcpetuję go. Co dalej?” This accepts the presented [B09 drawing](../schematics/enclosure/B09/DJC_Enclosure_Rev_B09_sections_DRAFT.pdf) in its nominal height-section/local-mount scope, including the18.2 triangular T heads and8×8/R1.4 passages. The accepted PDF SHA-256 is `3ab67c4c913234afff870fa935fe88a4c80712acdef58ad30f95325871b76f80`; source Swift SHA-256 is `d20d512d7e984671f83982b078e04f022f3335051ca1bb432905a015067266d1`.

Freeze all six B09 files and all predecessors byte-for-byte. Their original DRAFT names and pending statements record publication-time status; this later named acceptance supersedes those labels without regenerating or rewriting the accepted package. B09 T geometry is accepted; the complete panel drawing must incorporate it without changing R12 reference artifacts or seeking the same detail acceptance again.

Acceptance retains the drawing's explicit conditions and exclusions. It does not supply the unknown display rear/contact/connector geometry, AS5048A bare laminate thickness/clean clamp lands, actual control mating/stroke/return, complete DAC/RCA/electronics/connected geometry or real service-tool fit. Conditional sensor relations are accepted as drawn, not as measured actual-part dimensions. Complete walls/joints/print splits, optics, ventilation and safe mains/USB/power integration remain open. No complete enclosure drawing/model, Fusion operation, save/export, manufacture, physical strength or electrical/thermal release follows from this acceptance.

Next: close the actual display retention and sensor clamp inputs first, then the remaining installed interfaces; produce the complete reconstructible enclosure PDF plus separate illustrative concept for named approval before the corresponding Fusion model. Assessment for this acceptance update: Policy/Docs, Low criticality, documentation-only synchronization; no engineering package or geometry mutation. Tadzio owns record consistency and verification; the engineer retains complete-drawing and model acceptance.

## AS5048A laminate confirmed and display rear image assessed

The engineer explicitly confirms **AS5048A bare laminate thickness2 mm**, directs use of [the supplied dimension drawing](../elements/AS5048A_Fruugo_2626346230_dimensions.jpg) without an additional sensor photograph, and supplies [EP-0189-05](../elements/EP-0189-05.webp) for display retention assessment. Record this as a closed laminate input, not inferred from pixels.

Source correction: the sensor side view dimensions the laminate, with the IC projecting beyond it. Earlier accepted references incorrectly treated2 as the whole PCB-back-to-IC-face height. With retained ICface17.5 and assembled IC projectionh, PCB back is15.5−h, not15.5. The [ams datasheet](https://download.mikroe.com/documents/datasheets/AS5048A_datasheet.pdf), printed p34, gives package A≤1.20; this is not a measurement of the soldered module'sh. Direct substitutiont=2 at the old B09 seat gives toe top18.3 and holder gap0.2 versus its selected0.5 reserve; this is outside the conditionalt≤1.7 study, not proof of a physical collision or a revised-assembly clearance. A subsequent proposal must reconcile support/clamp/contact/cable geometry without silently shifting the IC face, reducing the retained jog stroke or modifying accepted files.

The display image shows the rear frame, driver PCB, FPC and port arrangement. It is sufficient for retention planning around the frame, not a dimensioned mounting interface or safe PCB-bearing permission. A rear-frame-clamp proposal still needs usable flat bearing width and its depth from the front bezel seating plane, plus actual plug/cable clearance. [52Pi EP-0189/P1126 documentation](https://wiki.52pi.com/index.php?title=EP-0189) reproduces this image but supplies no rear mounting dimensions; its catalogue body276.29×76.5(±0.1) is a separate reference. Engineer dimensions276×76, intrusion17, overlap2 and accepted opening272×72 remain unchanged.

Assessment: read-only mechanical/source assessment plus Low-criticality Policy/Docs fact synchronization. No new drawing geometry, CAD, model save/export or engineering approval is implied. B09's six files and all predecessors remain frozen; this record updates actual-part applicability, not historical acceptance. No sensor-photo request, invented IC projection/contact dimensions, physical contact/strength, electrical or thermal pass.

## Display rear-frame contact dimensions confirmed

In response to the illustrative A/B measurement diagram, the engineer states **“A - 2mm; B - 17mm”**. A is the usable flat width of the indicated rear-frame bearing band. B is the distance from the front bezel's panel-seating plane to that band's rear contact surface; its origin is not the front glass. These are explicit engineer measurements, not dimensions inferred from the product image. Both requested inputs are closed.

A is distinct from the existing2 mm front-bezel overlap. B is not an additional17 mm to add to the previously stated intrusion; use the actual seating-plane datum and installed slope when deriving the retention geometry. No uniform band around the whole perimeter, safe force/preload, final pad size, thread interface, connected/service fit or physical strength is inferred. Retain display276×76, opening272×72 and all accepted positions/artifact bytes.

Assessment: Policy/Docs, Low criticality, documentation-only input synchronization. Tadzio owns record consistency; no CAD, new drawing geometry, model save/export or manufacturing approval is performed. Next design work uses these inputs for frame retention and the separately required sensor support/clamp correction. New geometry remains subject to the applicable named drawing/model gates; no repeat A/B measurement or sensor-photo request.

## B10 display and sensor mounting-detail work authorized

The engineer requests “Domknij detale montażowe”, following the stated next scope: display rear-frame retention and corrected AS5048A floor supports/clamps. Explicit authority covers a new dimensioned B10 nominal drawing proposal and its source/verification package, not alteration of accepted B09/F.11/R12/L09, complete-shell release or Fusion/model/save/export work. Preserve accepted XY, whole-jog pose, nominal IC-face datum and1.5 stroke; display A=2/B=17 and sensor laminate2 are closed inputs.

Assessment: App/mechanical drawing plus project documentation, Standard-path, Medium nominal-interface criticality. Actual force, component/print tolerances, soldered IC height, safe contact and full connected fit are validation limits, not measured passes. A manufacturer-based nominal IC-height selection must be explicitly distinguished from a bought-module measurement; no hidden default or adjustment mechanism may replace missing evidence.

Execution/maintenance contract: Tadzio owns architecture, integration, the native PDF generator, final behavior checks, canonical records and self-review. Bounded helpers execute separate display and sensor numerical-definition slices only; engineer retains named drawing/model acceptance. Inputs: frozen B09/R12/L09/F.11, supplied component images, confirmed dimensions and cited hardware/package sources. Outputs: new numerical definitions, editable Swift, dimensioned PDF and executed evidence under `schematics/enclosure/B10/`. Integration order: source-backed local definitions → integrated drawing → native generation/reopen/render and independent geometry/presentation checks → documentation. No shared build/lint/test/format run while helper mutations are in flight.

Rollback is deletion of task-owned new B10 files and reversal of this task's canonical-document additions only; accepted source artifacts stay byte-identical. Temporary review artifacts, only where required, belong under repository `tmp/b10-mounts/` and must be removed before handoff. Existing user `test.svg` and other unrelated files remain untouched. No secret/governance/config edits, infrastructure/deployment or credential operations are authorized.

## B10 rear-insert display seating and depth explicitly selected

During detail design, unilateral rear pads were found insufficient to retain a top-inserted display against upward extraction. The earlier measurement illustration showed top insertion, but did not establish positive capture. Manufacturer P1126 specification sheet4 was inspected and supplies front outlines, not the missing front-keeper profile. No front thickness, adhesive bond or reverse seating was silently invented.

The engineer now explicitly selects **“Od wewnątrz obudowy”**: panel overlaps the display front edge, rear toes hold the display against the panel underside. A second explicit question asks whether the distance **from the front surface bearing on the panel underside to the identified rear frame land is17 mm**; engineer answers **“Tak, 17 mm”**. This confirms the actual rear-insert datum rather than assuming transfer from the earlier illustration. Keep A=2 mm, opening272×72 and all accepted XY. Rear-insert seating centre is the retained underside at(300,46.25,53.6875); rear bearing is17 inward along the inclined normal. The old B09 top-surface intrusion was a reference study, not this retention definition.

Updated approval scope authorizes the rear-insert nominal B10 proposal, new local floor columns/toes and necessary local floor driver galleries, with no front keepers or retained-panel/post changes. Tadzio retains integration/verification; display helper receives this updated concrete scope and all original safety/immutable-file restrictions. Named B10 approval, actual frame/contact/plug fit, strength, manufacture and Fusion/model/save/export gates remain separate.

## B10 display and sensor mounting details published

Delivered the new five-file [B10 package](ARTIFACTS.md#enc-b10--current-display-and-sensor-mounting-details): [six-sheet searchable A3 PDF](../schematics/enclosure/B10/DJC_Enclosure_Rev_B10_mounts_DRAFT.pdf), [editable Swift](../schematics/enclosure/B10/DJC_Enclosure_Rev_B10_mounts_DRAFT.swift), [display definition](../schematics/enclosure/B10/DJC_Enclosure_Rev_B10_display.json), [sensor definition](../schematics/enclosure/B10/DJC_Enclosure_Rev_B10_sensors.json) and [executed evidence](../schematics/enclosure/B10/DJC_Enclosure_Rev_B10_validation.json). B09 remains unchanged and governs its other mounts. Rear seating and reconciled17mm depth are engineer-confirmed inputs; **named B10 drawing acceptance remains pending**.

Display: four integral7×12 columns with side/end guides, two continuous1.9 rails each, four removable9×8×3 toes/1×8×1 bearing pads, reverse M3×8 with5 nominal thread/2 blind reserve/2 roof, four normalØ8 floor/column galleries. Cited real Wera2.5×50 bit fits the nominal gallery envelope. Right A2/B17 is measured; left mirrored pads and actual side engagement remain fit checks. No top keeper, retained panel/post change or adhesive is introduced; open shell/panel for9mm manual toe withdrawal. No closed-shell service or unknown complete display-body/plug fit is claimed.

Sensor: confirmed laminate2 plus explicitly selected nominal projection1.10 gives seat14.4, laminate top16.4 and retained nominal ICface17.5; toes top17.2 leave1.3 to the full-press holder. M2×6 remains outboard,5 engagement/2 tip reserve. Review reproduced floating inboard contact islands caused by a D2.4 through-cut spanning a narrowed2.4-wide toe. Removed the unnecessary locating relief: peg ends1.6 below the capped toe; no wider/taller clamp or adjustment mechanism was needed. Permanent generator material-path assertions and independent actual-PDF cap probes now pass. Nominal toe/back bearing overlap is2.678673 per side, not a strength result.

Checks executed: native generation/PDFKit reopen/render; six-sheet visual review and final corrected sensor-sheet reinspection, with the other four sheets pixel-identical. Independent72 new/789 retained conservative primitives,80736 counted cross-owner/reference/cap/driver pairs, source-axis/rail/pocket/thread/access/height/connectivity checks passed within declared coverage. Actual final PDF27 selected text cells/72 values and34 material/void probes passed; a raster boundary probe was moved off antialias fringe to known material/void interiors without changing source geometry or weakening colour criteria. Retained F.11 STEP clamp references were read in centimetres and converted×10; lower modeled reference remains7.8 above the toe at full press. No invented actual hardware-head extent or compressed-spring pass.

All216 engineering/source inputs, including all six B09 files, match retained hashes;11 Finder metadata records are excluded as volatile. Existing user `test.svg` is unchanged. Removed the entire task-owned `tmp/b10-mounts/` including native previews, vendor inspection copy and throwaway consumers. No secret/config/governance edits, new dependency, Fusion/CAD operation, save or model export.

Self-review: **APPROVED for bounded B10 nominal-detail publication** after the toe correction. This is not independent engineering acceptance. Actual soldered projection/tilt, contact/insulation, mirrored frame lands, thread/rail/toe strength, real harness/plugs/service, full shell/optics/vent/mains and physical/electrical/thermal gates remain open. The [P1126 manufacturer specification](https://wiki.52pi.com/images/c/c0/P1126-D3-V10-T3-11.26inch-capacitive-touch-display-specifications.pdf) was inspected; its front-outline drawing did not supply a substitute rear profile or override actual engineer dimensions.

| Final B10 artifact | SHA-256 |
|---|---|
| PDF | `8b6db90cad1bef22bc8ac9c8f9849f98ee7d40ed72211c5a5ea632df3c1abc57` |
| Swift | `c3c745d7b897fde758a445c0ee0099bab5523adcb88e73bc5d77452a2e2b6826` |

## Engineer acceptance of B10 display and sensor mounting details

After delivery of the six-sheet B10 mounting-detail drawing, the engineer states **“Wygląda dobrze. Akceptuję. Co dalej?”**. This is named acceptance of the delivered [B10 package](ARTIFACTS.md#enc-b10--current-display-and-sensor-mounting-details) for its nominal local display-retention and sensor-support scope. It closes the drawing-acceptance item left pending at publication; historical publication entries and package labels remain unchanged.

The accepted nominal definition includes rear insertion with the explicitly confirmed17 mm underside-seated depth and sensor seat14.4/ICface17.5 using the selected nominal IC projection1.10. Acceptance does not turn that projection into a measured soldered height or establish actual mirrored display lands, contact/insulation, printed retention/strength, installed plugs/service, complete-shell fit, electrical safety or thermal performance. Retain all previously stated verification limits and the nominal1.5 mm jog stroke.

Freeze all five delivered files at the fingerprints below, including their historical DRAFT names and pending-status evidence. No regeneration, rename or evidence rewrite is required. Every predecessor, including all six B09 files, remains unchanged. Current acceptance bookkeeping is Policy/Docs, Low criticality, docs-only; no engineering geometry, Fusion access, model/save/export or manufacturing authorization is added.

| Accepted B10 artifact | SHA-256 |
|---|---|
| PDF | `8b6db90cad1bef22bc8ac9c8f9849f98ee7d40ed72211c5a5ea632df3c1abc57` |
| Swift | `c3c745d7b897fde758a445c0ee0099bab5523adcb88e73bc5d77452a2e2b6826` |
| Display JSON | `bcbdfe1fec74a9a65de553ade8fc0703e15f928876e10af498b22fa8058ca5ae` |
| Sensor JSON | `7a1f33889a8e4195ec186b487c9117b0f2c3f0a2e83d362776040b341bd786dc` |
| Validation JSON | `6f299d2eefcdf5176d12ddb32f347a1b54c2f80e8f8fb5f7a1cb38373ef991e9` |

Next: close the remaining actual installed/connected inputs in MECH-02, then prepare the complete enclosure drawing and separate illustrative concept under MECH-03: floor/walls/panel interfaces, joints/print splits, hardware/assembly/service paths,20-LED diffuser stack and rear ventilation/mains guarding. Reuse accepted positions/mounts; do not restart the layout or re-request closed dimensions. Named complete drawing approval still precedes enclosure Fusion work; named model approval still precedes STL/STEP/F3D exports.

## Local OpenSCAD CLI selected for enclosure work

On2026-10-19 the engineer requests starting the stated MECH-02 installed/connected packaging review, with one change: try locally available **OpenSCAD through its CLI instead of Fusion360**. Basia owns source reconciliation and documentation integration. This authorizes the workflow change and preparation, not new dimensions, alteration of accepted artifacts, complete drawing/model approval, Fusion access/cloud save, fabrication or exports of an unapproved model.

Observed `/opt/homebrew/bin/openscad` resolves to `/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD`; `--version` returns2026.10.11. Version/help and a geometry-free stdin evaluation with `--hardwarnings --export-format echo -o - -` returned exit0; output includes `ECHO: "RED_CONTROLLER_CLI_PROBE", [2026, 10, 11]`. No product geometry or model files were created. CLI advertises STL/PNG but not STEP/F3D; mesh/PNG rendering has not yet been exercised for a product model.

The new editable source is `.scad`, and actual future model views use `_openscad-view.png` in the revision-matched model package. **No STEP/F3D waiver is inferred.** The final deliverable contract requires explicit engineer resolution or a permitted verified export route before complete handoff. No dependency/converter installation, flattened archive substitute or migration of approved F.11 is authorized. Named complete drawing approval still precedes enclosure modeling; named model approval precedes exports.

The [source-review findings](../DESIGN.md#installed-packaging-source-review) retain actual controller/harness/optical/mains gaps and the DAC manufacturer's65×58 versus65×57 outline discrepancy. Manufacturer kit illustrations are references, not actual stock or dimensional connected-fit evidence. No closed display/sensor/stack input is reopened and no physical/electrical/thermal pass is claimed. Existing Fusion state remains historical, uninspected this session.

Source-review verification: all532 local links and107 Markdown anchors across the six updated canonical documents resolved. All222 initial engineering/input files under schematics/models/elements/old_case plus user `test.svg` retained their SHA-256 fingerprints, excluding volatile Finder metadata; all five B10 files also matched the recorded approval hashes. Nominal LED calculations independently passed:62.5mm span,0.25mm centred end offset and4mm inter-strip gap. The task-owned DAC-page review PNG and `tmp/mech02-openscad/` were removed. No product mesh/PNG render, physical fit, electrical connection or thermal test was performed.

## Enclosure deliverables and integration scope confirmed

On2026-10-19 the engineer explicitly accepts the proposed OpenSCAD deliverables and supplies the following integration decisions. This supersedes the earlier open STEP/F3D and LED/harness prerequisites only in the stated new-enclosure scope; it does not approve a named drawing/model revision or authorize exports, changes to accepted geometry or Fusion operations.

1. **Deliverables accepted:** editable `.scad` with referenced inputs, separate printed-part STLs, actual model PNGs and a scoped validation report replace STEP/F3D for the new enclosure. Dimensioned PDF and separate illustrative concept PNG remain required. Existing approved Fusion/STEP/F3D artifacts are untouched.
2. **Controller inputs:** engineer identifies [ESP32-S3-DevKitC-1 v1.1 PCB reference](https://dl.espressif.com/dl/schematics/PCB_ESP32-S3-DevKitC-1_V1.1_20220429.pdf), supplies PCF8575 module plan32×21mm and CD74HC4067 module41mm length×18mm width×3.6mm height. Visual inspection of ESP PCB sheets1/3 and the matching manufacturer's dimension PDF reads62.74×25.40 plan,2.54 header pitch,1.27 side offsets and8.00 last-pin/end reference; no dimensions are scaled from pixels. Actual thickness/populated/pin-height and unprovided mounting details are not inferred. LED mechanics are deferred; hookup through ESP goldpin headers is intended, not an electrical-level/power approval.
3. **Audio/service/cables:** RCA outputs must be brought to the enclosure. ESP is programmed after opening the shell. Engineer instructs Basia not to work on cables/plugs and explicitly to assume the existing solution will not affect enclosure construction. Record that as engineer-owned non-impacting integration, not verified connected fit. Purchased panel RCA geometry/location and safe mains entry/guarding/strain relief/PE are not defined or waived by this assumption; USB/back-feed and physical/electrical validation remain separate.
4. **Optics deferred:** no diffuser selection/design now. Existing frontpanel LED apertures are sufficient for this stage and remain unchanged; no LED/diffuser/buffer-carrier geometry or optical-stack prerequisite is added. Earlier diffuser-first preference remains for a later trial, not the current shell scope.
5. **Mains entry clarification:** engineer asks what “inlet” means; no choice is made. Basia clarifies the physical mains cable-entry interface feeding the internal RS-25-5, not an air vent: fixed cable with retention/strain relief versus panel inlet for a detachable cable. No type, dimension, position or protection rating is selected.

All accepted R12/L09/B09/B10/F.11 packages retain their limited approvals and frozen bytes. [Current canonical scope](../DESIGN.md#current-enclosure-scope); [CAD contract](../DESIGN.md#enclosure-cad-workflow). No CAD geometry, model export, firmware/electrical implementation or physical/thermal test accompanies this documentation/source synchronization.

Executed checks for this update: six canonical documents passed537 local links/112 Markdown anchors with no failures. All222 initial engineering/input files retained their hashes and all five B10 files matched recorded approval fingerprints. Supplied ESP PCB PDF rendered five pages; sheets1/3 were visually inspected. The matching [manufacturer dimension PDF](https://dl.espressif.com/dl/schematics/esp_idf/DXF_ESP32-S3-DevKitC-1_V1.1_20220429.pdf) was rendered and visually inspected; it confirms the labeled planar dimensions, not populated height. Removed all six task-owned source previews and `tmp/mech02-engineer-inputs/`. No product model/render/export or physical/electrical test was performed.

## Panel mains inlet selected

On2026-10-19 the engineer selects [gniazdo_zasilania.webp](../elements/gniazdo_zasilania.webp) as the panel power-entry module and intends suitable internal wiring from it to the selected RS-25-5. This closes the fixed-cable versus detachable-panel-inlet choice. The image shows IEC-style inlet, switch and fuse-holder features; no exact manufacturer/model, contact circuit or electrical rating is established.

Source SHA-256: `9c96fdf28f4a3e78c06acf2a3623138c069e52acfca665d957afed7449cd8988`. [Canonical source dimensions](../DESIGN.md#selected-mains-inlet) distinguish cutout limits from the bezel and the20.7mm side-body callout from projecting terminals. No pixel-scaled dimensions, extra FDM clearance, location, permissible wall thickness/retention, complete terminal envelope or fuse rating is invented.

Selection does not approve a named enclosure drawing/model, mounting position, terminal wiring, PE continuity, guarding, electrical separation, energized tests, manufacture or export. Internal cables remain engineer-owned; that scope assumption does not waive safe mains packaging. Approved R12/L09/B09/B10/F.11 and deferred LED/diffuser scope remain unchanged; no CAD/Fusion operation or model export is performed.

Executed source/document check: supplied image visually inspected; six canonical documents passed548 local links/119 Markdown anchors with no failures. All223 current engineering/input files, including the new inlet source and all five approved B10 files, retained their hashes. No temporary artifacts, product geometry, model exports or physical/electrical tests were created/performed.

## Panel RCA candidate and supplied outline

On2026-10-19 the engineer proposes [rca_panel.png](../elements/rca_panel.png), supplying width20mm and length51mm and explicitly stating that screw-hole pitch is unknown. Record a dual-RCA purchased-panel candidate with that face outline, not a final model selection, a51×20 cutout or approval to infer mounting dimensions from perspective pixels.

Source SHA-256: `895fb13637b231f3315ee8c20adc2eecb27c5a320278f02f69f7cbf2458e7e8c`. [Source assessment](../DESIGN.md#selected-panel-rca) found the Goobay/Wentronic11310 manufacturer listing and Electrokit41003608 data/drawing:51.7×19.9 face,43.9 hole pitch and2×Ø3.6. The rendered PDF title is Wentronic CP02/11310 and explicitly labels Ø3.6;43.9 is confirmed by the supplier listing. TME CC-110 separately lists52×20/pitch44. These similar parts do not establish identity or measurements of the engineer's candidate; no comparison dimension overwrites supplied geometry.

Next input is the actual supplier/model or engineer-confirmed mounting measurements, or explicit selection of the documented variant. Socket/body/thickness/cutout and final installation still need definition. No fastener, slot/adapter workaround, geometry change, named drawing/model approval, CAD/Fusion operation or export is authorized by this input. Accepted packages, cable scope and deferred optics remain unchanged.

Executed source/document checks: supplied PNG and comparison images inspected; CP02/11310 PDF natively rendered and visually reviewed; manufacturer/supplier data read directly. Six canonical documents passed556 local links/123 Markdown anchors. All224 current engineering/input files retained their hashes, including the RCA image and all five approved B10 files. Removed the task-owned PDF preview and `tmp/rca-panel-source/`. No purchased-part fit, new product geometry, physical/electrical test or model export was performed.

## Goobay11310 panel RCA selected

On2026-10-19, directly after the proposed documented Goobay/Wentronic11310 (CP02) alternative, the engineer states: “Przyjmijmy Twoje znalezisko jako model, który będzie montowany”. This explicitly selects **one Goobay/Wentronic11310 dual-RCA panel** for the enclosure and accepts that part's cited manufacturer/supplier dimensions. It is purchased-part model selection, not approval of an enclosure CAD model revision.

The governing inputs are the manufacturer listing, Electrokit41003608 listing and Wentronic CP02/11310 drawing linked in the [selected-part contract](../DESIGN.md#selected-panel-rca). Use51.7×19.9 face,43.9 mounting pitch and2×Ø3.6 source holes. The drawing gives right-edge offset3.9 and bottom-edge axis height9.9; explicit local-datum derivation gives mounting centres(3.9,9.9)/(47.8,9.9) from the face lower-left corner. Do not recenter source Y9.9 to9.95 or infer unspecified dimensions.

This supersedes the earlier candidate/unknown-pitch status and51×20 outline for current design. Preserve the original image/earlier decision history unchanged apart from the working source link; TME CC-110 is not selected. No second identity/pitch confirmation is required. Actual plate thickness, complete body/terminal geometry, enclosure location/opening/fastener design and physical/electrical fit remain separate inputs/checks. No new dimensional delegation, named enclosure drawing/model approval, geometry mutation, model export, purchase or manufacturing release follows.

Executed synchronization checks: six canonical documents passed557 local links/125 Markdown anchors after the source-section rename and caller migration. All224 engineering/input files and recorded B10 approval hashes remained unchanged. Exact Decimal calculations confirmed the source43.9 pitch,3.9 side references and9.9 bottom-axis datum without recentering. No new geometry, temporary artifacts, model export or physical/electrical test was created/performed.

## B11 interface and review-zone study prepared

Following selected Goobay11310 RCA, the engineer requests “Kontynuuj”. Basia continues source-backed MECH-02 preparation and publishes the four-file [B11 interface study](ARTIFACTS.md#enc-b11--current-interface-and-review-zone-study), not a complete enclosure/model or new dimensional-selection grant. **CHANGES REQUIRED / NOT APPROVED**: proposed review zones have no selected new X/Y/Z; body/retention/shell/mains inputs remain explicit TBDs.

The three native A3 sheets retain accepted plan/B10 datums, show four unplaced controller outlines and local source RCA/inlet interfaces, and distinguish the display rear-contact plane from a body/usable-space bound and the inlet20.7 callout from complete terminal reach. Review zones only: rear/left RCA near Pi, rear/right inlet near PSU, controls beneath display. No wall/fastener/joint/split/protective dimension, new purchased geometry or physical acceptance is invented.

Read-only source review found no complete RCA/ESP body/height data. Similar INALWAYS0717-1S panel-thickness/depth data remain unselected comparisons; the exact inlet is not identified. Espressif's reference-design ZIP URL returned HTML, not a verified archive. Corrected a helper's cross-part20.7 attribution before integration: that value belongs only to the inlet, never RCA. Source-mount row9.9 is not a socket-axis definition.

Executed evidence is in the package report: native generation/reopen/render and all-sheet visual review; independent actual-PDF11 numeric cells/9 rendered boundary probes and three A3 sizes; underside/normal17, retained PSU/contact references and unplaced-state checks. All224 prior engineering/source files, including all accepted packages, retain their hashes. Removed task-only review images/directory; no permanent test scaffolds, new dependency/configuration, Fusion/OpenSCAD3D geometry, model save/export or physical/electrical/thermal test. PDF SHA-256: `a739b72675c750237911124fdce8a390ed04013aeb27fc202824536765c20d99`.

Next input: missing actual component heights/contact/retention/body data and engineer-supplied or bounded-authorized shell/new-placement dimensions; B11 does not close MECH-02 or the MECH-03 complete PDF/concept/named-approval gate. Accepted LED/harness exclusions, previous drawings/models and the SCAD/STL/actual-model-PNG/report contract remain unchanged.

## Shell dimensional delegation and installed-height inputs

In direct response to the B11 handoff, the engineer answers “ad.1 Tak” to Basia choosing shell-wall thicknesses, closure, segment joints, new printed mounts and their positions while preserving accepted geometry. This grants that printed-design dimensional scope; it does not approve B11 or a complete enclosure drawing/model, change accepted component positions/interfaces, supply purchased geometry, choose unspecified material/print settings, authorize CAD before drawing approval or allow unapproved exports.

The engineer supplies PCF8575 components2mm above/no components below, ESP components3mm above/no components below, and the same goldpin headers for both: installed projection8mm upward/1mm downward. PCB laminate thicknesses are not supplied; confirmation of upper/lower PCB-face datums is still required. Do not sum component and header heights or claim a complete installed-height chain.

The answer “ad.3 Przyjmij24mm” follows the grouped RCA/inlet full-depth request. Record24mm without silently assigning it to both parts or choosing an inner/outer mounting-face datum. Those two interpretation details require clarification; the inlet20.7 source callout remains a distinct body dimension.

For mains protection the engineer instructs: “Załóż, że to nie wpłynie na Twoje ustalenia geometrii.” Protection is engineer-owned and assumed geometry-neutral for the shell study, like the prior cable/plug scope exclusion. No mains guard, protective distance, fuse, PE continuity, electrical validation or energized-test approval is supplied; ELEC-01 remains open. Do not re-request the excluded protection design as a general shell-preparation prerequisite.

Canonical values and limits: [current input contract](../DESIGN.md#shell-delegation-and-controller-inputs). All accepted packages and the published B11 study remain unchanged. This update records authority/inputs only; no new geometry, dimensions selected by Basia, model/concept image, Fusion operation or export is created.

## Controller laminate and both panel-depth datums confirmed

The engineer confirms laminate thickness2mm for ESP and both PCF8575 modules, with the shared goldpin projections measured8mm above the upper PCB surface and1mm below the lower surface. Explicit calculation: ESP total1+2+max(3,8)=11mm; each PCF total1+2+max(2,8)=11mm. Component heights are parallel occupied envelopes, not additional header-stack terms. These purchased-part inputs and their datums are closed.

The engineer answers “ad.2 Tak” to the explicit question whether24mm applies to both selected RCA and mains inlet, measured inward from the inner shell surface. This confirms both full inward projections and the measuring datum. The inlet20.7 source body callout remains a distinct subdimension, not an additional reach. No whole-enclosure drawing/model approval, unprovided purchased retention/cutout geometry, material/print-setting selection or export authorization follows.

Continue the previously delegated printed shell/closure/segment-joint/new-mount design while preserving accepted geometry. Engineer-owned non-impacting cables/protection and deferred optics remain unchanged. [Canonical input contract](../DESIGN.md#shell-delegation-and-controller-inputs).

## B12 shell and installation draft prepared

After the confirmed2mm laminates/face-referenced8/1 headers and both24mm inward panel-interface depths, Basia uses the previously delegated printed-design authority to publish [B12's six-file package](ARTIFACTS.md#enc-b12--current-shell-and-installation-definition-draft). **CHANGES REQUIRED / NOT APPROVED**; no engineer drawing/model approval or manufacturing/export release is inferred.

Selected draft geometry:2mm walls and retained floor/datum/post closure, six floor/wall regions splitX220/380 andY120, ten separately printed28×10×3 bolted bridges/twenty nominalM3×8 screws, four new controller poses, side RCA(left)/mains(right) atY163/Z25 and rear-left24-cell honeycomb. Seams derive from nearest retained post-foot edges and are checked against represented floor additions, not chosen merely for a nominal grid fit. Initial ESP/mux poses were rejected after collisions with actual retained pot supports; accepted equipment is not moved.

Actual PCB clean contacts/pin locations/mux height datum, RCA rear transverse cutting/plate contact and selected inlet clip/permitted-wall/registration remain critical unresolved interfaces. Basia does not invent purchased holes/bearing bands, treat the RCA face as a cutout, adopt an unselected inlet family, or silently complete retainers. Material/setup/usable margins and physical joint criteria remain print prerequisites. Cables/protection are engineer-owned/geometry-neutral; deferred LED mechanics and all earlier approvals retain their limits.

Executed evidence:806 conservative retained additive/reference AABBs;50 new bridge/pad/driver bounds;40300 comparisons; cross-owner new-feature non-overlap;8060 additional vertical bridge-insertion/reference comparisons;432 floor additions clear seams and whole support owners stay on one floor; six-region joining graph connected; nominal segment envelopes≤220×180×56. These are numerical scoped bounds, not native BRep/all actual hardware checks. Native seven-sheet A3 generation/reopen/render and all-sheet visual review,12 actual-PDF numeric cells/11 rendered boundaries/seven media boxes passed. All229 earlier engineering/input files and five approved B10 hashes remained unchanged.

Separate LLM shell-only concept was generated from the draft, corrected for excessive illustrated height, converted from actual WebP bytes to PNG with AppKit, reopened and visually reviewed. It is deliberately unscaled/simplified and omits internal details/far-side inlet; never use pixels for geometry. Native PDF previews and the temporary vendor drawing copy were removed with `tmp/enclosure-b12/`. No Fusion, OpenSCAD product3D, model save/export, dependency/configuration or physical/electrical/thermal operation occurred.

PDF SHA-256: `8f5b8fc19b84fc40c3335f23d1385aea31923559e0c924d3cb6c294d1ec42557`. Concept PNG SHA-256: `ae6cc8ca94ebcb81600ba84721ed40f0589c7ffa07d3729c3286761b91ba28f3`. Continue from [B12 scope/remaining inputs](../DESIGN.md#b12-shell-and-installation-definition-draft), not another request for the closed11mm/24mm chains.

## Rear interfaces, PETG and mux pin exclusion — B13

The engineer prefers **both RCA and mains inlet on the rear wall**, selects **PETG**, confirms **CD74HC4067 body3.6mm does not include installed pins**, and instructs Basia to use the already supplied schematics for both boards. These decisions close material/pin-inclusion/source-policy questions; do not restart a blanket inventory or silently give the mux the ESP/PCF header geometry. They do not approve a named drawing/model, unprovided purchased geometry, print settings or exports.

The supplied My Allegro purchase-page URL returnedHTTP403. No account access/bypass or offer/variant data was obtained; the private transaction path is not copied into public artifacts. Existing `elements/gniazdo_zasilania_nowe.png` was visually inspected:47.5×28(+0.1) cutout conflicts with the original selected46.9..47.1 width. Its applicability is unconfirmed; sectional3/29.4/30.5 values are not silently equated with the closed24 inward datum. A public offer reference or explicit selection of the correct supplied drawing is still required before cutting/retention release. The retained B02 README's PCF supplier source was inspected;32×21 matches supplied dimensions; no hole/contact coordinates were scaled from photographs.

Published [six-file B13 amendment](ARTIFACTS.md#enc-b13--current-rear-interface-amendment): rear RCA centre(265,0,18), mains(335,0,18), wallY0..2 and confirmed24 inward =>Y2..26. Source RCA axes(243.05,0,17.95)/(286.95,0,17.95), pitch43.9/D3.6; faces stay between retained rear post-foot edges, gaps4.65/5.5. No accepted equipment, outer shell envelope, supports/joints/controllers or grille moves. B12 side poses/concept are superseded only; its six source/artifact files remain unchanged.

Executed: preserved B12 numerical source and two new rear proxies against806 retained bounds/50 joining-driver bounds/4 controller-plan reserves =>1720 non-overlap comparisons. Positive9.728763/4.428763 gaps to the display frame CONTACT plane are not complete display-body clearances; actual display interference remains UNVERIFIED. Three native A3 sheets generated/reopened/rendered and visually reviewed;11 actual-PDF cells/8 boundaries/media-box/draft gates passed. Both inlet inputs and all235 prior engineering/input files, including B12, retain their hashes.

Separate LLM concept was corrected for inlet proportions/invented flange screws, actually converted WebP→PNG1536×1024, reopened and reviewed. It shows rear interfaces only, omits internal details and is not CAD/dimensional evidence. Task `tmp/enclosure-b13/` previews removed. No3D/Fusion/OpenSCAD product model, cloud save, model export, dependency/configuration or physical/electrical/thermal operation occurred. **B13 CHANGES REQUIRED / NOT APPROVED**, with actual display/inlet and other inherited bought-interface limits explicit.

PDF SHA-256: `614e3fb8cddc277bc6dbe2f2c9af60689469a652c737e0051479420078d44057`. Concept PNG SHA-256: `47fac088a4e42eed5684d33a460a988e480a6a6a962d03ea1c7f23c7dca44381`.

## Purchased inlet drawing and twin rear grilles — B14

The engineer explicitly states that `elements/gniazdo_zasilania_nowe.png` is the drawing of the purchased inlet, likes the grille and asks for an identical second opening on the other side near RPi. This closes the source-selection/Allegro blocker and authorizes duplicate grille drafting; liking the concept is **not** named B13/B14/whole-enclosure drawing or model approval.

Published [six-file B14 amendment](ARTIFACTS.md#enc-b14--current-selected-inlet-and-twin-grille-amendment). Selected source47.5×28/source+0.1 height, face50×30.5, flange3 and sectional30.5/29.4 replace old46.9..47.1/20.7/R2 current assumptions; originals remain unchanged. Declared conservative axial interpretation: frontY−3 plus largest sectional30.5 →rearY27.5; minus innerY2 gives25.5 inward,1.5 more than the former24 proxy. This is not measured complete terminal geometry; do not add29.4/30.5 or claim clip/registration/electrical qualification. RCA24, both rear face positions, PETG and accepted equipment stay fixed.

V01 remainsX20..90/Z10..38 at retained RPiX47.6; V02 mirrors it byXnew=600−Xold intoX510..580 at the opposite/PSU endX569.75. This makes both ends vented without reversing/moving equipment because of concept/view handedness.24 holes each,48 total/across-flats6/web1.2/wall2/border≥3, nominal total opening area1496.492mm². No frame/fan or cuts through purchased components; the PSU-side vent is not electrical touch protection.

Executed: inherited source checks,1720 revised port/reference and41376 cut/reference comparisons; exact pattern reflection/containment, polygon non-overlap/minimum web1.2,10.5 minimum X gap to retained rearD9 foot references. Revised mains/frame-contact-plane gap4.353763 is not actual display-body clearance. Three native A3 sheets generated/reopened/rendered and visually reviewed;12 actual-PDF cells/8 rendered boundaries/media-box/draft gates passed. LLM concept generated against updated draft/selected inlet, actual WebP→PNG1536×1024 conversion/reopen/final review passed. It is unscaled shell-only illustration, not CAD/dimensional proof.

All241 earlier engineering/input files, including B13/B12/approved packages/both inlet images, retain hashes. Removed `tmp/enclosure-b14/` review data/previews. No3D/Fusion/OpenSCAD model, save/export, dependency/configuration or physical/electrical/thermal operation occurred. **B14 CHANGES REQUIRED / NOT APPROVED:** actual display body, bought contacts/clip/registration, mux pins and print/thread/strength/thermal/engineer-owned electrical release remain unverified; source identity is closed.

PDF SHA-256: `83d9d15d26c2afc9605407ba925e4ea125301af4974cf39ee029d3e58aab3e3a`. Concept PNG SHA-256: `70b4fee7fd9ce0cdf5f09c209ec54b476dad7927cb386f87df3e8dffd5a3772d`.

## Working enclosure 3D authorized before complete drawing approval — B15

The engineer explicitly requests: “Create a3D model from the data you already have. We will establish the display envelope and inlet snap-fit once there is a3D model” (English translation). This changes the sequence for this bounded working-model task: Basia may create the editable **B15 DRAFT OpenSCAD model** from B12/B13/B14 and accepted retained sources now. Actual display rear-body and inlet clip/capture/registration remain deferred and visibly unresolved; no invented purchased geometry or physical-fit pass follows.

This exception supersedes earlier blanket “no enclosure3D before complete drawing approval” instructions only for this draft review. It is **not** named B14/complete drawing approval, B15 model approval, permission to change accepted R12/L09/B09/B10/F11 geometry, or manufacturing/export release. Preserve all predecessor files. No STL/STEP/F3D fabrication exports; actual OpenSCAD PNG views and task-controlled temporary evaluation geometry may support review. PETG, engineer-owned geometry-neutral cables/protection, deferred LED mechanics and all physical/electrical/thermal gates remain unchanged. Fusion is outside this task and must not be accessed/saved.

Published the [twelve-file B15 working-model package](ARTIFACTS.md#enc-b15--current-working-openscad-enclosure-model): native editable floor/walls/joints and exact retained B09/B10 mounts, seven retained panel regions, unchanged F.11/legacy mesh inputs, four actual model PNGs, source compiler/manifest and scoped validation. The requested known-data3D delivery is complete; **CHANGES REQUIRED / NOT APPROVED** for complete enclosure release. There is no new engineer approval inferred from this publication.

Executed local OpenSCAD2026.10.11/Manifold: nine fully evaluated OFF meshes, six floor solids and bridge each one closed connected oriented surface, panel union one surface and66 removable surfaces from61 source groups. Floor-down nominal boxes are at most220×180×56, within nominal250³ without usable margins/support/brim qualification. Four final PNG1800×1100 were opened and visually reviewed. Input hashes cover23 retained references, all246 existing engineering/input files remain unchanged, and temporary OFF/log/continuation/cache files were removed. [Exact evidence and limits](../models/enclosure/B15/DJC_Enclosure_Rev_B15_validation.md).

Actual display rear-body and inlet snap/corner/registration remain deferred; other bought contacts/RCA body cut/mux pins and physical/print/electrical/thermal gates remain explicit. No full-hardware/all-body-interference or continuous-motion pass, fabricationSTL/STEP/F3D exports, Fusion access/cloud save or source remeshing. Main SCAD SHA-256: `fd32ee766e8e407fa2479efa7e00a3cce32ecc9d123ff0bf6a62a1250d8209f0`. Actual assembled PNG SHA-256: `1bec80859b2fd82f763fda32133d8db1e2b8bd119f6730947bd19a2fb96a70a6`.

## Trial RCA passage selection and correction — B16

The engineer reports that B15 has only RCA screw holes and no passage for the installed terminal. Basia acknowledges the missing functional opening. After source review found no complete rear cutout dimensions, the engineer explicitly selects **“Dobierz próbne okno”**: Basia may choose a common trial window while preserving screw-bearing lands, with actual purchased-part fit verified later. This is bounded dimensional-selection authority for this correction, **not** acceptance of a complete drawing/model, manufacturer body measurements, physical fit or fabrication exports.

Selected B16 window34.9×15.9, centre table(265,0,18), through wallY0..2, X247.55..282.45/Z10.05..25.95. Width43.9−9 preserves selectedØ9 wall lands around the unchanged source screw axes; height19.9−2×2 leaves2mm nominal top/bottom face cover. ExistingØ3.6 axes(243.05,0,17.95)/(286.95,0,17.95) remain unchanged, hole-edge ligament2.7, nominal side face cover8.4. These are agent design selections/derivations under the new authority, not pixel estimates or a cutout of the full51.7×19.9 face.

Published [thirteen-file B16 package](ARTIFACTS.md#enc-b16--current-trial-rca-passage-correction): editable model/shell, local dimensioned A3 amendment/definition/generator, five actual model PNGs and checker/evidence/report. **DRAFT / CHANGES REQUIRED / NOT APPROVED.** Only printed C02 changes; all258 prior engineering/input files, including the entire B15 and approved B10/F11 packages, retain hashes. Temporary vendor PDF/preview and task OFF/log/drawing preview files removed; no Fusion access/save or fabricationSTL/STEP/F3D exports.

Executed local OpenSCAD2026.10.11/Manifold: complete affected C02 closed/oriented/connected, unchanged160×120×56; actual opening34.9×15.9;195 actual material/void probes across three wall depths verify the empty window, existing holes, intact lands and rim. Removed volume1109.82mm³ matches retained C02 difference1109.820000000007. Five PNG1800×1100 visually reviewed; native PDF generated/reopened/rendered and reviewed, independent one-A3/10 searchable numeric/status cells passed. This is not a freshly rerun all-body/all-part audit. Actual rear-body insertion/fit, screw bearing/strength and inherited display/inlet/print/electrical/thermal limits remain unverified.

PDF SHA-256: `48fc627c33ba7aaa1c72e98cb5c49703a689877c4a9b6931e207fc8f8676d74a`. Main SCAD SHA-256: `53409c1964644b8515393b8aba25c4cba45908fe8c9765c8bf4b32b8ba2bad67`. Next: engineer reviews trial passage/real part fit; affected named drawing/model approvals still precede fabrication.

## Named B16 approval for one printed-assembly review STL

After requesting “Wyeksportuj STL całości”, the engineer explicitly selects **“Zatwierdzam B16 do STL”** in response to the named B16 nominal-model approval question. **APPROVED: the currently modeled printed-part assembly of B16 for one whole-assembly review STL**, excluding purchased/electronics/reference envelopes. This includes modeled shell/panel/mounts, jog printed meshes and caps/knobs in their assembled positions. Main source SHA-256 remains `53409c1964644b8515393b8aba25c4cba45908fe8c9765c8bf4b32b8ba2bad67`; every existing B16 source/drawing/evidence file must remain unchanged, including historical DRAFT labels.

The engineer was told that one STL loses component identity and is an assembled review file, not a printable layout for the250×250 bed. Agreed destination is `models/enclosure/B16/DJC_Enclosure_Rev_B16_assembly_review_mm.stl`, with1 coordinate unit interpreted as1mm; do not overwrite an existing export. Approval is nominal and scope-limited: actual RCA/display/inlet/other bought fit, threads/strength/calibration, material/print setup, electrical/thermal and production release remain unverified. Omitted free-state spring and unmodeled purchased parts are not silently added to “all modeled printed parts”. This is not complete enclosure drawing approval, approval of new geometry, individual fabrication-STL handoff, or Fusion/cloud-save authority.

## B16 working-model migration to Fusion

On2026-10-19 the engineer requests modeling in Fusion360 from `schematics/enclosure/B16/` and `models/enclosure/B16/`, stating that OpenSCAD is difficult to work with and asking to try Fusion again. This authorizes the tool migration of the existing known-data working-model scope, not new nominal dimensions, a complete drawing/model approval, cloud saving or new fabrication exports. Preserve the preceding original-B16 assembly-review-STL acceptance and all source/export bytes; it is not transferred to the new CAD representation.

Basia creates a separate **B16-Fusion-01 DRAFT** from retained B12/B13/B14/B15/B16/R12/B09/B10/F11 inputs. Fusion initially has zero open documents/no command dialog; the shared filesystem is positively confirmed by reading/hashing the B16 definition through Fusion. Final live document `DJC Enclosure B16-Fusion-01 DRAFT` is unsaved/modified, mm/APIcm; no other document is closed, overwritten or cloud-saved.

[Native report](../models/enclosure/B16/DJC_Enclosure_Rev_B16_Fusion01_validation.md) records native shell/panel/bridge features, exact analytic retained-mount BRep base features/Combine and embedded source meshes. Analytic circles preserve nominal dimensions but differ from OpenSCAD's48-sided mesh approximation; no mesh/volume identity is claimed. Native full recompute yields876 healthy timeline entries; six one-lump floor solids retain source boxes;195 actual RCA probes,108 panel-void probes and three bridge material/void probes pass. All93 represented BRep instances/98 lumps, including hidden/repeated/reference bodies, participate in4278 pairs/114 positive-AABB candidates. Four positive solid intersections involve incomplete Pi/DAC/contact-outline references; no non-reference BRep pair exceeds1e-6mm³. The65 retained mesh instances, missing purchased hardware, mechanism motion and physical fit are not certified.

Four actual Fusion PNG1800×1100 are opened/reviewed. Panel/caps/reference visibility is restored and the model left assembled/isometric. All272 pre-existing engineering/input files in the migration snapshot remain unchanged; no dependency/runtime/configuration or electrical changes. New Python builders/report/evidence/views are in the existing B16 model directory. No new STL/STEP/F3D or active-document save. **Fusion01 CHANGES REQUIRED / NOT APPROVED for release**; engineer owns review, named approval, actual-part checks and explicit save destination.

## Original B16 assembly review STL — export verified

The scoped original-B16 approval above is fulfilled by [the assembled review STL](../models/enclosure/B16/DJC_Enclosure_Rev_B16_assembly_review_mm.stl), with [report](../models/enclosure/B16/DJC_Enclosure_Rev_B16_assembly_review_export.md) and [machine-readable evidence](../models/enclosure/B16/DJC_Enclosure_Rev_B16_assembly_review_export.json). ASCII STL:808345920bytes,2635544triangles, interpreted dimensions600×300×76.75mm; SHA-256 `f7e75fd850817703e34a692d87447ae3b6bac415fb8e0a9b03492f114ebfbcec`. All modeled printed parts retain assembled poses; purchased/electronics/reference envelopes are excluded. No prior export was overwritten.

Local OpenSCAD/Manifold final export exits0/NoError without warnings. Independent full-precision facet/native-index correspondence finds zero degenerate facets, winding errors or open/non-manifold native indexed edges. There are2435 four-face coordinate-coincident contacts, all explained by paired closed native edges: this is a multi-surface review assembly, not one globally welded manufacturing solid. All271 pre-existing engineering/input files retain hashes; original geometry and historical DRAFT labels remain unchanged.

The binary32 trial was rejected for precision defects and removed. Its full viewport reimport hit the native cache limit; no successful final-ASCII-STL viewport is claimed. Temporary consumers/OFF/rejected mesh were removed; the host-protected initial-trial log `tmp/enclosure-b16-stl/native-export.log` remains disclosed evidence, with no permission change or deletion bypass. This export neither approves nor exports B16-Fusion-01, changes/saves a Fusion document, or closes physical/print/electrical/thermal qualification. The requested original-B16 single-file review export is complete; complete fabrication release remains CHANGES REQUIRED.

## Full Fusion cutover and named B16-Fusion-01 approval for export

On2026-10-19 the engineer confirms **full cutover to Fusion**, not a trial, and requests the complete Fusion delivery in **`models/enclosure/B16/FUSION/`**. Fusion is the sole active CAD editor/source workflow; retained B15/B16/OpenSCAD and migration scripts are preserved provenance, not the ongoing editing workflow. This supersedes the earlier SCAD-based waiver of new enclosure STEP/F3D for current work only; all chronological approvals and existing source/export files remain unchanged.

In response to the explicit named-model approval question for F3D/STEP/STL at that destination, the engineer selects **“Zatwierdzam B16-Fusion-01 do eksportu”**. **APPROVED: the current nominal modeled scope of B16-Fusion-01 for export.** This is its own approval, not a transfer from original B16's single review-STL acceptance. Current source is `DJC Enclosure B16-Fusion-01 DRAFT`, creationId `89a695ea-28cc-4d8b-b45f-3f6dfb7db786`, new/unsaved/modified, units mm/API cm, zero external document references. The [native evidence](../models/enclosure/B16/DJC_Enclosure_Rev_B16_Fusion01_validation.json) and [scope/editability report](../models/enclosure/B16/DJC_Enclosure_Rev_B16_Fusion01_validation.md) record876 healthy timeline entries,93 BRep instances/98 lumps and65 retained mesh instances.

Required package: revision-matched editable **`DJC_Enclosure_Rev_B16_Fusion01.f3d`**, full represented assembly **`DJC_Enclosure_Rev_B16_Fusion01_assembly.step`**, one STL per distinct printed part with BOM quantities and mm checks, actual Fusion PNGs and scoped validation. STEP must include retained mesh geometry, not silently omit it; conversion/coverage must be disclosed. These are agreed filenames/requirements, **not evidence that exports exist or passed verification**. Delivery is **IN PROGRESS pending final export verification** and registration of exact files/results.

The named approval permits local revision-matched F3D archive export without cloud saving. It does **not** authorize cloud save, overwrite of existing artifacts, close/discard of the modified active document, new geometric decisions or modification of preserved approved packages. It is not complete enclosure drawing/concept approval, actual fit/strength/thermal/electrical/manufacturing readiness or physical release. Display rear-body/inlet capture/RCA bought fit, mux pins/controller contacts, full hardware/motion and calibrated print setup remain unverified; four BRep intersections are incomplete-reference exceptions, and65 meshes are not covered by BRep interference checks. Jogs retain eight F11 definitions each without spring/complete purchased hardware;49 cap instances/six definitions include the recorded legacy tempo topology defects. Those limits remain explicit rather than being silently repaired or certified by export.


## B16-Fusion-01 complete Fusion package — export verified

The engineer's named nominal-scope export approval above is executed at **`models/enclosure/B16/FUSION/`**. [Delivery report and exact files](../models/enclosure/B16/FUSION/DJC_Enclosure_Rev_B16_Fusion01_delivery.md) record the completed requested package. Fusion is the sole ongoing CAD workflow; all original B15/B16/OpenSCAD/F11 and approved inputs remain preserved provenance. This completion record supersedes the earlier pending-delivery status, not its authority limits.

- Editable F3D:49,688,195bytes,212 archive entries/zero CRC errors; actually reopened in Fusion with exact source geometry/pose fingerprint `39b5a1e5357aa691be4cf1d34029141ef0cf44f3c173569c52da22be3aa3ce67`,879 healthy timeline entries,93 BRep instances/98 lumps,65 embedded mesh instances and zero external document references. Native history is retained, not flattened.
- Three added history entries are bounded topology-only cleanup: eight paired opposite zero-volume tempo facets and a six-facet disconnected planar T orphan are removed; equal binary32-mm T coordinates are welded. No new nominal dimensions or selected clearances. [Tempo evidence](../models/enclosure/B16/FUSION/DJC_Enclosure_Rev_B16_Fusion01_tempo_topology_repair.json), [T evidence](../models/enclosure/B16/FUSION/DJC_Enclosure_Rev_B16_Fusion01_Tcap_topology_repair.json).
- Complete represented assembly STEP:76,873,856bytes; actual Fusion reopen yields158 component identities/163 closed solid bodies and no open bodies,600×300×76.749999762mm. It covers93 original BRep instances,16 jog instances via unchanged approved native F11 STEP,43 faceted cap instances and six source-defined native T caps using approved B09 head/unchanged B_CAP stem. Rejected mesh-omitting/open-shell candidates are not delivered. Native T bound difference versus rounded source mesh is0.000033029mm.
- Two H05 retainer instances retain the inherited F11 STEP trial exception: final STEP versus original native source mesh maximum bound difference0.001480067mm, below the prior accepted0.002404457mm native/STEP difference; intermediate staging versus final reimport differs0.003884479mm. These are disclosed conversion effects, not silently accepted under the ordinary0.0001mm bound threshold or a physical-fit waiver.
- [BOM and exports](../models/enclosure/B16/FUSION/DJC_Enclosure_Rev_B16_Fusion01_BOM_and_exports.json):38 distinct binary STL files,154 printed pieces,9,318,804 triangles. All38 pass declared finite-data/count/length/duplicate/degenerate/edge-incidence/winding/connected-surface/signed-volume and native-mm-bound checks. Nominal part boxes fit250mm axes, not an approved print orientation/support/margin arrangement.
- Four actual Fusion PNG views,1800×1100, are opened and reviewed: assembly, interior, rear and RCA detail. No LLM retouch. Source assembled/isometric inspection state and agreed visibility are restored.
- Original `DJC Enclosure B16-Fusion-01 DRAFT` remains active/unsaved/modified. Three named unsaved verification/work copies remain open; none is closed/discarded, and no cloud save occurs. Task-only temporary export files are removed before handoff; retained checks/scripts are in the delivery directory. No dependency, runtime/configuration, permission or credential changes.

| Delivered file | SHA-256 |
|---|---|
| `DJC_Enclosure_Rev_B16_Fusion01.f3d` | `238b3adc09ee0ebf7a67916430fd8e785a561f543e10596bf29b3a4bd6bbef7c` |
| `DJC_Enclosure_Rev_B16_Fusion01_assembly.step` | `6943d01df5f41528dde6d132ee14f479f683e7e4554f7d7bddf3f563c214e2d7` |

**APPROVED — requested nominal modeled Fusion export package, delivered and verified within the recorded conversion limits. CHANGES REQUIRED for manufacturing/physical release.** Full bought hardware/mesh-solid interference, actual display/inlet/RCA fit, motion, print setup/strength, thermal/electrical safety and complete drawing/concept remain separate unclosed gates. Existing195 RCA probes/108 panel voids/4278 BRep pairs do not certify those omitted scopes. PETG enclosure is selected; retained accessory/H05 material scope and physical trials are unchanged. `C05_shell_Rev_B16_Fusion01.stl` is148,570,084bytes; large-file hosting needs review before commit/push, with no Git/LFS configuration changed here.


## Minimum T-cap request and B17-TCAP-01 drawing draft

The engineer plans a trial print of unchanged `models/enclosure/B16/FUSION/C05_shell_Rev_B16_Fusion01.stl`, reports T01–T06 cap heads too large, and requests the smallest triangular head whose boundary reaches the lower mounting-part corners. Basia confirms only the head changes, preserving the exact stem/socket, installed button axes/Z, panel and C05; the engineer replies **“Dokładnie tak. Zmień proszę zatem tę nakładkę.”** This is bounded dimensional-selection/change authority, not acceptance of an unseen named drawing/model or new exports.

Published **B17-TCAP-01 DRAFT**, [two-sheet dimensioned PDF](../schematics/enclosure/B17/DJC_T_cap_Rev_B17_drawing.pdf), [definition](../schematics/enclosure/B17/DJC_T_cap_Rev_B17_definition.json), [native generator/checks](../schematics/enclosure/B17/DJC_T_cap_Rev_B17_drawing.swift), [evidence](../schematics/enclosure/B17/DJC_T_cap_Rev_B17_validation.json) and [illustrative LLM concept PNG](../schematics/enclosure/B17/DJC_T_cap_Rev_B17_concept.png). Preserving triangle angles, all three support lines touch the nominal6.8/R1 stem: `a=7.2+sqrt(5)`, `b=3.4`, `L=a+b=12.8360679775`. Head remains4 thick, source stem4.6 and socket/entry unchanged. Derived head centroidX−0.878689 does not move the stem/button axis.

**New review consequence:** the unchanged8×8/R1.4 panel hole is not fully covered, with exposed normal extent0.668328 at sloping edges/0.6 at the base. This requires engineer acceptance with named drawing approval. No silent aperture reduction, moved axis or dust/light sealing claim. Nominal free-state panel-plane gap is1.179098 for T01/T02 and1.5 for T03–T06, not certified actual press travel. Actual mating fit, retention, stroke/return, cap material/print setup and strength remain unverified; no physical threshold is invented.

Executed: three analytic tight-support positive/negative boundary checks;204 retained source-stem vertices agree within1e−6mm numerical readback (maximum base roundoff9.54e−8mm, not a selected manufactured tolerance); new head vertices lie within old head. Two A3 sheets generated/reopened/rendered and visually reviewed;10 actual-PDF annotation checks pass. LLM WebP output opened, actually converted to PNG1536×1024 and final PNG opened/reviewed; not CAD/dimensional evidence. All59 captured source hashes, including the complete56-file B16/FUSION package, remain equal.

Read-only Fusion observation: only `DJC Enclosure B16-Fusion-01 DRAFT` open, saved/modified,879 timeline entries,0 external references and unchanged delivered geometry/pose fingerprint `39b5a1e5357aa691be4cf1d34029141ef0cf44f3c173569c52da22be3aa3ce67`. This differs from the earlier unsaved/four-document handoff; no source save/close, pose/camera/visibility or geometry mutation is performed here. No new Fusion model or STL/STEP/F3D export. Temporary B17 PDF review images are removed before handoff.

PDF SHA-256: `c9cc211f62c09b6274ae3f2a6a63a280fbe180e1c3fd1290c91369e0b444de71`. Unchanged C05 SHA-256: `90f16d5123eaaf76b1e0d031fd7f80bd24c81b4d0f931c70e50e67348e9ab682`.

**B17-TCAP-01 NOT APPROVED — named drawing approval required before Fusion changes; named model approval required before changed exports.** Existing B09/B16 approvals remain limited to their unchanged revisions; the C05 print plan is not a physical result or manufacturing release.


## Engineer approval of B17-TCAP-01 minimum head drawing

In the explicit named-drawing question the engineer selects **“Zatwierdzam B17-TCAP-01”**, accepting the12.836068×12.836068×4 head with unchanged mounting stem/socket, button axes/Z and panel, including exposed aperture portions up to0.668328mm normal to the sloping edges/0.6mm at the base. **B17-TCAP-01 is APPROVED for this nominal local geometry and Fusion modeling.** PDF SHA-256 remains `c9cc211f62c09b6274ae3f2a6a63a280fbe180e1c3fd1290c91369e0b444de71`.

Freeze the five B17 drawing-package files unchanged, including publication-time pending labels; this later named decision controls approval. Create the new B17-Fusion-01 model from the delivered B16 native archive, preserving the saved/modified B16 live document and all B16 outputs/C05. Approval does not authorize cloud saving, closing/discarding modified documents, new unrelated geometry, physical/manufacturing release or fabrication exports. Named model approval remains required after actual Fusion visualization and geometry/health checks.


## B17-Fusion-01 minimum-head model — ready for named review

The approved B17-TCAP-01 geometry is implemented in new **`DJC Enclosure B17-Fusion-01 DRAFT`**, unsaved/modified, without saving/closing the unchanged saved/modified B16 source. [Actual Fusion model/views/checks](../models/enclosure/B17/FUSION/DJC_Enclosure_Rev_B17_Fusion01_validation.md). New fingerprint `7d17f0afffd31a0e468e49bdf9b603060fb3b9056d09fcc659eecc2d40a55154`;884 healthy timeline entries after successful full recompute,99 BRep instances/104 lumps,59 remaining meshes and0 external references.

Only common T-head geometry changes across six unchanged occurrence transforms. Exact retained stem/socket differences are0/0mm³; new cap adds0mm³ beyond the old shape and removes332.949954835mm³ per head.573 changed-BRep pairs/18 AABB candidates have zero positive intersections above1e−7mm³.18 temporary cap translations against all seven panel bodies bracket geometric first contact at1.179098mm for T01/T02 and1.5mm for T03–T06 with±0.01mm probes. These are numerical/geometric checks, not actual switch travel, permitted stroke, full-hardware/mesh collision or physical certification.

Three actual1800×1100 Fusion PNGs are opened/reviewed: assembled, T01/T02 top and cap underside. Inspection visibility is restored, new model assembled/isometric; original B16 geometry/pose/flags and all prior files/C05 remain unchanged. A persistent preview MeshConvert feature blocked recompute; the dependency was removed, exact transient geometry persisted as an independent native faceted BRep, obsolete active T mesh removed, and head rebuilt with native sketch/extrusion. No failed recompute is suppressed or claimed passed.

**B17-Fusion-01 MODEL APPROVAL REQUIRED.** No new STL/STEP/F3D yet. After named nominal model approval, publish affected CAP_T STL/qty6, full native F3D/full represented assembly STEP and revision BOM; unchanged37 printed definitions remain their verified B16 part revisions, not copied/re-exported. No cloud save/closing/overwriting originals or physical/manufacturing approval follows. Inherited material/print/actual fit/strength/electrical/thermal limitations remain.


## Engineer approval of B17-Fusion-01 minimum-head model for export

After actual Fusion views and native checks are presented, the engineer selects **“Zatwierdzam B17-Fusion-01 do eksportu”**. **APPROVED: B17-Fusion-01 nominal local T-head change and its revision-matched exports**, based on approved B17-TCAP-01 and model geometry/pose fingerprint `7d17f0afffd31a0e468e49bdf9b603060fb3b9056d09fcc659eecc2d40a55154`,884 healthy entries. Exact retained stem/socket, installed transforms, unchanged panel aperture/exposure and original B16/C05 preservation are part of this scope.

Export destination is the new `models/enclosure/B17/FUSION/`: revised CAP_T STL/quantity6, complete native editable F3D and full represented assembly STEP, with actual Fusion PNGs, validation and a complete revision BOM referencing unchanged37 B16 STL definitions. Do not overwrite B16 or duplicate unchanged parts. This decision does not authorize cloud saving, closing/discarding modified documents, unrelated geometry, manufacturing readiness, actual travel/fit/strength/material/process or electrical/thermal acceptance. Existing physical/incomplete-hardware and H05 STEP trial limitations remain explicit. File presence/export verification is recorded separately after actual checks.


## B17-Fusion-01 approved export handoff — verification complete

The named drawing/model decisions above are executed. **Requested local T-cap correction and revision-matched exports are complete and verified** in `models/enclosure/B17/FUSION/`; [exact files/checks/limits](../models/enclosure/B17/FUSION/DJC_Enclosure_Rev_B17_Fusion01_validation.md). Only six T heads change; stem/socket differences0/0mm³, original axes/Z/panel and all B16/C05 bytes remain unchanged. No C05 print outcome is reported.

- CAP_T STL:20,884bytes/416 triangles, mm/qty6; finite/count/length, zero duplicate/degenerate/boundary/nonmanifold/winding conflicts, one edge-connected surface/positive volume; native-bound maximum difference3.9633e−7mm. Actual file checks and positive/negative checker fixtures pass. Not self-intersection/vertex-link/slicing or physical certification.
- F3D:49,894,113bytes,213 ZIP entries/zero CRC errors. Actual reopen/full recompute matches approved geometry/pose fingerprint `7d17f0afffd31a0e468e49bdf9b603060fb3b9056d09fcc659eecc2d40a55154`;884 healthy entries,99 BRep instances/104 lumps,59 meshes/13 closed oriented definitions and0 external references. Native history retained.
- Full represented STEP:75,113,276bytes; actual Fusion reopen retains158 component identities/163 closed solids/0 open bodies,600×300×76.749999762mm.99 source BRep instances (six new T included),16 unchanged native F11 jog instances and43 unchanged faceted cap instances.156 ordinary component bounds match staging to6.06e−10mm within0.0001mm numerical check.
- Two H05 instances retain the existing part-specific F11 STEP trial exception: stage/final difference0.002404456956mm; final versus unchanged native source mesh0.000030830mm, within prior accepted0.002404457mm. A bound differs0.001480022mm versus the older B16 STEP because this conversion is closer to unchanged native mesh, not a new nominal part size. Original H05 STL/F3D geometry unchanged; no physical thread/slot waiver.
- Complete BOM38 distinct definitions/154 pieces references37 unchanged B16 STL files by exact paths and reverified hashes, rather than duplicating them. Revised CAP_T is the only new STL. Three actual1800×1100 Fusion PNGs opened/reviewed, separate from the frozen illustrative concept.
- All export staging removed; source restored to884 entries/exact approved fingerprint and assembled/isometric visibility. Final native head replay/full computeAll passes with zero unhealthy features. A redundant computeAll after cross-document inspection returnedFalse without health/geometry changes; replay/recompute and fresh-archive proof pass. No general SDK root cause or unobserved successful call is asserted.
- Original B16 remains open saved/modified; new B17 and two named F3D/STEP verification copies remain open unsaved/modified. No cloud save or close/discard. Task drawing/export intermediates removed; helper code/evidence retained. No dependencies, runtime/configuration, permissions, credentials or unrelated geometry changed.

| File | SHA-256 |
|---|---|
| `CAP_T_Rev_B17_Fusion01.stl` | `8e0d93ec5d0d7b290face7c6e1e3f0654b98c07a7d0edf9917f895f48957b858` |
| `DJC_Enclosure_Rev_B17_Fusion01.f3d` | `fcde5503ee43c76df8012f745c19516d17b7aac8d6ac0fd30a70b1375edb7f9b` |
| `DJC_Enclosure_Rev_B17_Fusion01_assembly.step` | `e851ca87d45a4543bb872726a9b176548c3fab4e7d82db398b1fd91059786658` |

**APPROVED — nominal local T-cap revision and requested verified exports. CHANGES REQUIRED for physical/manufacturing qualification.** Actual cap material/process, plunger fit/retention/return/stroke, print strength and inherited whole-hardware/display/inlet/RCA/electrical/thermal limits remain. Engineer owns measurable physical acceptance; no pass thresholds are invented. Any new geometry returns through named drawing/model revision gates.


## B18 detail selections and drawing draft

The engineer requests three changes to the B17 baseline: triangular panel holes for T01–T06, rounded exterior enclosure edges like the legacy case, and cap/knob/fader detailing similar to the legacy panel. In grouped engineering choices the engineer explicitly selects **“R3 i łagodne krawędzie R0,8”** and **“Wypukłe kreski jak w źródle”**. This authorizes the described bounded paths/wall-derived corner transitions and local mark placement: R3 plan corners, actual R0.8 exposed rounds, raised0.4 marks/width0.8/lengths2/3/4 at P01–P13/F01–F05 and0.8×45 B/T upper chamfers. Preserve overall bounds, functional axes/mounts/joints/caps; no default E01/jog scale or copied deep fader relief. It is **not named drawing/model approval**.

Basia publishes [B18-DETAIL-01 six-sheet PDF](../schematics/enclosure/B18/DJC_Enclosure_Rev_B18_drawing.pdf), [exact source/authority specification](../schematics/enclosure/B18/DJC_Enclosure_Rev_B18_definition.json), [editable generator](../schematics/enclosure/B18/DJC_Enclosure_Rev_B18_drawing.swift), [drawing checks](../schematics/enclosure/B18/DJC_Enclosure_Rev_B18_drawing_validation.json) and [illustrative detail concept](../schematics/enclosure/B18/DJC_Enclosure_Rev_B18_concept.png). Existing aperture-selection delegation permits choosing the proposed0.6 normal T offset, derived from prior `(8-6.8)/2`; new exact vertices `(-10.777708764,0),(4,±7.388854382)`,14.777709 bounds, six unchanged axes/pointing directions. Replace old square profiles; do not union cuts. Drawing defines chamfer0.8 along actual upper face/45° to it, including the rear slope.

Source inspection: native legacy case plan arcs R3; lower STL side section has45° normals/linear0.8 chamfer, not an R0.8 arc. Legacy panel circular-hole section verifies0.8 upper chamfer. Pad001/Pad002 are raised0.4. Exclude20 construction segments from Sketch005:30 real closed profiles remain, including four identical five-mark knob groups; not35 manufactured profiles. New175 mark polygons versus108 aperture envelopes give18,900 planar comparisons, minimum1.3mm to an aperture and0.5mm to a panel seam. These are plan checks, not all-body/hardware/motion or strength proof.

Executed: native PDF generation/reopen/render, all six sheets visually reviewed,12 annotation checks and source-formula assertions. An initial fader detail crossed the header and was corrected/re-rendered before publication. LLM WebP source/final converted PNG opened; first full-product attempt omitted screw details and was replaced with a labeled cropped detail study. Final PNG1536×1024 is illustrative only, not CAD/dimensions. No new3D geometry, cloud save, closing/discarding document or STL/STEP/F3D export.

Latest read-only Fusion state changed externally since the B17 handoff: active B17 is **saved/unmodified**, two documents open,884 timeline entries and exact delivered geometry/pose fingerprint `7d17f0afffd31a0e468e49bdf9b603060fb3b9056d09fcc659eecc2d40a55154`; no assistant save is performed. Prior export verification/health remains its recorded coverage, not a newly recomputed model. Preserve all original files/documents. C05 original hash remains `90f16d5123eaaf76b1e0d031fd7f80bd24c81b4d0f931c70e50e67348e9ab682`; future B18 C05 differs at its front exterior lower edge.

PDF SHA256 `2f63d3fed26460e0068ee38329d16d6181a16196568484bc5b8c3567ce82cf8c`; concept SHA256 `dc917a359750d04acc8d4d36c61f50961ab1bc19f413da1023c656a9e2833177`. **B18-DETAIL-01 DRAWING APPROVAL REQUIRED before Fusion changes.** B17 remains the approved current native baseline. Separate named B18-Fusion-01 model approval is required before thirteen affected STL/full STEP/editable F3D exports to `models/enclosure/B18/FUSION/`. Actual fit/strength/print/electrical/thermal gates remain unchanged.


## Engineer approval of B18-DETAIL-01

In the explicit named question the engineer selects **“Zatwierdzam B18-DETAIL-01”**. **APPROVED for nominal local geometry and new Fusion modeling:** all three requested groups, T normal clearance0.6, R3/R1/R0.8, B/T0.8×45 upper chamfers, and the defined raised P/F marks/placement. PDF SHA256 `2f63d3fed26460e0068ee38329d16d6181a16196568484bc5b8c3567ce82cf8c`. Freeze all five drawing-package files, including historical pending labels; this later decision controls effective approval.

Use a new B18-Fusion-01 document from the exact approved B17 archive. Keep all caps/socket/axes/Z and other source geometry/quantities, original B16/B17 files and the C05 trial STL. Native geometry/health/interface checks and actual model views precede separate named model approval. No cloud save, original overwrite, closing/discarding documents, fabrication export, physical/manufacturing or electrical/thermal approval follows.


## B18-Fusion-01 native model ready for named review

Approved B18-DETAIL-01 is implemented in new `DJC Enclosure B18-Fusion-01 DRAFT`, unsaved/modified; original B17 saved/unmodified/exact source fingerprint and all prior files/C05 are preserved. [Actual model, sources, five actual PNGs and validation](../models/enclosure/B18/FUSION/DJC_Enclosure_Rev_B18_Fusion01_validation.md). Native fingerprint `d9001f10dcb2b9b75bf58efe3adc4553d43e1168be16af5e4e129ca0157e2f9d`,926 healthy history entries/full recompute,99 BRep instances/104 lumps,59 meshes/13 unchanged coordinate/index-hashed definitions. All three requested groups and thirteen changed printed parts are complete; no new loose solid or pose.

Executed: six triangular sketch replacements plus twelve restored-square-corner material probes;24 analytic R3/R1/R0.8 rounds with shared-centre wall2;24 B and6 T upper-face0.8/45 chamfers;175 raised0.4 top faces/native profile area411.253966292mm².86 untouched BReps have two-way differences below1e-7mm³ and all instance transforms are unchanged.1196 changed-native pairs/120 candidates have no new/increased overlap; four inherited incomplete Pi/display reference positives remain numerically unchanged.191 new-material islands versus all59 transformed-vertex mesh bounds/11,269 pairs have no candidate.70 post/full-head-seat zones remain unchanged;35 complete nominalD5.5/H3 head envelopes versus13 changed printed bodies/455 pairs are clear. Fifteen nominal fader centre/end samples clear new material; no continuous-motion or physical claim.

Native minimum-distance/corner checks: T04–B23 rim gap1.730714167mm; T06 upper rim to R06 boundary1.433436854mm; front panel edge vertical land1.2mm. All435 cap-rim pair lower bounds considered; one lowest candidate requires exact native edge refinement. Four rounded walls remain concentric2mm. Positive lands/gaps and nominal shell envelopes within250³ are not strength, final bed/support/brim/orientation or calibrated fit acceptance.

Five actual1800×1100 PNGs opened/reviewed; caps-hidden names disclose inspection visibility, then assembled/isometric state is restored. Square openings seen below the new triangles are unchanged switch retainers, not the panel cuts. Source assembly still lacks complete bought/metal hardware; nominal full-head envelopes supplement rather than fabricate it. Existing proxy/physical/electrical/thermal limits remain explicit. No cloud save/close or STL/STEP/F3D export. **B18-Fusion-01 MODEL APPROVAL REQUIRED** before export to `models/enclosure/B18/FUSION/`; requested package is13 affected STLs/qty1/mm, full represented STEP/editable F3D, actual views and complete BOM referencing25 unchanged part definitions.


## Engineer approval of B18-Fusion-01 for export

After the actual model/views/checks and nominal thin lands are presented, the engineer selects **“Zatwierdzam B18-Fusion-01 do eksportu”**. **APPROVED: B18-Fusion-01 nominal three-group geometry and revision-matched exports**, fingerprint `d9001f10dcb2b9b75bf58efe3adc4553d43e1168be16af5e4e129ca0157e2f9d`,926 healthy entries, as defined by approved B18-DETAIL-01. Include thirteen affected STL components/mm/qty1, full represented assembly STEP/editable F3D, actual Fusion PNGs, verified BOM/unchanged references in `models/enclosure/B18/FUSION/`.

Administrative BOM correction during export preparation: the prior38-definition catalogue combines PANEL_R05/PANEL_R07 as quantity2 of one old STL. Their newly opposite exterior-edge treatment makes them different parts, already individually listed/approved in the B18 drawing's thirteen changed components. Publish separate R05/R07 STLs: **39 distinct definitions,154 pieces,13 new STL definitions and26 unchanged references**, not the earlier38/25 estimate. No additional physical part, seam, quantity or approved model geometry changes.

Approval remains nominal prototype scope with disclosed1.433437/1.730714/1.2mm lands, four inherited incomplete-reference positives, missing complete bought/metal hardware and actual fit/strength/process/electrical/thermal limits. It does not authorize cloud save, prior-file overwrite, document close/discard or manufacturing/physical qualification. All B16/B17 files and the original C05 trial STL remain retained.


## B18 verified exports and accepted STEP representation

In the explicit STEP-REP-B18-01 question the engineer answers **“Tak. Zmiany są ok.”**, then requests additional fader/jog recesses. The answer accepts the disclosed sampled R01/R04 procedural-to-NURBS STEP approximation, maximum0.007807241mm, with native F3D authoritative. It does not define a manufacturing tolerance or certify a continuous trimmed-body distance. The new recess request is a separate B19 geometry revision, not an alteration of the approved B18 package.

[B18 delivery/evidence](../models/enclosure/B18/FUSION/DJC_Enclosure_Rev_B18_Fusion01_validation.md):13 new STLs/mm/qty1,39 distinct definitions/154 pieces with26 unchanged referenced files, complete represented STEP, editable native F3D and five actual Fusion PNGs.13 meshes/10,210,190 triangles pass closed/oriented/connected/scale checks, max bound error2.134840086e-6mm;71 frozen source hashes preserved. F3D50,978,850bytes/213 ZIP entries/zero CRC errors actually reopens/full recomputes926 healthy entries/exact approved fingerprint/zero external links. STEP76,797,489bytes actually reopens158 component identities/163 closed solids/zero open bodies,600×300×76.749999762mm.

STEP bound verification corrects two proven imported-body `preciseBoundingBox` omissions using exact verified trimmed-cylinder extrema, without changing geometry or the0.0001mm threshold;156 ordinary bounds agree within6.055e-10mm. All13 changed parts sampled bidirectionally,21×21 NURBS/5×5 other surface grids plus pointOnFace. R01/R04 maximum reprojection residuals0.007713001/0.007807241mm; other changed parts agree numerically.383/401 projections outside counterpart trims limit this to sampled surface evidence, not a continuous body certificate. Inherited H05 stage/final bound difference0.002404456956mm and source-mesh/final0.000030830mm remain within the prior exception, with no physical thread/slot waiver.

Export staging removed; source restored to926 entries/exact approved fingerprint,13 mesh hashes unchanged, full recompute passed; assembled/isometric restored. B16/B17 remain saved/unmodified at final observation. New B18/F3D/STEP verification documents remain open unsaved/modified; no cloud save/close/discard. Both task temporary directories/five OBJ files removed. Original C05 remains byte-identical; its trial does not qualify B18's new front lower round.

F3D SHA256 `a58235268aa1cb2f5e7dbdd457acca810bbff1f8ce70b416f727b44fb9a95769`; STEP SHA256 `f48cdd6f522597277962363710ed4575b9ebf56b123089eb9f65717d31eddd38`. **APPROVED — nominal B18 detail change and verified local exports; physical/manufacturing qualification separate.**

## B19 requested fader and jog panel recesses

The engineer additionally requests the legacy panel's shallow recesses at the faders and jogs in the new enclosure. Treat the scope as front-panel geometry at F01–F05 and JA/JB, not a change to the purchased faders, their travel, cap geometry or jog mechanism/platter. Read the supplied legacy native panel/STL for exact profiles/depths. Current slots/Ø100 platters differ from legacy geometry; adaptation dimensions, wall/mark/clearance consequences require an explicit source-backed B19 definition and named drawing approval before Fusion changes. B18 stays preserved; no new geometry, cloud-save or export approval is inferred.


## B19 visible-jog selection and drawing proposal

In the grouped source/adaptation question the engineer explicitly selects **“Widoczne wokół platera Ø100”**. The selected option defines visible floorØ108=`100+(58−50)`,4 radial outside the unchanged platter, depth1/upper-face0.8×45 and passage across the existingY120 panel split/slope crease. The hiddenØ60 alternative is not selected. The question discloses1mm remaining vertical panel stock and physical stiffness qualification. This is a dimensional selection, **not named B19 drawing/model or export approval**.

[B19-RECESS-01 four-sheet PDF](../schematics/enclosure/B19/DJC_Enclosure_Rev_B19_drawing.pdf), [definition/derivations](../schematics/enclosure/B19/DJC_Enclosure_Rev_B19_definition.json), [Swift](../schematics/enclosure/B19/DJC_Enclosure_Rev_B19_drawing.swift), [executed checks](../schematics/enclosure/B19/DJC_Enclosure_Rev_B19_drawing_validation.json), [illustrative concept](../schematics/enclosure/B19/DJC_Enclosure_Rev_B19_concept.png). Fader proposal69.7×14/R3: unchanged61.7 slot plus source8 total end extension; apply all five, including F05 while retaining its2-wide slot/28 travel. Both well types depth1 vertical; floorU−1/underside unchanged,110 F marks lower1/top51.4/height0.4;65 P/caps/jogs/poses remain exact. No source lower-slot chamfers/guide scratches/extra mark fillets copied.

Legacy native Sketch003/Pocket002 and binary STL sections independently verify1mm source depth,14×49.5/R3 vertical wells around2×41.5 slots andØ58 aroundØ50 jog holes; upper chamfer0.8. Current larger wells leave1 vertical/0.998752 rear-normal panel stock. Continuous assembled jog recess must preserve original printed-part boundaries and all hardware, with no artificial rim step atY120; exact native checks/strength remain required.

Executed: native PDF generation/reopen/render; four final sheets visually reviewed;14 annotation checks and749 conservative other-aperture box comparisons pass, min5.620030mm lower bound. Corrected a schematic jog section to retain the actualØ52 through void and a fader section scale label before publication. PDFKit split underscores in extracted part IDs; actual labels remain visually correct, incidental string assertion removed rather than mislabeling the drawing. Final LLM concept omits ticks with an explicit caption after inaccurate generated counts; it communicates relief only, not shape/dimensions or actual Fusion validation. Final generated WebP/converted PNG1536×1024 opened/reviewed.

PDF SHA256 `f00ac886b7eb6a274f7359fe3d17b9fcd4d63078c9bd5de73a8545d1d1942c8c`; concept SHA256 `75ce603816e8eaf617acf7cb6a9e1ef5b8dfd9317101e06a1166b12c2a2d2e1c`. Five changed/PETG/qty1 panel parts R01/R04/R05/R06/R07; planned5 new STL +34 unchanged references/39 definitions/154 pieces, complete represented STEP/editable F3D/actual views after separate model approval. Exact approved B18 F3D is baseline; all B18/predecessor files and C05 are preserved. **B19-RECESS-01 DRAWING APPROVAL REQUIRED; no B19 Fusion geometry/export, cloud save or document close/discard.**

Publication integration smoke passed: all9 frozen drawing-input/source hashes, final PDF hash, final PNG signature1536×1024/hash, exactly5 B19 package files and863 local document-link targets verified. Task-owned four PDF preview PNGs and `tmp/enclosure-b19/` removed after review. No B19 Fusion geometry or fabrication export was performed.


## Engineer approval of B19-RECESS-01

In the explicit named question the engineer selects **“Zatwierdzam B19-RECESS-01”**. **APPROVED for the defined nominal recess delta and new Fusion modeling:** five69.7×14/R3 fader wells, two visibleØ108 jog wells, depth1 globalZ, actual-upper-face0.8/45 chamfers,110 F marks lower1,65 P marks/caps/jog mechanisms/axes/travel unchanged. The question discloses1mm residual vertical panel stock without physical strength acceptance. PDF SHA256 `f00ac886b7eb6a274f7359fe3d17b9fcd4d63078c9bd5de73a8545d1d1942c8c`; freeze all five B19 drawing-package files, including historical pending labels. This later decision controls effective approval.

Use the exact approved B18 F3D in a new B19-Fusion-01 document. Separate native geometry/health/interface/actual-view review and named B19-Fusion-01 model approval precede5 revised STL/full represented STEP/editable F3D exports to `models/enclosure/B19/FUSION/`. No cloud save, original overwrite, document close/discard or physical/manufacturing release.

Read-only pre-mutation observation finds an external C02 occurrence pose change in the open B18: Fusion translation(-3.841094827,+1.327835485,+0.822000606)mm, table translation(-3.841094827,-1.327835485,+0.822000606)mm, no timeline-entry change. Live fingerprint `5dbf835e776fa030c5d0e8a4b1c85020f2a18d2936a88ea5f79dbb1504c34790`; exact archived verification copy remains `d9001f10dcb2b9b75bf58efe3adc4553d43e1168be16af5e4e129ca0157e2f9d`. Only C02 pose/bounds differ in that inventory comparison. Preserve live unsaved work; do not reset it. New B19 follows the explicitly approved archive, not this unapproved live pose.

## B19 flat enclosure and display-only tilt mockup request

On2026-10-20 the engineer requests an alternative mockup: the enclosure remains flat and only the display inclines approximately10°. This authorizes a separate illustrative concept, not native CAD changes, a replacement of B19-RECESS-01, manufacturing exports or physical acceptance. The operator-facing display edge is lower and its far rear edge higher; the rest of the rear panel and surrounding controls remain on a horizontal deck.

[B19-TILT-MOCKUP-01 concept PNG](../schematics/enclosure/B19-TILT-MOCKUP-01/DJC_Enclosure_Rev_B19-TILT-MOCKUP-01_concept.png), [sources, calculation, checks and limitations](../schematics/enclosure/B19-TILT-MOCKUP-01/DJC_Enclosure_Rev_B19-TILT-MOCKUP-01_validation.json). The existing B18 assembled view defines the illustrative layout, B19 concept the recess appearance, and the supplied display image its front proportions. For a76mm display face, the ideal10° rise is13.197mm and horizontal projection74.845mm; these are target arithmetic, not measured image dimensions. The first generated wedge appeared too steep; the final edit reduces its inclination. Final WebP and converted1536×1024 PNG were opened and visually reviewed; PNG signature/dimensions/hash and target-angle arithmetic were checked.

The local wedge is illustrative only. Exact rendered angle/layout, rear-body and electronics headroom, retention, screws, control supports, cables, strength, printability and physical/electrical/thermal fit remain unverified. No Fusion access/mutation/save/close/discard or fabrication export occurred. B19 and predecessor engineering files remain unchanged; this alternative has no named drawing/model approval.


## B19-Fusion-01 native model ready for named review

Approved B19-RECESS-01 is fully implemented in new unsaved/modified `DJC Enclosure B19-Fusion-01 DRAFT`, using exact approved B18 F3D. [Actual model/five PNGs/complete evidence](../models/enclosure/B19/FUSION/DJC_Enclosure_Rev_B19_Fusion01_validation.md). Native fingerprint `6a8c22715e05c00765e4f27dd30e94ad88bcd52a0c88ed7ff891295398b6c119`,970 healthy entries/full replay/computeAllTrue,99 BRep instances/104 lumps and59 mesh instances/13 exact unchanged definitions. Five changed PETG panels/qty1; no other geometry, pose, quantity or shell/C05 change.

Measured all five69.7×14/R3 floors/71.3×15.6/R3.8 upper rims/depth1,110 F marks lower1/H0.4 and65 P marks retained.40 actual chamfer faces45° within0.001°; four jog floor-sector analytic areas/slope normals; eight independently calculated rear/front rim-section points match edges within3.56e-14mm. Native full-solid differences show0 new material outside B18 and0 removal outside approved conservative well envelopes;94 other BReps unchanged within1e-7mm³, all poses/mesh hashes exact.

480 changed-versus-all99-native pairs/18 candidates have no positive intersection;35 full-head-seat zones unchanged,35 complete nominalD5.5/H3 heads versus5 panels/175 pairs clear, all35 posts retained in six unchanged shells. Each jog uses one common editable native cutter across original part boundaries; native Y120 section wires13/15 edges checked132/166 samples both directions per jog, maximum2.212e-10mm new-recess curve separation under1e-5mm numerical limit. No seam-edge round or platter/mechanism split.

Motion:15 actual source cap-mesh endpoint/centre translations keep bottom52.8 and1.4 vertical lower bound to lowered F marks.32 exact approved native F11 annular platter poses (0/1.5 press;0…315°/45° increments) versus all5 panels show no solid overlap, minimum sampled clearance1.997504678mm. Central hub/bearing/intentional engagement excluded; not continuous motion, spring/switch deflection, insertion/removal or physical certification.

All five1800×1100 actual Fusion PNGs opened/reviewed; overview framing corrected to include all5 wells before review. Visibility restored/assembled-isometric; no geometry/poses changed for pictures. Native root tool bodies0, no inspection geometry. Source B18 live C02 drag stays fingerprint5dbf835e…; no source reset/cloud save/close/discard. Previously open B18 verification copies were closed externally; approved F11 STEP opened in a separate unsaved reference for temporary native motion checks, not added to B19.

Earlier computeAllFalse returns on unchanged import/initial stages were not accepted. Verified execution uses the discovered native `FusionComputeAllCommand` after the modeling transaction, then a separate complete timeline replay/API computeAllTrue and zero-health-issue check. Final proof passes; no unsupported SDK cause or silent waiver.

**B19-Fusion-01 MODEL APPROVAL REQUIRED** before exports to `models/enclosure/B19/FUSION/`:5 new STL/mm/qty1,34 unchanged references/39 definitions/154 pieces, full represented assembly STEP/editable F3D, actual PNGs and verified handoff. Residual1mm vertical/0.998752 rear-normal panel stock remains a physical stiffness/strength risk; inherited complete-hardware, fit, process, electrical/thermal and spring limits stay separate. No physical/manufacturing approval follows.


## Engineer approval of B19-Fusion-01 for export

After actual native views/checks and the residual1mm stock risk are presented, the engineer explicitly selects **“Zatwierdzam B19-Fusion-01 do eksportu”**. **APPROVED: B19-Fusion-01 nominal recess delta and revision-matched local exports**, fingerprint `6a8c22715e05c00765e4f27dd30e94ad88bcd52a0c88ed7ff891295398b6c119`,970 healthy entries/full recompute, as defined by approved B19-RECESS-01.

Destination `models/enclosure/B19/FUSION/`:5 changed STL/mm/qty1, complete represented assembly STEP, editable/history-preserving F3D, five actual Fusion PNGs and complete39-definition/154-piece BOM referencing34 unchanged revisions. Verify actual files/scale/topology, archive reopen/history/CRC, STEP identities/solid count/scale and actual representation limits; inherited H05/B18 procedural-corner exceptions remain disclosed, any new exception needs disposition. No cloud save, overwriting prior revisions, resetting live B18 C02 or closing/discarding modified documents.

Approval is nominal prototype geometry only.1mm vertical/0.998752 rear-normal stock, real fit/strength/process/complete hardware and electrical/thermal/spring limits remain physically unqualified. Separate flat-case/display-tilt mockup remains illustrative and does not change this approved recess model.

## Engineer acceptance of STEP-REP-B19-01

After actual export/reopen and129182 bidirectional bounded-surface samples on all five changed panels, the engineer explicitly selects **“Zatwierdzam STEP-REP-B19-01”**. Accept the observed new-recess STEP representation difference up to0.0034568686693392863mm (reported0.003457mm), including the rear jog chamfers and tiny seam-face merging. **F3D remains the source/master; native geometry and STL are unchanged.** This accepts the stated sampled prototype representation, not a continuous Hausdorff bound, manufacturing tolerance or physical qualification. Existing STEP-REP-B18-01 and H05 exceptions remain separately disclosed.

The initial face-index-corresponding reprojection probe is retained but superseded: STEP merges R05/R07 from223 native to221 faces. Final checks measure points against bounded opposite-body faces without assuming matching face counts/order; three pruning/full-scan comparisons pass. [Actual representation evidence](../models/enclosure/B19/FUSION/DJC_Enclosure_Rev_B19_Fusion01_STEP_representation.json).

## Verified B19-Fusion-01 local export handoff

Under the three named approvals, requested local package in `models/enclosure/B19/FUSION/` is **APPROVED within nominal scope / DELIVERED AND VERIFIED**. [Detailed handoff and exact links](../models/enclosure/B19/FUSION/DJC_Enclosure_Rev_B19_Fusion01_validation.md):5 new STL/mm/qty1,34 unchanged exact references/39 definitions/154 pieces; full represented STEP158 identities/163 closed/0 open;970-entry editable F3D; five actual1800×1100 Fusion PNGs. STL1221946 triangles pass declared topology/scale, maximum native bound error1.944106e-6mm;111 frozen source hashes preserved. F3D actually reopened/full-recomputed/exact fingerprint,215 entries/CRC0/external references0; SHA256 `96a1377325974e34cff7a065154f471475a0f19e4067ba67ab290899888bfbce`. STEP actually reopened/scale/identity/solids checked; SHA256 `ad05bffb3ea24b6a386c76e2db1b8eb12d6ade39e3943f698a7a3a31680a5b71`. New sampled representation accepted above; inherited B18/H05 exceptions retained.

Post-staging cleanup/native UI recompute caused a target-reference failure at timeline589 `Attach F05-FIXED to C05` in the unsaved dirty DRAFT session, not in the exported F3D. Cause unestablished; no silent repair, failed-compute pass claim or archive overwrite. Failed copy remains open/unsaved. Active source is **`DJC Enclosure B19-Fusion-01 VERIFIED ARCHIVE`**, reopened from unchanged exact F3D, complete replay/computeAllTrue/970healthy/fingerprint/13 mesh hashes verified again. [Failure/recovery](../models/enclosure/B19/FUSION/DJC_Enclosure_Rev_B19_Fusion01_post-export-session-recompute.json), [healthy final state](../models/enclosure/B19/FUSION/DJC_Enclosure_Rev_B19_Fusion01_native_final_state.json). External live B18 C02 pose stays unchanged. No cloud save, original overwrite, document close/discard or physical release.

Task-owned drawing/export temporary directories removed. Next owner: engineer for measurable PETG1mm-floor/joint/fit trials and confirmed slicing/process/actual-interface checks. Existing full-hardware/electrical/thermal/spring limits and separate unapproved display-tilt concept remain; any geometry correction requires a new affected drawing/model approval.

## Low-profile enclosure and separated Pi/DAC design inputs

The engineer requests a successor to the approved B19 enclosure: one planar main deck gently descending toward the operator, without the inherited rear crease; a separately inclined display following the approximately10-degree concept; Pi4 and DAC Pro side by side beneath the display, connected using the engineer's available40-pin cable instead of direct GPIO stacking. Existing B19 recesses remain the accepted styling baseline.

Engineer-supplied PSU body height is28mm; requested useful internal height at the PSU is30mm. On clarification of the front target the engineer states **“Byłoby super jakby 20mm z przodu to była całkowita wysokość zewnętrzna obudowy”**: **20mm is the desired total exterior front housing height, not a20mm cavity**. Record as a design target pending geometric feasibility, not a proven fit or permission to shrink components, erase clearances or silently increase the target.

These are new design inputs, not approval of a named drawing/model or authorization to overwrite B19, modify Fusion geometry, cloud-save or export. The direct-stack36mm chain remains historical/approved-B19 evidence, not the new separated-board installed envelope. [Current requirements and unresolved geometry](../DESIGN.md#requested-low-profile-enclosure-and-separated-pidac).

## Engineer-owned low-profile jog replaces the old height constraint

During the inquiry about placing Pi/DAC/PSU together beneath the display, the engineer states: **“Nie przejmuj się, że jog wheel jest wyższy. OSobno przemodelowuję go na wysokość, która zmieści się w16mm”**. The successor must therefore use the planned engineer-owned jog fitting16mm, not reject the layout based on the existing41mm-high F11 housing.

This is an installation-budget/design-direction input, not evidence that the new jog is finished, an approval of its interfaces/motion/strength, or permission for Basia to modify the engineer's active jog work. Integrate and check the actual new revision when available; preserve approved F11/B19 and keep drawing/model/export approvals separate.

## Low-profile jog redesign delegation and upper height limit

On2026-10-20 the engineer requests redesigning the jog to fit a controller with16mm internal height. After the current F11 stack is measured read-only and its height conflict explained, the engineer selects **“Nowa mechanika, także inne łożyska”** and **“Nie zwiększaj obecnej wysokości”**.

Authorized scope: Basia selects dimensions of new printed mechanics and proposes a new spindle, bearings and metal spring; retain platterD100, axial travel1.5, AS5048A and currentD8x4 magnet. The selected upper limit is15.5mm above the local nominal panel top in the released position. Specific new purchased components require engineer acceptance. This supersedes the earlier engineer-owned-only jog preparation instruction for this separately requested redesign, not the scope of the unrelated enclosure work.

[F12-FEASIBILITY-01](../schematics/jog-wheel/F12/Jog_Wheel_Rev_F12_review.md) is a conditional axial/mount section and separate illustrative PNG, not a finished reconstructible drawing or a named approval. Proposed SKF61806-2RS1/D30x42x7 pair, metal spring/force and complete retention/hardware remain unresolved. **No drawing/model approval, Fusion mutation, cloud save, approved-file overwrite or fabrication-export permission.** F11/B19 remain preserved.

## Shared under-display zone and right-rear interfaces — B20

The engineer states **“Idźmy zatem w tę stronę, że RPi, DAC Pro i zasilacz będą umieszczone pod wyświetlaczem. Gniadzo zasilania i gniazda RCA przesuń do prawej sekcji obudowy.”** This confirms all three devices under the display and relocation of the two selected interfaces. Retain their existing rear-wall orientation as the conservative interpretation; no switch to side-wall ports, purchased geometry change or named drawing/model approval is inferred.

[B20-PACK-01](../schematics/enclosure/B20/DJC_Enclosure_Rev_B20_drawing.pdf) is a four-sheet source-backed initial plan/height study, not a complete reconstructible/model-ready release. Candidate centres Pi(217.5,46.25), DAC(305.5,46.25), PSU(388,55); rear mains(X420.5,Z18), RCA(X560.3,Z18).687 nominal plan pairs clear,35 posts/control envelopes retained; source-specified body/land reserves1/0.75 and inlet/PSU plan gap2 are not strength, service or electrical acceptance.

Agent proposal **front20/rear38**, not an engineer-approved new rear height: full-depth check rejects initial rear36 with0.716667 panel/proxy overlap; rear38 clears the whole inlet reach by1.1. Preserve the20 exterior-front target. Display angle10 is separate and its elevation remainsTBD from DAC heights and mounts. Proposed source-cell vent relocation avoids10 old grille/window intersections;48 cells/528 polygon-obstacle checks pass. Four final sheets and genuinely converted illustrative PNG reviewed; no actual Fusion surface is claimed.

Proposed low PSU mount requires **two BOSSARD1076450 / BN616 M3×6 countersunk A2 screws**, identified from [listing](https://www.tme.com/us/en-us/details/b3x6_bn616/bolts/bossard/1076450/) and [manufacturer drawing](https://www.tme.com/Document/7e7411081962d74ace4f61343f40af63/BN616.pdf): exact head maxD6/H1.7/90degrees, HEX2, countersunk length6. With pad top3/floor2, PSU top31/ceiling32, nominal engagement3 in max4 and top gap1. **Engineer acceptance is still required; no new fastener selection or physical strength/fit is approved here.** Manufacturer warns DIN7991 is withdrawn and ISO change-over needs verification; do not substitute different head dimensions.

Open input: separate DAC projection below PCB underside and height above the same datum; old36 stack is not reused. Separate conditional F12 remains its own workstream; this task does not modify it or certify its inclined interfaces. B19 archive matches its approved SHA256. Latest read-only host list contains0 documents; no assistant open/close/save/geometry/camera/pose action. Source packages preserved; task preview directory removed. **CHANGES REQUIRED before model-ready drawing approval; no B20 Fusion geometry or fabrication exports.**

## F12 bearing acceptance, spring selection delegation and pusher requirement

On2026-10-20, answering the specific F12 component questions, the engineer states **“ad.1 Tak / ad.2 Dobierz coś”** and asks whether the pusher pressing the microswitch is retained and whether a smaller switch is wanted.

**Accepted purchased input:** SKF61806-2RS1/D30x42x7, two per jog/four per controller, with the previously cited SKF source. **Delegated:** Basia chooses a prototype metal return-spring arrangement and presents its forces; do not require the engineer to supply a new force target before selection. Preserve the pusher function, cavity16, above-panel15.5, D100 and travel1.5. This does not approve a complete drawing/model, spring/switch proposal, purchase, Fusion mutation/save or exports.

[F12-COMPONENTS-02 proposal](../schematics/jog-wheel/F12/Jog_Wheel_Rev_F12_components_02.md):4xsteelD-111600070 per jog, installed3.5..2 after proposed0.5 underside reliefs, nominal2.01..4.02N. Pusher on nonrotating carrier; retain D2F family/FL3 and prefer compact solder suffix-D, not an arbitrary smaller switch. Calibrated ON1.1 and separate hard stop1.5; unloaded lever exceeds cavity, requiring assembled predeflection/panel-open service. New complete PDF and actual component/force/geometry/strength checks are still required. Initial F12 study/F11/B19 files remain preserved; no Fusion access or fabrication exports in this selection task.

## Engineer acceptance of F12-COMPONENTS-02

On2026-10-20, immediately after the spring/microswitch/pusher proposal and its stated limits are presented, the engineer replies **“Akceptuję”**. **APPROVED: F12-COMPONENTS-02 prototype component selection and described nominal actuation/return arrangement**, not a complete drawing or model.

Accepted scope: four EN10270-1-DH D-111600070 springs per jog/eight total from the cited supplier sources; proposed installed3.5..2 and nominal package2.01..4.02N with four0.5 underside reliefs; D2F-01FL3-D compact solder-terminal switch; pusher on the nonrotating carrier; target ON1.1, separate structural end stop1.5 and nominal remaining0.4; installed lever predeflection and panel-open service requirement. Retain cavity16/above-panel15.5/D100/current magnet/AS5048A and previously accepted SKF61806-2RS1 pair.

The accepted [report](../schematics/jog-wheel/F12/Jog_Wheel_Rev_F12_components_02.md), [definition](../schematics/jog-wheel/F12/Jog_Wheel_Rev_F12_components_02.json) and [executed checks](../schematics/jog-wheel/F12/Jog_Wheel_Rev_F12_components_02_checks.json) are preserved unchanged, including historical proposal/pending labels. Snapshot SHA256:

| Artifact | SHA256 |
|---|---|
| `Jog_Wheel_Rev_F12_components_02.md` | `5636db643397ec0484e326a9336c18ab7b4c9635c20064868acc33785b5e40eb` |
| `Jog_Wheel_Rev_F12_components_02.json` | `3008d6343441c4d4379e4042b5d81b7dfdd0ebfe3c4116a287fd813a13eec3c7` |
| `Jog_Wheel_Rev_F12_components_02_checks.json` | `2b1f5b8f9240cbe1fdb6e560b6c5bedf6e7e0d38f32cecb0cfaa5e31d2cf3695` |

Exceptions remain: unloaded switch lever can exceed16; actual spring batch/Ln/solid height/force, moving mass/friction/return,1-mm cover roof/base/pin strength, switch calibration/terminals, full geometry/tolerances/service/inclined integration and physical acceptance are unverified. Nominal OT/force checks are not safety, strength or functional certification.

Next owner: Basia completes a new uniquely reconstructible dimensioned PDF with these accepted inputs, full pusher/key/stops/retention, seats/hardware and PCB/wires, then requests explicit named drawing approval. **No complete F12 drawing/model approval, purchasing instruction, Fusion mutation/cloud save, approved-file overwrite, document close/discard or STL/STEP/F3D export authority is granted.** F11/B19 and initial F12 study remain preserved.

## B20 flat main body and local display housing direction

The engineer first requests mains in the former right RCA candidate, RCA left of the display, one central grille, and supplies **DAC vertical dimensions equal to Pi**. Exact proposed BN616/BOSSARD1076450 M3x6 countersunk PSU screws are accepted **“Jeśli zasilacz pozwala na ich użycie, to tak”**. The later instruction supersedes the far-right mains placement: **keep the existing mains inlet immediately behind the PSU**, in the separately raised rear display housing; RCA remains left of the screen.

**B20-DIRECTION-02 is a requirements record, not an approved drawing/model revision.** Target flat20mm EXTERIOR main body, including the rear outside the raised display region; independently inclined display near10degrees with a rear housing transition integrated into the enclosure styling. All three Pi/DAC/PSU stay beneath that local raised zone, preferably aligned. One central grille remains requested. The prior global front20/rear38 B20-PACK-01 PDF/concept and their executed checks are superseded layout evidence and remain byte-preserved, not permission to model the changed arrangement.

Executed source-based height calculation: retained floor2/panel2 leave16 useful inside20 exterior; bare Pi19.9 and PSU28 cannot fit this low region. Engineer-declared DAC equivalence uses the bare Pi datum chain2.1 below PCB underside/17.8 above it. A30mm useful local cavity with2mm floor and an EMPTY2mm roof would already be34 exterior, not the final display-housing height. Known display17 is an inward-normal rear-frame contact depth, not a uniform full-screen solid; actual display/mount placement must define the final local height. These components require local volume, not a slope over the whole main deck. A smaller inlet alone cannot make the PSU/display zone20mm.

Conditional fastener source check: supplied Mean Well drawing `elements/05839_datasheet.pdf` calls out bottom2-M3 L=4. Proposed6mm length INCLUDING countersunk head minus case-bottomZ3 gives3mm nominal penetration, matching the old nominal penetration and leaving1mm against that callout. The conditional acceptance and nominal depth condition are recorded; actual useful thread/tolerance, head seating, printed bearing/strength, torque and physical compatibility remain unverified. Do not substitute the larger ISO10642 head.

New checks still required before a model-ready drawing: inlet/PSU placement (old inlet proxy and PSU simply moved to the Pi/DAC row overlap6.75mm in plan, not proven actual solid collision); central grille versus retained rear postX300; RCA19.9-high face/window/lands in the proposed rear wall; headphone11.8 body plus6.5 straight-terminal axial reference versus16 main cavity; full display/control/support/assembly interfaces and separately accepted F12 integration. Exact centres, local housing dimensions, clearances, blends and grille pattern remainTBD. No new Fusion geometry, cloud save/close/discard, approved-file overwrite or STL/STEP/F3D export is authorized by this discussion.

## B20 horizontal rear headphone jack beside RCA

The engineer states **“Gniazdo słuchawkowe umieśćmy poziomo na tyle obudowy obok panelu RCA”**. Amend the current B20-DIRECTION-02 requirements: retain the selected J01 jack/nut, move it from the top panel to the rear wall beside RCA, with horizontal axis, plug entering from the rear and body/terminals directed into the enclosure. RCA remains left of the display. Remove the former J01 top opening in the successor drawing/model; frozen R12/B19 and all prior packages are unchanged.

Executed nominal source check from B09 equipment: bodyD8.15 is below the16mm main cavity height;11.8 body plus6.5 straight-terminal axial reference now occupy18.3mm along the horizontal axis rather than vertically. Retained2mm wall with4.5 threaded length and1.8 nut gives0.7mm nominal remaining thread. This removes the old orientation's height conflict, not proof of full installed fit or approval of the whole20mm case.

Exact X/Z axis, which side of RCA, spacing, panel seat/hole, nut/tool access and complete connected envelope remainTBD in the next model-ready drawing. No new clearance, purchased geometry, named drawing/model approval, Fusion mutation, cloud save/close/discard, approved-file overwrite or fabrication export is implied.

## B21-LAYOUT-01 source-checked proposal publication

On the engineer's **“Kontynuuj prace”**, Basia advances the latest flat20/local-display/rear-audio direction into [B21-LAYOUT-01 six-sheet PDF](../schematics/enclosure/B21/DJC_Enclosure_Rev_B21_drawing.pdf), separate [illustrative PNG](../schematics/enclosure/B21/DJC_Enclosure_Rev_B21_concept.png), [definition](../schematics/enclosure/B21/DJC_Enclosure_Rev_B21_definition.json) and [executed checks](../schematics/enclosure/B21/DJC_Enclosure_Rev_B21_validation.json). **Publication is not engineer drawing/model approval; CHANGES REQUIRED before complete model-ready release.**

Proposed geometry: main600x300/flat20 exterior; local housingX153.55..446.45/Y0..96,10deg roof/front bevel, seat centreZ56/rear roof66.155. The height uses a conservative extended frame-contact construction datum to provide requested30 local cavity at PSU, not a uniform17mm display solid or proven minimum. Devices commonY54; mains(X419.2,Z21.5) behindPSU clears source post390 foot/core without cutting it; RCA(X54.7,Z10) and horizontalJ01(X88,Z10) on rear-left, old top J01 hole absent. One48-cell central grille has a15-wide structural centre rib. Printed RCA passage becomes34.9x16 notch with full lands, source holeZ9.95; actual rear-body fit still trial/unqualified.

Under existing printed-dimension delegation, new display columns/toes narrow to5.7/7.7 and screw/galleryq140.7, preserving A2/B17 contact pads and source hardware; nominal pilot ligament0.95/head margin0.75/hole ligament1.8 are not strength approval. Housing clears B03/B05 **upper aperture rims**, not just caps. P01-P03 decorative ticks move to the exposed right semicircle, retaining175 marks and all control axes/travel. No purchased geometry is changed.

Executed824 source-union plan pairs and1 explicit post-foot/core height-separated pair;98 fixed/removable control groups/338 floor-bottom primitives rebuilt to flat seats,88 cap/housing pairs and576 grille polygon/post/port comparisons clear in stated scope.13 conservative region boxes fit nominal250, not confirmed margins/orientations/supports. All6 final PDF sheets generated/reopened/rendered/visually reviewed,16 annotations checked. Real finalPNG1536x1024 decoded/opened after correcting the first generation's steep screen; rear ports hidden/captioned, approximate image controls/scale not drawing evidence.62 source hashes and all B19/B20/F12 bytes preserved.

PDF SHA256 `d0a8deb4a4a29fa4223c5851a67403f9e0d76a63fbe3303b82f0a8f3059ddce6`; concept SHA256 `2d077954258be75a9fb173693c49ba175163d9a6da7188ab318b7e9405c1091b`. [Actual review](../schematics/enclosure/B21/DJC_Enclosure_Rev_B21_drawing_validation.json). Original B20 study is retained unchanged; future Fusion outputs belong in `models/enclosure/B21/FUSION/`, not created.

Blocking inputs: exact DAC PCB corner registration/laminate/new-fastener engagement not uniquely specified by supplier65x57 versus text65x58 and58x49 pitch; Pi-equivalent vertical heights are already supplied and must not be re-asked. Separate accepted F12 components are not a final mounting/retention/PCB/hardware drawing. Engineer review is still required for local66.155 height, RCA notch, display support/tick/gap choices. No named complete drawing/model approval, Fusion mutation, save/close/discard, approved overwrite, fabrication export or whole-body/head/motion/physical/thermal/electrical/strength certification follows.

## F12-D03 detailed nominal drawing publication — approval requested

On2026-10-20 the engineer says **“No to jedziesz maleńka”** after the next-step plan to complete the detailed drawing, obtain named approval and only then model in Fusion. This authorizes preparation/review work, **not approval of an unseen drawing/model**, purchased fasteners, saving or exports.

Published [F12-D03 14-sheet dimensioned PDF](../schematics/jog-wheel/F12-D03/Jog_Wheel_Rev_F12_D03_DRAFT.pdf), separate [LLM concept PNG](../schematics/jog-wheel/F12-D03/Jog_Wheel_Rev_F12_D03_concept.png), [complete nominal definition](../schematics/jog-wheel/F12-D03/Jog_Wheel_Rev_F12_D03_definition.json), [supplier sources](../schematics/jog-wheel/F12-D03/Jog_Wheel_Rev_F12_D03_hardware_sources.json) and [actual checks/scope](../schematics/jog-wheel/F12-D03/Jog_Wheel_Rev_F12_D03_review.md). Existing COMPONENTS-02 remains accepted/frozen; F11/B19 and the initial F12 study are not overwritten.

Under existing printed-dimension delegation: new hollow spindle/post/shoulders/customT30 collars, covers/bosses, floor-backed housing/guide/ears, key/pusher/registered H05 groove, independent hard stops, four spring seats/pins, PCB toes/nut bays/wire trough, switch wall/slots/captive-nut keepers. Ten printed definitions/12 pieces and full41-item nominal discrete BOM per jog, not actual CAD body counts. Retain accepted bearings/springs/switch, D100,1.5 travel, current magnet/module, cavity16 and above-panel limit15.5. Explicit new choice: same12 platter rim moves down0.1 to21.4..33.4, giving15.4 above nominal panel18. The complete moving packet passes throughD52; the entire jog is not16 high.

New exact fasteners proposed with the drawing: Newstar M2X4-KHA4MC-SF-DIN7991; Accu SSCF-M2-4-A2-BL/SSCF-M2-10-A2-BL/HPN-M2-A2-BL/HPW-M2-A2/HPN-M3-A2-BL. Retain floorM2.5x6 maximum-envelope reference. No ISO10642 substitution or actual lot/fillet/torque/thread-fit approval. H05 printed geometry unchanged. Magnet bonded flush at6.6, not bottomed against ceiling; actual adhesive qualification remains.

Current enclosure is flatB21, not superseded global-slopeB20: moduleCAD=(Xj,-150,2)+Rz60*local, Xj110/490; six axes on sheet14, direct floor backing plus retainedD10x6 bosses/raised ears. KeepD52 and D108x1 well; pressed nominal rim/well gap2.9. B21 files not changed; whole-case integration is not approved or checked here.

Executed49 static constraints and301 positions x14 inequalities at0.005mm, numerical1e-9 equality threshold, six axes/11 source hashes;14 A3 vector pages generated/reopened/rasterized/visually reviewed, real1536x1024 PNG generated/converted/opened. Final sensor screw review extends the blindD2.2 clearance below its nut bay toZ0.2, avoiding the tip/base clash and leaving0.1 axial reserve. **Zero native CAD body/feature-health/BRep-pair/whole-case/physical checks.** PDF SHA256 `e974162cf9e87fba07f7331a1ad4d43b7e53c4d21eb0bc282e13a404989fd1b3`; concept `22521105899ec1505d3c73643d6f552aa4ddf943af9adf8f28a8cda85a271afc`.

Limits expressly retained: spring package2.01..4.02N is not finger force/return proof; release ideal no-friction mass ceiling204.963g, bearings already50g, moving mass unmeasured. Fine customT30,0.4 cover rims/0.2 residual stock/1-mm spring roof/base/retainer strength need coupons/physical tests. OmronA is direction, not an exact XY contact point; no invented complete lever trajectory. Actual switch/terminals/solder/wires/clamp lands/bond/calibration and supplier tolerances remain unqualified. Unloaded lever can exceed16; installed predeflection/panel-open service remains required. Raw boxes below250 do not approve actual print settings/orientations/margins/supports.

**CHANGES REQUIRED / request named F12-D03 nominal printed-prototype drawing approval, including proposed fasteners and stated physical/reference limits.** Separate editable Fusion model/geometry/health/actual views and named model approval must follow before STL/STEP/F3D. No cloud-save/destination, close/discard, approved-overwrite or purchasing/export instruction. Latest read-only Fusion list0 documents; no mutation. Task-local previews/source inspection scripts are removed after review; permanent sources/evidence remain in the nine-file package.

## B22 rear packing, inlet removal and continuous screen-roof direction

The engineer explicitly instructs: remove the mains inlet for now; move Pi, DAC Pro and PSU as far rearward as possible; adapt screen inclination; eliminate B21's additional front display wall; a greater angle and horizontal cover behind the screen are allowed. DAC mounting pitch is the same as Pi. Keep the old jog mount and provisionally assume the separately redesigned mechanism fits the height while that work continues. **This is direction/dimensional authority, not named approval of a new unseen drawing/model.**

Published [B22-LAYOUT-01 eight-sheet PDF](../schematics/enclosure/B22/DJC_Enclosure_Rev_B22_drawing.pdf), [illustrative PNG](../schematics/enclosure/B22/DJC_Enclosure_Rev_B22_concept.png), [dimensional definition](../schematics/enclosure/B22/DJC_Enclosure_Rev_B22_definition.json) and [scoped executed checks](../schematics/enclosure/B22/DJC_Enclosure_Rev_B22_validation.json). No inlet opening/body/fasteners or replacement feed route. Fixed-X nominal body rearsY8.75 derive from rearpostD9 edge8.5+selected0.25 trial gap; Pi/DAC/PSU centresY37.95/37.75/34.25. Lower printed Pi/DAC bearing plane to6; Pi source spacer4/pilot5 leave1 nominal blind reserve/1 floor skin. DAC58x49 pitch is closed, independently datumed; no invented PCB registration/laminate/bore. Four plain pads require actual matched drilling/fastening qualification, not fictitious completed retention.

Proposed continuous49deg screen joins flat20 panel atY96 with no blank front wall; horizontal rear cover reaches80.376766. The angle follows targets24.8/24.8/32 at device fronts using the extended w-17 FRAME CONTACT construction datum; selected1 reserve over Pi/DAC baretop23.8 is a printed-layout choice. At48deg Pi misses that reserve. **This rear is taller than B21, not a proven minimum or actual LCD-body fit.** New module splitX335/rear10 lap/twoM3x8, roof-integral display supports/off-case assembly and front retention use explicit printed geometry. Remove only two LCD-conflicting panelposts/bores(228,90),(372,90), retain33 source axes. Old six jog mounts remain unchanged; height-fit is engineer-assumed, not verified old41mm/new-mechanism clearance.

Executed677 device/port/control/post/controller plan comparisons,1330 pad/obstacle pairs,88 cap/housing pairs,528 grille polygon/post/port pairs and48 roof-support/device bounds pairs;98 control groups/338 floor-bottom primitives, six old jog axes, screw stacks/front continuity and14 nominal print boxes checked.70 input hashes/56 prework B19/B20/B21/F12 files preserved. Eight final native A3 sheets reopened/rendered/visually reviewed,13 annotations checked; real1536x1024 PNG generated/converted/opened, not a Fusion view. PDF SHA256 `4f149bbafdadd366d3f30ba15ce00e8bc77c6fead07ac61c65c5fe297aae97aa`; concept `d4ed43c18f9c8da70a96b201a44139ad604d2776ad5a28347937f70eda869b69`.

**CHANGES REQUIRED / request engineer review of namedB22-LAYOUT-01 and49deg/80.377/new printed interfaces.** Actual DAC registered outline/bearing/retention, complete LCD rear/contact/service, future actual jog integration, native all-body/head/feature-health/motion, physical strength/thread/fit and final print constraints remain unqualified. Keep separate F12 approvals independent; do not re-ask already answered DAC pitch/vertical height or require final F12 before this provisional layout. No complete model-ready/named drawing approval, model approval, Fusion mutation/save/close/discard, approved-file overwrite, STL/STEP/F3D or electrical/thermal release. Latest read-only host list0 documents; task previews removed after review.

## Engineer approval of F12-D03 nominal printed-prototype drawing

On2026-10-20, directly answering the presented F12-D03 detailed drawing and request for its named nominal-prototype scope, the engineer states **“Zatwierdzam”**. **APPROVED: F12-D03 drawing**, including its explicitly proposed fasteners and stated reference/physical limits. PDF SHA256 `e974162cf9e87fba07f7331a1ad4d43b7e53c4d21eb0bc282e13a404989fd1b3`.

Freeze all nine files in `schematics/jog-wheel/F12-D03/` byte-for-byte, including historical NOT APPROVED/proposal labels. This later acceptance supersedes those labels without rewriting the package. [Exact nine-file fingerprints and scope](../models/jog-wheel/F12-D03/FUSION/Jog_Wheel_Rev_F12_D03_Fusion01_sources.json). Retain approved COMPONENTS-02/F11/B19 and unmodified B21.

Basia may now create the native editable standalone nominal jog model **F12-D03-Fusion01** in a NEW unsaved Fusion document, following the approved printed geometry and reference limitations. Cavity16, D100, travel1.5, top15.4 above nominal panel, carrier pusher/ON1.1/independent stops, full source hardware and unchanged H05 remain governing. New physical geometry/clearance corrections return through the drawing workflow.

This is **not** model approval, complete enclosure approval, physical return/strength/fit certification, purchasing authority or permission to cloud-save/overwrite/close/discard. No STL/STEP/F3D exports before separate named model approval. Full moving mass/friction, fine T30/cover/base/retainer strength, actual switch/lever/terminals/solder/wires/magnet bond and final print setup remain unqualified. Current Fusion inspection:2705.1.30,0 open documents/no active command; repository shared filesystem and exact approved PDF hash verified read-only.

## Engineer request for periodic Fusion recovery saves

The engineer confirms that Fusion360 crashed during F12-D03-Fusion01 work and requests periodic persistence, on disk or in the cloud. Record this as a workflow requirement: create a recoverable working copy after each completed modeling stage and before expensive validation, rather than waiting for model approval. Recovery copies are explicitly WIP/unapproved; they must not be confused with approved fabrication deliverables.

The engineer explicitly selects **“Lokalne archiwa F3D WIP”** and confirms `models/jog-wheel/F12-D03/FUSION/checkpoints/`: numbered local recovery archives before model approval, after completed stages and before heavy validation, no overwrites/cloud save/STL/STEP. This is a specific exception for unapproved recovery F3D copies, not approval of geometry or fabrication deliverables. First actual recovery archive: `Jog_Wheel_Rev_F12_D03_Fusion01_WIP_001.f3d`, timeline323,874016 bytes, ZIP CRC PASS, SHA256 `7ca8bdb9be3640e207bb10929d233adb6bf15ba6bd6bdad9f42fd989eb0bfae1`. Native history archive created by ExportManager; round-trip reopening has not yet been exercised. Active document remains unsaved to cloud. No approved overwrite, close/discard, dependency or runtime-configuration permission.

After the crash the tools reported zero documents and no retained builder module. A new unsaved `Jog Wheel F12-D03 Fusion01 DRAFT` was initialized from the nine hash-verified frozen drawing files. Last completed reconstruction stages: carrier, housing, covers and small printed parts; timeline323. Earlier native all-body validation did not produce a completed report and must not be claimed as passed.

## Engineer elects to interrupt Fusion and recover F12 WIP014

After the native P01 recess-pattern correction remained in flight and repeated MCP execution/read requests timed out, the engineer selects **“Przerwę Fusion; wracamy do WIP_014”**. The engineer will interrupt/restart Fusion and notify Basia. No assistant-forced close, discard or restart has been performed; do not issue further CAD operations until that notification and a fresh document inspection. The uncheckpointed correction may be lost. Existing recovery archives must remain unchanged.

Exact recovery file: `models/jog-wheel/F12-D03/FUSION/checkpoints/Jog_Wheel_Rev_F12_D03_Fusion01_WIP_014.f3d`,7853080 bytes, SHA256 `cdffe85cf9675c7a71375b7e4665e653f9dc031d394ca169e8930921089b5f66`; companion JSON records stage `before replacing ineffective combine-feature pattern with body-tool pattern`,726 timeline entries,45 logical instances/46 native body instances. All14 completed recovery archives were verified from the repository for size/SHA256/ZIP CRC/native-design segment; reopening has not yet been exercised. No completed WIP015 manifest was present at this check.

Known defect in WIP014: P01 has only one actual rim recess despite the feature reporting12 elements. Native radial rays confirmed45.25 at0deg but48.75 at the other11 intended recess axes. Changing the feature compute mode did not establish a successful correction. The replacement body-tool-pattern source is prepared, but its in-flight native result is NOT verified. Do not print or approve this checkpoint.

Other completed, scoped observations before this correction:726 healthy timeline entries; actual rigid slider moved all intended instances1.5mm, rotor exercised90deg and release restored.192 native ray/face thread samples passed, maximum sampled nominal radial deviation0.000002174mm and shared nominal gap0.05mm. Earlier pointContainment disagreed with a full-solid BRep witness and was not accepted as a thread-surface measurement. These are finite nominal observations, not all-body/full-recompute/continuous-motion/physical qualification.

**CHANGES REQUIRED / MODEL NOT APPROVED.** After engineer notification: inspect/reopen WIP014 without cloud-saving or overwriting it; rebind native objects rather than re-running constructors over an imported model; repair P01 to the unchanged approved12-recess drawing; rerun actual geometry/feature-health/all-body/motion checks, create actual PNG review views and only then request named model approval. All nine frozen drawing files remain hash-identical. No STL/STEP or final F3D fabrication delivery.

## Engineer reports Fusion ready and F12 recovery resumes

The engineer states **“Fusion gotowy”**, authorizing continuation after the selected restart/recovery. Read-only inspection finds0 open documents. Exact WIP014 is imported into a new unsaved `Jog Wheel F12-D03 Fusion01 DRAFT`; its726 native history entries,46 body instances and all previously recorded body volumes/instance transforms match the pre-export construction record. [Reopen evidence](../models/jog-wheel/F12-D03/FUSION/Jog_Wheel_Rev_F12_D03_Fusion01_recovery-reopen.json). Old recovery files are not overwritten.

Recovered native data revealed a separate implementation error: uncaptured H05/P09 transforms had already reverted before WIP014 was saved. Approved H05 mapping `(24.3,-7,10.5)` with source axis+X and P09 positions `(24.3,7.15,4.9)`/`(24.3,13.65,4.9)` are restored using Capture Position and a rebuilt fixed rigid group; actual installed bounds checked. This corrects the model to the unchanged drawing, not a new dimensional choice. Canonical construction now captures these placements.

P01's body-tool-pattern correction is appended at the history end without deleting/replaying the earlier thread-feature chain.24 actual native radial rays confirm all12 recess axes atR45.25 and12 retained intervals atR48.75/Z27.4. [Settled correction evidence](../models/jog-wheel/F12-D03/FUSION/Jog_Wheel_Rev_F12_D03_Fusion01_rim-correction.json). WIP017 records733 healthy history entries/45 logical/46 body instances; WIP018 is saved before full validation. Full recompute/all-body/motion validation is in progress, not yet a pass. No model approval, cloud save or fabrication exports are inferred.

## Engineer accepts exact Base Feature geometry for P01 P04 P07

After three procedural thread approaches failed native solid verification or Fusion stability, the engineer reports another crash/restart and explicitly selects **“Tak — Base Feature dla trzech części”**. Approved representation scope: preserve exact WIP018 geometry for printed P01 (platter/spindle/magnet post), P04 and P07 as direct-editable native Base Features without their procedural feature history. Retain native history for all other parts and rebuild the unchanged assembly relationships. This is **not** a dimensional change, drawing revision or whole-model approval.

Exact source: `models/jog-wheel/F12-D03/FUSION/checkpoints/Jog_Wheel_Rev_F12_D03_Fusion01_WIP_018.f3d`, SHA256 `24eeece69a92be5c5747de865036f5640a352e816cada8ad3e66cdf677151309`. Eight cached solid/void native BRep witnesses pass for P01/P04/P07 after reopening; [evidence](../models/jog-wheel/F12-D03/FUSION/Jog_Wheel_Rev_F12_D03_Fusion01_cached-thread-witnesses.json). Source archive remains intact. Preserve archived original history as provenance; do not replay the unstable procedural sweeps.

Known rejected alternative WIP021 passes surface rays but fails a native solid-material witness; its manifest explicitly excludes it from valid recovery. Quarter-cut construction did not settle before the engineer-reported crash. No failed or incomplete attempt is an approved model. Base Feature conversion still requires exact-shape comparison, feature-health/full-recompute/all-body/motion checks, actual Fusion review PNGs and separate named model approval. Local numbered WIP checkpoints remain authorized; no cloud save/approved overwrite/STL/STEP or final fabrication F3D delivery.

Implementation evidence after conversion: exact copied P01/P04/P07 topology, volume and bounds match cached WIP018; other43 native body instances are unchanged. [Conversion record](../models/jog-wheel/F12-D03/FUSION/Jog_Wheel_Rev_F12_D03_Fusion01_base-feature-conversion.json). Rebuilt unchanged relationships exercise1.5mm translation/90deg rotation and restore release. [Full native recompute](../models/jog-wheel/F12-D03/FUSION/Jog_Wheel_Rev_F12_D03_Fusion01_base-feature-recompute.json) passes in0.7804846s with582 timeline entries,46 recursive component definitions,zero health issues and192 passing native thread rays. WIP025 is the pre-validation recovery copy. This is implementation evidence, not engineer approval of F12-D03-Fusion01 or physical verification.

## F12-D03-Fusion01 completed inspection requires engineering decisions

This records observed results, **not engineer model approval or new dimensional authority**. [Final review](../models/jog-wheel/F12-D03/FUSION/Jog_Wheel_Rev_F12_D03_Fusion01_validation.md):46 represented bodies/16 poses/16560 pair outcomes,126 critical checks passed; independent all46-body native release analysis agrees in positive overlap volume. Corrective reference sampling retains15824 unchanged outcomes and rechecks736 affected pairs/64 native BRep intersections. Real switch/lever/spring behavior remains unqualified. Five final actual PNGs are inspected and source/camera/visibility restored.

**CHANGES REQUIRED:** both PCB M2 nut straight insertion paths hit the P03 floor,29 of33 samples per nut/max3.7501848324mm³; seated fit is not proof of access. Upper SKF source-ring envelope overlaps P01 R0.2 root by approximately0.493242155mm³ at every pose. Exact bearing corner relief is absent and three native containment qualification attempts fail; this is escalated, not accepted as an automatic exception or replaced by guessed geometry.

Next owner is the responsible engineer: authorize only the proposed localized P03 nut-entry drawing revision (D04), or demonstrate unchanged-D03 assembly, and resolve bearing-corner evidence/exception. No such authorization or model approval has yet been received. Preserve all nine approved D03 files. Any geometry change requires a new drawing approval before Fusion, then separate named model approval.

Post-review local recovery is WIP027,9197823bytes/SHA256 `71f4a71582956a99e8f30a39545eb95848c82ba106988a1bb533b5f3161742c7`; all27 local archives pass repository size/SHA256/CRC. WIP027 is not round-trip reopened. No cloud save, approved overwrite, fabrication export or physical verification occurred.

## Engineer authorizes a localized F12-D04 PCB nut-access drawing proposal

The engineer explicitly selects **“Tak — przygotuj F12-D04”** for the localized P03 access correction, retaining seated nut positions, screw axes, PCB height and the16-mm fixed-body envelope. Basia may select only the local access geometry and publish a new drawing proposal. This is not approval of D04, a changed model, Fusion geometry, cloud save or fabrication exports. All nine approved D03 drawing files remain frozen.

For the upper-bearing corner issue the engineer selects **“Zweryfikuję rzeczywiste łożysko”**. Actual corner/fit verification remains the engineer's action; the reference-envelope exception is not accepted, and P01/bearing geometry must remain unchanged. F12-D03-Fusion01/WIP027 stays CHANGES REQUIRED. After D04 publication, obtain the missing bearing evidence and explicit named drawing approval before model correction.

Publication evidence, not approval: selected entry endY8.0 above minimum `3+2*4/sqrt(3)=7.618802154`, loading centreY5.5. Existing cutX±2.1/Z0.6..2.3, seats, axes, PCB height/fixed16 envelope and all80 inherited parameter values retained. [Published F12-D04 review](../schematics/jog-wheel/F12-D04/Jog_Wheel_Rev_F12_D04_review.md):15 searchable A3 sheets,49 retained static constraints/301×14 stroke samples,20 access bounds/444 complete-nut positions/1870 inequalities,21 source hashes including nine frozen D03 files; actual PDF17 annotations and visual layout reviewed. Real1536x1024 concept PNG opened/converted/reopened; no D04 CAD geometry or physical approval. Named D04 drawing acceptance and engineer-owned bearing evidence are still pending.

New D04 PDF SHA256 `c37fcde3299725244f2aa33b4ee90d03e4aa9cc4abb062f7079532a9d53bd517`; concept SHA256 `c930a1d5f2b70878f38b066a2a6983668e08fdf9ed68cff6e748c0cc1a52d7ad`. D03 model/WIP027 remains unchanged/CHANGES REQUIRED; no cloud save or fabrication exports.

Final read-only Fusion observation after D04 publication: the named D03 draft now reports `isSaved=true`, `isModified=false`, cloud lineage `urn:adsk.wipprod:dm.lineage:fNqin9L-QfCpF8zZ6-06UQ`, parent project/folder `Default Project`. The agent issued no cloud-save operation; this observation does not establish who saved it, model approval or equality to WIP027. The unsaved-draft validation guard refused continued validation and was not bypassed. No further CAD mutation followed; cloud-version equivalence remains unverified.

## Engineer approval of F12-D04 nominal printed-prototype drawing

The engineer explicitly states **“Akceptuję F12-D04”**. **APPROVED: F12-D04 nominal printed-prototype drawing**, the published15-sheet package and its stated reference/physical limits. This accepts the localized P03 PCB nut-access geometry: two existing entry cuts extendY3.1→8.0, with top loading atY5.5 followed by seating in unchanged positions. Seated nuts, screw axes, PCB height, fixed16-mm envelope and all80 inherited parameter values remain governing. The integral printed P01 platter/hollow spindle/magnet post and inherited exact hardware are unchanged.

Freeze all nine files in `schematics/jog-wheel/F12-D04/` byte-for-byte. This later approval supersedes historical DRAFT/NOT APPROVED/proposal flags inside those files without rewriting them. Do not rename the PDF, rerun generators/checkers that write into the approved directory, or alter approved content; a geometry correction requires a new revision. Approved D03, COMPONENTS-02/F11/B19 and unrelated B21/B22 work remain preserved.

| Frozen file | SHA256 |
|---|---|
| `Jog_Wheel_Rev_F12_D04_DRAFT.pdf` | `c37fcde3299725244f2aa33b4ee90d03e4aa9cc4abb062f7079532a9d53bd517` |
| `Jog_Wheel_Rev_F12_D04_concept.png` | `c930a1d5f2b70878f38b066a2a6983668e08fdf9ed68cff6e748c0cc1a52d7ad` |
| `Jog_Wheel_Rev_F12_D04_definition.json` | `abbd7339fc5565befa5a889e7a82525f886202b4397df3b2bbc93c224fbd4b2c` |
| `Jog_Wheel_Rev_F12_D04_define.py` | `0a5d5012cdf27f70859b8012d12a4813aaa8d1f58a0942342c594ea155965be1` |
| `Jog_Wheel_Rev_F12_D04_drawing.swift` | `c9788444e16b647941226a67feea0ec514f3d5c456bfd8ea10cde004a0935d87` |
| `Jog_Wheel_Rev_F12_D04_check.py` | `6cb12660ca71638b67812fba53de2915cdd4f54b78a7ffe00b7f1a638f584917` |
| `Jog_Wheel_Rev_F12_D04_checks.json` | `6dea1c93afa3bd566394fe6e3080398cd767c870557ab8a3585ffd73f6b0b30a` |
| `Jog_Wheel_Rev_F12_D04_hardware_sources.json` | `fdc8ebc641a3f6a56dd815ffad4ab487af2de2045b6fc398d0b9a7f22b1b7875` |
| `Jog_Wheel_Rev_F12_D04_review.md` | `1cfca817ee04a5660c860ecb648aef0227e6252fef5873a965882cad8267ac0b` |

Verification at acceptance: the four published core-artifact sizes/hashes, all21 source hashes and the exact nine-file package match the reviewed publication. Existing D04 analytic/PDF/image evidence remains scoped as published; no new native or physical pass is inferred.

**Still open:** the engineer's selected actual upper-bearing corner/fit verification. No result has been supplied and the P01/C01_2 source-envelope overlap exception is not accepted. Drawing approval does not close this critical interface, approve a model, prove physical fit/return/strength or authorize fabrication exports. Continue to hold CAD correction/model approval until the missing bearing evidence is resolved; any resulting new geometric decision returns through a named drawing revision.

Latest read-only Fusion observation at acceptance: one active `Jog Wheel F12-D03 Fusion01 DRAFT`, `isSaved=true`, `isModified=true`, lineage `urn:adsk.wipprod:dm.lineage:fNqin9L-QfCpF8zZ6-06UQ`, parent project/folder `Default Project`. Preserve its current unsaved changes; cloud/live geometry equivalence to reviewed WIP027 is unverified. The agent performed no CAD mutation, save/overwrite/close/discard or fabrication export while recording this approval. No broader save permission or whole-model approval is inferred.

## F12 bearing recommendation and lower-cost trial alternatives

The engineer explicitly requests that **SKF 61806-2RS1 remain the recommended target bearing**, while **lower-cost, potentially lower-quality alternatives may be used for trials**. Alternatives must have confirmed nominal dimensions **30 mm bore x42 mm outside diameter x7 mm width**; 6806/61806 alternatives, including the researched 2RS versions, are trial candidates. Quantity remains two bearings per jog/four per controller. No particular alternative supplier or part is selected as the target bearing by this decision.

Matching boundary dimensions do not transfer SKF's corner/abutment specifications, tolerances, internal clearance, seal drag or performance to another manufacturer's bearing. Check the actual trial bearing's corner/seat fit, rotation and assembled axial retention; the unresolved physical verification and model-approval gates remain open. This decision does not certify SKF or an alternative as physically verified.

This is a component-use policy, not a geometry change or whole-model approval. Preserve all nine frozen F12-D04 files and the reviewed D03 evidence unchanged; do not infer authority for Fusion mutation, cloud save or fabrication exports.

## Engineer authorizes F12-D04 model correction with SKF retained

The engineer explicitly keeps SKF61806-2RS1 in the design, reports that the latest jog changes have been saved to Fusion cloud, accepts the planned D04 P03 correction, and requests the corrected model, validation and subsequent approval/export workflow. The cheaper substitute is still awaiting delivery; inspect its real fit later. **Proceed with the approved D04 model correction without waiting for that physical substitute trial.** This supersedes the earlier CAD hold pending that trial; it does not certify actual SKF/substitute fit or accept the unresolved square-reference-corner overlap as collision-free.

Authorized geometry remains only the two approved P03 nut-entry extensions toY8.0 with top loading atY5.5; seated nuts, axes, PCB height, other parts and the16-mm fixed housing remain unchanged. Preserve all nine approved D04 files and D03 review evidence. Continue numbered local WIP F3D recovery copies; no model approval, fabrication export, agent cloud save, approved-file overwrite or document close/discard is authorized by this instruction.

Fresh read-only preflight: one active saved/unmodified `Jog Wheel F12-D03 Fusion01 DRAFT`, cloud lineage `urn:adsk.wipprod:dm.lineage:fNqin9L-QfCpF8zZ6-06UQ`, version2, parent project/folder `Default Project`. Its complete native release snapshot equals the reviewed WIP027 snapshot:582 timeline items,45 logical/46 represented body instances, all transforms/topology/volumes/bounds unchanged, zero feature-health issues. This establishes the source for the localized correction, not approval of the resulting model.

## F12-D04-Fusion01 correction and native review evidence

Observed execution, **not engineer model approval**: [corrected model/report](../models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_validation.md). Two editable P03 cut extensions remove16.464mm3 exclusively inside the approved boxes; other45 body-instance snapshots, every transform, P03 bounds, SKF and all other parts remain unchanged. Full native recompute passes588 timeline entries/zero issues;46 solid single-lump bodies,126 critical checks pass. Six actual1800x1200 model PNGs are opened/reviewed and inspection state restored.

Pair scope:16 poses/16560 outcomes,15840 retained unchanged pairs plus720 fresh P03 pairs/664 native BRep intersections/56 pruned. Nineteen insertion paths/1077 positions/2208 pairs, including444 complete PCB-nut positions with no P03 intersection. D03 independent native analysis/thread probes/native-joint exercise are retained historical evidence, not reruns. Known0.493242155mm3 square SKF reference-corner overlap remains unresolved and not accepted; actual substitute trial remains deferred until delivery. No collision-free/physical certification.

Current local recoveryD04_WIP002 in the previously agreed D03 checkpoint directory:8832655bytes/SHA256 `56dd4fa9d18a26b56c8079f3a5d3269bfd5eeeb072e33a8ad98c88a105764dea`,588 entries; size/hash/ZIP-CRC verified, no round-trip reopen. Source-named D03 cloudversion2 remains unchanged in cloud; its live document contains unsaved D04 changes, exact release restored/zero temporary graphics. All nine approved D04 files remain unchanged. No assistant cloud save, approved overwrite, close/discard or fabrication exports. **Next: explicit review/approval of F12-D04-Fusion01 within the reported limits and disposition of remaining release blockers.**

## Engineer approval of F12-D04-Fusion01 nominal prototype model

After the named F12-D04-Fusion01 review, the engineer explicitly states that the design looks good and approves it. **APPROVED: F12-D04-Fusion01 nominal prototype model**, matching the approved D04 drawing, localized P03 correction and reported prototype/reference limitations. This is model approval, not physical verification or production/process certification. SKF61806-2RS1 remains the design bearing; cheaper30x42x7-mm alternatives remain permitted for trials after delivery.

Fresh read-only inspection at acceptance: `Jog Wheel F12-D03 Fusion01 DRAFT`, cloud lineage `urn:adsk.wipprod:dm.lineage:fNqin9L-QfCpF8zZ6-06UQ`, now cloudversion3, saved/unmodified. The complete live native snapshot exactly equals the reviewed D04 snapshot:588 timeline entries/46 represented bodies, zero feature-health issues/temporary graphics. The assistant issued no cloud-save operation and does not attribute who saved version3.

Freeze the thirteen existing files under `models/jog-wheel/F12-D04/FUSION/` and the two D04 WIP002 recovery files below byte-for-byte. This later approval supersedes historical NOT APPROVED/pending flags without rewriting them. Do not rerun scripts that overwrite those records or views; future outputs require new, distinct paths. The nine approved D04 drawing files remain frozen independently.

| Frozen file | Bytes | SHA256 |
|---|---:|---|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01.py` |20500|`d5c5b9f4ff5fcf54ae948a7eee534170bb17c567548c776bad5076aad9db4c5f`|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_P03-nut-loading_fusion-view.png` |550945|`108244888d3b5dbbffca483475360f39ac7acbdceddabc264497edd5f2ab360b`|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_assembled-iso_fusion-view.png` |332627|`e09cab0ed3c142f43e75310aaebd425e9f6391ee3b232e65225fce05c17bdc4f`|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_correction.json` |56513|`153b5906c1ee0e92aad82f4b3334f224158741b582a8ec7ad7ee6fb3137ff131`|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_exploded-review_fusion-view.png` |384514|`82a08982c9c7045384b6301f5213d32cc251553babd4db26e765433168458744`|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_final-native-state.json` |1312|`03ab8734139d4a10ecb777492deaea4cbf26254455aa1c48cc3a7513335e5c48`|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_nut-loading-view.json` |514|`eda2ffc171dd5505de3c181ca4b46c4394d3e3c920f73837d2819220112f96e2`|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_preflight.json` |20915|`fabad03d46ff32fd86e0011019ce8261960ed58d2adbf7f3d21039b3d38c6059`|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_pressed-iso_fusion-view.png` |331350|`9f5473937bcfc32d59bbd288424e678a3b12eb85a1e0e6c2daabc3db63fd150b`|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_section-Y0_fusion-view.png` |331822|`8d02f4f661f117e8ddbd886a43d240cb37edd515815da343924d436658336548`|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_section-switch-Y14_65_fusion-view.png` |381146|`d09e549ab77cf0ce1e8f5a94c17f144875952da504e5068deb664db44c27b025`|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_validation.json` |571069|`247df58c14024f06ee273bd86d758547f25e73bf2ece6f6f00b50c052f1b4760`|
| `models/jog-wheel/F12-D04/FUSION/Jog_Wheel_Rev_F12_D04_Fusion01_validation.md` |10448|`94b576b59f1b96e27a602389d06cd62c80f162831160e6490b54f684929cebcf`|
| `models/jog-wheel/F12-D03/FUSION/checkpoints/Jog_Wheel_Rev_F12_D04_Fusion01_WIP_002.f3d` |8832655|`56dd4fa9d18a26b56c8079f3a5d3269bfd5eeeb072e33a8ad98c88a105764dea`|
| `models/jog-wheel/F12-D03/FUSION/checkpoints/Jog_Wheel_Rev_F12_D04_Fusion01_WIP_002.json` |747|`2a682a7be5bbbfb052165486d7c00e636c4a7933c66173b9e6f6db2d381c0f6b`|

Verification at acceptance: thirty input hashes, two recorded source-code hashes, six native PNG signatures/dimensions/hashes and local WIP002 size/SHA256/ZIP-CRC pass. The archive has not been round-trip reopened. The later cloudversion3 observation supersedes historical saved-state metadata without changing the frozen records.

**Export disposition still required:** model approval does not silently accept the previously escalated0.493242155mm3 P01/C01_2 square SKF reference-envelope overlap, certify its missing corner geometry or waive physical fit tests. Obtain an explicit scoped prototype-reference exception or wait for verification before issuing STL/STEP/final F3D. No fabrication export has occurred at this approval-recording stage. No geometry change, assistant cloud save, approved overwrite or close/discard is authorized by the approval.

## Engineer accepts the scoped SKF reference exception for prototype exports

Asked explicitly whether to release prototype exports despite the disclosed0.493mm3 simplified SKF envelope overlap, without treating real fit as verified, the engineer selects **“Wyeksportuj do prób”**. **ACCEPTED FOR NOMINAL PROTOTYPE EXPORTS ONLY:** retain the unchanged P01/C01_2 source-envelope overlap as a documented reference-model exception. Actual SKF/substitute corner geometry, fit, preload/endplay, rotation, return and physical performance remain unverified; the substitute trial follows delivery. This is not physical collision-free certification or approval of invented bearing geometry.

The named F12-D04-Fusion01 model approval remains valid. Release the revision-matched separate printed-part STL files, complete-assembly STEP and editable F3D archive in the agreed `models/` output tree, without changing geometry, overwriting frozen artifacts or cloud-saving the active document. Verify actual files, units/scale, STL mesh validity and assembly/archive completeness; report unsupported or failed outputs rather than marking handoff complete. All other drawing/model/process/workspace gates remain unchanged.

## D04 export validation finds a blocking P06 tangency

Actual delivery checks find **P06 STL NOT VALID**: four edges have incidence4, atX/Y(+/-14.14213562,+/-14.14213562),Z4..4.5. The [mesh diagnostic](../models/jog-wheel/F12-D04/Jog_Wheel_Rev_F12_D04_Fusion01_P06_mesh_diagnostic.json) and [complete ten-file check](../models/jog-wheel/F12-D04/Jog_Wheel_Rev_F12_D04_Fusion01_STL_validation_complete.json) are retained. Other nine meshes pass the stated topology/scale checks; no repair or tolerance welding occurred. Do not release the complete D04 package as valid or generalize the SKF exception to this separate issue.

Root cause follows the approved P06 definition: boreR20, relief radial20..23/tangent+/-1.5/Z4..4.5. At each of four relief axes the rectangular cut is exactly tangent to the bore, leaving zero-thickness contact and side lips up to `20-sqrt(20^2-1.5^2)=0.0563293248`mm. This matches the four nonmanifold mesh edges, not merely a failed dimensional fit. Opening the complete3-mm width requires the cut start below `sqrt(20^2-1.5^2)=19.9436706752`mm.

Native editable F3D actually reopens/full-recomputes:588 healthy entries/46 bodies, exact source topology/bounds/volumes/transforms, parameters/relationships preserved, zero external references. STEP is exported and declares44 unique closed BReps/46 product identities/47 assembly uses, but its actual native reimport remains in progress at this observation; a native stack sample confirms STEP component creation. No duplicate import, source geometry change, cloud save or close/discard occurred.

## Engineer authorizes F12-D05 P06 relief correction

Presented with the actual P06 failure and the proposed localized change, the engineer explicitly selects **“Przygotuj F12-D05”**. Authorized new drawing geometry: **only the four P06 relief inner radial starts change20.0->19.9mm from the axis**. Keep boreD40, radial outer end23, tangentwidth3, axial cutZ4..4.5/depth0.5, spring positions and every other part/interface unchanged. The selected19.9 is below the derived full-width opening threshold19.9436706752; it is not a revised bearing bore or an invented manufacturing tolerance.

Prepare a complete revision-matched F12-D05 dimensioned PDF and separate illustrative concept PNG for review, retaining all D04 part/assembly coverage and adding a clear P06 detail. **D05 DRAWING NOT APPROVED; no D05 Fusion geometry before its explicit named approval, then separate model approval before exports.** This is dimensional selection authority only, not preapproval of an unseen drawing/model. Freeze/preserve approved D03/D04 drawing packages, D04 model-review/recovery files and F11/B19/concurrentB22. D04 model approval remains recorded, but its export release is blocked by the newly discovered P06 defect. No mesh-only repair or source overwrite is authorized.

## F12-D05 drawing proposal published; D04 STEP verification settled

Basia publishes the [complete16-sheet F12-D05 proposal, concept and executed analytic/publication evidence](../schematics/jog-wheel/F12-D05/Jog_Wheel_Rev_F12_D05_review.md). Only the authorized four P06 relief starts change20.0->19.9; all83 inherited parameters/hardware/BOM/interfaces remain. Actual PDF reopen/16A3 pages/18 selected annotations, all-sheet/critical-page visual review, real1536x1024 PNG conversion/raster validation,33 source hashes and stated analytic checks pass. **D05 DRAWING NOT APPROVED; no changed Fusion geometry before explicit named approval, separate model approval before exports.** Publication/check success is not engineer approval.

The actual D04 STEP reimport has now settled; no repeat import occurred. All46 bodies reopen closed with matched identities, but **P04 minimumZ changes by0.110086335654mm and volume by+22.0469353415mm3/+12.6794313651%**. No acceptance of this representation is recorded; the historical H05/SKF exceptions do not cover it. [Finalized export evidence](../models/jog-wheel/F12-D04/Jog_Wheel_Rev_F12_D04_Fusion01_export_review.md) records this second release blocker alongside P06's invalid mesh. Editable F3D round-trip passed exactly; D04 approvals remain recorded, but complete fabrication handoff is not approved/complete.

Latest read-only source observation: original D03-named lineage active, cloudversion4/saved/unmodified; entire reviewed D04 snapshot still equal,588 entries/46 bodies/zero health issues/zero temporary graphics. Separate unsaved F3D/STEP verification copies remain open. No assistant cloud save, actor attribution, close/discard, D05 CAD or frozen-package overwrite.

## Engineer approval of F12-D05 nominal printed-prototype drawing

After Basia explicitly requests approval of the named F12-D05 drawing, especially sheet16, the engineer replies **“Wygląda dobrze. Akceptuję.”** **DRAWING F12-D05 APPROVED** for its stated nominal printed-prototype scope: only four P06 spring-relief inner radial starts20.0->19.9mm; boreD40, radial end23, width3, Z4..4.5/depth0.5, roof1.0, spring positions, all83 inherited parameters, other parts/interfaces and BOM remain unchanged. The complete16-sheet PDF and its cited dimensional definition govern; the separate LLM concept is illustrative, not a Fusion model or dimension source.

Freeze these nine files under `schematics/jog-wheel/F12-D05/` byte-for-byte; historical pending flags inside the approved proposal remain unchanged and are superseded by this register:

| File | Bytes | SHA256 |
|---|---:|---|
| `Jog_Wheel_Rev_F12_D05_DRAFT.pdf` |122515|`a79451c414513671d489871711c969473be4e8ac8df0099339ff71c7c7e77938`|
| `Jog_Wheel_Rev_F12_D05_check.py` |35361|`80189e7cbe7be0ad223cbcd254f7023bcc2ae827489ad2440f6e8263fe846651`|
| `Jog_Wheel_Rev_F12_D05_checks.json` |300770|`6accf6b845a810f233535fd51d9fb6776a24dd30cf00dd473688946d1ad47ba3`|
| `Jog_Wheel_Rev_F12_D05_concept.png` |1444842|`10c468408c84019aefdaf662672cebf00af7d312a3d0d6be88ccc444083e037d`|
| `Jog_Wheel_Rev_F12_D05_define.py` |51688|`1691a95498c7e1273d2552df23915010e91bc492597c60ae255254653b80b928`|
| `Jog_Wheel_Rev_F12_D05_definition.json` |277103|`0798e7ca6d62e07e768f4e262c47525c98effcb4b56a275a5da85e81228f9e7d`|
| `Jog_Wheel_Rev_F12_D05_drawing.swift` |21285|`4a8ae2e68ca2ed0deb695eaa5d3659b0c34657f16940021c9ce628f5fa4ad748`|
| `Jog_Wheel_Rev_F12_D05_hardware_sources.json` |37552|`edd1ccf25fb55f6ed7171cf782bb5b7a707ca6a20c8eb660a5e9ec0894b134d9`|
| `Jog_Wheel_Rev_F12_D05_review.md` |9201|`afcd26924aead6718fe9a4155efee297631c93cf77f0503b106c3873b52a9c69`|

This clears only the drawing-to-CAD gate for the specified P06 correction on the identified, fingerprint-verified source. Preserve approved D03/D04/F11/B19 and concurrentB22; use the existing numbered local WIP recovery authorization. **F12-D05-Fusion01 MODEL NOT APPROVED; no D05 fabrication STL/STEP/final-F3D exports before separate explicit model approval.** Local WIP recovery archives remain authorized, not release exports. No cloud save, approved-file overwrite, document close/discard, physical-fit/process/strength/return/switch certification or acceptance of the D04 STEP P04 representation discrepancy follows from this drawing approval.

## F12-D05 native correction checkpointed; mesh calculation blocks model review

Under the approved D05 drawing, Basia implements only four P06 cut extensions19.9..23/width3/Z4..4.5. [Native correction/report](../models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_validation.md) records0.112595113089mm3 removal, zero addition/outside-authorized removal,45 unchanged other body snapshots/all transforms/P06 bounds,600 healthy entries/46 solid bodies after correction. Pre/post WIP001/WIP002 are actual locally SHA/CRC-verified archives; postchangeWIP0024246610bytes/SHA256 `f5b546c7c5f677d83941336051e033399f3d43c128ab85ff86dee3a66afe35a2`, not round-trip reopened. Nine approved D05 drawing files remain unchanged.

Native validation persists126 passing critical checks/16 poses/16560 pair outcomes (15840 retained;720 freshP06/372 intersections/348 pruned), but postchange TriangleMeshCalculator.calculate does not return during3500seconds of event-driven waiting. Two native stack samples confirm active ASM faceting, later100%CPU. **CHANGES REQUIRED / MODEL NOT APPROVED; no final mesh/restore/views or completed model approval request.** No duplicate native operation, quality reduction, forced process termination, cloud save, document close/discard or fabrication export occurred. The operator must safely release/restart the host before recovery and remaining work; this execution record grants no new destructive authority, physical acceptance or STEP representation waiver.

## F12-D05 recovered after engineer-reported Fusion crash

The engineer states Fusion crashed and live D05 is absent. Basia confirms zero open documents, verifies the actual WIP002 archive and opens it in a separate new unsaved document. [Actual recovery/checks/views evidence](../models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_recovered_validation.md):600 entries/46 solid bodies, exact recorded D05 topology/bounds/volumes/transforms; full recompute/126 native checks pass. No drawing/model geometry is changed or rebuilt.17 insertion paths rerun plus two unchanged D04 nut paths retained,total19/1077 positions/2208 pairs;16 recorded D05 poses retained by exact geometry identity, not rerun. Six actual Fusion PNGs inspected, geometry/camera/visibility restored,zero temporary graphics.

The previous calculate() is not repeated. P06 has30 native faces/76 two-face edges/no zero-sized elements; an existing978-triangle cached display mesh passes stated topology checks, **not final STL certification**. SDK cached nodeCount metadata inconsistency is disclosed; it is not asserted to cause the prior crash. Tessellation and D04 STEP P04 fidelity risks remain unresolved and unaccepted.

New WIP003/WIP004 are independently local size/SHA/CRC verified; latestWIP0046880905bytes/SHA256 `ede0d79528cd725368eb49e5a7453da380da13362d9dde0d4ee1e9f3eb34a06a`, not itself round-trip reopened. WIP002 now has actual successful reopen evidence; original files/manifests remain unchanged. Active `Jog Wheel F12-D05 Fusion01 RECOVERED WIP002 — NOT APPROVED` isSaved=false/isModified=true/no dataFile; no cloud save/overwrite/close/discard/fabrication export. **D05 drawing approval remains valid; F12-D05-Fusion01 MODEL NOT APPROVED.** Recovery and nominal geometry checks enable engineer review, not automatic approval, physical qualification or representation acceptance.

## Engineer approval of F12-D05-Fusion01 nominal prototype model and STL request

After Basia explicitly asks whether the engineer approves the named F12-D05-Fusion01 model for nominal prototype trials, without accepting exports or physical performance as verified, the engineer replies **“Ok, zatwierdzam F12-D05. Przygotuj STLe do druku.”** **F12-D05-Fusion01 MODEL APPROVED** for that stated nominal-prototype scope. Prepare revision-matched separate STL/mm files for ten distinct printed definitions, with twelve printed pieces per jog and their BOM quantities. Drawing approval remains separate and unchanged.

Fresh read-only approval-source inspection: `Jog Wheel F12-D05 Fusion01 RECOVERED WIP002 — NOT APPROVED`, cloud lineage `urn:adsk.wipprod:dm.lineage:rCsKqvaXTxqppcLYV-mtXA`, now **version2/saved/unmodified**. Its entire recorded D05 native snapshot still matches:600 timeline entries/46 represented solids, no feature-health issues or temporary graphics. The prior version1 observation is historical; no geometry/pose change or assistant cloud-save call occurred. The recovered document's name and old pending labels are not silently rewritten.

Freeze these sixteen native model/review files and two WIP004 recovery files byte-for-byte. Historical pending/unsaved/export-risk flags remain evidence of their capture time and are superseded only as to model approval/source state by this register:

| File | Bytes | SHA256 |
|---|---:|---|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01.py` |19866|`177be80927762f2951e285928c256b8bb914994ec8ad0963ffa9f34c6611c914`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_P06-topology-recovered.json` |14864|`b9bcb4921256b7b5659ba938da1706d5c24fe2dc7bd52c5e6f8895d487b1d47b`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_correction.json` |56378|`7581a1739e136ec79d6b82435b7fc086f922e5e2671a546cab4dc02ef866ec91`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_preflight.json` |65509|`0fb38488cb88031789d26b530490e1a6219dbb7f83a1ba84f94a38c092682232`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_recover.py` |16927|`4717a8114931915648124085626e5ae4f183d3725d2dd49644040792261e7204`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_recovered_P06-underside-reliefs_fusion-view.png` |477339|`792e04ad4e4d67ee60c6aaca9110bec07dedf8f836df8db614f4d9390aeac463`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_recovered_assembled-iso_fusion-view.png` |332627|`e09cab0ed3c142f43e75310aaebd425e9f6391ee3b232e65225fce05c17bdc4f`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_recovered_exploded-review_fusion-view.png` |384518|`04beead5e68ff15685bc66976ce070afa24ec04289776253d405faa920a8d920`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_recovered_pressed-iso_fusion-view.png` |331356|`4b5ad88b8851d016bdc4c4126389bf74b2a320b858011764d995b0d8405fb88e`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_recovered_section-Y0_fusion-view.png` |331834|`e1ba5e6a72197f7df2ff473df26c6bd81c560fe14ceba304dd3e562cf2189c7c`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_recovered_section-switch-Y14_65_fusion-view.png` |380958|`18254648e392c7531a26c191c7ff212b92e8e46d423d16132362aca684774d18`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_recovered_validation.json` |559020|`4e3bf32112ea9e6937e2e2f08bf5f7607f37290376834b6c408e502dfa6220fd`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_recovered_validation.md` |11250|`5929650ef01fab918e1ab7cd2b5162c08eeee2f66b6fb4c5ce4dd66744d46d1e`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_recovery.json` |56993|`e65d208d947f0efef1d63194df63aa8906049ecd4947c3a8d0954cd990ae21ff`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_validation.json` |271168|`d6b4e977bc0bf02108ad7d5bc697b426baf6f65d428e18f25074d3ccec25f558`|
| `models/jog-wheel/F12-D05/FUSION/Jog_Wheel_Rev_F12_D05_Fusion01_validation.md` |9023|`adab6e21c514684d2d18988b6be06e6bf614eecd3045bc6efc02a1a7b264edb9`|
| `models/jog-wheel/F12-D03/FUSION/checkpoints/Jog_Wheel_Rev_F12_D05_Fusion01_WIP_004.f3d` |6880905|`ede0d79528cd725368eb49e5a7453da380da13362d9dde0d4ee1e9f3eb34a06a`|
| `models/jog-wheel/F12-D03/FUSION/checkpoints/Jog_Wheel_Rev_F12_D05_Fusion01_WIP_004.json` |861|`6920cf256957f12acf32b6e28328a0e4075dfc3eb3fb252a9d7e2c665db776d9`|

The approval covers the disclosed nominal model, not a claim of actual SKF/substitute corner/fit verification, spring return, microswitch calibration, strength, print settings or complete-controller clearance. Preserve the unchanged bearing-reference limitation; it does not authorize invented bearing geometry or silent interference exceptions. Cached display-mesh PASS is not final STL PASS. The earlier invalid D04 P06 STL and STEP P04 representation discrepancy remain unaccepted; all new/reused delivery files must have actual revision/scale/topology evidence. The known blocked TriangleMeshCalculator.calculate call must not be blindly repeated; a native STL exporter may be exercised against isolated P06 with a prior local recovery checkpoint. No mesh repair, quality reduction concealing failure or dimension change is approved.

Current request is the STL set, not a completed all-format handoff. Complete assembly STEP and final editable F3D remain required for final project delivery and must be verified separately; do not silently substitute WIP recovery or claim them delivered here. No cloud save, approved-file overwrite or document close/discard is authorized. Existing numbered local recovery saves remain authorized.

## F12-D05 requested STL set completed and verified

Basia delivers [ten revision-matched separate STL/mm files and printed BOM](../models/jog-wheel/F12-D05/Jog_Wheel_Rev_F12_D05_Fusion01_STL_handoff.md),12 printed pieces/jog/24/controller,749047440bytes/14980932triangles. P06 is freshly exported by native ExportManager after a local checkpoint; the blocked TriangleMeshCalculator.calculate is not repeated. Nine other files are exact independent copies after verified45 unchanged native body snapshots/local bounds/volume/source fingerprints. The failed D04 P06 is not copied. **All ten final D05 files are freshly parsed and pass the declared finite/closed-edge/winding/connectivity/positive-volume/scale checks**; maximum native bound discrepancy0.000499725342mm at representation/numerical thresholds, not manufacturing tolerances.

P06 final STL has17712triangles/zero boundary or nonmanifold edges; installed BambuStudio --info actually imports it with exit0/manifold=yes/one part/48.499908x45.999844x1.5mm. No slicing/G-code, physical tests, repair, decimation, quality reduction or geometry change. Source remains cloudversion2/saved/unmodified/exact600-entry/46-body D05 with zero temporary graphics, eighteen frozen model/recovery files unchanged; no assistant cloud save/close/discard. New local WIP0056567418bytes/SHA256 `4e9081b5860f3b152deb869e4b9090ab6f5ce4a68196ccced1d0a35f905f00f0` has actual size/hash/ZIP-CRC PASS, no round-trip reopen/final-F3D claim.

Delivery evidence fingerprints:

| File under `models/jog-wheel/F12-D05/` | Bytes | SHA256 |
|---|---:|---|
| `Jog_Wheel_Rev_F12_D05_Fusion01_STL_exports.json` |19638|`10cb059f74611d16f7ed38afded76bd2b2db2db06bf1edb521b396b53345311d`|
| `Jog_Wheel_Rev_F12_D05_Fusion01_STL_validation.json` |34832|`a1c983ddf52e8fc345f3fc1100a72ceb21aa3bc0fb5eb4dc60725be336b9246b`|
| `Jog_Wheel_Rev_F12_D05_Fusion01_STL_handoff.md` |9710|`0ae916dbe4dfefb5ff8e9d5464274a336c1a510be17eeb4b0d150e87f0043554`|
| `Jog_Wheel_Rev_F12_D05_Fusion01_P06_Bambu_info.json` |762|`0f448b5e9c0b8413170342c7dd13bb5c6c75cc8403e089b839c70a4c402dfabe`|

**Requested STL task complete; full project handoff not complete.** Native component coordinates are not approved print orientations/process settings. Actual bearing/guide/thread fit, spring return, switch calibration, thin-stock/mounting strength and whole-controller integration remain unqualified. Complete-assembly STEP and final editable F3D are not supplied by this STL-only request; faithful/explicitly accepted STEP representation remains required. Model approval and mesh checks do not certify manufacturing readiness.

## Engineer approval of B22-LAYOUT-01 nominal mechanical-prototype drawing

After reviewing the B22 PDF/concept and requesting Fusion modeling, the engineer explicitly selects **“Zatwierdzam B22 — prototyp mechaniczny”**. **APPROVED: B22-LAYOUT-01 drawing in its stated nominal mechanical-prototype scope**, including the two-piece printed display housing,49deg tilt/80.376766 rear height, flat20 main body, removed inlet, rear-packed electronics, proposed printed roof/module/support interfaces and explicit reference/physical limits. PDF SHA256 `4f149bbafdadd366d3f30ba15ce00e8bc77c6fead07ac61c65c5fe297aae97aa`.

Retain all seven files in `schematics/enclosure/B22/` byte-for-byte, including historical NOT APPROVED/model-ready labels. This later scoped approval supersedes those labels without rewriting the package. Actual DAC outline registration/laminate/retention is not invented: model the defined four plain pads for later physical matched drilling/qualification. Incomplete LCD reference geometry and old F06 jog mount with engineer-assumed16mm mechanism height remain explicit limits. No complete bought-body, connected-fit, motion, strength, electrical/thermal or final print-process approval follows.

The engineer also explicitly selects **“Nie — Fusion jest dostępny”**: Basia may create a separate unsaved B22 document; the existing unsaved jog document must remain open and untouched. Preserve approved B19 archive and all unrelated work. Implement editable native model **B22-Fusion-01** and perform geometry/feature-health/represented-body/dimension/print-envelope checks and actual Fusion review PNGs.

This is not model approval or permission to save to the cloud, close/discard modified documents, overwrite approved artifacts, or export STL/STEP/F3D. Obtain separate named model approval before fabrication/archive exports. Final print margins/orientation/supports/calibration and physical interface qualification remain independent.

## B22-Fusion-01 native model review published; fader fit disposition required

The approved B22-LAYOUT-01 nominal mechanical-prototype drawing is implemented in the separate **`DJC Enclosure B22-Fusion-01 DRAFT`** native document. [Executed model review/actual views](../models/enclosure/B22/FUSION/DJC_Enclosure_Rev_B22_Fusion01_validation.md), [machine evidence](../models/enclosure/B22/FUSION/DJC_Enclosure_Rev_B22_Fusion01_validation.json), [87 frozen sources](../models/enclosure/B22/FUSION/DJC_Enclosure_Rev_B22_Fusion01_sources.json). This publication is **NOT engineer model approval**.

1063 entries pass full replay/compute/feature health;407 represented BReps/375 solids/32 datum sheets/131 printed pieces/zero meshes. All70125 solid pairs screened and750 candidates explicitly intersected: zero printed/printed positives, independently confirmed by native Fusion126-body interference analysis.191 full nominal outer heads clear;2220 seating probes pass, with six unmodeled actual jog ears excluded.58 sampled cap poses pass, minimum1.062910mm; not continuous mechanism validation. Four actual1800×1100 Fusion PNGs were opened/reviewed and assembled visibility/camera/poses restored. Fourteen principal printed components and all remaining printed-body boxes nominally fit250-cubed before slicer margins/supports.

**CHANGES REQUIRED / MODEL NOT APPROVED:** five inherited fader end screw towers overlap the source60×9×6 case envelopes (F01–04 axial0.95mm/28.978614mm³ each, F05 1.10mm/35.671856mm³). Actual end relief is not dimensioned; this is neither proven physical collision nor an accepted fit exception. Engineer supplies trustworthy actual end-profile evidence or authorizes a new drawing/mount correction. No silent reference trimming, mount/axis changes or export.191 intentional nominal pilot/thread engagements and3 conservative Pi/DAC support-envelope overlaps are individually explained, not suppressed.

Final read-only identity observes B22 cloudlineage `urn:adsk.wipprod:dm.lineage:7Lqp25VsSb-kx1vXjdNSmw`, version1, `isSaved=true/isModified=true`; **no assistant save was issued**, actor/time and final-live/cloud correspondence unestablished. Geometry/pose fingerprint `6650408df3fbaeba0be2bc3fcda84c143e3e0ad8af29854acb8aee113277bcf4`. No local B22 STL/STEP/F3D exists; preserve the modified live source. Separate saved/unmodified600-entry/46-body F12-D05 jog retains fingerprint `95d61725b9d42c0dd92664c6b86c66ac488f74d84bf28289fdcb5d90c7c3cc23`; no geometry/save/close/discard. Frozen B22 drawing/B19/B20/B21 and listed source hashes remain unchanged.

Actual DAC matched-drilled retention, complete LCD/contact/service, controller retention/zero nominal header clearance, new-jog integration, real thread/head-bearing/strength, full movement/assembly paths, final printing and physical/electrical/thermal qualification remain open. Nominal drawing approval is retained; separate named model approval and required verified exports remain subsequent gates.

## Five successor enclosure corrections requested after B22 model review

The engineer requests: (1) shift B01–B10 left by one key-cap width; (2) place P01–P03 right of B06–B10 halfway between B08 and the right panel edge; (3) move AUX rear→front; (4) cut the supplied `elements/gniazdo_zasilania_nowe.png` inlet in C01, explicitly accepting unverified inward overlap with electronics; and (5) recess the panel-to-shell screw heads so their tops are flush with the panel. This is change/dimensional direction, **not named approval of B22 or an unseen successor drawing/model**, and does not authorize cloud save, overwrite or STL/STEP/F3D.

Read-only native reinspection retains exact B22 fingerprint/1063 entries, cloudversion1/saved/modified and separate jog saved/unmodified. Native cap/source agree on nominal14mm, so proposed buttonX shifts−14; newB08X511 gives proposed pot columnX555.5 to outer edge600, existingY21/49/77 retained. Supplied inlet matches the identified B14 source47.5×28 nominal trial/50×30.5 face, not a new inferred purchased part. Candidate C01 raised rear position and all derivations/limits are in [requested successor scope](../DESIGN.md#requested-b23-control-connector-and-flush-screw-corrections).

**Await engineer choices:** AUX identity (separate J01 headphone jack or RCA panel; historic U01 is absent), and flush-head hardware route. Existing cylindrical headH3 cannot retain an unthickened panel2 with a simple3-deep counterbore; propose a source-qualified90deg countersunk M3 replacement or properly supported local underside thickening. No holes/mounts/poses are changed before the new drawing gate. Inlet/electronics overlap permission is not permission to cut structural posts or accept mains protection, actual fit, electrical/thermal safety or energized operation. Fader findings and separate model approval remain open; preserve all B22 source/review files.


## Engineer selects F12-TH01 printed trial hardware parameters

The engineer requests STL preparation using mrvarity bearings and LyraMaker screws/nuts/washers. After an actual LyraMaker M2 flat/hex assertion failure, the engineer explicitly chooses **“Osobny model nominalny”**: a separate nominal M2x4 countersunk model using the accepted envelope overall4/headD4/K1.2/90deg/pitch0.4/hexAF1.27, not another drive or scaled screw. The engineer also chooses **“Przyjac ustawienia autorow”**: nut `$slop=0.1`, nominal30x42x7 bearing with automatic double-cone rollers, clearance0.4/chamfer0.5. This authorizes these trial geometry choices, not calibrated fit, physical strength or an all-plastic functional jog.

[F12-TH01 named model review](../models/jog-wheel/F12-TH01/Jog_Hardware_Rev_TH01_review.md), [exact source/mesh check evidence](../models/jog-wheel/F12-TH01/Jog_Hardware_Rev_TH01_preview.json) and [actual generator-mesh view](../models/jog-wheel/F12-TH01/Jog_Hardware_Rev_TH01_generator-view.png) are published for separate model approval. Eight in-memory meshes represent22 instances per jog/44 per controller,2130872bytes/42604triangles. Seven single-part topology checks pass; the bearing's26 individually checked closed outward shells are2 races/24 rollers, with the unchanged single-body count failure expressly retained. Bearing measured Y-box41.986946 versus nominal42 is a disclosed facet approximation, not manufacturing tolerance.

**F12-TH01 MODEL APPROVAL REQUESTED; NO STL FILES WRITTEN.** No native Fusion mutation/save/close or change to approved F12-D05 files. Active modified B22 remains preserved. Further STL writes require explicit acceptance of this named model and trial-only limitations; actual slicer/file checks follow export. The separate manual springS01 proposal is recorded in the procurement document, not a generated/approved spring or proof of steel-equivalent behaviour. No credentials or dependencies were requested or installed.

## Engineer approval of F12-TH01 printed trial hardware model and STL destination

After the actual eight-mesh view, source/quantity checks and explicitly scoped topology/facet limitations, the engineer selects **“Zatwierdzam F12-TH01”**. **F12-TH01 MODEL APPROVED** for nominal printed-hardware trials only, with the already selected counter-screw exception and generator fit settings. The engineer approves writing eight separate STL/mm files in `models/jog-wheel/F12-TH01/`;22 instances per jog/44 per two-jog controller, no springs.

Freeze these three reviewed sources byte-for-byte; their historical pending/no-STL labels remain capture-time evidence, superseded as to approval by this entry:

| Source | Bytes | SHA256 |
|---|---:|---|
| `models/jog-wheel/F12-TH01/Jog_Hardware_Rev_TH01_preview.json` | 51985 | `fd4aac3ff0c37cd34d11adfba429d509cd18bbc519ba3a8a23ce0017e14e5d98` |
| `models/jog-wheel/F12-TH01/Jog_Hardware_Rev_TH01_review.md` | 5000 | `98c6e904ccfda2b8f91b73b33191527482e47527fef7da1d25f1233637b95261` |
| `models/jog-wheel/F12-TH01/Jog_Hardware_Rev_TH01_generator-view.png` | 232782 | `faa7e00bc2afa44b19216616d3229fe2afc8e3914c5e664902ccc8836f56b7ee` |

Export only the exact reviewed mesh bytes recorded in that manifest; do not regenerate/scale/repair them or rewrite the frozen sources. Verify all actual output files and slicer import. This approval does not certify physical thread/head-seat/bearing fit, clamp strength, rolling resistance, spring return, fatigue or the whole controller, and does not authorize cloud save or changes to Fusion/F12-D05. The modified B22 native document remains unrelated and preserved.

## F12-TH01 requested STL set completed and verified

Following the explicit model/destination approval, all eight reviewed buffers are written as separate binary STL/mm files in `models/jog-wheel/F12-TH01/`. Actual local files match the approved mesh hashes exactly;22 instances/jog/44 per two jogs,2130872bytes/42604triangles. Seven fresh one-part mesh checks pass; bearing26 closed surfaces remain intentionally separate and individually validated. All eight actual files import into installed BambuStudio with exit0/manifold=yes, correct facet counts and1/26 expected part counts. No slicing, G-code, printer job, regeneration, repair, scaling, dependency install, native Fusion mutation, cloud save or change to the three frozen review sources.

| Delivery evidence | Bytes | SHA256 |
|---|---:|---|
| [STL handoff, eight file links and quantities](../models/jog-wheel/F12-TH01/Jog_Hardware_Rev_TH01_STL_handoff.md) | 7826 | `6153330c4387f42ae9fcc61958d2cf8ed4075c357e5031f064358b16934a41b6` |
| [Actual STL export/hash/mesh manifest](../models/jog-wheel/F12-TH01/Jog_Hardware_Rev_TH01_STL_exports.json) | 25794 | `3b0cb0fa72a0825ddeece04ee572c70189f766af59ce8aa8279ee887266935b4` |
| [All-eight BambuStudio import record](../models/jog-wheel/F12-TH01/Jog_Hardware_Rev_TH01_Bambu_info.json) | 9286 | `5517bbce1e1f5e3b73d8e03b9e1bcd5e3164d22554893d4871500061215ad28c` |

**APPROVED nominal trial geometry / requested STL-only delivery COMPLETE / NOT PHYSICALLY VERIFIED.** SpringS01 is a manual parameter proposal only; no spring STL or calibrated force. Fit, thread/head-seat strength, rolling resistance, return, material/nozzle/layers/orientation and whole-controller qualification remain separate. Existing approved F12-D05 files and unrelated modified B22 are preserved; no complete project STEP/F3D handoff is claimed. Owned browser session is closed; no task-created repository temporary files remain.
## B23 choices resolved and five-correction drawing published for approval

The engineer explicitly selects: **P01–P03 midpoint from the RIGHT EDGE of the B08 cap**, **AUX means J01 single3.5mm jack**, and **M3 countersunk90deg exterior screws**, including two visible display-roof lap screws. These close the three choices, not named approval of the unseen drawing/model. NewB08axis511/rightedge518 gives Paxis559; retainY21/49/77. RCA stays rear, U01 absent; J01 moves to frontC04(X101,Z10), old rear hole closes. B01–B10 complete chains shift−14.

Published **B23-LAYOUT-01** [four-sheet PDF](../schematics/enclosure/B23/DJC_Enclosure_Rev_B23_drawing.pdf), SHA256 `11adb99d9f549b2e48c343aec146869613037759715b6195c71d19f6b9a420a3`, [illustrative concept PNG](../schematics/enclosure/B23/DJC_Enclosure_Rev_B23_concept.png), SHA256 `c3beae2e44dc2288738c75211d8f0472a1554737332eff37faa55fb4237458b7`, [source/calculations/limits](../DESIGN.md#requested-b23-control-connector-and-flush-screw-corrections). The supplied47.5×28 nominal trial inlet is centred on raised rearC01 at(X180.775,Z48.188383), between actual-height module-inner155.55/post-core206 edges; full50-wide proxy gap0.225 and roof-support gap0.299248, not physical fit. The prior low-foot-basedX179.525 proposal is superseded. Electronics-overlap permission remains an unverified exception, not structural cutting or mains safety.

Proposed exact replacement is **Bossard BN616/1076469 M3×8 A2**,35 exterior fasteners (33 closure+2 lap), headD6/H1.7/HEX2, pitch0.5/length INCLUDING head; manufacturer family and exact supplier dimensions are cited. No generic ISO10642 substitution. D3.4/entryD6/90deg seat gives depth1.3, remaining panel stock0.7; minimum outside flat ligament after existingR0.8 is0.2, lap side2, screwtips unchanged. **These thin/tight nominal limits require explicit prototype-scope drawing review, not assumed head-bearing/strength/calibrated-fit approval.** Internal hardware and source pilot axes unchanged.

Executed analytical checks:2496 changed-control/858 post-footprint/98 jack/98 inlet-control/16 inlet-support/2485 seat-aperture comparisons pass within documented conservative coverage;102 source hashes unchanged. Native four-page PDF generation/reopen/render/13 annotation checks and final all-sheet review pass; realPNG conversion/signature/dimensions/opened content verified. First LLM rear inset misrepresented RCA/inlet and was removed, not presented as a model. Task preview directory removed.

**B23-LAYOUT-01 DRAWING NOT APPROVED; no B23 Fusion geometry/native views/STL/STEP/F3D or cloud save.** Next engineer approves or corrects this named nominal mechanical-prototype amendment, including selected source/limits, then Basia may model and validate before separate model approval. Preserve B22 packages/live source and separate jog work; five fader findings, actual DAC/LCD/jog/process/physical/electrical/thermal gates remain open.

## B18 mounting trial reported good; B24 left encoder-group drawing published

While reviewing B23, the engineer states it looks good but requests another geometry change: move **E01 and T01/T02 left of B01–B05 near the left controller edge**. This is not named B23 drawing/model approval. Retain orderT01–E01–T02 and relative23mm spacing/local source interfaces. Proposed B24 axes areT01(19.45,46.25),E01(42.45,46.25),T02(65.45,46.25), derived from the available interval between innerwallX2 and shiftedB01 mount edge82.9 and existing lower-rowY46.25. B23's seven files remain byte-identical historical draft.

The engineer also reports an actual **B18 enclosure trial print with excellent button/fader/pot mounting seats and good part fit**. Record as ground truth for tested hardware; do not rerun/re-request the same physical fit. Tested segment IDs/count, material/process/orientation, measured gaps/strength, encoder/full enclosure/new-position fit were not supplied and are not inferred. Source comparison retains all98 local mating-cut/addition groups, with only338 floor-bottom primitives rebuilt toZ2/poses changed. Keep working cavities/pilots/retainers unchanged. This informs a conservative-reference disposition of the old nominal fader-case/end-tower positives, not a mandatory redesign or blanket complete B24 physical approval.

Published **B24-LAYOUT-01** [five-sheet PDF](../schematics/enclosure/B24/DJC_Enclosure_Rev_B24_drawing.pdf), SHA256 `225eb0a9a1ce07e694c17b709d23593f8cad98d47156d240dc294621fe7e2893`, [illustrative concept PNG](../schematics/enclosure/B24/DJC_Enclosure_Rev_B24_concept.png), SHA256 `71310ded247c68a179a71bbe8b0bb8d518ce33c3c8febec5963e0ca4078f10ec`, [complete scope/limits](../DESIGN.md#b24-left-encoder-group-and-reported-b18-mounting-fit). Earlier five changes remain, including explicit electronics-overlap exception and35 proposed BN616/1076469 countersunk exterior screws. Thin stock0.7/flat edge0.2/inletproxygap0.225 remain reviewable nominal limits, not physical strength/fit/safety acceptance.

Executed32 moved-group/3072 control/1056 post-footprint/6 left-group-RCA comparisons, minimumRCA gap7.45 and side reserve9.35; inherited98 jack/16 inlet-support/2485 seat comparisons pass analytically.109 frozen source hashes unchanged, including seven B23 files. Five A3 sheets generated/reopened/rendered/reviewed,17 annotations; real1536×1024 PNG converted/opened and main intent checked. Task previews removed. Concept is NOT Fusion/dimensional validation.

**B24-LAYOUT-01 DRAWING NOT APPROVED.** Request explicit named nominal mechanical-prototype drawing approval before any new native geometry. No B23/B24 native model/view/export or cloud save; no closing/discarding modified B22 or changing unrelated jog work. Later native review/separate model approval/export/physical/process/electrical/thermal gates remain.

Latest read-only source observation after B24 publication: B22 cloudlineage `urn:adsk.wipprod:dm.lineage:7Lqp25VsSb-kx1vXjdNSmw`, **version2/saved/unmodified**,1063 entries/exact prior geometry-pose fingerprint. No assistant save or geometry mutation was issued; save actor/time not established. Earlier modified/version1 observations stay historical, not current guards. Separate jog unchanged. [Native observation](../schematics/enclosure/B24/DJC_Enclosure_Rev_B24_drawing_validation.json); no local archive/reopen claim or additional save/export authority.

## Engineer approval of B24-LAYOUT-01 nominal mechanical-prototype drawing

The engineer explicitly selects **“Zatwierdzam B24-LAYOUT-01”** after reviewing the five-sheet PDF/concept and the stated thin-seat/tight-inlet limits. **APPROVED: B24-LAYOUT-01 nominal mechanical-prototype drawing**, including the six changes, T01/E01/T02 positions/source23 spacing, earlier closed midpoint/AUX/screw choices, exact proposed BN616/1076469 M3×8 exterior hardware and named reference/physical exceptions. This permits native modeling and validation, not model approval, exports, cloud save, physical strength/fit or electrical/thermal release.

Freeze all seven files under `schematics/enclosure/B24/` byte-for-byte, including historical pending labels; this later scoped approval supersedes those labels without rewriting them:

| File | SHA256 |
|---|---|
| `DJC_Enclosure_Rev_B24_check.py` | `04dda875a9672296e3b40aad8a105dfa5fa37c15300524d980baad2c3eb5c632` |
| `DJC_Enclosure_Rev_B24_concept.png` | `71310ded247c68a179a71bbe8b0bb8d518ce33c3c8febec5963e0ca4078f10ec` |
| `DJC_Enclosure_Rev_B24_definition.json` | `a5b1b33bb07f4ffc497bb9184bdb579a1e91642561466b7847a17e4014659179` |
| `DJC_Enclosure_Rev_B24_drawing.pdf` | `225eb0a9a1ce07e694c17b709d23593f8cad98d47156d240dc294621fe7e2893` |
| `DJC_Enclosure_Rev_B24_drawing.swift` | `f435b24204f66b4f281d5547b62a60c7e6b793c09b07fe56f8e7a9abe08a15d1` |
| `DJC_Enclosure_Rev_B24_drawing_validation.json` | `fc8ebce2f04eeeb31162632d5d99ec0e64728e908bcf48711e66c367a426df16` |
| `DJC_Enclosure_Rev_B24_validation.json` | `f2a7d273d8c8300eaab4db50a651f28ecbc0bce5deea65a7a6f7c23edb546b4a` |

**Subsequent pre-mutation annotation finding:** B24 sheet02 incorrectly calls the P01–P03 upper apertureD10.1 “retained.” Actual native B22 has one cylindricalD8.5 face acrossZ18..20 at each axis, measured read-only for all three; the source native chamfer scope is B/T only. No new Fusion geometry has been created. Preserve approved B24 and propose **B24-ERRATA-01**, correcting only this annotation toD8.5 straight through/no new P chamfer, consistent with the unchanged-source/working-fit intent. Obtain the targeted erratum approval before applying the otherwise approved B24 native changes; do not silently add an unrequested chamfer or overwrite approved drawing bytes.

Published targeted [B24-ERRATA-01 one-sheet PDF](../schematics/enclosure/B24-ERRATA-01/DJC_Enclosure_Rev_B24_ERRATA_01_drawing.pdf), SHA256 `caa6c24e1b80201fb62e080911b17fa233dbc8f5980644c65180e16ee9f6fec8`, correcting BOTH B24 sheet02's false upperD10.1 note and its extra outer circle for P01–P03. Correct source isD8.5 straight through2/no new chamfer; native actual three-cylinder diameter/thickness assertions pass read-only. [Evidence/review](../schematics/enclosure/B24-ERRATA-01/DJC_Enclosure_Rev_B24_ERRATA_01_drawing_validation.json):1 A3 page reopened/rendered/reviewed/8 annotations,9 source hashes including all seven unchanged approved B24 files. Same main B24 concept remains applicable; no new geometry/concept generated. **Main B24 approval remains recorded; targeted erratum NOT APPROVED**, no native changes/save/export. Request only this annotation acceptance, not repeat main drawing/physical-fit approval.


## Engineer approval of B24-ERRATA-01

The engineer explicitly selects **“Zatwierdzam B24-ERRATA-01”**. **APPROVED: B24-ERRATA-01**, limited to correcting B24 sheet02's P01–P03 aperture note and extra outer circle: retained native diameter8.5 mm, straight through the2 mm panel, no new potentiometer chamfer. B24-LAYOUT-01 otherwise remains approved unchanged.

Freeze the following five erratum files byte-for-byte, including their historical pending labels. This later recorded approval supersedes those labels. Together with the main B24 approval, it permits a separate native B24 model and geometric validation, not model approval, fabrication exports, cloud save or physical/electrical/thermal certification.

| File | SHA256 |
|---|---|
| `DJC_Enclosure_Rev_B24_ERRATA_01_definition.json` | `f9ff6d75282989a04a5560bf19c57eae53ad8fd9ac593834247ee2e6be206186` |
| `DJC_Enclosure_Rev_B24_ERRATA_01_drawing.pdf` | `caa6c24e1b80201fb62e080911b17fa233dbc8f5980644c65180e16ee9f6fec8` |
| `DJC_Enclosure_Rev_B24_ERRATA_01_drawing.swift` | `1f63c68a993a5b437c77c7d208a07199d35a780fd74ba362049ea97e26ac0860` |
| `DJC_Enclosure_Rev_B24_ERRATA_01_drawing_validation.json` | `8a1e4a2d30028bf8f0b32d1b554deb0af10c0456d42c1e5b53b7ec84931029f9` |
| `DJC_Enclosure_Rev_B24_ERRATA_01_validation.json` | `0dfa6af2857dddd20b18013a0ba6c0f1fe71fcb936ccbd22a6a5e8090b7cbfdd` |

Preserve the saved B22 source and unrelated jog document; create B24 separately. No assistant cloud save, source overwrite or unapproved STL/STEP/F3D.

## B24-Fusion-01 native model published for engineer review

Implemented the approved B24-LAYOUT-01 + B24-ERRATA-01 six-change scope in separate **`DJC Enclosure B24-Fusion-01 DRAFT`**, unsaved/modified,1327 healthy entries. [Scoped model review and six actual Fusion PNGs](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion01_validation.md), [executed native evidence](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion01_validation.json), JSON SHA256 `ba67f21485581fe485639bc2372bcb10f9b47eeeb2ed41886f8f95c78eed778c`.

Stable review fingerprint `289c4ba298c854994adb5f7fe5982b433b0977a62ac47c3d37ab721606104012`.409 body instances/377 solids/32 sheets/126 printed bodies/131 lumps/zero meshes;98 complete occurrence moves/360 retained shapes and expected poses checked.70876 solid pairs screened/737 explicit BRep intersections; zero printed/printed positives/native126-body confirmation.191 complete nominal heads/2220 seat probes pass;244 changed-path probes and58 sampled cap poses pass/min1.062910mm.199 positive references are individually explained:191 nominal pilot engagements,3 board envelopes,5 retained fader-case exceptions informed by the reported B18 physical mounting fit. Thin seats/inlet and incomplete purchased/service/jog/physical/process/electrical limits remain explicit.

All109 dimensional-source hashes/twelve approved drawing-package files unchanged; native saved/unmodified B22 cloud2 and unrelated saved/unmodified jog cloud2 protected snapshots unchanged. Independent B22 native history rebuilt because cross-document Paste New is unsupported; source407 body/sheet shapes/poses matched before deltas. Complex interfaces retain exact analytic/faceted Base Features. Camera/visibility restored, final live view assembled; no task temporary files, no assistant cloud save/close/discard.

**MODEL NOT APPROVED — request explicit named B24-Fusion-01 nominal unpowered mechanical-prototype approval or corrections.** Drawing approval and passed geometry checks do not grant model approval or strength/physical/electrical certification. No STL/STEP/F3D exists for this revision yet; requested fabrication/archive exports follow separate model approval, preserving the reviewed fingerprint and source files. No cloud-save authority follows.

## Engineer approval of B24-Fusion-01 and requested STL, STEP and F3D

After the named B24-Fusion-01 review, the engineer states **“Jest super. Przygotuj STL, STEP i F3D. Do chmury zapisałem.”** This explicitly accepts the current **B24-Fusion-01 nominal unpowered mechanical-prototype model for the requested exports**. It is not physical/strength/printing/electrical/thermal certification or authority for the assistant to cloud-save/overwrite.

Fresh read-only native inspection confirms `DJC Enclosure B24-Fusion-01 DRAFT`, saved/unmodified, cloudlineage `urn:adsk.wipprod:dm.lineage:1eQw5IU3TvGv3uWuLvf00Q`, version1,1327 entries/409 bodies and exact reviewed fingerprint `289c4ba298c854994adb5f7fe5982b433b0977a62ac47c3d37ab721606104012`. No external component links. The engineer reports the cloud save; no assistant save is issued or inferred.

**APPROVED: B24-Fusion-01**, limited to the review's nominal geometry and explained reference/thin-seat/inlet/physical/process limits. Export and verify all distinct printed parts as separate STL/mm with BOM quantities, the complete represented assembly as STEP, and the native editable-history F3D archive in `models/enclosure/B24/FUSION/`. Preserve B22, unrelated jog work and approved files.

Freeze the eleven accepted B24 native review files byte-for-byte, including historical pending labels. This later scoped approval supersedes those labels:

| File | SHA256 |
|---|---|
| `DJC_Enclosure_Rev_B24_Fusion01_assembled_fusion-view.png` | `e08d674f49432b47e5f6e8ba8d64525fa43770d0f8b19bbd47c930a7a1cfa198` |
| `DJC_Enclosure_Rev_B24_Fusion01_flush-seat_fusion-view.png` | `eae631c31fd65f88e919b0ef2c7dd45f72e8381de53d787fd5a52545acfda5e4` |
| `DJC_Enclosure_Rev_B24_Fusion01_left-controls_fusion-view.png` | `e61092c70df79c37ba3f1e22af9978917c3c688d670602f59924412cb0aabe3c` |
| `DJC_Enclosure_Rev_B24_Fusion01_open_fusion-view.png` | `93a0382f7f0940870ab536e2410cc9165c02c6868723a2dbeadf29bb761de4f5` |
| `DJC_Enclosure_Rev_B24_Fusion01_rear-inlet_fusion-view.png` | `aad8db96792fa189cc6a348899a846749b5dab3db063834aaa6beb4e3df5429d` |
| `DJC_Enclosure_Rev_B24_Fusion01_rear_fusion-view.png` | `b8b72247d4850a60119e17dd134860abde24bf8fd940e5ca30c9ad532c7e2cf3` |
| `DJC_Enclosure_Rev_B24_Fusion01_validation.json` | `ba67f21485581fe485639bc2372bcb10f9b47eeeb2ed41886f8f95c78eed778c` |
| `DJC_Enclosure_Rev_B24_Fusion01_validation.md` | `8885094513ca5f829700e832552594a4554ffadbdd23a601eca60d1c57cc7a81` |
| `DJC_Enclosure_Rev_B24_changes.py` | `06b9681dd9e75be5612776f722091560a2b7d6e962158f97256cbad9ed2e7d91` |
| `DJC_Enclosure_Rev_B24_fusion.py` | `9d9456f40220b721c8f1d0df9d2518f35dcfdb881a02f6f6436a700f8abf6fe5` |
| `DJC_Enclosure_Rev_B24_validate.py` | `df2a7891b507ddc69db57fc8c7eb116d55b349ba9687713887ceb2e3fdcbef00` |

Seven main/five erratum drawing files remain frozen independently. Actual export verification and the latest saved state will be recorded in a new delivery report, not by rewriting accepted review evidence.

## B24-Fusion-01 requested nominal export handoff verified

[Complete handoff](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion01_delivery.md), [all-file manifest](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion01_delivery.json), [BOM/paths](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion01_BOM_and_exports.json). **APPROVED NOMINAL SCOPE / REQUESTED STL, STEP AND F3D COMPLETE AND VERIFIED**, under the preceding explicit engineer acceptance. No new geometry/physical/electrical/thermal approval is inferred.

- 28 actual binary STL/mm definitions/131 printed pieces in `models/enclosure/B24/FUSION/`,353660552bytes/7073164triangles total. All28 freshly pass exact edge/winding/degeneracy/connectivity/positive-volume/native-scale checks, maximum bound difference0.000005957098mm; no mesh repair, slicing or G-code.
- Editable [F3D](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion01.f3d),12662361bytes/SHA256 `0b6bc50781710a45c4b8f5eaa03f5fcb4e708915b31c21c769a0f2e4d934a827`,368-entry ZIP CRC pass; actual reopen/full replay/computeAll1327 healthy entries/9 parameters/409 bodies/zero external links. Identities/bounds/poses/topology exact;39 cap-instance computed volumes differ only by floating roundoff≤2.274e-13mm³, with zero two-way BRep difference for all four affected definitions. Raw numerical fingerprint distinction is disclosed in round-trip JSON.
- Complete represented [STEP](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion01_assembly.step),15909565bytes/SHA256 `12360237148cdb4a7c2d7e1622c9625a57706ec5cf94c83b4c19aa588c2a144d`; actual reopen matches408 geometry-bearing component instances/382 closed solid lumps/32 datum faces, including hidden/repeated/reference hardware. Maximum corrected bound difference6.054e-10mm; every solid component checked by two-way BRep difference, maximum0mm³ at kernel resolution. No omitted low-profile jog or complete bought geometry is fabricated.
- Source remains engineer-saved/unmodified cloudversion1/exact reviewed geometry, active and untouched. All132 frozen inputs/drawing/review files and native B22/jog preserved. Eleven accepted review files retain their historical pending labels. Three modified task-owned verification/empty-workspace documents remain open, clearly named; no authority to close/discard them or cloud-save the source was inferred.

Detailed executed evidence: [STL](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion01_STL_validation.json), [F3D](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion01_F3D_roundtrip.json), [STEP](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion01_STEP_roundtrip.json), [final native state](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion01_native_final_state.json). Physical fits/strength, complete installation, usable print margins/orientations/process/calibration and safe mains/thermal use remain engineer-owned gates. No repeat approval/export is required for the delivered unchanged nominal scope.

## B24-TH01 nominal trial fastener route authorized and model published for review

The engineer requests the missing enclosure fasteners from [LyraMaker](https://lyramaker.com/products/screw/) and a file listing STL quantities. After disclosure that the stock UI lacks M1.6, M2 flat/hex is unsupported and the stock M3 flat head differs from B24, the engineer explicitly selects **“Modele nominalne B24”**. Authorized scope: prepare five separate nominal models in the same published engine, preserve B24 outer diameters/lengths/countersinks, and choose only missing drive geometry/depth. No enclosure changes, new dependencies/runtime configuration, print-fit compensation or automatic model approval.

Selected source-library drive dimensions in mm: M3 countersunk hexAF2/depth1.1; M3 socket hexAF2.5/depth1.5; M2 slotwidth0.5/depth0.5; M1.6 slotwidth0.4/depth0.41. All use coarse threads. EH02 is an actual unmodified UI render; the four countersunk definitions are separate nominal SCAD rendered by the same public website OpenSCAD/BOSL2 worker, preserving B24 pure90-degree cone envelopes. These are trial models, not complete certified purchased screws.

[Named B24-TH01 review](../models/enclosure/B24-TH01/Enclosure_Hardware_Rev_TH01_review.md), [exact preview buffers/SCAD/sources/checks](../models/enclosure/B24-TH01/Enclosure_Hardware_Rev_TH01_preview.json), [actual five-mesh PNG](../models/enclosure/B24-TH01/Enclosure_Hardware_Rev_TH01_generator-view.png), [planned print quantities](../models/enclosure/B24-TH01/Enclosure_Hardware_Rev_TH01_print-quantities.md). Five renders/31440triangles/1572420preview bytes; all five pass the existing checker and nominal length/head-radius/cone/depth checks within a1e-6-mm numerical threshold, not a manufacturing tolerance. PNG1800x1250 opened/reviewed; independent cameras/normal colours, not Fusion/LLM/physical proof.185 new screws including2 conditional PSU screws;6 existing M2.5x6 are reused, not added again.

| Review artifact | SHA256 |
|---|---|
| `Enclosure_Hardware_Rev_TH01_review.md` | `3a9c627ab5486d1578df13bed978b118b40023d77cb5d427697c544b402c9a79` |
| `Enclosure_Hardware_Rev_TH01_preview.json` | `a7d2ef4ca4c9f17cfa817312a5b3cdbca442b134aaae5f8e614519b9cd5cfda2` |
| `Enclosure_Hardware_Rev_TH01_generator-view.png` | `bd552338d3ddd713ac2aa3695c23b98987a1af5fcac4775c0bf0e47ce7c4cfdd` |

**B24-TH01 MODEL NOT APPROVED / NO FINAL STL FILES.** Request explicit named nominal printed-trial approval before writing the exact five reviewed buffers as fabrication STL/mm, then verify destination meshes/hashes/scale and installed slicer import and update the quantity file. Material/process/fit/torque/strength remain unconfirmed; PSU thread compatibility/penetration conditional, initial trial unpowered. Approved B24 and F12-TH01 packages preserved; no Fusion operation or cloud save. The nominal-route selection is not whole-controller, physical or electrical approval.

## Engineer approval of B24-TH01 printed trial hardware and STL destination

After viewing the actual five-mesh PNG and model-review report, the engineer explicitly selects **“Zatwierdzam B24-TH01”** and confirms final five-file STL/mm delivery to `models/enclosure/B24-TH01/`.

**APPROVED: B24-TH01 nominal printed trial hardware**, limited to the five exact reviewed models, retained B24 outer envelopes and stated delegated drive choices. The three review artifacts/hashes in the preceding entry are frozen byte-for-byte, including their historical pending labels; this later approval supersedes those labels without rewriting accepted evidence. Write the approved preview buffers exactly, without regeneration, scaling, repair or substitution, then verify actual files and installed slicer import and update the print-quantity file.

This does not approve physical fit/strength/torque, print settings, safe PSU mounting or mains use, or the complete controller. EH05 remains conditional on actual PSU thread compatibility/permitted penetration and initial unpowered trial. Preserve approved B24/F12-TH01 files; no Fusion geometry, cloud save or model overwrite is authorized or needed.

## B24-TH01 approved trial-fastener STL handoff verified

All five requested binary STL/mm definitions now exist in `models/enclosure/B24-TH01/`, byte-for-byte equal to the exact approved preview buffers:1572420bytes/31440triangles. [Actual file links and print quantities](../models/enclosure/B24-TH01/Enclosure_Hardware_Rev_TH01_print-quantities.md), [destination hashes/full mesh evidence](../models/enclosure/B24-TH01/Enclosure_Hardware_Rev_TH01_STL_exports.json), [actual installed BambuStudio imports](../models/enclosure/B24-TH01/Enclosure_Hardware_Rev_TH01_Bambu_info.json).

Five fresh destination parses pass finite/degeneracy/duplicate/closed-edge/winding/single-surface/positive-volume checks; bounds match the approved previews exactly. Five `BambuStudio --info` runs exit0, all `manifold=yes`/one part, matching facets and interpreted mm dimensions. No slicing/G-code/printer job, mesh repair, scale change or regeneration. The three accepted review artifacts remain byte-identical to the preceding registered hashes, retaining historical pending labels; this verified handoff supersedes those labels.

**APPROVED NOMINAL TRIAL SCOPE / REQUESTED FIVE-STL HANDOFF COMPLETE.** Print35 M3x8 countersunk,24 M3x8 socket,72 M2x6 countersunk,52 M1.6x5 countersunk and2 conditional M3x6 PSU screws;185 new total. Reuse the same6 existing M2.5x6 jog-floor screws already counted in F12-TH01, not an extra batch. No new nuts/washers for B24 joining pilots. No approved B24/jog geometry/file overwrite or Fusion/cloud operation. Engineer owns slicing/process, individual fit/drive/seat/strength tests and actual PSU thread/penetration/electrical checks; none is certified by the nominal mesh release.

## B24-KCAP-01 larger B11–B22 heads requested; drawing published for approval

The engineer requests larger B11–B22 keycap models for use in `models/enclosure/B24/FUSION/`, referring to the existing frontpanel specification. R05 sheet3 and retained R06–R12 references define four CUE/PLAY heads D40 and eight HC heads40×40, retaining the mounting stem. Read-only native inspection confirms all24 current B caps still use the common14×14 definition. This request authorizes preparing the local correction, **not named approval of an unseen detailed drawing/model**.

Published **B24-KCAP-01 DRAFT**: [two-sheet dimensioned PDF](../schematics/frontpanel/K01/DJC_Keycaps_Rev_K01_drawing.pdf), [complete definition/source hashes](../schematics/frontpanel/K01/DJC_Keycaps_Rev_K01_definition.json), [editable generator](../schematics/frontpanel/K01/DJC_Keycaps_Rev_K01_drawing.swift), [executed checks](../schematics/frontpanel/K01/DJC_Keycaps_Rev_K01_drawing_validation.json), [illustrative LLM concept PNG](../schematics/frontpanel/K01/DJC_Keycaps_Rev_K01_concept.png) and [review/remaining gates](../schematics/frontpanel/K01/DJC_Keycaps_Rev_K01_review.md). Proposed detail retains headheight4, source lower/upper offsets0.6/0.8, HC R3, exact stem/socket and exact small square ornamental recess on both head shapes. No head-wide scaling of the mechanical interface. Keep original CAP_B x12 at B01–B10/B23/B24; do not edit its shared24-instance definition.

Actual drawing checks:2 A3 pages generated/reopened/annotation-checked/rendered/opened;4764 conservative head-box pairs against397 other archived B24 bodies, zero positive AABB overlaps,6mm minimum new-head box gap. No native replacement geometry or all-body BRep collision certification yet. Actual returned WebP opened/converted/reopened as1536×1024 PNG, CRC/raster checks pass. Five source hashes unchanged. PDF SHA256 `e634f435e754b8c79febe69c3d451eb04e2275fabc42269150432af29bf56a45`; concept SHA256 `251d22d2091baf2c82a526cf79afeeb5ec34c43d820a455d72d82d878858e397`.

**DRAWING B24-KCAP-01 NOT APPROVED; no new Fusion geometry or STL/STEP/F3D.** Planned standalone native revision is `B24-KCAP-Fusion-01`, new output subdirectory `models/enclosure/B24/FUSION/KEYCAPS_K01/`. Separate model approval precedes exports; this kit does not overwrite or reapprove the complete B24 assembly. Live B24 is now externally observed saved/modified/cloudversion1,1327 entries/zero reported health issues; no assistant cloud save/close/discard, pose, visibility, camera or geometry change. Cap material, actual stroke, eccentric-load strength and print-process/fit qualification remain open.


### Engineer requests a correction before B24-KCAP-01 approval

Presented with the PDF/concept and the named approval question, the engineer selects **“Potrzebna korekta detalu”**. No correction description or revised dimensions accompany that selection. **B24-KCAP-01 remains unapproved; obtain the requested correction before revising the drawing.** Do not guess a new profile, dimension, finish, stem or socket, and do not create Fusion geometry or STL/STEP/F3D. The reviewed draft files remain available as the reference for the engineer's correction.


## B24-KCAP-02 source logos and proportional HC outline authorized; drawing published

The engineer clarifies the K01 correction: copy logos from `old_case/play-pause.FCStd`/`.stl` and `old_case/cue.FCStd`/`.stl` onto the new PLAY/PAUSE and CUE heads, and enlarge the HC square logo. Asked for the HC size, the engineer explicitly selects **“Proporcja obrysu do główki”**: outer mouth10.4×40/14=29.7142857143mm, lengthening straight runs while retaining source corner radii, straight groove width0.8, depth0.4 and entry0.2. The same selected option explicitly retains CUE/PLAY symbols at1:1. This is bounded correction/dimensional authority, **not named drawing/model approval**.

Published **B24-KCAP-02 DRAFT**: [three-sheet dimensioned PDF](../schematics/frontpanel/K02/DJC_Keycaps_Rev_K02_drawing.pdf), [definition](../schematics/frontpanel/K02/DJC_Keycaps_Rev_K02_definition.json), [native sketch/final STL source data](../schematics/frontpanel/K02/DJC_Keycaps_Rev_K02_logo_sources.json), [source extractor](../schematics/frontpanel/K02/DJC_Keycaps_Rev_K02_sources.py), [editable generator](../schematics/frontpanel/K02/DJC_Keycaps_Rev_K02_drawing.swift), [executed drawing checks](../schematics/frontpanel/K02/DJC_Keycaps_Rev_K02_drawing_validation.json), [illustrative concept PNG](../schematics/frontpanel/K02/DJC_Keycaps_Rev_K02_concept.png), [complete review/gates](../schematics/frontpanel/K02/DJC_Keycaps_Rev_K02_review.md). Three definitions:CAP-CUE40 x2/B11+B17;CAP-PP40 x2/B12+B18;CAP-HC40 x8/B13–B16+B19–B22. Keep all K01 exteriors, current4.6 stem/socket, panel and other12 small caps; legacy CUE/PLAY stems3.6 are not copied. Remove the former square ornament from both circular variants. All six K01 files remain unchanged, superseded unapproved history.

Actual source checks: both FCStd archive CRCs pass; native closed profiles contain30 PLAY/PAUSE curves/four regions and14 CUE curves/two regions. Final source STL floor vertices agree with analytic native curves to2.264412e-7/1.001704e-7mm, below1e-6 numerical check, not a manufacturing tolerance. Final mouth/floor coordinates,0.4 depth/0.2 entry and source spacing/orientation are retained; no font/pixel tracing/recentering. Three A3 sheets generated/reopened/annotation-checked/rendered/opened;4764 archived head-box pairs clear,6mm minimum head gap. Actual LLM WebP opened/converted/reopened as1536×1024 PNG, CRC/raster checks pass. PDF SHA256 `000de38e08a47f5edef9db8fac290c6f50a8996fb8c7c49af0b81cfc74e1097c`; concept SHA256 `2fd9435ffccf511f4093681291cc78bd481ad02336993fb0e1bbf0ecf1d554ce`.

**DRAWING B24-KCAP-02 NOT APPROVED; no new native cap geometry or STL/STEP/F3D.** Planned `B24-KCAP-Fusion-02`, destination `models/enclosure/B24/FUSION/KEYCAPS_K02/`. Separate model approval remains mandatory before exports. Active B24 saved/modified,3 open documents; no assistant geometry/presentation/cloud-save/close/discard change. Actual switch travel/return, cap material/process/calibration and eccentric-load strength remain physically unqualified.


### Further correction requested before B24-KCAP-02 approval

After presentation of the corrected three-sheet PDF and separate concept, the engineer selects **“Potrzebna kolejna korekta”**. No description or revised dimensions accompany that response. **B24-KCAP-02 remains unapproved.** Obtain the specific correction before preparing another revision; preserve the K02 review package and do not guess a size, orientation, symbol or finish change. No new Fusion geometry or STL/STEP/F3D is authorized.


## B24-KCAP-03 larger CUE and PLAY/PAUSE symbols authorized; drawing published

The engineer clarifies **“Logo na play/pause i cue powiększ. Same kształty są super.”** Asked whether to use exact40/14 for both, the engineer explicitly selects **“Tak, powiększ ×2,857”**. The presented option specifies complete outline/radius scaling in XY, retained depth0.4, PLAY/PAUSE about29.71×12.80 and CUE17.06×12.57mm, unchanged HOT CUE/heads/mounting. Use exact20/7, not the rounded label. **Existing source shapes accepted; bounded enlargement authority only, not named drawing/model approval.**

Published **B24-KCAP-03 DRAFT**: [three-sheet PDF](../schematics/frontpanel/K03/DJC_Keycaps_Rev_K03_drawing.pdf), [amendment/authority](../schematics/frontpanel/K03/DJC_Keycaps_Rev_K03_definition.json), [editable generator/self-checks](../schematics/frontpanel/K03/DJC_Keycaps_Rev_K03_drawing.swift), [executed checks](../schematics/frontpanel/K03/DJC_Keycaps_Rev_K03_drawing_validation.json), [illustrative concept PNG](../schematics/frontpanel/K03/DJC_Keycaps_Rev_K03_concept.png), [review/gates](../schematics/frontpanel/K03/DJC_Keycaps_Rev_K03_review.md). Inherit all unchanged K02 data and exact source coordinates; map each complete CUE/PLAY void by(u,v,w)->(20u/7,20v/7,w). No recenter/mirror/font replacement. Depth0.4/floorw3.6/entry height0.2 remain fixed; lateral nominal entry0.2 becomes0.571429, so CUE/PLAY are no longer0.2×45 entry. Do not silently re-chamfer; submit this source-preserving consequence with the named drawing. HC retains its unchanged entry/width/radii and29.714286 outline. Exterior heads, exact4.6 stem/socket, all positions/panel and other12 small caps remain unchanged.

Actual Swift smoke:3 A3 pages generated/reopened,12 selected annotations checked, all pages rendered/opened/reviewed. New envelopes CUE17.060804×12.571429 and PLAY/PAUSE29.714285×12.803431; both bounding boxes fit circular topR19.2 with conservative radial reserves8.590892/3.022341mm.4764 archived head-box pairs clear,6mm head gap; not native model collision/strength certification.23 input/review hashes preserved, including all6 K01/all8 K02 files and B24 archive. Actual returned WebP opened, converted/reopened as1536×1024 PNG, signature/CRC/raster pass. PDF SHA256 `a31b600e5c6c5c7c2b0ef55fc7a9c4f03b409903709d1b4404a59faaf0638159`; concept SHA256 `8f7088f14008da35b9c399d5e7f1bef57c32dace0ae60a7696b2bc06cdb593b5`.

**DRAWING B24-KCAP-03 NOT APPROVED; no new native cap geometry or STL/STEP/F3D.** Planned `B24-KCAP-Fusion-03`, destination `models/enclosure/B24/FUSION/KEYCAPS_K03/`; separate model approval before export. Fresh Fusion query:3 open documents, B24 active/saved/modified. No assistant geometry, pose, camera, visibility, cloud-save, close or discard. Physical fit/return/stroke/strength and print/material/process qualification remain separate.


## Engineer approval of drawing B24-KCAP-03

After the enlarged CUE/PLAY PDF and illustrative concept are presented, the engineer explicitly selects **“Zatwierdzam B24-KCAP-03”**. **DRAWING B24-KCAP-03 APPROVED** for the stated nominal prototype accessory scope: complete CUE/PLAY source voids scaled exactly20/7 in XY and1 in Z, depth0.4 retained, including the documented entry-profile consequence. HOT CUE, head exteriors, exact current4.6 stem/socket, all positions/panel and other12 small CAP_B remain unchanged. This authorizes building the three standalone native cap definitions; it is not model approval, fabrication/export approval, physical qualification or permission to cloud-save/overwrite B24.

Freeze these six K03 files byte-for-byte; their historical pending/DRAFT labels are superseded by this explicit approval, not rewritten:

| File | Bytes | SHA256 |
|---|---:|---|
| `DJC_Keycaps_Rev_K03_concept.png` |1980772|`8f7088f14008da35b9c399d5e7f1bef57c32dace0ae60a7696b2bc06cdb593b5`|
| `DJC_Keycaps_Rev_K03_definition.json` |6107|`17eb6b31df913ba0e59d658b9821d27b61ace95e66251596bfa5488f4886dcec`|
| `DJC_Keycaps_Rev_K03_drawing.pdf` |43492|`a31b600e5c6c5c7c2b0ef55fc7a9c4f03b409903709d1b4404a59faaf0638159`|
| `DJC_Keycaps_Rev_K03_drawing.swift` |21917|`12ba9363477b80f9b635b0216ebd2cd8e675fc60668a04eac52f8b86e5ec8965`|
| `DJC_Keycaps_Rev_K03_drawing_validation.json` |6017|`adebbe69bc160d1094040f051df099a2071bb5918d9c842a033f2d77712e775a`|
| `DJC_Keycaps_Rev_K03_review.md` |6402|`47c16f76c27456ebcb66de099230ff6a5bb8f3623584bd39d0ea6f2acd0997fb`|

The unchanged K01/K02 exact mechanical/source definitions remain cited inputs, not newly approved alternative cap proposals. Preserve the modified native B24 and all existing files. Planned model is `B24-KCAP-Fusion-03`; actual geometry checks/Fusion PNGs and separate engineer model approval are required before STL/STEP/F3D in `models/enclosure/B24/FUSION/KEYCAPS_K03/`. No assistant cloud save/close/discard is authorized.


## B24-KCAP-Fusion-03 native model published for approval

Following explicit drawing B24-KCAP-03 approval, Basia builds a separate **`DJC Keycaps B24-KCAP-Fusion-03 DRAFT`** document: three single-solid component definitions, representative occurrences at X0/50/100mm for review only; BOM quantities CUE2, PLAY/PAUSE2, HC8. [Native review](../models/enclosure/B24/FUSION/KEYCAPS_K03/DJC_Keycaps_Rev_K03_Fusion03_validation.md), [executed checks](../models/enclosure/B24/FUSION/KEYCAPS_K03/DJC_Keycaps_Rev_K03_Fusion03_validation.json) and actual Fusion [isometric](../models/enclosure/B24/FUSION/KEYCAPS_K03/DJC_Keycaps_Rev_K03_Fusion03_kit-iso_fusion-view.png), [top](../models/enclosure/B24/FUSION/KEYCAPS_K03/DJC_Keycaps_Rev_K03_Fusion03_top_fusion-view.png), [underside](../models/enclosure/B24/FUSION/KEYCAPS_K03/DJC_Keycaps_Rev_K03_Fusion03_underside_fusion-view.png) are published; all views opened/reviewed, final kit camera restored.

Executed native checks:32 healthy timeline entries,6 user parameters,0 current meshes/external references; exact current stem/socket and expected enlarged CUE/PLAY voids each have0/0mm³ two-way differences. HC removed volume matches an independent section integral within1e-5mm³. Twelve installed caps against397 other represented B24 bodies plus66 cap pairs =4830 static pairs;60 positive-box candidates explicitly intersected, zero positive volume above1e-6mm³ and no inherited-overlap exceptions. All409 source inventory rows match approved B24 geometry/poses/topology/solid flags with zero observed maxima; source fingerprint and29 protected hashes unchanged. All-body scope includes hidden/repeated hardware and32 reference sheets, not absent vendor detail or the omitted replacement jog mechanism.

Native model geometry/pose fingerprint: `d771132cfa606e0daf4792096f13e50ac90dd08816032cec633c6c4162885a5d`. New kit is unsaved/modified; source B24 remains saved/modified and untouched. No assistant cloud save, close or discard. **MODEL B24-KCAP-Fusion-03 NOT YET APPROVED; no STL/STEP/F3D exported.** Request separate approval for this standalone kit and exports to `models/enclosure/B24/FUSION/KEYCAPS_K03/`, not replacement/overwrite of the whole-controller master. Physical material/process/fit/return/stroke/eccentric-load strength remain unqualified.


## Engineer approval of model B24-KCAP-Fusion-03

After the actual Fusion top view, native checks and kit scope are presented, the engineer explicitly selects **“Zatwierdzam B24-KCAP-Fusion-03”**. The question explicitly authorizes three STL/mm definitions, STEP of the complete three-definition kit and editable F3D in `models/enclosure/B24/FUSION/KEYCAPS_K03/`. **MODEL B24-KCAP-Fusion-03 APPROVED for the stated nominal prototype accessory scope and these exports.** This is not approval of a changed complete B24 assembly, physical/process qualification or authority to cloud-save/overwrite/close/discard documents.

Approved native geometry/pose fingerprint: `d771132cfa606e0daf4792096f13e50ac90dd08816032cec633c6c4162885a5d`. Freeze these eight review artifacts byte-for-byte in the agreed KEYCAPS_K03 directory; historical pending labels are superseded by this decision:

| File | SHA256 |
|---|---|
| `DJC_Keycaps_Rev_K03_fusion.py` |`de264ee164b99ff25acad5879b321f2a556edc6a4fe6c1754f3617de17b94648`|
| `DJC_Keycaps_Rev_K03_validate.py` |`2f09101c75fdb0cd5f3d9f014efe7fcc1ba707e1ee6c4b82d0f74aa06972a9c1`|
| `DJC_Keycaps_Rev_K03_Fusion03_source_snapshot.json` |`b20d11b92082ae69f79aecbec5b344c60b63735090b8874f138e358d593b79b1`|
| `DJC_Keycaps_Rev_K03_Fusion03_validation.json` |`91c24f36544873597e694431546a875867618b5f4701f377548de933db655fff`|
| `DJC_Keycaps_Rev_K03_Fusion03_kit-iso_fusion-view.png` |`dcad94196ca44aa06e17fa9ee51e2783aafacaf8c76c0b09a511bc1525128221`|
| `DJC_Keycaps_Rev_K03_Fusion03_top_fusion-view.png` |`73b204d93989c3872d7a92379d73515878b42072a575af991132baa5b0ab9635`|
| `DJC_Keycaps_Rev_K03_Fusion03_underside_fusion-view.png` |`2518b87ab648616f101fd34eb6971aa18bff8d867f47fb0630198dba6e3178d2`|
| `DJC_Keycaps_Rev_K03_Fusion03_validation.md` |`b57e441d3c85d1721871a1c175b87527bb151a677296f3aed4cf587259fdc554`|

Keep the six approved K03 drawing files and all protected B24/K01/K02/source inputs unchanged. Native kit remains unsaved/modified; source B24 saved/modified untouched. Export verification and actual destination file checks follow this approval; none are inferred from it. Material, slicing orientation/settings, physical fit/retention/return/stroke and eccentric-load strength remain unqualified.


## B24-KCAP-Fusion-03 approved kit exports verified

After the preceding explicit model/export approval, Basia delivers three STL/mm definitions (CUE2, PLAY/PAUSE2, HOT CUE8), the complete standalone three-component kit STEP and editable F3D in `models/enclosure/B24/FUSION/KEYCAPS_K03/`. [Current handoff/integration guide](../models/enclosure/B24/FUSION/KEYCAPS_K03/DJC_Keycaps_Rev_K03_Fusion03_handoff.md) and [BOM/export hashes](../models/enclosure/B24/FUSION/KEYCAPS_K03/DJC_Keycaps_Rev_K03_Fusion03_BOM_and_exports.json) identify the actual files; not a regenerated complete-controller STEP/F3D.

| File | Bytes | SHA256 |
|---|---:|---|
| `CAP-CUE40_Rev_K03_Fusion03.stl` |215284|`b5f8374b7fe40e5e8d02d47cfbf4d6c739d020cb72bfb5ba36059ce4b38ce571`|
| `CAP-PP40_Rev_K03_Fusion03.stl` |234484|`59245a23c144f44d41961fe8b7d75fd3b78d0cc92ffb29293b260076498d332d`|
| `CAP-HC40_Rev_K03_Fusion03.stl` |455484|`a7d5ed2b3b24f522ea4d68b192ed64052bf3c69c7bc3b1e5eae24732725e0e31`|
| `DJC_Keycaps_Rev_K03_Fusion03_kit.step` |2110822|`f5216b87714517901c28fd16f0cf30da31d6ae4c9a523f828571575ea38a6e69`|
| `DJC_Keycaps_Rev_K03_Fusion03.f3d` |1624390|`d6233feb1a2810f8e1ca9106c49675235022a6521ff1022d19fe19f354b037b5`|

Actual verification: three fresh destination STL parses pass finite/duplicate/degenerate/closed-edge/winding/single-surface/positive-volume checks,18100 triangles total; maximum native bounding-coordinate difference0.000497818mm. Three installed BambuStudio `--info` imports exit0/`manifold=yes`/one part with matching facets and approximately40×40×8.6mm interpreted size. The initial1e-6mm metadata comparison failed by float32/reporting resolution, not raw STL scale: observed maximum1.818e-6mm passes the recorded one-ULP-at40mm plus six-decimal bound4.315e-6mm; no repair/scale/process change.

F3D actually reopened with full timeline replay/recompute:32 healthy entries,6 identical parameters,3 named closed solids/no meshes/external links; bounds/poses/topology identical, all three two-way BRep differences0/0mm³. STEP actually reopened/recomputed:3 named closed solids, identical poses/all three two-way differences0/0mm³; maximum bound difference5.673e-8mm, computed-volume roundoff9.639e-6mm³. Final five local byte counts/SHA256, F3D ZIP CRC, three1800×1100 review PNG signatures/hashes and all37 protected input/review hashes verified.

Active approved kit remains unsaved/modified despite historical DRAFT name; source B24 saved/modified untouched. Original jog/B22 saved/unmodified; two unsaved/modified `Untitled` verification documents remain open. No cloud save/close/discard/approved-file overwrite. **APPROVED NOMINAL ACCESSORY SCOPE / REQUIRED KIT HANDOFF COMPLETE.** No slicing/G-code/physical tests, full triangle self-intersection or vertex-link certification. Material/orientation/layers/support/usable margins/calibration/actual fit, return/stroke and eccentric-load strength remain engineer-owned physical/process work. Geometry/export approval is not manufacturing readiness.


## B24-Fusion-02 integration of approved K03 keycaps requested

Engineer requests: **“Uwzględnij te nowe key capy w modelu @models/enclosure/B24/FUSION/ i w samym Fusion”**. Integrate only the twelve already approved K03 caps at approved original B24 transforms: CUE B11/B17, PLAY/PAUSE B12/B18 and HOT CUE B13–B16/B19–B22. Retain twelve other small CAP_B, all mounts/panel/hardware and all other geometry. No new dimension, tolerance, placement or material selection. The drawing basis is the approved composite **B24-LAYOUT-01 + B24-ERRATA-01 + B24-KCAP-03**; the K03 drawing already defines these twelve installed positions and unchanged interfaces. Preserve the approved drawing packages; no new geometry beyond that basis is authorized.

Create full **B24-Fusion-02** in a separate document and new revision-matched files in the existing `models/enclosure/B24/FUSION/`; preserve B24-Fusion-01 and K03 archives/exports. The request authorizes integration work, not advance approval of the unseen full model or cloud saving. Actual native validation/review and explicit named B24-Fusion-02 model/export approval precede new STL/STEP/F3D. Approved unchanged STL geometry may be referenced/reused with verified hashes and current quantities rather than silently duplicated or re-meshed.

Fresh read-only native inspection: active original `DJC Enclosure B24-Fusion-01 DRAFT` now saved/unmodified, cloudversion2, same lineage,1327 healthy entries/409 body instances and geometry/pose fingerprint `826a52b0e3214f4af79a860beb90b03e392c46687cbd53ae2f703e56ba9e79bd`; all24 CAP_B still small. K03 kit is now saved/unmodified, cloudversion1, lineage `urn:adsk.wipprod:dm.lineage:9Said6GcSuWrbM7IRFHu8Q`, unchanged approved geometry fingerprint. These are observed external save-state changes, not assistant saves. Other original documents and two modified verification copies remain open and must be preserved.


## B24-Fusion-02 full integrated model published for approval

Following the explicit integration request and already approved composite drawings, Basia builds separate **`DJC Enclosure B24-Fusion-02 DRAFT`**, unsaved/modified. [Full review](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion02_validation.md), [executed native inventory/checks](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion02_validation.json) and actual Fusion [assembled](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion02_assembled_fusion-view.png), [top](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion02_top_fusion-view.png), [left-control detail](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion02_left-controls_fusion-view.png) are published; all three PNGs opened/reviewed, final assembled isometric restored.

Native1386 healthy timeline entries/15 parameters,409 represented body instances (377 solids/32 sheets),126 printed body instances/131 printed lumps; no current meshes/external links. All397 other body/sheet identities, bounds, poses, topology/solid flags and measured volumes unchanged. Each new cap definition has0/0mm³ difference from approved K03; twelve installed transforms/bounds agree exactly. CUE2/PLAY2/HC8 replace only B11–B22, leaving12 original small CAP_B. Staged native timeline0→1386 replay preserves every identity/bounds/pose/topology/solid flag and volume (maximum drift0). This is not a claim of successful global computeAll; direct archive merge failed its recompute/health assertion and was verified rolled back, then the frozen K03 native builder successfully rebuilt independent editable cap features.

Actual changed-geometry coverage4830 pairs:12×397 other bodies plus66 cap pairs. All60 positive-AABB candidates explicitly BRep-intersected; zero positive solid volumes above1e-6mm³. Prior unchanged B24 all-body/seat/sampled-motion checks and199 explained pilot/reference overlaps remain inherited, not freshly rerun or declared absent. All100 protected files and original document state/geometry/visibility unchanged. Original B24 cloud2/K03 cloud1 are saved/unmodified; other original and earlier modified verification documents preserved. New caps' lighter appearance is visual-only, not material selection.

**MODEL B24-Fusion-02 NOT YET APPROVED; no Fusion02 STL/STEP/F3D exports.** Request explicit named full-model/export approval for new complete-assembly STEP/editable F3D and current31-definition/131-piece STL BOM in `models/enclosure/B24/FUSION/`, preserving original files and reusing unchanged approved meshes by exact hashes. No cloud save, close/discard, new dimensions or physical/process/electrical/thermal qualification is authorized.


## Engineer approval of full model B24-Fusion-02

After the actual full assembled PNG, native checks, left-control detail and full scope are presented, the engineer explicitly selects **“Zatwierdzam B24-Fusion-02”**. The question authorizes new complete represented-assembly STEP, editable full-history F3D and updated31-definition/131-piece STL BOM using the existing verified immutable meshes, in `models/enclosure/B24/FUSION/`. **MODEL B24-Fusion-02 APPROVED for the stated nominal, unpowered mechanical-prototype integration and these exports.** Preserve Fusion01/K03; no assistant cloud save, overwrite, close/discard or physical/process/electrical/thermal qualification.

Approved full-model geometry/pose fingerprint: `988eff1b04b56df9419772dd4545190c5706cf0586d97b416dbd6e46b97ab826`. Freeze the following eight review artifacts byte-for-byte; historical pending labels are superseded by this explicit approval:

| File | Bytes | SHA256 |
|---|---:|---|
| `DJC_Enclosure_Rev_B24_Fusion02_integrate.py` |11558|`bf4de7dcd00343cfcebcd58933337a3799e9a090fa7d1eec78ca3842f2b52f8b`|
| `DJC_Enclosure_Rev_B24_Fusion02_validate.py` |12088|`7ce4fcd9779a6b8d18940d686d1c6e173b96f8f8afca41ed68cc2e8b12b9679e`|
| `DJC_Enclosure_Rev_B24_Fusion02_source_snapshot.json` |376108|`8aab14d8c624b1027c47465c1374e314c210b3ffedbf5597f7878085d67b56a5`|
| `DJC_Enclosure_Rev_B24_Fusion02_validation.json` |387689|`9d01a9740f45eb74ab0469ecf8f91c40fc793b83f6b2a6ff53638aa2e1b653d7`|
| `DJC_Enclosure_Rev_B24_Fusion02_validation.md` |6271|`55dbb0e77fcf323be65ac6219c42afb8dcecc56a72d3b265c673ab95ff43a5bf`|
| `DJC_Enclosure_Rev_B24_Fusion02_assembled_fusion-view.png` |570827|`e32fbf0322f92eba2374fbbc77f8b9956cc1ae236927a607124b747fd5a36372`|
| `DJC_Enclosure_Rev_B24_Fusion02_top_fusion-view.png` |238823|`0a9e239bbeb79f50a8cf5756a44567042de2870ede2b3d8f2337411f6cb1ee97`|
| `DJC_Enclosure_Rev_B24_Fusion02_left-controls_fusion-view.png` |165687|`930cadad45ca4e606b3020f73dd2eb5a866d5442001216bd1e860638db274832`|

This approval accepts only the reviewed installed caps/unchanged rest and disclosed staged-history/all-relevant-body check scope. No dimensional change, global computeAll success, continuous motion, physical fit/return/load or manufacturing readiness is inferred. Keep original saved B24 cloud2/K03 cloud1 and all100 protected files unchanged; verify exported full assembly files and current STL paths/quantities before handoff.


## B24-Fusion-02 complete integrated assembly handoff verified

Following explicit named full-model/export approval, the complete represented assembly is delivered in `models/enclosure/B24/FUSION/`. [Current handoff](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion02_delivery.md), [31-definition/131-piece BOM](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion02_BOM_and_exports.json), [verified all-file manifest](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion02_delivery.json).

| File | Bytes | SHA256 |
|---|---:|---|
| `DJC_Enclosure_Rev_B24_Fusion02.f3d` |14320928|`67eab9f407524cb0406388881402f8ab9aeed9df30f1b2ae5ed60d9844bb3c52`|
| `DJC_Enclosure_Rev_B24_Fusion02_assembly.step` |18174289|`71642b4dea706f27fa7cc756eda3561e4185a408b45d780ed3d2cb185a58b38e`|

Actual F3D reopen and staged0→1386 replay preserve exact approved fingerprint `988eff1b04b56df9419772dd4545190c5706cf0586d97b416dbd6e46b97ab826`,1386 healthy entries/15 identical parameters/409 instances/no meshes or links; all body identities/roles/bounds/poses/topology/solid flags and computed volumes match (maximum drift0). All3 new cap definitions also explicitly BRep-compared0/0mm³. ZIP CRC passes377 entries; no global computeAll success claimed.

Actual full STEP reopen: all408 nonempty component occurrences matched,382 closed solid lumps/32 datum-sheet faces retained. Every represented solid component aggregate compared by BRep in both directions, maximum0mm³. Maximum bounding-coordinate difference5.672214e-8mm/computed-volume difference9.638511e-6mm³; trimmed-half-cylinder fixture passes, no corrections required. Numerical thresholds do not define manufacturing tolerances.

All31 actual STL paths/headers/byte sizes/facet counts/SHA256 verified and bound to unchanged passing mesh topology/scale evidence:28 immutable Fusion01 geometries plus3 K03,7091264 unique-definition triangles/354565804bytes. No duplicate batch, re-meshing, scaling, repair or topology re-parse this stage. Current quantities CAP_B12/CUE2/PLAY2/HC8;131 pieces total. Final consumer checker runs with exit0, writes delivery manifest, verifies108 protected hashes and three actual1800×1100 PNG signatures/hashes.

Active complete `DJC Enclosure B24-Fusion-02 DRAFT` remains unsaved/modified with agreed assembled isometric. Original B24 cloud2/K03 cloud1/B22/jog remain saved/unmodified; two earlier Untitled and two new named VERIFY F3D/STEP Fusion02 modified copies preserved, nine documents total. No cloud save, approved-file overwrite, document close/discard or task temporary files.

**APPROVED NOMINAL FULL INTEGRATION / REQUESTED COMPLETE HANDOFF VERIFIED.** Prior199 pilot/reference overlap dispositions, incomplete purchased/service/electrical/jog geometry, thin-seat/inlet/process limits and physical fit/return/stroke/eccentric-load tests remain explicit. No physical, mains/electrical, thermal or manufacturing release. Engineer owns slicing/process and measurable physical acceptance; preserve predecessor packages and use the Fusion02 current BOM/full model.

## Engineer selection of B24-COLOR-C03 Pine Cherry

On 2026-10-22, after reviewing the red-accent Pine Retro variant, the engineer explicitly selects **Pine Cherry / B24-COLOR-C03 / proposal 07** as the controller color scheme. **APPROVED COLOR SELECTION ONLY.** [Canonical part-group palette](../DESIGN.md#selected-enclosure-palette-b24-color-c03): dark beige top panel; pine green lower shell/display housing; red HOT CUE/CUE/PLAY/PAUSE caps and all five fader caps; dark brown rotary knobs/remaining small button caps.

Selected [illustrative LLM PNG](../schematics/enclosure/B24-COLOR-C03/DJC_Enclosure_B24_COLOR_C03_07_pine-cherry_concept.png), SHA256 `399a315e482f7a230d2a8a1beb34eebd9d20a9349f44883a04629191d92f10b8`, is retained unchanged. Earlier B24-COLOR-C01/C02 concepts remain historical alternatives. The concept is not dimensional/geometry evidence; absent jog platters and internal parts receive no new color assignment. Actual filament shade/finish remains unverified.

Only design/approval/artifact records are updated. No Fusion operation, geometry/material-type/print-process change, new model approval, cloud save, approved-file overwrite or STL/STEP/F3D export is authorized or performed by this color-selection record.


## B24-R04-MARKS-01 accent-pattern correction published for drawing approval

On 2026-10-23 the engineer reports incorrectly arranged knob accents on PANEL_R04 and requests the same arrangement as the other knobs. Read-only native inspection confirms fifteen raised P01-P03 tick faces: each pattern uses theta0/45/90/135/180 degrees, with theta0 toward rear(-Y) and positive toward+X. P04-P13 instead share theta-140/-70/0/+70/+140 degrees:280-degree arc,70-degree spacing,80-degree operator-side gap. All ten source-local polygon patterns agree within2.842170943040401e-14mm. This is a real discrepancy, but B24-LAYOUT-01 sheet02 explicitly preserves the former right semicircle; it is a drawing change, not a presentation-only adjustment.

**DRAWING B24-R04-MARKS-01 DRAFT / NOT APPROVED.** [One-sheet dimensioned PDF](../schematics/enclosure/B24-R04-MARKS-01/DJC_Enclosure_Rev_B24_R04_MARKS_01_drawing.pdf), [dimensional definition](../schematics/enclosure/B24-R04-MARKS-01/DJC_Enclosure_Rev_B24_R04_MARKS_01_definition.json), [executed drawing checks](../schematics/enclosure/B24-R04-MARKS-01/DJC_Enclosure_Rev_B24_R04_MARKS_01_drawing_validation.json) and [separate illustrative LLM concept PNG](../schematics/enclosure/B24-R04-MARKS-01/DJC_Enclosure_Rev_B24_R04_MARKS_01_concept.png). Proposed correction translates exact P04 source polygons to the existing P01/P02/P03 axesX559/Y21,49,77; no rotation, scaling, dimensional invention, new parts or change to other geometry. Existing widths0.8, radial lengths4/3/4/3/4, innerR6.5 and raisedZ20..20.4 retained; apertureD8.5 throughZ18..20 and all assembly interfaces unchanged. Supersedes only the P01-P03 right-semicircle note.

Actual checks: Swift/CoreGraphics PDF generation/reopen/render passes, one searchable A3 sheet/9 annotation checks; reviewed the PDF and its2399x1697 raster. Source angle/length/width/radius and ten-pattern equality checks pass;15 distinct proposed polygons lie inside R04. Separate generated WebP opened, converted with installed sips to actual1536x1024 PNG, PNG signature/dimensions verified and image opened. PDF SHA256 `3818221f02d60ae16e45ee36313bfcd654d0dbd079532aa87ca1c7ea6d81d5bc`; concept SHA256 `f576a981f4ca556956780aff7139770390c8fba5a424b80037993076c1439a81`. Six registered approved drawing/model/script/export files remain hash-identical.

Native model unchanged: active `DJC Enclosure B24-Fusion-02 DRAFT`, saved/modified, cloudversion1, lineage `urn:adsk.wipprod:dm.lineage:FkOOTwGqTmCvGdYSo5phAQ`,1386 healthy timeline entries. Existing unsaved changes preserved; all three open documents retained, jog/K03 saved and unmodified. Shared repository/Fusion filesystem verified. No native geometry/camera/visibility/selection mutation, cloud save, approved-file overwrite or STL/STEP/F3D export. Existing delivered model/exports still have the old R04 marks; they are not represented as corrected.

**CHANGES REQUIRED / NEXT OWNER: engineer — explicitly approve drawing B24-R04-MARKS-01 or specify a correction.** Only after this gate may Basia implement the fifteen-mark delta in a new named model revision, check exact target geometry and unchanged bodies/interfaces/feature health, and request separate named model approval before exports. No cloud-save or physical/manufacturing approval is implied.


## Engineer approval of drawing B24-R04-MARKS-01

On 2026-10-23, after the dimensioned PDF, illustrative concept and exact fifteen-mark scope are presented, the engineer explicitly selects **“Zatwierdzam B24-R04-MARKS-01”**. **DRAWING B24-R04-MARKS-01 APPROVED** for copying the complete P04-P13 local pattern to P01-P03, retaining approved axes, apertures, mark dimensions and every other part. Frozen drawing PDF SHA256 `3818221f02d60ae16e45ee36313bfcd654d0dbd079532aa87ca1c7ea6d81d5bc`; its historical DRAFT/pending labels are superseded by this entry, not overwritten.

This authorizes native implementation and validation in separate **B24-Fusion-03**, not advance model approval, STL/STEP/F3D, cloud saving, overwriting prior approved artifacts or discarding existing unsaved changes. The current saved/modified B24-Fusion-02 exactly matches the approved full-geometry fingerprint `988eff1b04b56df9419772dd4545190c5706cf0586d97b416dbd6e46b97ab826`; preserve that original and all open documents. The already approved local Fusion02 F3D may be reopened as an independent editable source copy and verified against the active baseline before applying only this drawing delta.


## B24-Fusion-03 exact R04 accent correction built and checked

After the named drawing approval, Basia reopens the approved Fusion02 F3D into independent **`DJC Enclosure B24-Fusion-03 DRAFT`**, verifying the exact approved baseline fingerprint before changes. Native cut/join features replace only fifteen P01-P03 raised ticks with exact P04 source polygons. [Executed native checks](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion03_validation.json), [editable delta implementation](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion03_marks.py), actual Fusion [assembled](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion03_assembled_fusion-view.png) and [R04 detail](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion03_R04-detail_fusion-view.png). Both1800x1100 PNGs opened/reviewed. Detail temporarily hides only the three caps and enables visible edges; all original visibility/style restored and final camera assembled isometric. No generated/retouched image is used for model validation.

Actual geometry evidence: corrected R04 versus independently assembled expected before-minus-old-plus-new BRep has **0/0mm³ two-way difference**;15 tick top faces, maximum centroid discrepancy1.1457157353758233e-13mm. All408 other body/sheet instances preserve identities, bounds, poses, topology, solid flags and volumes with maximum drift0. All409 instances retained:377 solids/32 reference sheets,126 printed bodies/131 printed lumps,15 unchanged parameters, no meshes or external links. All1392 timeline entries healthy; appended1386→1392 replay preserves exact final fingerprint `1ca5736a04de2144e419d2e5115cd0c422568f8e8f11a0f86db40cdc8b779a59`. Imported base's complete historical replay is inherited, not rerun this stage.

Changed-mark interference scope:15 marks×408 other bodies/sheets =6120 pairs, including hidden/repeated hardware. All15 positive-AABB candidates explicitly BRep-intersected; zero positive solid volumes above1e-6mm³. AABB numerical threshold1e-6mm, not a manufacturing clearance. Existing unchanged pilot/reference overlaps and prior physical/process/electrical/thermal limitations remain inherited; no whole-assembly collision-free or physical-strength claim.

All11 registered protected source/drawing/export files remain hash-identical. Original saved/modified Fusion02 and its unsaved changes preserved; jog/K03 saved/unmodified, all original documents retained. New Fusion03 is UNSAVED/MODIFIED and left active. No cloud save, approved-file overwrite, document close/discard, task temporary files or Fusion03 STL/STEP/F3D export.

**MODEL B24-Fusion-03 NOT YET APPROVED.** Request explicit named model approval before delivering revision-matched corrected R04 STL/mm, complete represented-assembly STEP and editable F3D to the existing `models/enclosure/B24/FUSION/`. Other30 immutable printed definitions and original quantities can be reused by exact hash/current BOM; no unnecessary re-meshing. Existing exports still contain the prior R04 pattern.


## Engineer approval of model B24-Fusion-03 and revision-matched exports

On 2026-10-23, after the actual Fusion R04 detail/assembled view and native geometry/health/interference checks are presented, the engineer explicitly selects **“Zatwierdzam B24-Fusion-03”**. **MODEL B24-Fusion-03 APPROVED** for the fifteen-mark correction in the stated nominal unpowered mechanical-prototype scope. Approved fingerprint `1ca5736a04de2144e419d2e5115cd0c422568f8e8f11a0f86db40cdc8b779a59`.

The selected option expressly requests corrected R04 STL in mm, complete represented-assembly STEP, editable F3D and current BOM in `models/enclosure/B24/FUSION/`, preserving previous files/revisions and reusing the other30 immutable STL definitions. No cloud save, overwrite of approved files, closing/discarding modified documents, new dimensions/material/process or physical/manufacturing qualification is authorized. Freeze the Fusion03 native delta script, validation JSON and both reviewed Fusion PNGs; their historical DRAFT/pending labels are superseded by this explicit approval.


## B24-Fusion-03 corrected R04 and full-assembly exports delivered

**APPROVED / REQUESTED CORRECTION AND VERIFIED EXPORT HANDOFF COMPLETE.** Drawing B24-R04-MARKS-01 and model B24-Fusion-03 approvals are recorded above. Only the fifteen R04 P01-P03 raised ticks change; local geometry now exactly matches P04-P13. [Current31-definition/131-piece BOM](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion03_BOM_and_exports.json) and [46-file destination manifest](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion03_delivery.json) identify all actual files on the shared Fusion/repository filesystem.

| New file in `models/enclosure/B24/FUSION/` | Quantity / scope | Bytes | SHA256 |
|---|---|---:|---|
| `PANEL_R04_Rev_B24_Fusion03.stl` |1 printed PETG-intent panel, coordinates in mm |10451684|`18b1c2d9e90e4fbd8d83f36b41909205b4a0c658049e6a175cbf5696fe107b9b`|
| `DJC_Enclosure_Rev_B24_Fusion03_assembly.step` | Complete represented assembly |18180662|`04e013d204279716e29472774ab76b9b35b6151cd4a573b4da565a2fc048d92f`|
| `DJC_Enclosure_Rev_B24_Fusion03.f3d` | Editable full-history assembly |14267691|`28f61461fed75922fe2d95b024a7083ecb9ac413080e8fc35adf348c9ebf4454`|

The other30 existing STL definitions are reused at verified original paths/SHA256 with unchanged quantities; no redundant mesh batch, scaling, repair or previous-file overwrite. Use the Fusion03 BOM/new R04 STL instead of the older R04 file. Canonical R04 frame retains source axes and translates minimumXYZ to0. Its raw220×120×2.4mm envelope fits bare250³, not an approved print orientation/support/brim/usable-bed-margin layout.

Actual new-STL checks:209032 triangles; finite geometry, zero degenerate/duplicate facets, boundary/nonmanifold edges or winding conflicts; one connected closed positive-volume surface. Maximum native-bound difference9.536743172944284e-8mm. Independently parsed top triangles match **all15 approved tick footprints**, including their area, centroid and corner coordinates under2e-5mm numerical vertex/1e-4mm² area thresholds. The same checker rejects the old wrong-pattern R04 STL; existing closed-tetrahedron/missing-face self-checks pass. [Fresh mesh/tick evidence](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion03_STL_validation.json).

Actual STEP reopen: all408 component occurrences match retained identity/world geometry,382 closed solid lumps/32 reference-sheet faces retained; all represented solid aggregates have0/0mm³ two-way BRep difference. Maximum bound difference5.6722136321241123e-8mm, computed-volume roundoff9.63851016422268e-6mm³; healthy features/no external links. Actual F3D reopen and staged0→300→600→900→1200→1392 replay preserve exact approved fingerprint,1392 healthy entries,15 parameters and all409 body/sheet instances; corrected R04 BRep difference0/0mm³ and volume drift0. ZIP CRC passes374 entries. No global computeAll claim. [STEP round-trip](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion03_STEP_roundtrip.json), [F3D round-trip](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion03_F3D_roundtrip.json).

The final consumer command `python3 models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion03_check_exports.py` passes: all31 actual STL paths/SHA256, both complete assembly exports, two1800x1100 review PNGs,15 protected source/review files and46 manifest entries verified. No task temporary files remain. Existing physical/process/electrical/thermal limitations and unchanged pilot/reference exceptions remain explicit; no new physical print, fit, strength, slicing/G-code, mesh self-intersection or vertex-link certification.

Observed external session change during approval: prior Fusion02 was closed outside assistant operations; its final unsaved state cannot now be inspected. Fusion03 was externally cloud-saved as version1, lineage `urn:adsk.wipprod:dm.lineage:sYLqRyR6RdiQClGZGsxS7w`, saved/unmodified and read-only, with the exact approved geometry. Initial export protection stopped on the now-invalid closed-document handle before creating export files. Only the known closed-source record was retired from live protection; original jog/K03 protection and all frozen file checks remain. No assistant cloud save/close/discard was performed. Final source is active, unchanged, assembled isometric with original cap visibility/style; empty task STL workspace and STEP/F3D verification copies remain open/modified without inferred close/discard permission. [Final native state](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion03_native_final_state.json).

**Next owner: engineer — use Fusion03 R04 and current BOM; physical printing/process acceptance remains separate.** The old approved revisions remain available and are not silently represented as corrected.


## B24-AC01-LOW-01 inlet lowering requested; drawing published for approval

On 2026-10-23 the engineer requests: **“Przenieś gniazdo zasilania w dół. Tak, żeby było na wysokości kratek wentylacyjnych. Nie dodawaj referencyjnej geometrii gniazda do modelu, żeby uniknąć kolizji. Resztę pozostaw bez zmian.”** Bounded scope: change only the C01 AC01 opening height and omit its two existing flange/inward-proxy reference solids in the new model revision. All other geometry, poses, hardware, fits, grille features and BOM quantities stay unchanged. Omitting reference solids is a CAD representation choice, not evidence of collision-free real installation.

**DRAWING B24-AC01-LOW-01 DRAFT / NOT APPROVED.** [One-sheet dimensioned PDF](../schematics/enclosure/B24-AC01-LOW-01/DJC_Enclosure_Rev_B24_AC01_LOW_01_drawing.pdf), [definition and read-only native measurements](../schematics/enclosure/B24-AC01-LOW-01/DJC_Enclosure_Rev_B24_AC01_LOW_01_definition.json), [executed drawing checks](../schematics/enclosure/B24-AC01-LOW-01/DJC_Enclosure_Rev_B24_AC01_LOW_01_drawing_validation.json), [editable generator](../schematics/enclosure/B24-AC01-LOW-01/DJC_Enclosure_Rev_B24_AC01_LOW_01_drawing.swift), [separate illustrative LLM concept PNG](../schematics/enclosure/B24-AC01-LOW-01/DJC_Enclosure_Rev_B24_AC01_LOW_01_concept.png).

Interpretation submitted for explicit approval: align the **opening centre** with the vertical midpoint of the existing grille's opening envelope, not its bottom/top edges. All48 native six-edge rear-face loops give Z5..30.63435195201938; midpoint Z17.81717597600969 agrees with approved source calculation `5+2*sqrt(3)+1.5*(7.2*sqrt(3)/2)`. Retain X180.775 and nominal sharp rectangular47.5×28 trial opening; no new fit/tolerance/FDM allowance. Move Z48.18838320891088 down30.371207232901188 to17.81717597600969. New edges X157.025..204.525/Z3.81717597600969..31.81717597600969; wall tableY0..2. Restore the old opening to the original wall profile; cut only C01. Remaining wall above floorZ2 is **1.81717597600969mm**; known bezel lower extent Z2.56717597600969 is source arithmetic, not a reference solid or clearance/strength certification.

Actual read-only native inspection: active `DJC Enclosure B24-Fusion-03 DRAFT`, saved/modified, mm,1392 healthy timeline entries/409 body instances; exact approved geometry/pose fingerprint `1ca5736a04de2144e419d2e5115cd0c422568f8e8f11a0f86db40cdc8b779a59`. Nine point-containment probes confirm existing C01 material at the proposed opening; this is not an implemented-cut or interference test. PANEL_R01 and D02L have broad AABB candidates at that region; no collision is inferred from boxes. Explicit resulting BRep/unchanged-body/feature-health checks follow drawing approval.

Actual drawing checks: Swift/CoreGraphics generates, reopens and renders one searchable A3 sheet;10 annotation checks,48 native grille loops, analytic position/retained-size checks and eight protected source hashes pass. PDF and2399×1697 preview opened/reviewed. PDF SHA256 `272c6a8887e9f9eadf17d78817d865e3b7ff75f5fa54e656b6ed4678dcf25763`. Initial LLM concept rejected for an invented central slot; corrected generated WebP opened and truly converted to PNG1536×1024, signature/all114 chunk CRCs pass. Corrected concept SHA256 `403ae571a62940b7ed72b5b4061142fd12d4b77a75c6c6fe13722bddc8bdf7ba`; it is illustrative only, not Fusion or dimensional evidence.

**CHANGES REQUIRED / NEXT OWNER: engineer — approve named drawing B24-AC01-LOW-01 or specify the intended alignment.** Planned native revision `B24-Fusion-04`, existing output directory `models/enclosure/B24/FUSION/`; retain all approved predecessor files and current unsaved Fusion03 changes. No Fusion geometry/camera/visibility/pose change, cloud save, close/discard or STL/STEP/F3D export at this stage. Separate named model approval remains required before exports. Physical inlet/clip/terminal/wiring fit, thin-wall strength, electrical safety and print-process qualification remain unverified; omitted inlet geometry cannot be counted as verified installed-component coverage.


## Engineer approval of drawing B24-AC01-LOW-01

On 2026-10-23, after the dimensioned PDF, corrected illustrative concept, exact centre alignment and remaining1.817176mm wall ligament are presented, the engineer explicitly selects **“Zatwierdzam B24-AC01-LOW-01”**. **DRAWING B24-AC01-LOW-01 APPROVED** for lowering only the C01 AC01 opening centre toZ17.81717597600969, retaining X180.775/nominal47.5×28, restoring its former opening and omitting the two AC01 reference solids. All other geometry/poses/interfaces/quantities stay unchanged.

Freeze the five published drawing-package files; historical DRAFT/pending labels are superseded by this approval, not overwritten. PDF SHA256 `272c6a8887e9f9eadf17d78817d865e3b7ff75f5fa54e656b6ed4678dcf25763`, concept SHA256 `403ae571a62940b7ed72b5b4061142fd12d4b77a75c6c6fe13722bddc8bdf7ba`. This authorizes implementation/validation in separate **B24-Fusion-04**, not advance model approval, STL/STEP/F3D, cloud saving, approved-file overwrite or close/discard. Preserve saved/modified Fusion03 and all other open documents. Actual inlet installation, thin-wall strength, electrical safety and process qualification remain unverified; absent reference solids cannot establish physical clearance.


## B24-Fusion-04 approved inlet-height delta built and checked

Following named B24-AC01-LOW-01 drawing approval, Basia opens the approved Fusion03 F3D as independent **`DJC Enclosure B24-Fusion-04 DRAFT`**, verifies the exact approved baseline, and changes only C01: restore old AC01 opening, cut the unchanged47.5×28 opening centredX180.775/Z17.81717597600969 through wall2, and remove the existing AC01 reference component/two solids with a native Remove feature. [Editable native delta](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion04_inlet.py), [source snapshot](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion04_source_snapshot.json), [executed native validation](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion04_validation.json), actual Fusion [assembled view](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion04_assembled_fusion-view.png) and [rear-inlet detail](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion04_rear-inlet_fusion-view.png). Both1800×1100 PNGs opened/reviewed; assembled isometric restored.

Actual results: restored2660mm³/removed2660mm³, independently constructed expected C01 versus result has0/0mm³ two-way BRep difference,54 old-solid/new-void containment probes pass. All406 other represented body/sheet identities/bounds/poses/topology/solid flags/volumes unchanged, maximum drift0. Current407 body instances=375 solids+32 reference sheets;126 printed body instances/131 printed lumps and15 parameters retained, no meshes/external links. All1397 timeline entries healthy; appended1392→1397 replay preserves final fingerprint **`a2a47627618c7b9abb42ea288765433e0b34f4fe423544d769db256f4fe93653`**. Prior full base-history replay inherited, not rerun or represented as global computeAll.

Changed-added-material interference coverage: restored wall versus all406 other bodies/sheets, including hidden/repeated hardware. One positive-AABB candidate explicitly BRep-intersected; zero positive solid interference above1e-6mm³ (box threshold1e-6mm, numerical comparison only). Removing material cannot introduce new solid interference; unchanged inherited pilot/reference exceptions remain documented, not freshly rerun or declared absent. **The real AC01, clips, terminals and wiring are absent by request; this does not certify their installation clearance.** Existing interior components are visible through the empty aperture. Remaining1.817176mm wall ligament, real connector retention/fit, assembly/service access, process/strength/electrical/thermal qualification remain unverified.

All13 protected drawing/source files and all six original open-document shape-revision/bounds/topology/pose/visibility/save-state snapshots preserved, including the exact source full-geometry fingerprint and its unsaved changes. Initial protection stopped before any document creation because an old verification copy rejected a volume query; protection now uses body revision IDs/bounds/topology for those unrelated copies and still verifies exact original Fusion03 geometry. No exception suppressed or original document repaired/closed. New Fusion04 is active, UNSAVED/MODIFIED; no cloud save, approved-file overwrite, close/discard, task temporary files or Fusion04 STL/STEP/F3D export.

**MODEL B24-Fusion-04 NOT YET APPROVED.** Next owner: engineer — approve this named nominal unpowered prototype revision and authorize corrected C01 STL/mm, full represented-assembly STEP, editable full-history F3D and current BOM in `models/enclosure/B24/FUSION/`, retaining all prior revisions and reusing the other30 unchanged verified STL definitions. No physical/manufacturing release or cloud-save authority follows.


## Engineer approval of model B24-Fusion-04 and revision-matched exports

On 2026-10-23, after the actual Fusion rear-inlet/assembled PNGs, exact C01 delta and unchanged406-body/feature-health evidence are presented, the engineer explicitly selects **“Zatwierdzam B24-Fusion-04”**. **MODEL B24-Fusion-04 APPROVED** for the shown nominal unpowered mechanical-prototype scope: lowered AC01 opening, no AC01 reference solids, all other geometry unchanged. Approved fingerprint `a2a47627618c7b9abb42ea288765433e0b34f4fe423544d769db256f4fe93653`.

The selected option expressly authorizes new C01 STL/mm, complete represented-assembly STEP, editable full-history F3D and current BOM in `models/enclosure/B24/FUSION/`, reusing the other30 unchanged verified STL definitions and preserving all predecessor files. Freeze the inlet delta script, source snapshot, validation JSON and both actual Fusion PNGs; historical pending/DRAFT labels are superseded by this approval. No cloud save, approved-file overwrite, close/discard, physical inlet-installation/retention/strength, print-process or electrical-safety approval is authorized or inferred.


## B24-Fusion-04 lowered inlet and full-assembly exports delivered

**APPROVED / REQUESTED CHANGE AND VERIFIED EXPORT HANDOFF COMPLETE.** Drawing B24-AC01-LOW-01 and model B24-Fusion-04 approvals are recorded above. Only C01 opening height changes; both AC01 reference solids are absent and all406 other represented bodies/sheets retain their shapes/poses. [Current31-definition/131-piece BOM](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion04_BOM_and_exports.json) and [47-file destination manifest](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion04_delivery.json) identify actual files on the verified shared repository/Fusion filesystem.

| New file in `models/enclosure/B24/FUSION/` | Role | Bytes | SHA256 |
|---|---|---:|---|
| `C01_shell_Rev_B24_Fusion04.stl` | Printed C01, qty1, PETG intent, mm coordinates |41000984|`a78cea5c8669b13c2b4a84ccb69a23f9a75cebc2d2ed39196303957db966f7dc`|
| `DJC_Enclosure_Rev_B24_Fusion04_assembly.step` | Complete represented assembly; no AC01 proxy |18163963|`78cab7e1813d899a1abfe252a0f3979674a596f7d3d4176cd07b30a78a443cd7`|
| `DJC_Enclosure_Rev_B24_Fusion04.f3d` | Editable full-history assembly; no current AC01 proxy |14392262|`a7ea4674b1bb9ac15afd540c2e8a7cb6a89da989dc4f1daf9a6d73ffcdd03a0c`|

Other30 approved STL definitions are reused by exact path/hash/unchanged quantity, including the corrected Fusion03 R04 and K03 caps; no redundant remeshing/copy batch. C01 frame retains source axes and translates minimumXYZ to0 (CADY+120mm), no rotation/mirroring/scaling. Actual bounds220×120×78.376770mm agree with native220×120×78.3767664 to3.619531e-6mm. This fits bare250³ but does not establish a usable-bed/support/brim/raft/orientation/layer/calibration release. Material remains PETG intent; no new process selection.

Fresh C01 STL checks:820018 triangles, finite coordinates, zero degenerate/duplicate facets/boundary/nonmanifold/winding-conflict edges, one connected closed positive-volume surface. Actual outer-rear-wall triangles pass9 new-opening void/9 old-opening filled probes and all four new-opening corner checks, maximum corner error6.161435e-6mm under2e-5 numerical threshold. The same checker rejects the old high-opening C01 STL; existing closed-tetrahedron/missing-face fixtures pass. [Mesh evidence](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion04_STL_validation.json).

Actual F3D reopen/full staged0→300→600→900→1200→1397 replay preserves exact approved fingerprint,1397 healthy entries/15 parameters/all407 body identities/bounds/poses/topology/roles and volumes (maximum drift0); C01 two-way BRep difference0/0mm³; no meshes/external links/current AC01 solids. ZIP CRC passes377 entries; no global computeAll claim. Actual STEP reopen matches all407 geometry-bearing component instances/380 closed solid lumps/32 reference sheets; all represented solid aggregates compared in both directions have0mm³ BRep difference. Maximum bound difference5.672214e-8mm/computed-volume roundoff9.638510e-6mm³; trimmed-cylinder fixture passes. [F3D round-trip](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion04_F3D_roundtrip.json), [STEP round-trip](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion04_STEP_roundtrip.json).

Final consumer command `python3 models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion04_check_exports.py` passes:31 actual STL headers/sizes/SHA256, complete STEP/F3D, two1800×1100 actual Fusion PNGs,47 manifest entries and62 protected source/review hashes verified. Long native calls exceeded the MCP response timeout but their completed state/reports were inspected before continuing; no duplicate native mutation/export or timeout configuration change. [Final native state](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion04_native_final_state.json): active approved Fusion04 remains UNSAVED/MODIFIED with assembled rear isometric/unchanged visibility; original saved/modified Fusion03 and all six original documents preserved. Ten documents remain open, including task-owned empty STL workspace and modified verification copies. No cloud save, approved-file overwrite, close/discard or task temporary files.

**Next owner: engineer — use Fusion04 C01/current BOM; physically verify actual inlet installation and1.817176mm lower-wall strength.** The inlet/clip/terminal/wiring geometry is deliberately omitted, so no collision-free real installation is certified. Inherited pilot/reference exceptions, actual service/retention, cap motion/return/load, print process, electrical/thermal and complete jog-integration limits remain. No slicing/G-code, physical print/fit/strength tests or full STL triangle-self-intersection/vertex-link certification. Nominal geometry/export approval is not manufacturing readiness.


## B24-JOINTS-02 four missing bottom connections proposed for approval

On 2026-10-23 the engineer requests two connections at each currently single-connected pair: C01-C04, C03-C06, C01-C02 and C02-C03. Preserve C02-C05, C04-C05 and C05-C06, which already have two. This bounded correction request is not approval of a new named drawing/model or fabrication exports.

**DRAWING B24-JOINTS-02 DRAFT / NOT APPROVED.** [Two-sheet dimensioned PDF](../schematics/enclosure/B24-JOINTS-02/DJC_Enclosure_Rev_B24_JOINTS_02_drawing.pdf), [definition/derivations](../schematics/enclosure/B24-JOINTS-02/DJC_Enclosure_Rev_B24_JOINTS_02_definition.json), [editable generator/self-checks](../schematics/enclosure/B24-JOINTS-02/DJC_Enclosure_Rev_B24_JOINTS_02_drawing.swift), [drawing/PNG checks](../schematics/enclosure/B24-JOINTS-02/DJC_Enclosure_Rev_B24_JOINTS_02_drawing_validation.json), [separate illustrative concept](../schematics/enclosure/B24-JOINTS-02/DJC_Enclosure_Rev_B24_JOINTS_02_concept.png), [inspection-only native source](../schematics/enclosure/B24-JOINTS-02/DJC_Enclosure_Rev_B24_JOINTS_02_native_check.py), [completed native evidence](../schematics/enclosure/B24-JOINTS-02/DJC_Enclosure_Rev_B24_JOINTS_02_native_screening.json).

Proposal under existing printed-joint dimensional delegation: retain ten old joints and exact C07 shape28x10x3/D3.4/pitch18. Add J11 tableXY(170,120), J12(430,120), J13(220,75), J14(380,70). J11/J12 mirror outer-bay joints; J13/J14 lie forward of represented Pi/PSU envelopes, not at rejected Y45. Reference-box bridge gaps2.85/5.25mm are arithmetic, not physical wiring/manufacturing clearance acceptance. Add eight source-type integral D9/Z2..8 pads with blind D2.5x5.5 pilots: C01+2,C02+2,C03+2,C04+1,C05 unchanged,C06+1. C07 quantity10->14; purchased joint ISO4762 M3x8 quantity20->28. No new screw type or printed-hardware substitution.

Read-only native inspection: active `DJC Enclosure B24-Fusion-04 DRAFT`, saved/modified, lineage `urn:adsk.wipprod:dm.lineage:aqH6GLfwQIWoBbNycsFHjQ`, mm,1397 healthy entries/407 bodies and sheets. Only one open document; earlier ten-document/unsaved snapshots are historical. Shared filesystem verified. Twenty proposed temporary bridge/pad/full-nominal-screw BReps versus all407 existing instances, including hidden/repeated hardware and sheets: **8140 pairs /40 positive-AABB candidates explicitly intersected /zero positive solid intersections above1e-6mm3**. Box threshold1e-6mm; these are numerical, not FDM tolerances. Eight driver cylinders D7.332348/Z14..64 screened separately: J11/J12 hit only removable PANEL_R01/R05 and PANEL_R04/R07; J13/J14 no positive hits. Assemble with upper panels removed before equipment/roof blocks access. Hand/tool insertion, connected wiring and real service access remain unverified.

No persistent Fusion geometry/selection/visibility/pose/camera operation. Before/after revision/volume/topology/pose/visibility/save-flag and camera eye/target signature matches `17dd820299a82a9e39a37b1db5c412e817a425afb87be4363112a77cf3231814`. No cloud save/close/discard, approved-file overwrite or STL/STEP/F3D export. Initial long screening exceeded the MCP response timeout; its completed evidence was inspected before proceeding. The final selected-position run returned success. Rejected Y45 trials are not part of this drawing.

Executed local checks: two searchable A3 sheets generated/reopened/rendered and visually reviewed;13 annotation checks; seven adjacency pairs each have two joints; four centres/eight axes match native results; eight pad owners verified. PDF SHA256 `0c690e3eed729cbd3db04a2d6b79cfc68066187a07ea977515d5b8c65eff9dff`. Five registered predecessor hashes preserved, including approved Fusion04 F3D/C07 STL. Returned WebP opened, converted with installed sips to real1536x1024 PNG, final PNG opened;142 chunk CRCs pass, SHA256 `e0e2726b9d0633e37e871ceb37989c6c1bb0c4f102b34e219f289e66cdf1ad51`. Concept is a localized illustrative detail; orange highlighting does not change the selected palette. Task-only temporary files removed; native evidence/checker retained in the drawing package.

**CHANGES REQUIRED / NEXT OWNER: engineer — explicitly approve drawing B24-JOINTS-02 or request a correction.** After approval Basia may implement only eight integral pad regions/four C07/eight nominal screw instances in separate B24-Fusion-05, validate resulting geometry/feature health/unchanged parts, then request named model approval. Current Fusion04 exports still contain ten bridges and are not represented as corrected. No load, printed-thread, actual-installation, calibrated process or electrical/thermal qualification is inferred.


## Engineer approval of drawing B24-JOINTS-02

On 2026-10-23, in direct response to the named B24-JOINTS-02 drawing, four-pair scope, PDF/concept and prospective native checks, the engineer explicitly replies **“Akceptuję”**. **DRAWING B24-JOINTS-02 APPROVED** for J11(170,120), J12(430,120), J13(220,75), J14(380,70), four unchanged C07 bridges/eight integral source-type pads/eight retained ISO4762 M3x8 joint screws. Retain all ten old bridges and every other interface; final14 C07/28 joint screws. C05 geometry remains unchanged.

Freeze the seven drawing-package artifacts below; existing DRAFT/pending labels are historical and superseded by this entry, not overwritten. This authorizes implementation and validation in a separate **B24-Fusion-05**, not advance model approval, STL/STEP/F3D, cloud save, approved-file overwrite or close/discard. Preserve saved/modified Fusion04 and its existing unsaved changes. Physical joint/thread strength, calibrated print process, real connected/service geometry and inherited electrical/thermal limits remain unverified.

| File in `schematics/enclosure/B24-JOINTS-02/` | SHA256 |
|---|---|
| `DJC_Enclosure_Rev_B24_JOINTS_02_drawing.pdf` | `0c690e3eed729cbd3db04a2d6b79cfc68066187a07ea977515d5b8c65eff9dff` |
| `DJC_Enclosure_Rev_B24_JOINTS_02_definition.json` | `1488cd468959536bf8f2fd25393b111c007b28bc9dbf6ebd3669b504ae229b6d` |
| `DJC_Enclosure_Rev_B24_JOINTS_02_drawing.swift` | `11701a9fb1024ce47e29dc56434ab45f1d057fa015399fb93715b3bc1366375d` |
| `DJC_Enclosure_Rev_B24_JOINTS_02_drawing_validation.json` | `e049c1b15dfad59f3fe43f4cb6ce4248ca04a67abc324fe17a3b8cde260c5432` |
| `DJC_Enclosure_Rev_B24_JOINTS_02_concept.png` | `e0e2726b9d0633e37e871ceb37989c6c1bb0c4f102b34e219f289e66cdf1ad51` |
| `DJC_Enclosure_Rev_B24_JOINTS_02_native_check.py` | `2d2c3e6876d7014d44c377c63445d4de1406d904bed28113bbded75408f0ee8f` |
| `DJC_Enclosure_Rev_B24_JOINTS_02_native_screening.json` | `a7c603ae04b2b1618477c745371ca5a27ea552eadf5710eb8cd8ec0193c006d9` |


## B24-Fusion-05 bottom-joint completion built and checked

After explicit B24-JOINTS-02 drawing approval, Basia opens the retained approved Fusion04 F3D as independent **`DJC Enclosure B24-Fusion-05 DRAFT`**, verifies exact baseline fingerprint `a2a47627618c7b9abb42ea288765433e0b34f4fe423544d769db256f4fe93653` against both the live original and archive copy, then appends only the approved joint delta. [Editable staged native implementation](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_joints.py), [initial source snapshot](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_source_snapshot.json), [executed native validation](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_validation.json).

Actual Fusion review PNGs, each2200x1400 and opened/reviewed: [assembled](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_assembled_fusion-view.png), [open lower shell](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_joints-open_fusion-view.png), [complete14-bridge plan](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_joints-top_fusion-view.png). These are direct Fusion captures, not LLM retouches. Temporary visibility restored; final active copy is assembled isometric. Source appearances retained; existing incomplete enclosure/jog/reference representation is not upgraded by this correction.

Implementation: C01/C02/C03 each gain two integral pads; C04/C06 one each; C05 unchanged. Native circle-sketch/join/cut features preserve blind pilots and floor. Four occurrences of the unchanged editable C07 component and eight occurrences of the unchanged nominal ISO4762 M3x8 component added. All ten original bridge centres and20 old joint screws retained; final14 C07/28 joint screws, seven adjacency pairs with two connections each. Existing31 distinct printable definitions remain; five shell meshes require successor exports after model approval, while C07 shape and C05/other definitions may be reused by verified hashes/current quantities.

Exact resulting-shell checks: all five expected-before-plus-approved-pads comparisons have **0/0mm3 two-way BRep difference**. Added volume C01/C02/C03 each709.410891mm3, C04/C06 each354.705446mm3; source cylinder-minus-blind-pilot formula agrees within1e-6mm3.48 containment probes confirm pad material, blind holes, retained pilot bottoms and no extra height. All402 other original body/sheet identities, bounds, poses, topology, solid/lump flags and volumes preserved, maximum volume drift0. Current419 body/sheet instances=387 solids+32 reference sheets;130 printed body instances/135 printed lumps,15 unchanged parameters, no mesh bodies/external links. All1439 timeline entries healthy. Appended1397->1439 replay preserves final fingerprint **`68f6de7a901dbcfa07be4e3c73759cbc054d083b34245206574eb1816551df42`**. Full base-history replay inherited from approved Fusion04, not rerun or represented as global computeAll.

Implemented changed-region interference coverage:20 new pad/bridge/full-nominal-screw solids versus all419 resulting bodies/sheets, excluding each integrated owner/self => **8360 directed pairs /56 positive-AABB candidates explicitly intersected /zero unintended positive solid intersections above1e-6mm3**. Sixteen directed positives are exactly eight intended M3-major-shaft/D2.5-pilot engagements, each nominal10.799225mm3, checked against the analytic annular volume; they are not suppressed collision errors or qualified physical threads.128 annular head-seat probes pass, nominal supported bearing annulus14.6797557mm2 per new head; this is geometric support, not preload/load/printed-strength acceptance. Unchanged inherited overlaps are not rerun or claimed absent. Prior driver-cylinder screening remains applicable; upper panels must be removed and actual hand/tool/wiring/service access remains unqualified.

Six floor-down shell bounds remain identical, at most220x180x78.3767664mm; unchanged C07 local envelope28x10x3mm. Added pads remain within original boxes. All fit nominal250-cubed geometry; usable margins/supports/brim/raft, layer/orientation/calibrated fit and physical strength remain separate. PETG/P2S/nozzle0.4 intent retained, no new process selection.

An initial expected-pad checker used CAD-Y where the retained temporary-cylinder helper already converts table-Y. The48 actual-body location probes and native-volume delta identified a checker-only mirrored expectation. Corrected only the temporary expectation/intersection helper, not model geometry, then exact BRep/interference checks passed. Initial source snapshot retains the initial implementation-script hash as time-specific provenance; final validation protects the corrected executed script hash. All seven frozen drawing artifacts, approved Fusion04 archive/validation and retained helper source hashes preserved.

Source Fusion04 remains saved/modified with its existing unsaved changes; new Fusion05 remains active UNSAVED/MODIFIED, both documents open. No cloud save, approved-file overwrite, close/discard, task temporary files or Fusion05 STL/STEP/F3D export.

**MODEL B24-Fusion-05 NOT YET APPROVED / CHANGES REQUIRED: named engineer model approval.** Next owner: engineer — approve the shown nominal mechanical-prototype revision. Only afterward authorize revision-matched C01/C02/C03/C04/C06 STL/mm, full represented assembly STEP/editable history F3D and updated14-C07 quantities in `models/enclosure/B24/FUSION/`, preserving predecessor files. Existing Fusion04 exports do not contain the added joints. Omitted AC01 installation, actual printed-thread/joint strength, connected/service geometry, print process and inherited physical/electrical/thermal/jog limits remain explicit.


## Engineer approval of model B24-Fusion-05 and revision-matched exports

On 2026-10-23, after the actual Fusion open-shell/14-bridge views, five-shell exact BRep checks, retained402-body inventory and1439-entry health/replay/interference evidence, the engineer explicitly replies **“Wygląda dobrze. Zatwierdzam”** to Basia's named model-and-export question. **MODEL B24-Fusion-05 APPROVED** in the shown nominal mechanical-prototype scope, fingerprint `68f6de7a901dbcfa07be4e3c73759cbc054d083b34245206574eb1816551df42`.

This explicitly authorizes new C01/C02/C03/C04/C06 STL in mm, complete represented assembly STEP, editable full-history F3D and updated31-definition/135-piece BOM in `models/enclosure/B24/FUSION/`; C07 remains the unchanged STL but quantity14. Retain26 unchanged STL definitions and all predecessor files. No cloud save, approved-file overwrite, close/discard or physical thread/joint-strength, usable-bed/calibrated-process, real service/wiring/electrical/thermal qualification is authorized or inferred.

Freeze these six reviewed native artifacts; historical DRAFT/model-pending labels are superseded by this entry, not rewritten.

| File in `models/enclosure/B24/FUSION/` | SHA256 |
|---|---|
| `DJC_Enclosure_Rev_B24_Fusion05_joints.py` | `9a0f46e5eb07f53bc54a2cd0cdb1c4c04e7c66ac1d78fadc7cb66cc6de2adf06` |
| `DJC_Enclosure_Rev_B24_Fusion05_source_snapshot.json` | `79577c20edb794ef03d2641acf70911641a445901407067f0d447bb2019a1763` |
| `DJC_Enclosure_Rev_B24_Fusion05_validation.json` | `8c8763c0427f119f73fb7061c340cf74baaa1c86386e6f1529abfe795974d5ae` |
| `DJC_Enclosure_Rev_B24_Fusion05_assembled_fusion-view.png` | `7b6f40ac0af8179e563f60b813e23e6aa4c9112e17bcf1ddd226724ff4a1cd90` |
| `DJC_Enclosure_Rev_B24_Fusion05_joints-open_fusion-view.png` | `9ec2d12ecac17319d5207a9031877ca7034afd779c3a9849ae98f20c120772ee` |
| `DJC_Enclosure_Rev_B24_Fusion05_joints-top_fusion-view.png` | `22f5500ff15b7ec63220bf67f450f3a4df35f3544874a7bcd8879760649ff1ce` |


## B24-Fusion-05 joint completion and full-assembly exports delivered

**APPROVED / REQUESTED CORRECTION AND VERIFIED EXPORT HANDOFF COMPLETE.** Drawing B24-JOINTS-02 and model B24-Fusion-05 approvals are recorded above. Current [31-definition/135-piece BOM](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_BOM_and_exports.json) and [49-file delivery manifest](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_delivery.json) identify actual files in the verified shared destination `models/enclosure/B24/FUSION/`.

| New STL / mm coordinates / quantity1 each | Triangles | Actual XYZ envelope mm |
|---|---:|---|
| `C01_shell_Rev_B24_Fusion05.stl` |845938|220x120x78.376770|
| `C02_shell_Rev_B24_Fusion05.stl` |389866|160x120x78.376770|
| `C03_shell_Rev_B24_Fusion05.stl` |1024024|220x120x78.376770|
| `C04_shell_Rev_B24_Fusion05.stl` |819230|220x180x18|
| `C06_shell_Rev_B24_Fusion05.stl` |817066|220x180x18|

All26 other approved STL definitions are reused at exact prior paths/hashes, including unchanged C05, corrected Fusion03 R04 and K03 caps. **Print C07 qty14 total**, using unchanged `C07_bridge_Rev_B24_Fusion01.stl`; do not print14 additional bridges. Joint hardware is28 purchased ISO4762 M3x8, not printed screws and not the countersunk panel screw. Eight new pads/pilots are integral to the five new shells, not separate STL parts.

Fresh new-STL evidence:3896124 total triangles, all five finite/closed/single edge-connected/oriented positive-volume surfaces; zero degenerate/duplicate facets, boundary/nonmanifold/winding-conflict edges. Maximum native-bound difference3.619531e-6mm. All eight new D9 pad/D2.5 blind-pilot features pass actual oriented cylinder/annulus/blind-bottom triangle-area checks and25 material/void columns per pad, including bottomZ2.5/topZ8/open mouth/retained floor; prior five no-new-pad STLs are rejected at every new location. Retained lowered C01 inlet void/wall/corner probes pass. Existing closed-tetrahedron/missing-face topology fixtures and chorded-pad/missing-bottom/wrong-radius/wrong-height/reversed-surface/closed-mouth/unchanged-floor geometric fixtures pass. [Mesh evidence](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_STL_validation.json), [executable checker](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_check_meshes.py). Export frame retains source axes and translates minimumXYZ to0 only; no repair/rotation/mirroring/scaling or implied slicing orientation.

Full represented [STEP](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_assembly.step):18220520bytes/SHA256 `e6f1a6b7926d330204ed99ad3a807c5578c9031e165eb4fcfc94a43dee8610b4`. Actual reopen matches all419 geometry-bearing component instances/392 closed solid lumps/32 reference sheets. Every represented solid aggregate has0/0mm3 two-way BRep difference; maximum bound difference5.672214e-8mm and volume roundoff9.638510e-6mm3. Trimmed-cylinder bound fixture passes. [Full STEP round-trip evidence](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_STEP_roundtrip.json).

Editable full-history [F3D](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05.f3d):14337473bytes/SHA256 `11d3a62ef877beed6ca23f76ee603af5f77cf8eea51afe82d70a7e85cb169797`. ZIP374-entry CRC passes. Actual reopen and staged0->300->600->900->1200->1439 replay preserve exact approved fingerprint `68f6de7a901dbcfa07be4e3c73759cbc054d083b34245206574eb1816551df42`, all419 body/sheet identities/bounds/poses/topology/roles,15 parameters,1439 healthy entries and zero volume drift; each changed shell again has0/0mm3 two-way BRep difference. No meshes/external links or missing linked components. [F3D round-trip evidence](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_F3D_roundtrip.json). No global computeAll claim.

The actual consumer command `python3 models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_check_exports.py` verifies all31 STL paths/headers/sizes/SHA256, both assembly exports/F3D CRC, three2200x1400 actual Fusion PNGs,49 manifest entries and92 protected predecessor/source hashes. BOM quantity/replacement self-check and26 retained topology-report bindings pass; repeat mode verifies existing BOM/manifest without overwrite. [Executable consumer](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_check_exports.py), [export source record](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_export_sources.json), [native final state](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_native_final_state.json). No task-controlled temporary files remain.

Observed external session change: Fusion05 was cloud-saved outside assistant operations as version1, lineage `urn:adsk.wipprod:dm.lineage:cO_UsY8kRjqYVSutQHfKww`, saved/unmodified; active document was switched to Fusion04. Initial export guard stopped before output creation. Exact approved inactive Fusion05 geometry and original Fusion04 protection passed before reactivation and export setup. Final active source is saved/unmodified/assembled isometric with original visibility; original Fusion04 stays saved/modified. Five documents remain open: both originals, empty task STL workspace and two modified verification copies. No assistant cloud save, approved-file overwrite, close/discard or permission/configuration change. Long STEP import/matching, archive verification and one comparison batch exceeded MCP response deadlines; completed native state/reports were inspected before continuing, never duplicate import/export/replay.

**Next owner: engineer — use Fusion05 BOM/new five shells and C07 qty14 for slicing and physical assembly tests.** Enclosure PETG/P2S/nozzle0.4 intent retained; floor-down nominal boxes and C07 broad-face orientation fit bare250-cubed geometry only. Usable margins/supports/brim/raft/layers/calibrated fits and physical printed-thread/joint/head-bearing strength remain unqualified. Eight intended pilot engagements and inherited reference exceptions remain explicit. Omitted AC01 clip/terminal/wiring installation, real service access, low-profile-jog integration and physical/electrical/thermal limits remain. No G-code/physical print/strength tests or full STL triangle-self-intersection/vertex-link certification; approved geometry/exports are not manufacturing readiness.


## Post-delivery live-document observation — exports unchanged

The final document query after the successful repeat consumer verification shows a subsequent external session change: only saved/unmodified Fusion05 and saved/modified `Jog Wheel F12-D05 Fusion01 RECOVERED WIP002 — NOT APPROVED` are now open; the jog is active. Fusion04, empty STL workspace and both verification copies were closed outside assistant operations. Their final unsaved-change disposition cannot now be inspected and is not inferred. Basia did not close/discard/save documents or reactivate Fusion05 over the engineer's active jog work. The earlier native-final-state file remains a frozen export-time snapshot, not the latest live-document list. All verified49 export/review files and92 protected hashes remain unchanged; no export or geometric approval is reopened.


## Engineer confirmation of controller control population

On 2026-10-25 the engineer states the complete-controller population, based on the accepted 3D model: **30 buttons, 5 faders, 1 BROWSE encoder, 2 jog-wheel encoders, 13 potentiometers and 2 × 10 VU-meter LEDs**, and requests synchronization of the design. The current approved enclosure baseline remains **B24-Fusion-05**; this is a specification/count confirmation, not a new drawing/model revision or an additional physical approval.

The [current model BOM](../models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_BOM_and_exports.json) corroborates 30 panel caps as12 CAP_B +6 CAP_T +2 CUE +2 PLAY/PAUSE +8 HOT CUE, five fader caps as4 CAP_F +1 CAP_C,13 CAP_P and1 CAP_E. The retained R12 panel schedule confirms24 B +6 T,5 F,1 E,2 J,13 P and20 L records in two10-window columns; its positions are historical, not current B24 coordinates. [DESIGN section 3](../DESIGN.md#3-controls-and-supplied-mechanical-inputs) records the synchronized population and interface limits.

Existing BROWSE push and two jog mode contacts remain additional to the30 panel buttons:33 press inputs total, versus32 ports on the two selected PCF8575s. The one-input allocation remains deferred to electronics connection. The18 analog controls,3 rotary channels and two master-only LED chains do not establish a complete GPIO map, electrical validation or power budget.

Scope: documentation only. No change to geometry, dimensions, materials, approved drawing/model files or exports; no new save/overwrite/export authority. The read-only open-document query found saved/unmodified `DJC Enclosure B24-Fusion-05 DRAFT` and the engineer's active saved/modified F12-D05 jog document. Neither document was activated, changed, saved or closed by Basia.


## Engineer removal of BROWSE push function

On2026-10-25, after reviewing the33-contact breakdown, the engineer explicitly requests: **“Wycofajmy przycisk z browse enkodera. Nie ma sensu go robić.”** BROWSE E01 remains an incremental A/B rotary control; its push function is removed. Leave the selected encoder's push-switch contacts unconnected, allocate no press input/GPIO to them and define no MIDI push action. This does not select a replacement encoder, lock out physical axial movement or authorize a mechanical modification.

The current requirement is **30 panel buttons +2 jog mode switches =32 press inputs**, matching the32 ports on two PCF8575s with no spare press port. This supersedes the earlier33-input/32-port shortfall and BROWSE-push requirement, including the preceding population entry; retain earlier decisions and frozen source/model records as history. The remaining18 analog controls,3 rotary channels and20 master-VU LEDs/two data lines are unchanged. Final per-port/GPIO mapping, electrical interfaces, USB/power safety and physical validation remain required.

Synchronized current requirements: [DESIGN](../DESIGN.md#3-controls-and-supplied-mechanical-inputs), [electronics/firmware queue](../TODO.md#electronics-and-firmware--before-their-corresponding-build-gates) and [session restart baseline](history/SESSION-HANDOFF.md#2-product-and-approved-baseline). Scope is functional specification only: approved B24-Fusion-05 geometry/dimensions, selected encoder/cap, drawing packages and STL/STEP/F3D files remain unchanged. No wiring schematic, PCB or firmware implementation is created by this decision, and no save/overwrite/export authority is added. A read-only document query found0 open Fusion documents; Basia did not open, close, save or mutate a document.


## Electrical E01 schematic request and draft publication

On2026-10-25, after discussing direct GPIO versus an analog-mux connection for BROWSE, the engineer explicitly replies **“Ok. Zostawmy jak jest. Zrób schemat ideowy połączeń.”** This retains direct BROWSE A/B with the previously removed push function and authorizes an electrical schematic, not a PCB, firmware implementation or mechanical change. It does not approve the new GPIO/port assignments, SPI interface proposal, addresses, component values or power design.

Published [Electrical E01 PDF](../schematics/electronics/E01/DJC_Electrical_Rev_E01_schematic.pdf): eight A3 sheets, SHA256 `ef42320a0e33ded7ac9a56bb78db120cb82730c6c6724342281d09fc8b97328b`; [editable connection definition](../schematics/electronics/E01/DJC_Electrical_Rev_E01_definition.json), [Swift generator](../schematics/electronics/E01/DJC_Electrical_Rev_E01_drawing.swift) and [actual validation/limits](../schematics/electronics/E01/DJC_Electrical_Rev_E01_validation.json). **E01 DRAFT / CHANGES REQUIRED / NOT APPROVED FOR WIRING OR ENERGIZING.** Named actual-module and power gates E01-TBD-01…08 remain unresolved; no approval is requested while those design-critical inputs are open.

Proposed GPIO map preserves the earlier fader/mux/I2C/INT candidates, adds shared full SPI15/16/17 with CS18/21, direct BROWSE39/40 and VU data41/42; GPIO47/48 remain unassigned under the stated DevKitC-1 v1.1/memory/boot reservations. PCF0x20/0x21 and32 port-to-contact choices are proposals. BROWSE D/E push contacts stay unused; CH13–CH15 are spare analog mux channels; both PCF8575s have no spare press port.

Executed: native PDF generation, actual eight-page reopen/A3 checks/render and all-sheet visual review; structural GPIO/header/ADC/contact/address/VU checks plus six rejected invalid-definition fixtures. Corrected analog-label spacing, BROWSE contact labeling and the U5 supply-net label before final review. Eight supplied/reference/CAD files match protected source hashes, including the approved B24-Fusion-05 F3D/STEP. Temporary task-owned drafts and raster previews were removed. No native EDA ERC/DRC, simulation, physical wiring, power-up or electrical test was performed.

During schematic preparation, the read-only Fusion query found zero open documents; this is a time-specific observation, not an inferred disposition of earlier unsaved work. No assistant document open/close/save, Fusion geometry change, approved-file overwrite or STL/STEP/F3D export. Next owner: engineer for actual module/terminal identification and power requirements; Basia can then resolve affected schematic gates before named electrical approval and staged prototype testing.


## Electrical E01-P01 real-board pictorial request and delivery

On2026-10-25 the engineer clarifies that the requested aggregate connection diagram should be an attractive PDF using **real ESP32, PCF8575 and74HC4067 board drawings**, not the preceding Mermaid/block overview. This authorizes a presentation companion, not revised electrical decisions, assumed purchased-board identity or wiring/power release.

Delivered [E01-P01 pictorial PDF](../schematics/electronics/E01-P01/DJC_Electrical_Rev_E01_P01_pictorial.pdf), one A2 landscape sheet, SHA256 `3bbe4b48c72ecdd4794deba43c9f931bc1607202610d0646e771499559235976`, with [editable native generator, original image inputs, provenance and validation](../schematics/electronics/E01-P01/). The official Espressif DevKitC-1 v1.1 drawing and genuine Make Electronics/Envistia module photographs are cropped/rotated, not AI-generated or re-labeled. PCF/mux photographs are explicitly reference modules; the actual purchased variants remain unidentified. No component dimensions are derived from pixels.

The drawing preserves all22 E01 external GPIO signal nets, the direct non-push BROWSE, both PCF address proposals and32-contact allocation, five direct faders, shared jog SPI and two VU data outputs. Each of the13 pot wipers has its own line to CH0–CH12; grouped PCF port buses denote16 separate contacts each, not shorts. Power/GND/EN/OE and supporting passive networks are omitted from this signal overview, not waived. In particular, VCC/VDD on the reference PCF board are not assumed equivalent through its unverified regulator topology.

Executed: actual one-page native PDF generation/reopen/A2 bounds/render, final visual inspection, exact22-net coverage, image-rotation self-check, three source-image hashes and seven protected E01/CAD hashes. Final image heading/lead separation and independent pot leads reviewed; task-owned draft PDFs/raster previews removed. Original E01 four-file package and approved B24-Fusion-05 sources/exports remain unchanged. Read-only Fusion query found zero open documents; no assistant activation/save/close, geometry mutation, PCB work, ERC, simulation, power-up or physical test.

**E01-P01 DRAFT / REFERENCE-BOARD SIGNAL OVERVIEW / CHANGES REQUIRED FOR WIRING OR ENERGIZING.** Neither this presentation request nor image similarity approves E01 GPIO/port choices or closes its eight actual-module/power gates. Next owner: engineer for actual-module confirmation before a physical wiring drawing or electrical release.


## B25-ELEC-01 bottom controller placement request

On2026-10-25 the engineer says, “Ok. Teraz rozmieść to na spodzie naszej obudowy”, following the E01-P01 pictorial signal overview. Basia treats this as a request to position the four controller modules on the inside floor of the existing B24 enclosure, not to move accepted controls/jogs/Pi/DAC/PSU or approve unseen mounting geometry, electrical wiring, cloud saving or fabrication exports.

Prepared [B25-ELEC-01 placement PDF](../schematics/enclosure/B25-ELEC-01/DJC_Enclosure_Rev_B25_ELEC_01_drawing.pdf), one A2 sheet SHA256 `b093e10262746bbdb5634d4a5c449697e996df3542417db9b62dcb9e2cd13c7a`, [editable source/evidence](../schematics/enclosure/B25-ELEC-01/) and [separate illustrative concept PNG](../schematics/enclosure/B25-ELEC-01/DJC_Enclosure_Rev_B25_ELEC_01_concept.png). Existing engineer-confirmed ESP/PCF dimensions and heights remain closed; no renewed blanket supplier/measurement inventory. The module photographs in E01-P01 are not used as mechanical measurements.

Proposed centres in mm, rear-left exterior datum: ESP(300,225), U2PCF(181,165), U3PCF(419,150), mux(410,180), long edges parallelX. Only U3 changesXY, from(181,195), to distribute the expanders left/right without changing E01 contact identities. Proposed ESP/PCF undersideZ4 and full stated normal envelopeZ3..14 give1 above floor/4 below panel; this is a selected new-mount packaging datum under retained dimensional delegation, not completed supports. Mux retains supplied body-only41×18×3.6/Z8..11.6: pins excluded and full installed fit not claimed. No purchased holes, contact lands, pins or printed retention geometry invented.

Executed: native PDF generation/reopen/A2 bounds/render/final visual review;1636 recorded native-body AABB,392 control-group,164 closure/new-joint-post and six board-pair checks clear at1e-6mm threshold. All419 inventory records accounted for: six nonlocal whole-shell AABBs and four replaced module references are explicit exclusions;409 other records checked per module. Integral control/post proxies supplement, but do not replace native shell BRep analysis. Minimum retained-control clearance1.85mm atESP; minimum module-body pair gap10.5mm. No continuous-motion, retention/insertion, antenna, actual mux pins, thermal, physical or electrical validation. Nine protected source/CAD/electrical hashes unchanged.

Actual image model returned1536×1024 WebP; converted to PNG and both opened. It depicts four simplified board envelopes, not exact purchased geometry or a Fusion view. Task-owned PDF previews removed. Live read-only Fusion document query found zero open documents; no assistant document activation/close/save, geometry mutation, approved-file overwrite or STL/STEP/F3D export.

**B25-ELEC-01 DRAFT PLACEMENT / CHANGES REQUIRED BEFORE MOUNT MODELING.** No named drawing/model approval recorded. Next owner: engineer for acceptance/correction of the proposed positions, U4 installed pin projections/full height and trustworthy clear support/retention contact zones on the actual boards; Basia then prepares a reconstructible mounting revision for named drawing approval. Existing engineer-owned, geometry-neutral cables and deferred LED/diffuser/buffer implementation remain outside this step.


## Engineer acceptance of B25-ELEC-01 board placement

The engineer replies **“Akceptuję schemat”** (“I accept the diagram”) immediately after Basia asks whether the board positions in **B25-ELEC-01** are accepted and explicitly distinguishes placement acceptance from completed mounting approval. This records **APPROVED — PLACEMENT ONLY**, not electrical E01/E01-P01 wiring approval, a model-ready mounting drawing or a Fusion model approval.

Accepted scope: the four module envelopes and placement datums shown in [B25-ELEC-01 PDF](../schematics/enclosure/B25-ELEC-01/DJC_Enclosure_Rev_B25_ELEC_01_drawing.pdf), rear-left exterior origin/mm/CAD=(X,-Y,Z), long board edges parallelX: U1ESP(300,225), U2PCF(181,165), U3PCF(419,150), U4mux(410,180). U1/U2/U3 PCB undersideZ4 and the stated installed envelopeZ3..14 are accepted packaging datums, not completed supports. U4Z8..11.6 remains a body-only datum, not acceptance of unknown installed pins. Existing controls/jogs/Pi/DAC/PSU and E01 signal identities remain unchanged.

Preserve all five package files byte-for-byte, including original DRAFT/pending labels as publication-time records; this later entry governs the scoped acceptance:

| File under `schematics/enclosure/B25-ELEC-01/` | SHA256 |
|---|---|
| `DJC_Enclosure_Rev_B25_ELEC_01_drawing.pdf` | `b093e10262746bbdb5634d4a5c449697e996df3542417db9b62dcb9e2cd13c7a` |
| `DJC_Enclosure_Rev_B25_ELEC_01_definition.json` | `e764911c117540c058ba755544feb9541f812615478ce69eb001812283f116c8` |
| `DJC_Enclosure_Rev_B25_ELEC_01_drawing.swift` | `cf8a1f272594dd757803163176413333ce678e83e44c03faa7ccd59df7eccfca` |
| `DJC_Enclosure_Rev_B25_ELEC_01_validation.json` | `0c3e49df2efbbc9657725cef7f773491d8650157187779c53608224f5e425295` |
| `DJC_Enclosure_Rev_B25_ELEC_01_concept.png` | `0017e8c709eadc03f55b745879007f4348ebb8edc49a19f510fb434e7c9d70af` |

Remaining prerequisites: trustworthy clear support/retention contacts on the actual four boards and U4 installed pin projections/full height. No new purchased geometry, retention dimensions, tolerance, print-setting or electrical-safety decision follows from acceptance. Basia prepares a separate model-ready mounting revision once those inputs are available; named drawing approval and subsequent model validation/approval remain required. Do not request acceptance of these unchanged positions again.

Acceptance recording changes documentation only. Five accepted package hashes and nine protected B24/electrical input hashes checked unchanged. No new geometry, Fusion activation/save/close, fabrication export, physical test or repeated collision analysis; B24-Fusion-05 remains the approved mechanical master.


## Mux header projections confirmed equal to PCF8575

After the placement acceptance record identifies missing mux installed pin heights, the engineer replies **“Tyle samo co PCF”** (“The same as PCF”). This supplies the CD74HC4067 header projections using the already confirmed PCF face datums: **8mm above the upper PCB face and1mm below the lower PCB face**. These pin dimensions are now closed; do not ask for them again.

Scope is the requested pin projections, not an instruction to copy PCF's2mm laminate, component arrangement, clean contact zones or11mm complete installed height. The retained mux body41×18×3.6mm still explicitly excludes pins. Register PCB faces within that body and derive/check the full installed envelope in the next model-ready mounting revision; neither a guessed11mm total nor treating3.6+8+1 as an exact total is justified by this input.

Remaining actual-board mounting input: trustworthy clear support/retention contact zones. The five accepted B25-ELEC-01 files, their body-only mux datum/coverage and named placement acceptance remain unchanged. This input does not select new retention geometry, approve a new drawing/model, waive electrical gates or authorize a save/export. B24-Fusion-05 remains the approved mechanical master. Documentation updated only; no new CAD/collision/physical check claimed.


## B25-MOUNT-01 holder-location design request and floor-anchor proposal

Following confirmation of mux header projections, the engineer asks **“Zaprojektuj miejsca na uchwyty”** (“Design locations for the holders”). This is a new design request within the retained delegation for PRINTED mount positions/dimensions, not approval of unseen geometry or permission to invent purchased-board contacts. Basia preserves accepted B25-ELEC-01 module positions/Z and all five frozen files.

Prepared [B25-MOUNT-01 two-sheet A3 PDF](../schematics/enclosure/B25-MOUNT-01/DJC_Enclosure_Rev_B25_MOUNT_01_drawing.pdf), SHA256 `405db2bd9238f7f5dc002cbd36792621cb5536f8b9cc0e7feae72d1265472518`, [editable definition/generator/evidence](../schematics/enclosure/B25-MOUNT-01/) and [separate illustrative anchor-detail PNG](../schematics/enclosure/B25-MOUNT-01/DJC_Enclosure_Rev_B25_MOUNT_01_concept.png). Eight floor-anchor features and their mating attachment interface are dimensioned. This is the reachable floor-attachment design, NOT a substitution for the still-unresolved complete PCB support/clamping interface or four completed holders.

Selected new printed anchors: for each board, centreX retained and axes5 beyond its two Y edges. IntegralD7/Z2..6 with straight coaxial blindpilotD2/Z1..6 leaves1 floor skin. Native B22 Pi support supplies that floor-feature pattern; legacy B02 PCB-carrier code supplies only outboard5/D7 ear intent and explicitly does not qualify its old contact pads/heights. New mating land minimumD7/thickness2/Z6..8/D2.9 through,8 additional purchased nominal CHC M2.5x6/maxheadD4.5/H2.5. Nominal engagement4, tipZ2/reserve1; selected straightD8 access reserveZ6..18 with upper panels removed. Interface fragments are not PCB pads or complete carriers. C04 gains2/C05 gains2/C06 gains4 integral anchors; no extra loose anchor prints, purchased PCB holes, snap fit, nut/insert, countersink, new tolerance or accepted equipment move.

Two read-only helpers investigated actual-board contact sources and independent floor-anchor constraints; neither edited files or accessed/mutated Fusion. Basia inspected the cited legacy/native patterns, owns the selected geometry, ran final checks and inspected artifacts. Available ESP manufacturer drawing/pin data, PCF supplier dimensions and supplied mux body/header inputs do not numerically establish clean actual PCB contact lands; catalogue photo pixels and old provisional tray contacts are not used as substitute dimensions. This unresolved interface is retained as a blocker before complete mounting approval/modeling, not silently assumed safe.

Executed parent evidence:8 anchors/32 zones;13024 recorded-body AABB +3136 control-group +128 accepted-board reference +1952 floor-closure/joint plan-proxy +448 inter-anchor comparisons,18688 total, clear at1e-6mm threshold. Minimum inter-anchor-zone AABB gap1, minimum recorded-body gap2.419 body/sheet records,98 control groups,33 floor closure axes and28 joint axes accounted for. Explicit exclusions: six nonlocal whole-shell AABBs, four replaced module reference boxes; eight removable upper-cover AABBs additionally removed only for access. Actual shell BRep, unknown mux pins, complete mechanisms/motion, contacts/retention, physical printed threads/strength/preload/torque and hand/tool service are NOT certified. Shaft/pilot engagement within each selected fastener interface is intentional, not an unintended clash.

Actual native PDF generated/reopened/A3-bounds-checked/rendered and both final sheets visually inspected. Image model returned1536×1024 WebP; converted to PNG, original/final opened and nonblank native RGB decode checked. Single-anchor concept is illustrative, not a Fusion view, complete carrier or dimensional evidence. Sixteen protected source/CAD/accepted/electrical hashes unchanged; task-owned previews/inspection code removed. Read-only live Fusion document query found zero open documents; no assistant document open/activate/close/save, model mutation or STL/STEP/F3D export.

**B25-MOUNT-01 DRAFT FLOOR-ANCHOR LOCATIONS / CHANGES REQUIRED FOR COMPLETE PCB HOLDERS / NO MODEL RELEASE.** No named drawing/model approval inferred. Engineer may review the proposed floor-anchor locations; to finish actual PCB-bearing supports Basia still needs trustworthy dimensioned pin/contact geometry or specifically located clear contact surfaces and extents on the actual boards. No renewed blanket component inventory or re-request of closed outline/PCF-equivalent header dimensions. A complete mounting revision then returns for named drawing approval before Fusion/model validation and separate model approval/export.


## Engineer rejects B25-MOUNT-01 and requires original PCB screw holes

The engineer reports: **“Przy takim ustawieniu, uchwyty będą nachodziły na goldpiny. Każda z tych płytek ma otwory na śruby. Wykorzystaj je.”** (“In this arrangement the holders will overlap the pin headers. Each board has screw holes. Use them.”) This is accepted ground truth. Basia withdraws **B25-MOUNT-01 — REJECTED / DO NOT IMPLEMENT**; no rerun of old clearance checks is used to confirm or dispute the reported interference.

Governing replacement approach: support each actual board coaxially at its ORIGINAL mounting holes, fastening through those holes. No edge clamps, unverified contact strips or arbitrary outboard carrier anchors. Hole presence is now confirmed for all four modules; hole count/pattern/diameters are not inferred. Do not carry over the old eight axes, D7/ear dimensions, eight-screw quantity or M2.5x6 selection. Support/fastener/head/land geometry and installation clearances follow the actual PCB hole data in a new named drawing. Accepted B25-ELEC-01 module positions and existing B24/control/equipment geometry remain unchanged; any required positional correction returns for approval.

Targeted source review: [official ESP dimension PDF](https://dl.espressif.com/dl/schematics/esp_idf/DXF_ESP32-S3-DevKitC-1_V1.1_20220429.pdf) discovered through the official guide and actually opened/rendered; outline/header dimensions do not define the engineer's mounting-hole pattern. [Retained PCF supplier](https://sklep.msalamon.pl/produkt/pcf8575-ekspander-portow-i-o-16-kanalow/) provides32×21 and board photographs, but no dimensioned hole axes/diameters. Supplied mux dimensions and local project references also lack that numeric pattern. No dimensions derived from pixels, no unconfirmed variant transferred and no contradiction of the engineer's confirmed hole presence.

Exact remaining inputs for the corrected drawing: actual hole diameters and all centre coordinates relative to one PCB-edge datum for ESP32, PCF8575 and74HC4067 (one pattern for both PCFs only if identical); a dimensioned drawing of those actual versions or engineer measurements suffices. ESP/PCF laminate2 and header projections stay closed. U4 laminate thickness/PCB registration within the3.6 body remains open; equal header projections do not supply those values. No renewed blanket parts/photo inventory, new mains decisions or unknown purchased-hole assumptions.

Preserve all five B25-ELEC-01 files and all five rejected B25-MOUNT-01 artifacts as history, including their original labels/evidence. The old limited envelope comparisons excluded the missing real pin/holder interface and are not mounting validation; rejection supersedes any implication of suitability. Documentation/navigation/task state corrected; no new incomplete drawing, CAD geometry, Fusion activation/save/close, file overwrite or fabrication export. Temporary source-inspection PDF/raster/script removed after review. Next owner: engineer for the precise missing hole/laminate data; Basia then produces the corrected hole-based mounting drawing and validation for named approval.


## B25-ELEC-02 rotated outer-board layout and electrical circuits

The engineer directs: **“Dobra. Na ten moment nie rób mocowań. Płytkę U1 obróć o 90 stopni i umieść na lewo od Joga A. Płytkę U4 obróć o 90 i umieść na prawo od Joga B. Następnie rysunek uzupełnij obwodami elektrycznymi.”** Mounting is now explicitly DEFERRED; no hole measurements are requested for this task. Original PCB screw holes remain the intended future method; rejected B25-MOUNT-01 is not reinstated. This is a change request, not named drawing/model approval.

New [B25-ELEC-02 combined PDF](../schematics/enclosure/B25-ELEC-02/DJC_Enclosure_Rev_B25_ELEC_02_layout_and_circuits.pdf), [editable definition/generator and validation](../schematics/enclosure/B25-ELEC-02/) and [separate illustrative concept PNG](../schematics/enclosure/B25-ELEC-02/DJC_Enclosure_Rev_B25_ELEC_02_concept.png). Both boards rotate90° clockwise in the top/table view. Unitsmm, rear-left table origin: U1 centre(28.75,150), plan25.4×62.74; U4 centre(571.25,150), plan18×41. U2(181,165), U3(419,150) and all other equipment remain fixed. Accepted B25-ELEC-01/five frozen files and approved B24-Fusion-05 are preserved byte-identically.

Position derivations use retained closure/joint geometry: U1X=(12.5+45)/2=28.75 leaves3.55 nominal side reserves between the closure foot and J07 bridge. The initial U4 trialX563.75 would overlap J10's bridge box by0.25 inX and was not delivered; actual J10 right edge555 to right closure-foot edge587.5 gives U4X571.25 and7.25 nominal side reserves. U1's reference installedZ3..14 is retained; U4Z8..11.6 is BODY ONLY. Confirmed mux headers8 above upper PCB face/1 below lower face do not establish its laminate registration or complete installed height. U1 crosses Y120 seam in projection; no purchased board is cut and mounting/assembly access is not thereby qualified.

PDF delivery: one new A2 placement/topology sheet with reused reference-board imagery and functional connection bundles, followed by all eight original A3 E01 circuit sheets unchanged. Final PDF SHA256 `c8bbbb102306fa04b46b19bca24b1d1c9b5a4e9fa3023a1a1b00bdcddfcb7455`. Native generation, reopen, rasterization and layout review completed; all eight appended sheets preserve source rendered pixels, text, links and bounds.22 GPIO signal nets,32 press contacts,13 mux pot channels/three spare channels and five direct faders retain E01 assignments. BROWSE has no push contact. The AHCT125/VU card shows electrical function, not a newly mounted buffer board. E01-TBD-01…08 remain open; no wiring, power-up or PCB-layout approval is implied.

Screening coverage:419 source body records, excluding six nonlocal whole-shell AABBs/four replaced controller references;4×409=1636 recorded body pairs,4×98=392 control-group envelopes,4×61=244 closure/joint plan proxies and six board pairs,2278 comparisons total at1e-6mm. No tested intersections; this is not native shell BRep, complete mux-pin, real harness or physical-fit validation.27 protected source/CAD/accepted/rejected/electrical files unchanged. Actual generated concept WebP opened, converted to1536×1024 PNG and reopened; illustrative only, not Fusion evidence. Task-owned raw PDF/previews removed after review.

Zero new holders, PCB/floor holes, posts or fasteners. Read-only live query found zero open Fusion documents at this task's observation; no geometry, camera, save/close or fabrication export operation. **B25-ELEC-02: DRAFT / REVIEW REQUIRED / MOUNTING DEFERRED.** Next owner: engineer reviews the named revised drawing; Basia may change Fusion only after that gate. Existing model/export approvals do not cover these proposed board moves or an electrical installation.


## Engineer approval of drawing B25-ELEC-02

The engineer replies **“Akceptuję. Co dalej?”** immediately after delivery of the named **B25-ELEC-02** PDF and its stated limits. Record **APPROVED — DRAWING / BOARD PLACEMENT AND CONNECTION TOPOLOGY ONLY; MOUNTING DEFERRED**. This closes the drawing-review gate for the specified board positions/orientations and the combined presentation of unchanged E01 circuits. It does not approve a new Fusion model, mounts, actual module pinouts, physical wiring, energizing or PCB fabrication; E01-TBD-01…08 remain unresolved. No function or GPIO assignment changes.

Approved placement, mm/rear-left table origin: U1(28.75,150), U4(571.25,150), both90° clockwise; U2(181,165)/U3(419,150) unchanged from the preceding placement drawing. Retain all supplied dimensions and the explicit U4 BODY-ONLY height limitation. Original-hole mounting remains deferred; do not request hole data or implement rejected B25-MOUNT-01.

Freeze all five files in [B25-ELEC-02](../schematics/enclosure/B25-ELEC-02/), including their historical DRAFT/pending/false-approval fields. This later approval record governs the effective scoped status; do not regenerate or relabel the approved payload:

| File | SHA256 |
|---|---|
| `DJC_Enclosure_Rev_B25_ELEC_02_layout_and_circuits.pdf` | `c8bbbb102306fa04b46b19bca24b1d1c9b5a4e9fa3023a1a1b00bdcddfcb7455` |
| `DJC_Enclosure_Rev_B25_ELEC_02_definition.json` | `263a9abed777caa24dd7e4ba00fe1cc8fbf36f954ef19fa3cf31751a11c188d6` |
| `DJC_Enclosure_Rev_B25_ELEC_02_drawing.swift` | `0484c76a585cc3fd214d445a3059af51890952e8a30fef4f20c69f0cf617da66` |
| `DJC_Enclosure_Rev_B25_ELEC_02_validation.json` | `cfe502fe9894c9068ebafc4ec49a7838f48fa0cd12b17dc80c18e3895a3a7175` |
| `DJC_Enclosure_Rev_B25_ELEC_02_concept.png` | `e9b486b55e2a1b6c5f61d93a6b8de41df88e8717a34f96ee9337b79c5d7cdc6c` |

Next owner: Basia for a separately started CAD placement update in a new working revision derived from approved B24-Fusion-05. Inspect the live document/save state before that work; preserve unrelated unsaved work and never infer permission to cloud-save/overwrite. Synchronize all four controller references to this approved drawing; do not assume the earlier B25 placements were already implemented in B24. Reuse known reference geometry, with U4's full installed envelope explicitly unqualified. No new supports, holes, fasteners or invented purchased geometry. Check known-body interference, transforms and feature health; obtain actual Fusion review PNGs and submit the named model revision for engineer approval. This “what next” response itself starts no Fusion operation and authorizes no fabrication exports.


## Direct-input ESP32-S3 serial bench firmware request

The engineer requests code for one directly connected fader, potentiometer, button and printed jog with its encoder, plus an explanation of compilation/upload. In the grouped tool questions, the engineer selects **“Odczyty w monitorze szeregowym”** and **“Tak, zainstaluj pakiet ESP32”**. This authorizes a standalone serial diagnostic and installation of the official Espressif Arduino board package/toolchain using the existing Arduino IDE/CLI. It does not authorize uploading over existing board firmware, changing OMP configuration, or adopting MIDI, a fixed/touch jog, CAD/mounting changes, mains or combined-power wiring.

Source and instructions: [firmware/bench_inputs](../firmware/bench_inputs/README.md). Arduino C++/Espressif3.3.12; temporary direct inputs GPIO1/7/4 and AS5048A SCK15/MOSI16/MISO17/CSn18. The full-controller E01 assignments and approvals remain untouched. GPIO4 is a bench-only button, not an approved permanent reassignment. Firmware checks the IC-level SPI protocol; the retained100x100 image does not establish the actual breakout header or supply topology. Confirm actual board/memory variant, sensor3.3V configuration and physical terminals before wiring/upload. No source/physical pin order is inferred from pixels. Existing jog mechanism and the decision to defer proposed mechanical changes remain unchanged.

Verification for this bench delivery: host C++ regressions and actual-sketch simulated-I/O smoke passed; real Espressif3.3.12 cross-build produced ESP32-S3 ELF/application images, and esptool5.3.1 verified chipID9 plus valid checksum/image hash for319968 application bytes. Generic image4MB/DIO/80MHz is a reference configuration, not detected actual-board settings. Compiled helper source matched after Arduino's generated line directive.27 prior protected files plus five approved B25-ELEC-02 artifacts stayed unchanged. Task-owned adapters/executables/build outputs removed. Firmware source/instructions delivered; FW-BENCH-01 physical execution remains open. No automatic flash/port connection, powered sensor test, CAD change or electrical-installation approval.


## Engineer approval of model B24-build123d01 for prototype export

After review of the named build123d revision, its assembled and fader-extreme viewer images, the pre-export review, and the explicitly stated unresolved geometry and physical limitations, the engineer selected **“Zatwierdzam B24-build123d01”** for STL and STEP export. **APPROVED — NOMINAL, UNPOWERED MECHANICAL PROTOTYPE MODEL AND ITS STATED EXPORT REPRESENTATIONS ONLY.**

The approved source snapshot and dependencies are recorded in `models/enclosure/B24/BUILD123D/DJC_Enclosure_Rev_B24_build123d01_validation.md`; the supplemental pre-export review records the volume-preserving working-copy C01–C03 topology cleanup, 0.005 mm absolute / 5° BRep STL tessellation, 1 mm local-frame offset, retained original cap meshes, and faceted cap BReps in STEP. The incomplete purchased/reference geometry, unresolved D02L exact-equivalence result, limited sampled-motion and nominal seat checks, omitted jog-ear seats and AC01 installation, and unspecified cap material and slicing parameters remain limitations. This approval does not qualify physical fit, strength, actual motion, electrical or thermal safety, print settings, or production readiness, and does not authorize overwriting prior Fusion files.

## Engineer acceptance of B26-STUDY-01 layout

The engineer replied “Wygląda dobrze. Akceptuję” after review of the revised B26-STUDY-01 plan with both jog axes moved 5 mm toward the rear and the calculated 8 mm minimum plan separation to the nearest HOT CUE cap envelopes. Record **ACCEPTED — PRELIMINARY LAYOUT ONLY**. This is not approval of a complete reconstructible technical drawing or of a model. The historical DRAFT / NOT APPROVED labels in the frozen PDF remain accurate for the uncompleted drawing and manufacturing scope.

The reviewed study and its generator are preserved unchanged:

| File | SHA-256 |
|---|---|
| `schematics/enclosure/B26-STUDY-01/DJC_Enclosure_Rev_B26_STUDY_01_drawing.pdf` | `9545c391830cf32c2d12c3f851a1c9b3f79ffa384e0c30473e795ef5e3929691` |
| `schematics/enclosure/B26-STUDY-01/DJC_Enclosure_Rev_B26_STUDY_01_drawing.swift` | `5b9a98b52695f8d54e69ba470fc7c0f22121d19c97496d0f6f56db56cac47e23` |

The jog mounting, bearing capture, display transition and supports, enclosure joints and complete part interfaces remain to be dimensioned and reviewed. The 8 mm result is a nominal plan-envelope calculation, not a 3D interference or physical-fit result. No final model, STL or STEP approval is inferred; future geometry changes require a new drawing revision and explicit approval.

## B26 clarification: display measurements and existing jog sensor mounting

The engineer states that the display dimensions were supplied earlier and that the jog sensor PCB mounting used with B24 is acceptable. Reuse the existing mounting approach; do not ask again for its nominal edge contact or silently treat the new F13 sensor plate and its integration as approved. The B24-build123d01 review identifies empty jog recesses, not an integrated sensor mounting; the separate approved F12-D05 jog defines the P03 locating pegs, toe bosses and P08 pair. F13-STATIC-02 currently references those features on a proposed separate plate, but that changed surrounding structure and its assembly still require review. The engineer's statement is not a physical test, complete B26 drawing/model approval, or authorization to overwrite approved files.

The previously supplied display outside dimensions are 276 x 76 mm. Its approved 272 x 72 mm opening gives 2 mm front overlap per edge. The measured short-side rear bearing band is 2 mm wide; its contact surface is 17 mm inward from the front surface that bears against the panel underside. This is a frame-contact datum, not a measured complete rear body or connector envelope. See [display measurements](#pidac-and-display-measurements--2026-10-17), [rear-frame contact dimensions](#display-rear-frame-contact-dimensions-confirmed) and [rear insertion](#b10-rear-insert-display-seating-and-depth-explicitly-selected). Do not request those measurements again. The engineer previously assigned cable and plug integration to himself under an explicit geometry-neutral assumption; this is not proof of connected fit.

Correction to the preceding request: the mux header projections are already confirmed as 8 mm above the upper PCB face and 1 mm below the lower PCB face; see [mux confirmation](#mux-header-projections-confirmed-equal-to-pcf8575). Its PCB registration and complete installed height remain unqualified, and board mounting is deferred by B25-ELEC-02. No new geometry, physical test, drawing/model approval or export is claimed by this record.

## Engineer approval of B26 and F13 drawing drafts

The engineer states **“Akceptuję całość B26 oraz F13”** after presentation of the following drawings. Record the engineer's approval of all three presented revisions and preserve their PDF and generator snapshots:

| Revision and file | SHA-256 |
|---|---|
| `schematics/enclosure/B26-DETAIL-01/DJC_Enclosure_Rev_B26_DETAIL_01_drawing.pdf` | `72b4371c01f78daf6964bd814d40c29256ee6c326642f7faccf73fe1bb7198e4` |
| `schematics/enclosure/B26-DETAIL-01/DJC_Enclosure_Rev_B26_DETAIL_01_drawing.swift` | `41aad6113b8d87a71191347724aff9415da010718d5f47e21b480d38b1da87d5` |
| `schematics/enclosure/B26-ROOF-01/DJC_Enclosure_Rev_B26_ROOF_01_drawing.pdf` | `cfefc4ac62c718c91429c0b8a43f91748fc49275d8140d93c959744605eb2576` |
| `schematics/enclosure/B26-ROOF-01/DJC_Enclosure_Rev_B26_ROOF_01_drawing.swift` | `7281bdf4adbfb4b94db3a2ef962b7ef8aaf097c08eef713891b647003937586a` |
| `schematics/jog-wheel/F13-STATIC-02/Jog_Wheel_F13_STATIC_02_drawing.pdf` | `58fc5cb3ca1bd7416ddb8241e50e44cc302f6fc0962c3684bc7796761c8898c2` |
| `schematics/jog-wheel/F13-STATIC-02/Jog_Wheel_F13_STATIC_02_drawing.swift` | `7d570c17d030abb58ebbb143f9505c03ab9d3403c5dd81a9cbf94768cfc24f73` |

Approval of these presented revisions does not fill unspecified geometry or constitute a physical, model or export approval. They explicitly leave panel edges and closure, full screen/support interfaces, bottom-tool access, complete assembly, print constraints and other integrations unresolved; therefore they are not yet complete reconstructible drawings for the model gate. The separate existing F12-D05 sensor mounting is acceptable as clarified above, but integrating it into F13's proposed separate plate still needs definition. Complete the missing details in new revisions, retain these accepted snapshots unchanged, and obtain approval of the resulting named complete drawings before 3D geometry. Do not generate final STL or STEP without named model approval.

## B26-PANELS-02 and F13-STATIC-03 draft assembly details

After the engineer requests continuation, prepared [B26-PANELS-02](../schematics/enclosure/B26-PANELS-02/DJC_Enclosure_Rev_B26_PANELS_02_drawing.pdf) and [F13-STATIC-03](../schematics/jog-wheel/F13-STATIC-03/Jog_Wheel_F13_STATIC_03_drawing.pdf), with separate Swift sources in those directories. These are **new drafts, not approved drawings or a complete model-ready set**. Accepted B26-DETAIL-01, B26-ROOF-01 and F13-STATIC-02 PDFs were checked against their recorded hashes and remain unchanged.

B26-PANELS-02 defines six nominal flat-panel XY regions and the two stepped jog seams; lists 28 flat-panel closure axes, distinct from five roof posts and two roof-lap axes; and preserves source references for cuts. The Swift generator reopened three PDF pages and checked 192000 one-mm plan cells, 28 axis owners, 100800 head-rim samples before cuts/fillets, and 56 plan pairs between D6 heads and D108 jog wells, minimum 2.908 mm. These are limited two-dimensional checks, not validation of the complete panel, supports or installed parts. Four outer rear panel posts remain at Y24 after the extension; rear-edge support is not qualified.

F13-STATIC-03 explicitly registers local jog Z to case Z by +2 mm and proposes lifting the front panel 1 mm during a 35 mm rearward slide, with the tempo blade at the forward travel end. Its generator reopened three PDF pages and sampled 105350 shaft/aperture plan sections, minimum 1.638 mm lateral reserve; 8.35 mm fader longitudinal reserve and 2.4 mm panel/platter vertical reserve are nominal arithmetic only. Rear panels cannot simply descend vertically over an installed platter: for R01 at (110,130), radius35 is outside the D52 opening and within the D110 platter, with panel material below the D108 well. A separate staged-assembly proposal uses the combined opening and nominal D51 carrier-cover envelope, 0.5 mm radial reserve, but fixture, complete motion, tool access and real parts are not validated. Sensor mounting remains based on the engineer-accepted F12-D05 approach; cable integration remains engineer-owned under the documented geometry-neutral assumption.

Initial PDF pages were rendered and visually reviewed. Initial source/PDF SHA-256: B26-PANELS-02 source `3590e2adb480acf7dcfae90767f2a606727c9fa41d6fa474d6ab6c9df16cb93e`, PDF `5d2f945bb191778d350b9409ff2b6a23fe21082f5660b943311ac80a63133edb`; initial F13-STATIC-03 source `dc6be2e6354f66d3c62725ebd46b304911b5bcdc30aea022336a6dcf18160fcc`, PDF `ad562348b174fe722b7ee413df99020f3f9d26ad07202611c6ab46f0426a8e0a`. The unapproved F13-STATIC-03 draft was subsequently updated as recorded below. No 3D geometry, full-body collision, print, physical assembly, safety or manufacturing release is claimed.

## F13-STATIC-03 contact assessment

In the approved F13-STATIC-02 numerical geometry, each P02 foot reaches local Z4 and the P06 lower bearing cover begins at local Z4. Their footprints overlap within the annulus R22..23. They therefore have three nominal coincident contact patches, not a positive-volume interference at exact dimensions. The analytical intersection area is 3.883926 mm² per foot; the closest D5 cover-lobe edge is 7.225 mm away in plan. These are nominal geometric calculations, not proof of actual contact, seating, preload or strength. Tolerances could turn nominal contact into a gap or interference. Both parts are fixed, but unverified contact may affect cover/bearing seating; seek the engineer's decision on accepting the contact or delegating a clearance selection. No dimensional change is made to approved F13-STATIC-02.

Added a fourth sheet to the still-unapproved F13-STATIC-03 draft; generated and reopened all four pages, rendered and reviewed the new sheet. Current source SHA-256 `434b711c374b2d14f2b84d61ca35cba205943f61bdbb476dc743b6f083ab93b5`, current PDF SHA-256 `6a51495a8927d5973b21746d65cc2a98aa81f1f48011a39930704092dd568483`. No 3D, physical assembly, fit, strength, preload, screw torque or manufacturing verification.

## F13-STATIC-04 delegated foot clearance

After the nominal foot/P06 contact was explained, the engineer selected **“Dobierz luz”**, explicitly delegating selection of that clearance without moving the bearing or sensor. Selected **0.2 mm nominal** as a small prototype separation; it is not a measured printer accuracy or an accepted tolerance. New drawing [F13-STATIC-04](../schematics/jog-wheel/F13-STATIC-04/Jog_Wheel_F13_STATIC_04_drawing.pdf) replaces each P02 foot's Z1..4 with Z1..3.8 and extends its web from Z4..9 to Z3.8..9; retain all XY, axes, sensor-plate contact at Z1, bearings, P06 cover and other F13-STATIC-02 interfaces. The P02 foot/web share a nominal 6.8 mm² face, web/cover annulus radial separation is 1 mm, and foot/plate ideal plan overlap is 11.893 mm² per foot; neither interface is a physical strength or BRep-connectivity proof.

Generated and reopened two PDF pages using the new Swift source; both pages rendered and visually reviewed. Numerical assertions cover the 0.2 mm axial gap, 1 mm web-to-annulus radial separation, nearest cover-lobe plan separation and ideal plate overlap only. Drawing PDF SHA-256 `d95ba7c038bf770cabff6b38dea45f2806f51ff98137a92d7955c314043b1deb`; source SHA-256 `c6cfc7b86fdd25806c3d09f8fcd1e116ab14da4b91eb7bb17cfda14a85b8b946`. The approved F13-STATIC-02 PDF still matches `58fc5cb3ca1bd7416ddb8241e50e44cc302f6fc0962c3684bc7796761c8898c2`. **F13-STATIC-04 is NOT APPROVED**; dimensional delegation is not drawing or model approval. Require print/fit trials and engineer-defined acceptance criteria; 0.2 mm may be consumed by print variation. No 3D assembly, BRep interference or distance, physical fit, strength, model approval or final export.

## Engineer approval of F13-STATIC-04 foot clearance drawing

After review of F13-STATIC-04, the engineer replies **“Zatwierdzam. Możesz kontynuować”** to the explicit request to approve the foot modification. **APPROVED — F13-STATIC-04 foot clearance drawing only.** The approved nominal 0.2 mm gap and revised P02 foot/web dimensions supersede the corresponding F13-STATIC-02 foot/web dimensions; all other F13-STATIC-02 interfaces remain in force. Freeze the PDF and generator:

| File | SHA-256 |
|---|---|
| `schematics/jog-wheel/F13-STATIC-04/Jog_Wheel_F13_STATIC_04_drawing.pdf` | `d95ba7c038bf770cabff6b38dea45f2806f51ff98137a92d7955c314043b1deb` |
| `schematics/jog-wheel/F13-STATIC-04/Jog_Wheel_F13_STATIC_04_drawing.swift` | `c6cfc7b86fdd25806c3d09f8fcd1e116ab14da4b91eb7bb17cfda14a85b8b946` |

Historical DRAFT / NOT APPROVED labels within the frozen PDF and source are superseded for this local drawing scope only. This does not approve a complete integrated drawing or a model, or prove physical fit, print tolerance, clearance, strength or bearing seating. Complete the B26/F13 integration drawing before new 3D geometry; obtain a separate named model approval before final STL/STEP. Physical gap/fit and print calibration remain necessary.

## B26-PANELS-02 additional nominal proximity screening

After the F13-STATIC-04 approval and the engineer's instruction to continue, the unapproved B26-PANELS-02 working draft was extended to five PDF sheets without changing its proposed dimensions or any approved drawing. The Swift generator reads the R12 coordinates and B24-JOINTS-02 definition, applies the recorded B26 layout moves, and reopens the generated PDF. All numerical results below are **nominal, conservative XY bounds only**, not a 3D, physical, functional or strength validation:

- 28 panel-head discs against 49 control-opening bounds: 1372 pairs, minimum 6.950 mm, with 0.8 mm added to the bounds.
- 28 heads against five fader-recess bounds: 140 pairs, minimum 6.569 mm with the same expansion.
- 28 heads against 12 K03 cap maximum plan envelopes: 336 pairs, minimum 7.000 mm; actual cap travel and other caps excluded.
- 14 candidate translated C07 bridge plates against 50 fixed fader-support boxes: 700 pairs, minimum 3.300 mm; 28 D9 pad bounds against the same 50 boxes: 1400 pairs, minimum 4.244 mm.
- Seven B26 roof-post D8 cores against 14 bridge plates: 98 pairs, minimum 2.000 mm; seven maximal D9 feet against 28 D9 pads: 196 pairs, minimum 2.045 mm.

Actual tool, screw, body, seam, wiring and complete installation paths remain outside the checked coverage. The D108 well comparison on sheet 3 excludes its 0.8 mm upper chamfer. Two added sheets were rendered and visually reviewed. Current B26-PANELS-02 PDF SHA-256 `4393af40b95654473ee94da95da87549040278d8fbeec494ed7b79db674b2a13`, source SHA-256 `c53584e9a0d569e2949a57cb94c0de1bad0f6392c681012a87a44adc683bae8b`; R12 CSV SHA-256 `13a9926564f874d7f20e2aff74f90b460e42c0f264cfaa15fac10c6c1432559e`, B24-JOINTS-02 definition SHA-256 `1488cd468959536bf8f2fd25393b111c007b28bc9dbf6ebd3669b504ae229b6d`. The earlier three-sheet draft hashes above are historical. **B26-PANELS-02 is not approved or complete**; no new CAD/model/export approval follows.

## B26-REAR-POST-03 rear closure proposal

Under the recorded [shell and closure dimensional delegation](#shell-dimensional-delegation-and-installed-height-inputs), the new [B26-REAR-POST-03 drawing](../schematics/enclosure/B26-REAR-POST-03/DJC_Enclosure_Rev_B26_REAR_POST_03_drawing.pdf) proposes moving the four outer rear panel post/hole axes from Y24 to Y8, retaining X8/110/490/592. The reason is to place the fasteners closer to the new rear edge and match the existing 8 mm front-edge axis convention, without adding fasteners or moving other components. This is a **new, unapproved geometry change**; F13-STATIC-04 and approved B26 snapshots remain unchanged. If adopted, the four proposed Y8 axes replace, not supplement, the Y24 axes shown in the older B26-PANELS-02 draft. The five high roof posts remain at Y4.

Retain B24 D8 post core, D9-to-D8 foot, D2.5 pilot and nominal BN616 countersunk M3x8 interface. The D9 foot's minimum plan distance to the new rear wall is 1.5 mm, so its intended load path is through the floor; nominal countersink-to-R0.8 exterior-fillet separation is 4.2 mm. These numbers do not prove floor/post strength, actual edge profile or screw fit.

Reopened the generated two-page PDF and rendered/reviewed both sheets. Asserted limited XY bounds: four proposed heads against 49 control openings plus 0.8 mm allowance (196 pairs, minimum 22.950 mm), four post cores against 14 candidate C07 plates (56, minimum 119.065 mm), four D9 feet against 28 D9 joint-pad bounds (112, minimum 120.973 mm), and four feet against the RCA and AC01 wall-opening bounds (8, minimum 25.359 mm). Actual connector bodies, hardware, tools, all other mounts, complete seam geometry, physical fit, print tolerance, strength and 3D interference remain untested. The PDF SHA-256 is `4070fc141538226db621bfbed0045145544262d7487be7e3cfc82ca39c42adbb`; Swift source SHA-256 `365928e270de404cfa0ca5b7b38f132fdabe8ac1bcfd8275cf325910b36d2384`. No complete B26 drawing or model is approved, and no CAD geometry or fabrication export was produced.

## Engineer approval of B26-REAR-POST-03 and model request

In response to the explicit B26-REAR-POST-03 local drawing approval question, the engineer says **“Akceptuję. Zbuduj model 3d.”** Record **APPROVED — B26-REAR-POST-03 local rear-closure drawing** and the request for a 3D model. The approved four outer rear post/hole axes are (8,8), (110,8), (490,8), (592,8) in the new B26 datum; they replace the Y24 axes in the earlier B26-PANELS-02 draft. Five roof-post axes at Y4 are unchanged. Preserve the approved snapshots:

| File | SHA-256 |
|---|---|
| `schematics/enclosure/B26-REAR-POST-03/DJC_Enclosure_Rev_B26_REAR_POST_03_drawing.pdf` | `4070fc141538226db621bfbed0045145544262d7487be7e3cfc82ca39c42adbb` |
| `schematics/enclosure/B26-REAR-POST-03/DJC_Enclosure_Rev_B26_REAR_POST_03_drawing.swift` | `365928e270de404cfa0ca5b7b38f132fdabe8ac1bcfd8275cf325910b36d2384` |

The historical DRAFT / NOT APPROVED labels remain in the frozen files; this later record supersedes them only for the local drawing. The user requests a 3D model, but the required complete reconstructible B26/F13 drawing still has unspecified critical interfaces and is not approved. The model request does not define those missing dimensions, imply an approval for an unnamed complete drawing, or waive the no-geometry-before-complete-drawing gate. Complete and submit a named integrated drawing before building new 3D geometry; model approval and final STL/STEP authorization remain separate. Physical assembly, print fit, bearing clearance and safety are not established.

## B26/F13 drawing synchronization after the 3D request

Updated the still-unapproved [B26-PANELS-02 working drawing](../schematics/enclosure/B26-PANELS-02/DJC_Enclosure_Rev_B26_PANELS_02_drawing.pdf) to carry the four approved B26-REAR-POST-03 Y8 axes rather than the superseded Y24 draft values, and added a preliminary roles/quantities sheet using the B24 source BOM and F13 jog definitions. The generator reopened six pages; its scoped XY assertions pass, including 1372 control-opening/head pairs at minimum 7.950 mm, 140 fader-well/head pairs at minimum 6.569 mm, 336 K03-cap/head pairs at minimum 7.000 mm and 700 C07/fader-support-bound pairs at minimum 3.300 mm. These are source-bound calculations, not all-body or installed clearance checks. Rendered and reviewed the updated axis, proximity and preliminary inventory sheets. Current panel PDF SHA-256 `4f013f742936b316f702fe4c794da22b3f1aea4b9a1a8b43b88e83ac51437ca3`; Swift source SHA-256 `f7433770c134f2fa7aec7efc295461f7a0af702e0e6293d0868b48147c11b4fd`. Earlier B26-PANELS-02 draft hashes and Y24-based results are historical.

Updated the unapproved [F13-STATIC-03](../schematics/jog-wheel/F13-STATIC-03/Jog_Wheel_F13_STATIC_03_drawing.pdf) sheet 4 to label the previous foot/cover contact as historical and explicitly reference approved F13-STATIC-04. Four PDF pages reopened; the updated page was rendered and reviewed. Current PDF SHA-256 `460e11f86d8e538f4a326c5fefb1929e375d247ddddf09d0880a4863dd74239e`; source SHA-256 `97c2eecb31882f592ceabd6fd98bd8ca7c0157bafee656fcfb07ba066c3eea6f`. Approved F13-STATIC-04 and B26-REAR-POST-03 PDFs retain the hashes in their approval entries. These working documents remain incomplete and do not constitute the required approved integrated drawing.

Concrete remaining model-gate issues: B26-PANELS-02's panel boundaries and C07 transfers are not approved as a complete integrated assembly; the roof/panel and rear shell/joint connections remain incompletely specified. R01/R04 cannot be lowered vertically over the fixed D110 platter; the staged alternative in F13-STATIC-03 has no defined support fixture, full tool access or demonstrated complete installation path. The actual display and mux supplied measurements remain closed inputs; cable/plug scope remains engineer-owned and geometry-neutral, not an invitation to re-request them. No 3D source or geometry, viewer review, model approval or STL/STEP was created by this synchronization.

## B26 joint and F13 assembly studies after renewed model request

The engineer reiterated “Buduj”; this repeats the model request but does not specify the remaining geometry or explicitly approve an identified complete drawing. Prepared two new **unapproved, incomplete 2D studies**, without changing approved snapshots or creating 3D geometry:

- [B26-JOINTS-03](../schematics/enclosure/B26-JOINTS-03/DJC_Enclosure_Rev_B26_JOINTS_03_drawing.pdf) records the candidate transfer of the 14 B24 C07 bridges by Y+20, with 28 integral pad axes, the owning C01–C06 shells and the retained nominal joint section. The generator checked that both pad axes belong to the stated shells and each of the seven adjacent pairs receives two joints. The rear strip seam, roof interfaces, electronic bodies, tooling and complete assembly remain unresolved. The proximity results cited from B26-PANELS-02 are limited XY bounds, not newly verified installed-body clearances.
- [F13-STATIC-05](../schematics/jog-wheel/F13-STATIC-05/Jog_Wheel_F13_STATIC_05_drawing.pdf) documents the captured rear-panel witness and a conditional off-case assembly sequence. The generator checks the nominal 0.5 mm radial opening reserve and 0.2 mm foot/cover gap; neither is a measured fit tolerance. Fixture support points and safety, collar tools and the complete shell/panel approach remain unspecified. The study is not an executable or verified service procedure.

Each generator was run with Swift, reopened its three-page PDF and all six pages were rendered and visually reviewed. These studies do not close the complete named drawing gate, approve a model or authorize STL/STEP. No BRep, viewer, collision sweep, physical fit or strength assessment was performed. Cable/plug geometry remains the earlier engineer-owned assumption, not a proven connected fit.

| Study artifact | SHA-256 |
|---|---|
| `schematics/enclosure/B26-JOINTS-03/DJC_Enclosure_Rev_B26_JOINTS_03_drawing.swift` | `41567731edfdd9ff9c6f5ff984bac74e25eccb129011ffb325f3a5339e75693f` |
| `schematics/enclosure/B26-JOINTS-03/DJC_Enclosure_Rev_B26_JOINTS_03_drawing.pdf` | `ba49faa2b4da4cfdeda69df188ef82cf3f8283d1bf23c56d586bbcc85d385319` |
| `schematics/jog-wheel/F13-STATIC-05/Jog_Wheel_F13_STATIC_05_drawing.swift` | `13c6f7e19868490e034d4b4d9f0013c23d6b8ee41ab356d7d2f0312ea29a3aa6` |
| `schematics/jog-wheel/F13-STATIC-05/Jog_Wheel_F13_STATIC_05_drawing.pdf` | `91a0a62ba533322cc4b99f9dbcf4013cba8a3b384d3324a2ab388dd06db6252e` |

## Engineer acceptance of B26-JOINTS-03 and F13-STATIC-05 studies

After reviewing the two linked new studies, the engineer says **“Nowe rysunki są ok. Działaj dalej. Wypracuj całe rozwiązanie bez stopu co chwilę na moją akceptację.”** Record acceptance of the named **B26-JOINTS-03** and **F13-STATIC-05** studies with the PDF and source hashes immediately above. The frozen files retain their historical DRAFT/NOT APPROVED labels; this record supersedes those labels for these named study snapshots only. Preserve the snapshots.

Proceed autonomously with the previously delegated printed-shell, joining and jog-service design and prepare the complete integrated solution rather than seeking approval of each intermediate detail. The accepted studies themselves explicitly leave the rear strip, roof interfaces, fixture, tool access and complete assembly unproven. Acceptance does not define unspecified dimensions, prove assembly or fit, constitute approval of a named complete drawing/model revision, or waive the drawing/model/export gates. Connected wiring, process margins and physical strength remain subject to their recorded limitations.

## B26 and F13 integration work after study acceptance

Under the engineer's instruction to develop the whole solution without repeated intermediate reviews, prepared these distinct **unapproved 2D working proposals**; no existing approved study was overwritten:

- [B26-INTEGRATION-01](../schematics/enclosure/B26-INTEGRATION-01/B26_roof_shell_drawing.pdf) records the retained roof/panel interfaces and proposes two additional C07 floor joints at (220,14)/(380,14), in addition to the 14 accepted-study joints. Four pad axes and nominal source fasteners are specified. Selected XY screens give 1.050 mm minimum between new pad bounds and rear roof-post feet and 1.000 mm between new plates and roof-post cores. Separately compared the two plate rectangles against three B22 PI/DAC/PSU plan proxies translated Y+20: six comparisons; minimum 9.750 mm. The proxies do not include actual connectors or all geometry. An initially considered roof-owned shelf was rejected because it obstructed vertical roof installation beside installed panels; it is not in the resulting proposal. Roof-first, R03-last is only an intended ordering, not a verified installation.
- [F13-INTEGRATION-01](../schematics/jog-wheel/F13-INTEGRATION-01/F13_service_drawing.pdf) quantifies one off-case registration fixture. Its four support columns occupy the eventual closure-post axes; raising the shell into the fixture is blocked. Upper suspension and safe support transfer remain unspecified. Do not treat this fixture or sequence as usable.
- [F13-PANEL-06](../schematics/jog-wheel/F13-PANEL-06/F13_PANEL_06_drawing.pdf) proposes moving the local panel seam from Y145 to Y165 within X75..145 / X455..525 so the D52 hole is divided through the jog axis. This changes a detail of approved F13-STATIC-02 and is a candidate successor, not an approved change. It offers a different assembly concept: the rear panel is mounted first, then an assembled jog is moved from +Y while raised 6 mm, then lowered, and the front panel is approached from +Y. The circular D51 carrier/cover envelope against the D52 semicircle has a 0.5 mm nominal minimum half-width reserve; 65,536 sampled sections at 0.1 mm movement / 0.05 mm transverse resolution corroborate the analytic bound. Ear top at the lifted pose is 1 mm below panel underside; feet are 1 mm above the nominal boss top. These checks exclude other components and all full swept solids, tolerances and physical handling; no complete installation is demonstrated.

All three generators were run with Swift, PDFs reopened (4, 4 and 3 pages respectively), all pages rendered and visually inspected; the fixture section was corrected and regenerated for readability. Print constraints beyond nominal machine/nozzle, physical fit, simultaneous collar tools, full-body interference and real installation remain open. Electronics mounting remains explicitly deferred by B25-ELEC-02; no rejected PCB supports or unknown mounting holes are added. No new 3D geometry, viewer evidence or export was created. These studies are not a complete integrated drawing or model approval.

| Study artifact | SHA-256 |
|---|---|
| `schematics/enclosure/B26-INTEGRATION-01/B26_roof_shell_drawing.swift` | `fbeb287d97840b1248a5d6a2d0e114ea63b61a211d8b63cdbaf2e32e989a6b8c` |
| `schematics/enclosure/B26-INTEGRATION-01/B26_roof_shell_drawing.pdf` | `17513176e93efbdde36ec6baf043920ecce6e5c4dfd3c29d7bcad57e731bc3ff` |
| `schematics/jog-wheel/F13-INTEGRATION-01/F13_service_drawing.swift` | `a951e7cff8cf5133f1c8688317353ec59ade53847ced1cb1ac316a2ec57fe57d` |
| `schematics/jog-wheel/F13-INTEGRATION-01/F13_service_drawing.pdf` | `0180ad62e5b5380d53f3a28fba9eed9164b31130f126bf380d84b3a20d259ee1` |
| `schematics/jog-wheel/F13-PANEL-06/F13_PANEL_06_drawing.swift` | `b02af37011a440c120526e8b3fcf0a34959726c0d7ee1d3b53c67522ea5d5549` |
| `schematics/jog-wheel/F13-PANEL-06/F13_PANEL_06_drawing.pdf` | `1a05ac331c32d99238d15ba1a164e33f5264d11e457b9624066925c8942269ef` |

## Engineer acceptance of F13-PANEL-06 and B26-INTEGRATION-01

In response to the two linked proposals, the engineer says **“Akceptuję. Kontynuuj. Masz moją akceptuję z góry. Pokaż mi dopiero model 3d”**. Record explicit acceptance of the presented named **F13-PANEL-06** and **B26-INTEGRATION-01** drawing snapshots and preserve their PDF and Swift hashes listed immediately above. The historic NOT APPROVED labels in those frozen PDFs are superseded for the stated drawing proposals only. The user requests autonomous completion and only the 3D model for review; do not request approval of intermediate sketches.

Neither accepted proposal is a complete integrated B26/F13 drawing. The F13 installation and simultaneous collar tools, full control/body clearance and actual fit remain unproven, as do the documented roof and joint limitations. The user's advance consent does not specify unspecified dimensions or make the as-yet-unwritten integrated drawing a named approved revision. The profile requires explicit engineer approval of the completed named drawing before creating new build123d 3D geometry, and a separate named model approval before final STL/STEP; physical and electrical safety are not implied. Continue all reachable design work before escalating an actual blocker.

## B26-INTEGRATED-01 candidate drawing and scoped service checks

Prepared a single [B26-INTEGRATED-01 review PDF](../schematics/enclosure/B26-INTEGRATED-01/DJC_Enclosure_Rev_B26_INTEGRATED_01_drawing.pdf) from the accepted drawing amendments and new [B26-PANELS-03](../schematics/enclosure/B26-PANELS-03/DJC_Enclosure_Rev_B26_PANELS_03_drawing.pdf) and [F13-TOOLS-01](../schematics/jog-wheel/F13-TOOLS-01/F13_collar_tools_drawing.pdf) drafts. The cover explicitly resolves Y165 panel seams, four Y8 rear closure axes, 16 C07 bridges, F13-STATIC-04 foot clearance, selective F12 sensor features and non-pressing D110 jogs; source sheets retain their historical labels. The PDF includes seven cover/snapshot sheets and 47 appended source pages, with SHA-256 of 57 source drawings/data/legacy mesh assets. K02/K03 and B17 cap drawings and legacy control assets are included; the cap meshes are reference geometry, not an editable source history. It is a **candidate for review, not an approved named complete drawing or model**. U1–U4 hole-based mounting remains explicitly deferred; no unprovided PCB holes or rejected holders were added.

The B26-PANELS-03 generator checked 192,000 nominal 1 mm partition cells, 100,800 sampled D6 closure-head perimeter points and 49 source-derived control aperture bounding boxes for panel ownership; these are plan-only checks before evaluated 3D bodies. F13-TOOLS-01 proposes two concentric trial tools and derives an ideal −120° / −1⁄6 mm starting phase, with 0.8333 mm nominal male-thread overlap and approximately 0.180 mm minimum radial tool separation. Prong widths 0.45/0.5 mm approach the 0.4 mm nozzle; actual tool printability, engagement, torque, wear and safe use are unverified.

[F13-PATH-01](../schematics/jog-wheel/F13-PATH-01/F13_path_screen_drawing.pdf) compared 246 selected source-derived conservative plan bounds with both jog approach envelopes (492 comparisons). The decomposed moving under-platter capsule screen reports 0.745 mm minimum to the checked bounds after excluding removed K03 caps and intended boss contacts; the D110 AABB overlaps other bounds that are reported, not hidden. Separate ideal height checks cover the listed bare switch/reference heads; toe-to-D26-shaft nominal radial reserve is approximately 0.3505 mm and the IC-to-magnet nominal axial gap is 2.5 mm. These are partial analytical checks, not actual BRep distance, complete motion, printed fit, cable clearance, or physical validation; all omitted bodies are listed in the PDF.

Executed Swift generators, reopened the 4-page panel, 2-page tool and 5-page path PDFs and rendered/reviewed all pages. Reopened the combined 54-page PDF, verified fingerprints remained unchanged during generation, and rendered/reviewed its seven cover sheets plus first and last appendix pages; the source drawing pages had been reviewed in their original workflows. Generated a separate [illustrative concept PNG](../schematics/enclosure/B26-INTEGRATED-01/DJC_Enclosure_Rev_B26_INTEGRATED_01_concept.png) from the earlier concept, converted WebP to PNG and opened both files; it is not a model or dimensional source. Read installed `.venv` package metadata: build123d `0.13.1.dev254+gc49a0493a`, `cadquery-ocp-novtk` `8.0.1.1.0`, `ocp_viewer` `1.2.0`; no Python geometry or viewer was run.

| Artifact | SHA-256 |
|---|---|
| `schematics/enclosure/B26-INTEGRATED-01/DJC_Enclosure_Rev_B26_INTEGRATED_01_drawing.swift` | `6c9a5ac6e93c432d68e4d0cc9fcafc7e3c0220f84593f0b0c149f0d10712a803` |
| `schematics/enclosure/B26-INTEGRATED-01/DJC_Enclosure_Rev_B26_INTEGRATED_01_drawing.pdf` | `3c53cf83ea016da892db967b70096fe1dd8a45eecfe6aa11ac3295e9d90bebf0` |
| `schematics/enclosure/B26-INTEGRATED-01/DJC_Enclosure_Rev_B26_INTEGRATED_01_concept.png` | `bd316c61a7c0cb962a4c68c95dbb8bf7f6f16f7a9d4debea2fb2b266e165d3f9` |
| `schematics/enclosure/B26-PANELS-03/DJC_Enclosure_Rev_B26_PANELS_03_drawing.swift` | `5c63e5f37b3054271868799d832f0135906ac2212b8be376428462b620f96e29` |
| `schematics/enclosure/B26-PANELS-03/DJC_Enclosure_Rev_B26_PANELS_03_drawing.pdf` | `bb18a44bedbeaa97a3462f3f8aab4248fdf212cd47080eed21cedaa086c2db8a` |
| `schematics/jog-wheel/F13-TOOLS-01/F13_collar_tools_drawing.swift` | `61715ddd29b87a9a8084f9203e7fad6ac6fab01fca46abe8dd11d814316f8e8f` |
| `schematics/jog-wheel/F13-TOOLS-01/F13_collar_tools_drawing.pdf` | `58f3c3275f150c0b86c7a65154394cb86ea458800e187ac9d4df5ee1d382b371` |
| `schematics/jog-wheel/F13-PATH-01/F13_path_screen_drawing.swift` | `30ca12b1069581ad618c630e06e9074b10967d12d82d433121af0a82af6e8f72` |
| `schematics/jog-wheel/F13-PATH-01/F13_path_screen_drawing.pdf` | `af455168f066cd17bad0a0c50bd0dd2a793b4098b6a8070c5fd740ee032cb01c` |

Per the CAD workflow, the engineer must explicitly approve the named integrated drawing revision before any new build123d 3D geometry, even though advance consent to continue was requested. Named model approval remains separate from drawing approval and is required before final STL/STEP. No model, actual-model review images, mesh or final export exists in this work; no geometric or physical approval is implied.

## Engineer approval of B26-INTEGRATED-01 drawing

In direct response to the named B26-INTEGRATED-01 drawing approval request, the engineer says **“Zatwierdzam. Póki co dobrze to wygląda. Nie jestem do końca przekonany o panelach pod platerami. Ale to obadam na modelu 3d.”** Record **APPROVED — B26-INTEGRATED-01 drawing** for the exact PDF SHA-256 `3c53cf83ea016da892db967b70096fe1dd8a45eecfe6aa11ac3295e9d90bebf0`, source SHA-256 `6c9a5ac6e93c432d68e4d0cc9fcafc7e3c0220f84593f0b0c149f0d10712a803`, and concept SHA-256 `bd316c61a7c0cb962a4c68c95dbb8bf7f6f16f7a9d4debea2fb2b266e165d3f9`. Preserve all approved snapshots and their historical draft labels; this entry supersedes those labels only for this named drawing.

This explicitly opens the CAD modeling gate. The engineer reserves judgment of the panels under the platters for actual-model review; include clear actual-model views of that interface. Drawing approval does not approve a model or authorize final STL/STEP, physical fitness, calibration, electrical safety, strength or manufacture. Maintain the drawing's documented deferred U1–U4 mounting, incomplete purchased references, unvalidated tool fit and legacy-cap editable-source limitations. Any geometry correction returns to a new drawing/model revision and named approvals.

## Engineer approval of B26-build123d01 appearance-only model

After reviewing the `--appearance-only` model in ocp_viewer, the engineer said: **“Jest super. Zatwierdzam model.”** Record this approval for the presented **B26-build123d01 appearance-only snapshot**, with source and image SHA-256 values recorded in [the review report](../models/enclosure/B26/BUILD123D/DJC_Enclosure_Rev_B26_build123d01_review.md). The approved presentation deliberately omits the P01 shafts and P04/P07 collars; it is not a complete jog assembly.

The known T30 Boolean defect, incomplete reference hardware and unperformed validation remain unresolved. This approval does not make the omitted or defective geometry valid, authorize a different corrected revision, or establish manufacturing or physical approval. Do not produce final STL or STEP from the incomplete snapshot. Reconstruct and validate the missing geometry, preserve the approved snapshot, and obtain explicit approval of the resulting named model revision before final exports.

## Engineer approval of B26-build123d02 model

After presentation of the named B26-build123d02 model, its T30 checks and the unresolved bearing and Pi/DAC reference-envelope intersections, the engineer said **“No i super. Z mojej strony akcpetacja całości”**. Record **APPROVED — B26-build123d02 model**, including the disclosed reference-envelope limitations, for the source, evidence and view hashes in [the revision review](../models/enclosure/B26/BUILD123D02/DJC_Enclosure_Rev_B26_build123d02_review.md). The source and views were rehashed against that report at approval; all matched. Preserve this approved snapshot.

The engineer's acceptance is not a measurement or a finding that actual bearing, PCB underside, connector, wire or hardware geometry is collision-free. It does not identify the actual purchased bearing or authorize a new geometric revision. The review's unperformed print-volume setup, cap-source completeness, mesh, STEP, physical fit, strength, assembly and electrical checks remain open. Correcting any actual geometry requires the drawing/model revision workflow and renewed approval. Final export and handoff remain blocked until their applicable verification and source requirements are satisfied.

## Engineer approval of B26-FADER-01 drawing

In direct response to the request to approve **B26-FADER-01**, the engineer said: **“O tak. Jest super. Akceptuję.”** Record approval of the named drawing amendment and preserve the approved snapshots: [PDF](../schematics/enclosure/B26-FADER-01/DJC_Enclosure_Rev_B26_FADER_01_drawing.pdf) SHA-256 `b955582992afb8ae453df722c3251c50223a0f217f3ee08df89503fdf45a0457`, [Swift source](../schematics/enclosure/B26-FADER-01/DJC_Enclosure_Rev_B26_FADER_01_drawing.swift) `69ec2e1785f870c8fb032606e3ea9c39150ebd94a867354a181b2460e4b75f47`, and [illustrative concept](../schematics/enclosure/B26-FADER-01/DJC_Enclosure_Rev_B26_FADER_01_concept.png) `8f0cc68fa809448b549281d2f77b68de29c237b33faf68c356891ac4e4a48cb4`. The concept omits the retainer and is not CAD or dimensional evidence; historical draft labels remain on the preserved files.

The approved scope moves both fader end bosses and pilots another 1.2 mm outward relative to B26, retains the cup walls and retainer inner edges, and lengthens the retainers as dimensioned for all five faders. This opens a new build123d model revision; it does not approve that model, physical fit, collision clearance, print strength or exports. Keep B26-build123d02 and its existing STL files unchanged and held. The new named model requires its own review and explicit engineer approval before final STL/STEP.

## Engineer approval of B26-build123d03 model and STEP numerical exception

In direct response to the two questions whether to approve model **B26-build123d03** for STL/STEP and accept a trial STEP with the disclosed volume-comparison exception, the engineer replied **“Akceptuję.”** Record **APPROVED — B26-build123d03 model** and **accepted bounded P01 STEP numerical-comparison exception for trial use**, not a physical, electrical, strength or production approval. The approved model review manifest SHA-256 is `38c7bf1db87ddaead6112364c72ac23a54d1158d9426b2d37a09d267bad64a33`; source and dependency hashes are recorded in that manifest. Preserve the B26-FADER-01 drawing and prior model snapshots.

The [preflight report](../models/enclosure/B26/BUILD123D03/PREFLIGHT/B26-build123d03_preflight.md) SHA-256 `2b25b4359a1e71e12a6ce921309dfd1f9dbf849e2c319617a94af95abc065e0e` and its evidence manifest SHA-256 `8ec79c17bd52a8dc79e2331f72b98654aa55815ed7ce43ce1efe8a158f74fe82` record the disclosed exception: the strict default OCCT volume comparison fails by approximately 0.6410915 mm³ for each P01 rotor; adaptive integration, 0/0 directional differences and dense mesh sampling strongly indicate a numerical integration effect after cone reparameterization. The strict check remains failed, not waived as passed. This consent is limited to the stated trial representation and evidence; final output must be independently reopened, compared to the approved source and disclose the failure and limits. No unrelated exception, absent mounting, missing physical fit or electrical safety is approved.

## Engineer selects exact mesh data for consolidated B26 cap documentation

For the new standalone B26 documentation, the engineer selected **“Dokładne siatki w JSON”** for the nine cap definitions inherited as STL meshes. Preserve their exact faceted geometry in JSON rather than inventing analytic dimensions or claiming parametric feature history. This is a documentation-representation decision; it does not approve the new drawing revision, change the existing model, approve physical fit or authorize manufacturing.

## Engineer accepts the B26-CONSOLIDATED-01 draft PDFs

After presentation of the named B26-CONSOLIDATED-01 draft set and its disclosed outstanding completeness checks, the engineer said **“O. PDFy są super. AKceptuję”**. Record acceptance of the three PDFs as presented, without rewriting their historical DRAFT labels:

| PDF | SHA-256 |
|---|---|
| [Enclosure](../schematics/work/enclosure/B26-CONSOLIDATED-01/B26_CONSOLIDATED_01_enclosure_DRAFT.pdf) | `6885827656b9742273fa4450d495ef3228005dbcc279cee145d5b2c6af35eaa3` |
| [Front panel and caps](../schematics/work/enclosure/B26-CONSOLIDATED-01/B26_CONSOLIDATED_01_frontpanel_DRAFT.pdf) | `b990dad0644586630b96a6e42c836b91683907a0e4ce0983128542599ab9be82` |
| [Jog](../schematics/work/enclosure/B26-CONSOLIDATED-01/B26_CONSOLIDATED_01_jog_DRAFT.pdf) | `722cfad1f2ab7597c9f0a7667963a1de202ba465b336969c3394403dc6f4c6ac` |

The three hashes were checked against the existing validation record at acceptance. Preserve these exact files; acceptance does not establish completeness or waive the disclosed gaps in detailed sections, standalone reconstructibility, or independent jog/T30 verification. Companion JSON was not explicitly approved by this statement. Corrections affecting geometry or dimensions require a new drawing revision and explicit approval; neither a new model nor STL/STEP exports are approved by this PDF acceptance. Keep the release documentation task open until the required evidence and applicable revision approvals exist.

## Engineer confirms no jog press switches in the current design

On 2026-10-29 the engineer states **“Na ten moment nie mamy ich”** in response to the earlier description of two jog switches. Remove them from the current control population. A separate NUDGE/SCRATCH button is requested; location, exact behavior, part and input allocation remain TBD. This clarification does not modify or approve a drawing, model, electrical wiring or firmware; preserve historical decisions and approved snapshots.

## Project name: beatbreaker

On 2026-10-29 the engineer names the project **beatbreaker**, spelled in lowercase. Historical paths, frozen drawings, model packages and records retain their original names and bytes; the naming decision does not change geometry, approvals or the local repository path.

## Engineer approves B26-CONSOLIDATED-02 for reconstruction review

In response to the request to approve the named drawing revision for an independent verification reconstruction, the engineer said **“Zatwierdzam”**. Record **APPROVED — B26-CONSOLIDATED-02 drawing for control reconstruction**, with the disclosed incompleteness and unverified equivalence: [69-page PDF](../schematics/work/enclosure/B26-CONSOLIDATED-02/B26_CONSOLIDATED_02_complete_DRAFT.pdf) SHA-256 `35ab5a40ae0051ec4080cb6cfb287782c482859d1a6f666e9a8b0ccca00226c2` and seven numerical JSON files whose hashes are recorded in the [validation snapshot](../schematics/work/enclosure/B26-CONSOLIDATED-02/B26_CONSOLIDATED_02_validation_DRAFT.json). These eight files matched their recorded hashes when approval was recorded. The concept PNG listed in that historical snapshot was absent when checked; do not claim it was verified or silently recreate it. Preserve approved PDF and numerical data without changing their historical DRAFT labels.

Approval authorizes the requested independent control reconstruction, not an assertion that the drawing is complete, a new model approval, final exports, physical fit, electrical/thermal safety or manufacturing. The existing P01 STEP strict-volume failure and bounded trial exception remain exactly as recorded. Any geometric or dimensional correction requires a new drawing revision and explicit approval.

## Release-package naming: REV_A

The engineer requests **“Całość powinna być zreleasowana pod nazwą REV_A”**. Use `REV_A` as the name of the requested release package; retain the B26 drawing/model revision identities and traceability of all inherited artifacts. This naming decision does not establish reconstruction completeness, change geometry or replace model/export approvals.

## Engineer accepts bounded C03/C05 reconstruction exception

After being informed that the independent C03/C05 reverse Boolean cuts returned invalid outputs and opposite-order intersections contradicted each other, despite matching sampled checks, the engineer selected **“Dopuść wyjątek próbny”**. Record acceptance of a bounded documentation/reconstruction comparison exception for the `REV_A` **unpowered mechanical trial only**. The strict C03/C05 comparison remains unresolved, not passed; the exception does not establish exact surface identity, fit, strength, electrical or thermal safety, or production readiness. The existing separately accepted P01 STEP volume exception remains unchanged.

The disclosed evidence is [the reconstruction review](../models/work/enclosure/B26-CONSOLIDATED-02-CHECK/REV_A_reconstruction_review.md) SHA-256 `6169e7e7bf0f3a83b88843fb28f06464cfb10c397bbb1da2d15b3e0708747ea4`, [shell comparison](../models/work/enclosure/B26-CONSOLIDATED-02-CHECK/shell_evidence.json) `4a37aed4ee74b3bbb4ce0ea73aa76d2917a0fdab6b094ca566c0ae80d2b77659`, [diagnostics](../models/work/enclosure/B26-CONSOLIDATED-02-CHECK/shell_diagnostics.json) `80b08b7c000e731c55cc410fca92a8a76749407cc42561a0a73725121bdda69f`, and [fuzzy comparison](../models/work/enclosure/B26-CONSOLIDATED-02-CHECK/shell_fuzzy.json) `c575bbc786c7d7a41bd325f38df80d9b0980d9a32d8e332390113f51e020`. Preserve those snapshots; new geometry or changed drawings require their applicable approvals.

## REV_A unpowered trial package delivered

Published [drawing and companion data](../schematics/release/enclosure/REV_A/) and [the trial model package](../models/release/enclosure/REV_A/) under the engineer-requested name `REV_A`. The [70-page PDF](../schematics/release/enclosure/REV_A/beatbreaker_REV_A_drawing.pdf) SHA-256 `84644f4b69d62213cb9386ea128ff90f1d73002459063434a9fcfbc7810201d8` adds a release/status cover to the unchanged 69-page B26-CONSOLIDATED-02 drawing content; historical DRAFT labels are retained. The [manifest](../models/release/enclosure/REV_A/REV_A_manifest.json) SHA-256 `5c52b8bcc085c0cf1d87668f6a7cbfc7d7b55b1a5a20cec50566526577d41164` records 138 released files, excluding itself, and the [handoff](../models/release/enclosure/REV_A/REV_A_handoff.md) SHA-256 `5fa9098af6c4cd8be40fcc2eef125d59633935a8ab4edc4c0c48c4d871fec6a6` records actual checks and limitations.

All 104 inherited model-package files were checked byte-for-byte by SHA-256 against the existing approved release; no new STL or STEP was generated. All 36 copied STLs were decoded and screened, the 476-leaf STEP reopened, and all 52 source/asset hashes and the rebuild were checked. The 49 STL-imported cap references are triangulation-only display Faces that do not pass BRep validity; the separately delivered cap meshes were checked. C03/C05 and both P01 strict comparisons remain unresolved/failed with only the recorded bounded trial exceptions. Physical, electrical, thermal and production qualification remains open.
