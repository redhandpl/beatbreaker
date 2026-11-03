# Current release approval register

This register records the engineer's decisions relevant to the current [REV_B mechanical release](../models/REV_B/beatbreaker_REV_B_validation.json). The scope of each decision is limited to what was actually accepted; publication or relocation of an artifact does not itself grant or revoke approval. The complete release drawing is [here](../schematics/REV_B/beatbreaker_REV_B_drawing.pdf).

## Engineer withdraws F11 and focuses jog work on B26

On 2026-10-29 the engineer stated **“Starszy jog F.11 jest zupełnie wycofany. Skupiamy się tylko na B26.”** F.11 is withdrawn and B26 is the only active jog design. F.11 press, switch and spring requirements, including the final metal-spring requirement, do not apply to the non-pressing B26 jog. F12 is not pursued under this scope; its incomplete export and physical gates are not passes. This decision did not itself approve new geometry, exports or physical or safety performance.

## Engineer approves B26-LAP-build123d07

After receiving the disclosed failed C03/C05 directed Boolean checks and C01/C03 volume-delta comparisons, the engineer stated **“Ok. Zatwierdzam model. Działaj dalej.”** The accepted model was B26-LAP-build123d07, bound to manifest SHA-256 `64181575a477c80870996e8dcba086f6e1c4d3f35a2f4ccd22dba13a65f4695d`. Approval of that model did not turn failed comparisons into passes, separately approve DRAWING-06, or qualify physical performance or safety.

## Engineer selects integral shell mounting for the jog sensor

On 2026-10-31 the engineer accepted the stated tradeoffs: **“Godzę się na te kompromisy. Pasuje mi montaż enkodera do obudowy.”** The selected AS5048A seat is integral to C04/C06 and remains in the shell when the jog is removed; its alignment depends on jog-floor mounting, and damage to the integral seat has repair/reprint consequences. The PCB remains removable. This direction was not itself approval of an unbuilt named model, exports, actual fit or the upper-bearing reference overlap.

## Engineer approves REV_B-PREP-01 drawing/model and REV_B publication

After review of the consolidated drawing and source-bound model, the engineer selected **“Zatwierdzam rysunek i model”** for REV_B-PREP-01, based on unchanged B26-LAP-build123d09 geometry, for **REV_B / unpowered mechanical trial only**. Final STL/STEP generation, export verification and publication were authorized without geometry changes. Approved source SHA-256: `2863f516138bf7e70d7dcc0b1d365435cacc56f4794111813ae784e54f978636`; approved draft drawing SHA-256: `c5846598f4f28601345ae98c34fe5728b121836bec1aca0857ab63a48dc9a4fb`. The original sharp-bearing-reference failures and separate selected-SKF nominal compatibility result remain distinct; no physical or powered-use qualification was granted.

## Engineer approves B26-ESP-DRAWING-01 and B26-LAP-build123d10 for the C04 STL trial

For the named ESP drawing and model the engineer selected **“Zatwierdzam i eksportuj C04”**. The drawing and model were approved for an **unpowered mechanical trial**, with export authority limited to C04; this decision did not authorize a new complete release or unrelated STEP and part exports. Actual fit, retention, strength, print calibration and electrical/thermal safety remained unverified.

## Engineer approves B26-PCB-DRAWING-01 and B26-LAP-build123d11 for C04/C06 STL

For the named PCB drawing and model, after presentation of the CAD views, assembly order and limitations, the engineer selected **“Zatwierdzam i eksportuj STL”**. The drawing and model were approved for an **unpowered mechanical trial**, with export of C04 and C06, one each. This decision did not by itself authorize a complete release, STEP, other-part exports, powered use or physical qualification. The selected PCF/mux configuration requires flat finished undersides, no headers and top-only wires.

## Engineer accepts all controller holders and authorizes updating REV_B

The engineer stated **“Akceptuję ostatnie zmiany (trzymadełka dla ESP, PCF8575 i multipleksera. Zaktualizuj odpowiednio REV_B”**. This accepts the already named and approved B26-ESP-DRAWING-01 / B26-LAP-build123d10 ESP geometry and B26-PCB-DRAWING-01 / B26-LAP-build123d11 complete controller-holder geometry, and authorizes updating the complete REV_B publication to geometry11. The authority extends the earlier two-STL-only scope to the coherent release package: standalone source, complete current drawing, 37 part STLs, complete assembly STEP, actual-model views and consolidated validation/BOM/handoff JSON.

Only consolidation and presentation changes beyond accepted geometry11 were authorized, with source/model equivalence, complete drawing reconstruction and actual exports to be verified. The selected PCF/mux configuration remains flat undersides, 2 mm PCBs, no headers and top-only wires; ESP reversed headers remain unchanged. Original sharp-bearing-reference failures remain separate from selected-SKF nominal compatibility.

**UNPOWERED MECHANICAL TRIAL ONLY.** This acceptance does not establish physical fit, insertion force, retention, strength, slicer/support/calibration suitability, or electrical or thermal safety. Actual bearing fit and operation, PCB damage, PETG creep and DAC screw retention remain open. The [release validation and handoff](../models/REV_B/beatbreaker_REV_B_validation.json) records the delivered artifacts and the limits of the computational evidence; it is not an additional engineer approval.
