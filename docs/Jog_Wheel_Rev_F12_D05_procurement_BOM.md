# Jog Wheel F12-D05 — hardware BOM, source links and trial generators

Research date: 2026-10-21, CEST. Units: mm, N, PLN. Quantities exclude spares.

**PROCUREMENT RESEARCH COMPLETE; ALTERNATIVE HARDWARE NOT APPROVED; SPRING PURCHASE SOURCE UNRESOLVED.** This is a purchasing reference for one F12-D05 jog and the two jogs in a controller, not a complete controller BOM or a change to approved geometry. Initial procurement research made no order, cart change, vendor enquiry, Fusion access/mutation, cloud save or fabrication export. The later generator assessment includes read-only Fusion document-state inspection only.

## Approved baseline and scope

- [F12-D05 drawing approval](APPROVALS.md#engineer-approval-of-f12-d05-nominal-printed-prototype-drawing) and [F12-D05-Fusion01 model approval](APPROVALS.md#engineer-approval-of-f12-d05-fusion01-nominal-prototype-model-and-stl-request) remain valid for the stated nominal printed-prototype scope, not physical fit/strength/return certification.
- Source quantities: [frozen D05 checks, `hardware_population_per_jog`](../schematics/jog-wheel/F12-D05/Jog_Wheel_Rev_F12_D05_checks.json). Geometry and locations: [drawing, sheet12](../schematics/jog-wheel/F12-D05/Jog_Wheel_Rev_F12_D05_DRAFT.pdf). Exact accepted vendor baseline: [D05 hardware sources](../schematics/jog-wheel/F12-D05/Jog_Wheel_Rev_F12_D05_hardware_sources.json), accepted with [F12-D03 drawing](APPROVALS.md#engineer-approval-of-f12-d03-nominal-printed-prototype-drawing) and retained in D05; historical proposal labels in frozen files are not reopened or rewritten.
- Screws, nuts and washers were searched **only at AlpinPower**. Links to accepted historical fastener specifications above are design provenance, not new sourcing at other retailers. Springs were researched on the Polish market and compared against the accepted manufacturer's data.
- Source model was last recorded as cloud lineage `urn:adsk.wipprod:dm.lineage:rCsKqvaXTxqppcLYV-mtXA`, version2, with the historical title `Jog Wheel F12-D05 Fusion01 RECOVERED WIP002 — NOT APPROVED`. Fresh document-list inspection during generator research confirms it is saved/unmodified. A separate active `DJC Enclosure B22-Fusion-01 DRAFT` is modified and remains untouched. No document activation, geometry/camera/visibility change, save, close or export was made. Approved drawing/model packages and existing STL files are unchanged.

## Screw and nut BOM

Offer links are procurement **candidates**, not accepted replacements. Listed AlpinPower nominal dimensions agree with the checked main envelopes below, but actual-lot tolerances, fillets, thread runout and strength are not established. The cover screw, M2 cap screws and nuts differ from the approved A4/A2 material baseline. The retained floor screw had a maximum-envelope reference, not an accepted exact supplier/material specification.

All seven listed AlpinPower offers, including the washer below, state **one piece per package**. Prices are the displayed PLN prices; VAT inclusion was not explicitly established from the inspected product pages/terms. Shipping and springs are excluded from totals.

| Item | Function | Qty / jog | Qty / two jogs | AlpinPower offer | Offered material | Price / piece | Cost / jog | Cost / two jogs |
|---|---|---:|---:|---|---|---:|---:|---:|
| M2x4 countersunk, DIN7991 | Bearing covers | 6 | 12 | [Product4739](https://alpinpower.com.pl/m2x4-sruba-aluminiowa-stozkowa-imbus-din-7991-sruby-aluminiowe-stozkowe-p-4739.html) | Aluminium6061 | 0.19 | 1.14 | 2.28 |
| M2x4 socket cap, DIN912 | Sensor PCB toes | 2 | 4 | [Product6761](https://alpinpower.com.pl/m2x4-sruba-imbusowa-din-912-iso-4762-tytanowa-sruby-tytanowe-grade-5-p-6761.html) | Titanium Grade5 | 4.01 | 8.02 | 16.04 |
| M2x10 socket cap, DIN912 | Microswitch mounting | 2 | 4 | [Product5997](https://alpinpower.com.pl/m2x10-sruba-tytanowa-imbusowa-din-912-iso-4762-tytan-grade-2-p-5997.html) | Titanium Grade2 | 1.60 | 3.20 | 6.40 |
| M2.5x6 socket cap, DIN912 | Housing ears to integral enclosure floor bosses | 3 | 6 | [Product6747](https://alpinpower.com.pl/m2-5x6-sruba-imbusowa-din-912-iso-4762-tytanowa-sruby-tytanowe-grade-5-p-6747.html) | Titanium Grade5 | 4.01 | 12.03 | 24.06 |
| M2 plain hex nut, DIN934 | Two PCB + two microswitch nuts | 4 | 8 | [Product7053](https://alpinpower.com.pl/nakretka-m2-din-934-iso-4032-nakretki-aluminiowe-nakretka-aluminiowa-6061-p-7053.html) | Aluminium6061 | 0.39 | 1.56 | 3.12 |
| M3 plain hex nut, DIN934 | Captive nut for printed H05 retainer | 1 | 2 | [Product7051](https://alpinpower.com.pl/nakretka-m3-din-934-iso-4032-nakretki-aluminiowe-nakretka-aluminiowa-6061-p-7051.html) | Aluminium6061 | 0.23 | 0.23 | 0.46 |
| **Screws + nuts total** | **13 screws + 5 nuts / jog** | **18** | **36** | | | | **26.18** | **52.36** |

### Required washers — additional to the requested screw/nut BOM

| Item | Function | Qty / jog | Qty / two jogs | AlpinPower offer | Offered material | Price / piece | Cost / jog | Cost / two jogs |
|---|---|---:|---:|---|---|---:|---:|---:|
| M2 plain washer, DIN125, ID2.2 / OD5 / thickness0.3 | One under each microswitch screw head, outside the mounting wall | 2 | 4 | [Product7127](https://alpinpower.com.pl/podkladka-m2x5x0-3-din125-iso-7089-tytanowa-grade-2-p-7127.html) | Titanium Grade2 | 0.51 | 1.02 | 2.04 |
| **Screws + nuts + washers total** | | **20** | **40** | | | | **27.20** | **54.40** |

The custom **H05 / JW-H05P is a printed PLA-trial retainer**, one per jog. Do not buy an ordinary M3 grub screw in its place. The M3 nut remains a purchased metal part. There are no additional floor nuts, inserts or washers in the approved jog mounting population. The three floor screws are included above even when the first standalone bench trial does not yet use an enclosure.

### Dimensional comparison and supplier codes

| Item | Approved requirement / baseline | Observed AlpinPower dimensions and code | Remaining difference / limit |
|---|---|---|---|
| M2x4 countersunk | Newstar A4 `M2X4-KHA4MC-SF-DIN7991`; overall length4 including head, headD4/K1.2, nominal90deg, family hex1.27 | `M2x4din7991alu6061`: overall4, shank without head2.8, headD4/K1.2, pitch0.4, hex1.5; DIN7991 description | Aluminium instead of A4; different drive. Attribute also says DIN7991/ISO10642. Exact head-angle/lot tolerances not established; do not treat generic ISO10642 as an accepted substitution. |
| M2x4 cap | Accu A2 `SSCF-M2-4-A2-BL`; under-head length4, headD<=3.8/H<=2, pitch0.4, hex1.5, full thread | `M2x4din912tygr5`: under-head4, overall6, headD3.8/K2, pitch0.4, hex1.5, full thread | Titanium instead of A2; quoted nominal dimensions are not guaranteed maximum tolerances. |
| M2x10 cap | Accu A2 `SSCF-M2-10-A2-BL`; under-head10, headD<=3.8/H<=2, pitch0.4, hex1.5, full thread | `M2x10din912tygr2`: under-head10, overall12, headD3.8/K2, pitch0.4, hex1.5, full thread | Titanium instead of A2; actual lot/usable engagement unverified. |
| M2.5x6 floor cap | Retained reference: under-head6, headD<=4.5/H<=2.5, hex2 | `M2,5x6din912tygr5`: under-head6, overall8.5, headD4.5/K2.5, pitch0.45, hex2, full thread | Main nominal envelope matches. Exact vendor/material was not defined by the retained reference; supplier selection still needs acceptance. |
| M2 nut | Accu A2 `HPN-M2-A2-BL`; AF<=4/H<=1.6, pitch0.4 | Listed code `M2din933alu6061`, despite product title/description DIN934: AF4/H1.6, pitch0.4 | Aluminium instead of A2; supplier code contains DIN933, a catalogue inconsistency to confirm. Corner/chamfer and tolerances not established. |
| M3 nut | Accu A2 `HPN-M3-A2-BL`; AF<=5.5/H<=2.4, pitch0.5 | `M3din934alu6061`: AF5.5/H2.4, pitch0.5 | Aluminium instead of A2; printed H05 thread fit, captive retention and strength still need physical qualification. |
| M2 washer | Accu A2 `HPW-M2-A2`; OD5/ID2.2..2.34/thickness0.25..0.35 | `M2din125tygr2`: OD5/ID2.2/thickness0.3 | Nominal dimensions lie within the stated range; titanium instead of A2, actual tolerances/flatness unknown. |

For countersunk screws, M2x4 means **4 overall including the head**. For the DIN912 screws, length is measured **under the head**. Do not interchange these length conventions. Supplier generic tightening-torque recommendations are not validated torque limits for FDM pilots or the thin printed cover seats.

### Observed availability and search coverage

All seven linked product URLs were actually loaded. On rendered product pages the price metadata matched the table, availability metadata said `InStock`, the product add-to-cart control was visible, and the unavailable panel was hidden. No cart action was performed. The green stock indicator uses a level value `5.0`; **this is not a verified count of five pieces**. Available quantities and delivery dates were not confirmed with the seller.

The user-provided countersunk screw showed shipping from11.57PLN; actual basket shipping remains unverified. Search-engine snippets gave a different price for the floor screw; the table uses the actual rendered product price4.01PLN, not that snippet.

Research covered AlpinPower screw/nut/washer categories, DIN912/DIN125 branches and size-specific searches. No corresponding A2/A4 steel offers were found in that coverage; this is not proof of complete site-wide absence. No alternative fastener retailer was searched. These are found nominal-size candidates, not a claim of the cheapest possible AlpinPower basket.

## Bearing links — two per jog / four per two-jog controller

The engineer supplied the following three links for retention. **SKF61806-2RS1 remains the recommended target and approved design baseline. Lower-cost6806/61806-2RS bearings are for fit/prototype trials, not an automatically qualified SKF replacement.** All three identify the nominal30 bore /42 outside diameter /7 width family; corner radii, usable race faces, tolerances, friction and actual fit are not established by those three nominal dimensions alone.

| Role | Link | Inspection result |
|---|---|---|
| Recommended target / manufacturer reference | [SKF61806-2RS1](https://www.skf.com/us/products/rolling-bearings/ball-bearings/deep-groove-ball-bearings/productid-61806-2RS1) | User-supplied official reference retained exactly. Static reader exposes a JavaScript application shell, not fresh dimensional data. Approved supplier dimensions remain governed by existing design sources. |
| Lower-cost trial candidate | [Allegro6806/61806-2RS, offer16180059900](https://allegro.pl/oferta/lozysko-kulkowe-6806-61806-2rs-30x42x7-16180059900?dd_referrer=) | User-supplied offer retained exactly; direct access returnedHTTP403. Current seller, price, stock and conformity were not independently verified; no access denial bypassed. |
| Lower-cost trial candidate | [Poltech6806-2RS, product1600](https://poltech24.pl/6806-2rs-lozysko-kulkowe-30x42x7-mm-61806-2rs-p-1600.html) | Actual page identifies30x42x7, rubber seals, catalogue6806 2RS and one bearing per offer; shows available. No reliable current product price was extracted. Not confirmed as SKF or as having identical corner geometry. |

Bearing costs are not included in the fastener subtotals. Printed bearing mockups, if later approved, cannot qualify real steel-bearing fit, corner support, friction or life.

## Springs — four per jog / eight per two-jog controller

The accepted baseline remains **Vollmer D-111600070**, catalogue111600070 / legacyD-006A. [Accepted design source record](../schematics/jog-wheel/F12/Jog_Wheel_Rev_F12_components_02.json), retained unchanged in approved D05.

| Parameter | Accepted published/design value |
|---|---|
| Type / material | Compression spring, EN10270-1-DH spring steel |
| Wire diameter | 0.2 |
| Outside diameter | 2.5 ±0.15 |
| Inside diameter | 2.1 nominal |
| Free length | 5 |
| Active coils | 4; not the total coil count |
| Catalogue guide limits | Maximum mandrel1.8; minimum sleeve2.8 |
| Rate used in design | 0.335N/mm per spring |
| Minimum test length used | Ln1.74; **not a published solid/coil-bind height** |
| Installed length | 3.5 released; 2.4 at target switchON; 2.0 at the mechanical stop |
| Four-spring nominal force | 2.01N released; 3.484N at switchON; 4.02N at full stroke |

These are ideal spring forces, not finger-force or physical-return results. The published web page gives0.334N/mm, Ln1.73 and Fn1.09; the accepted catalogue record gives0.335, Ln1.74 and Fn1.092. This is a recorded source discrepancy/rounding, not an invented tolerance. Confirm current data before purchase. End geometry, total coil count, solid height, lot variation and cyclic qualification remain unverified.

### Sourcing result

**No ready-to-buy Polish-market product was confirmed to meet the complete accepted specification. No replacement spring is approved by this note.**

| Source | Actual evidence / purchase status | Decision |
|---|---|---|
| [Lagerfedern / Vollmer D-111600070](https://lagerfedern.net/druckfedern-federstahldraht/Druckfeder-Federstahldraht-D-111600070--d-0-2--De-2-5--Lo-5.html) | Exact accepted part; actual page gives wire0.2/OD2.5±0.15/L05/n4/EN10270-1-DH/rate0.334/Ln1.73. German source, not a verified Polish warehouse. Current price, minimum order, stock, lead time and shipment to Poland not confirmed. | Keep as the exact part reference; do not claim Polish availability. |
| [Dopak — Gutekunst Federn, all27 listed products](https://eshop.dopak.pl/pr/54-gutekunst-federn?resultsPerPage=36) | Polish seller lists Gutekunst springs, including other D-series references. D-006A was not found in the indexed27-product list. This does not establish whether it can be supplied on enquiry. | Best identified domestic catalogue-distribution enquiry lead: ask whether legacyD-006A/current equivalent can be supplied with a complete datasheet. No confirmed equivalent, price or stock. |
| [DamRaf, Poznan — compression springs](https://www.damraf-sprezyny.pl/sprezyny-na-sciskanie/) | Offers individual/short-series manufacture, wire from0.2; published carbon-steel grades SM/SH, not confirmed DH. No exact-part quote or lead time. | Domestic custom-manufacture enquiry lead only, not a compliant offer. |
| [TECH-AR — compression springs](https://www.tech-ar.pl/sprezyna-srubowa-naciskowa/) | Publishes EN10270-1 wire0.2..10 and custom spring production. DH, exact size/rate, quantity/pricing and lead time not confirmed. | Second domestic custom-manufacture enquiry lead only. |
| [Swiat Sprezyn — N71](https://sklep.swiatsprezyn.pl/sprezyny-naciskowe/148-sprezyna-naciskowa-n71.html) | Published wire0.2, OD2.84, ID2.50, freeL12.50, stainless; rate and minimum working length absent. Page metadata price5.00PLN, page stock39 at inspection. | **Reject:** different outside diameter and free length; not a substitute, not included in the purchase BOM. |

Additional searches used the exact Vollmer number, legacyD-006A, Polish spring suppliers and Gutekunst/Lesjofors/Tevema catalogue terms. Search results for Gutekunst D-006A point to a plausible matching data sheet, but direct access to the current data-sheet host returned HTTP403; Maxsprings returned503. These are unverified leads, not evidence of current Polish stock or accepted equivalence. No access denial was bypassed. The available manufacturer catalogue/source record remains the engineering baseline.

### Enquiry specification — not sent

Request quotations for **4 and8 pieces** of VollmerD-111600070, or a fully documented catalogue equivalent. Include wire0.2, OD2.5±0.15, freeL5, EN10270-1-DH, four active coils, rate0.335N/mm and the installed working range3.5..2.0. Ask the supplier to confirm tolerances, force at those two lengths, minimum permitted working length at or below2.0, end geometry, total coils, solid height, cyclic-use limits, price/VAT, minimum order, stock/lead time and Polish delivery. These are requests for supplier data, not new acceptance thresholds or permission to change the spring. Any changed material, dimensions or force characteristic requires engineer review before use.

## Printable test hardware — generator assessment

**CAPABILITY ASSESSMENT, NOT A NEW PRINTED-HARDWARE RELEASE.** The engineer asks whether the linked generators can produce trial parts or whether Basia can give the required clicks. No new STL, sliced plate, G-code or printer job is produced here. Existing approved F12-D05 printed-part STLs remain unchanged. Approval of the jog with purchased hardware does not establish the performance of printed replacements.

### The four supplied MakerWorld models

| Model | Actual purpose and observed capability | Decision for this jog |
|---|---|---|
| [1131125 — Spring Generator, Koolm](https://makerworld.com/models/1131125) | Parametric OpenSCAD compression-spring generator: free length, outside diameter, wire diameter, active coils, dead end coils, variable pitch, circular/rectangular profile and ground ends. Author documents Generate/Download and shows parameters. Actual Customize click in an unauthenticated browser opens a login/sign-up gate. | Can generate spring geometry, but **not a qualified PLA/PETG replacement for our steel spring**. End/total-coil data are incomplete; do not copy example dead-coil settings or claim a functional0.335N/mm spring. |
| [118564 — Various ISO metric nuts, bolts and connectors](https://makerworld.com/models/118564) | A collection of existing threaded parts/profiles based on [TrevM's OpenSCAD ISO library](https://www.thingiverse.com/thing:311031/), not an observed in-page parametric generator. Actual page has no Customize control. The required complete M2/M2.5/M3 population is not established by its description. | Do not print the full example plate or scale an arbitrary screw. Less direct than1055250 for our exact sizes and head types. |
| [34145 — Print-in-place BALL bearings, Jerryie](https://makerworld.com/models/34145) | Actual page lists608 8x22x7,609 9x24x7,6902 15x28x7,6000 10x26x8,6001 12x28x8 and6002 15x32x9. No Customize control observed. | **No listed6806/61806 30x42x7.** Uniformly scaling608 toOD42 gives bore15.2727/width13.3636, not30/7. Anisotropic scaling would distort rolling geometry and is not an accepted fix. |
| [1055250 — Screw Generator, Koolm](https://makerworld.com/models/1055250) | Parametric screw/nut/washer generator using BOSL2; published sizes includeM2, M2.5 andM3. Head/drive, length, nut shape/custom thickness, washer family and fit controls; v2 adds independent shaft/head diameter and custom drive sizing. Actual Customize click opens the login/sign-up gate. | **Preferred supplied fastener generator.** Suitable candidate for geometric trial parts after verifying actual output dimensions. It is not proof that printed M2 threads work on the known nozzle or that every ISO flat head matches the required DIN7991 head. |

### What a printed substitute can and cannot test

| Item | Useful limited trial | What it does not qualify |
|---|---|---|
| Washers and nut-shaped mockups | Nominal assembly stack, access and approximate pocket occupation, if printed dimensions are measured | Metal clamp load, thread strength, real nut corner/chamfer fit or long-term retention |
| M2/M2.5/M3 screws and nuts | Geometry or very light manual assembly trials if the slicer actually resolves the features and a calibrated sample fits | Reliable tightening, repeated threads, screw-head seat strength or retention. Do not force a weak printed screw into an approved thin-seat/pilot feature. |
| A custom30x42x7 printed bearing | Approximate assembly-envelope or deliberately scoped demonstration trials, with independently specified bore/OD/width | SKF/substitute tolerance, corner support, seal/race-face geometry, friction, endplay, life or real-bearing fit |
| The0.2-wire spring in PLA/PETG | At most a separately identified illustrative geometry sample, if it can be printed at all | Steel spring rate, preload, return, travel force, fatigue or switch calibration |

The known nozzle is0.4; the required spring wire0.2 is half that diameter. Matching the steel spring's geometry in PLA/PETG does not match its material response. Increasing wire size, changing coil geometry/material or enlarging spring seats is a design change, not a slicer correction; it needs a new drawing/model decision. Four **active** coils do not uniquely define total coils or end geometry. Do not claim a functional all-printed replacement set for the unchanged jog.

For a functional press/return/friction test, retain real metal springs and bearings; real fasteners are the reliable mounting baseline. For an assembly mockup, explicitly record which bought items are represented by printed stand-ins and do not transfer their results to actual bought-part fit.

### MakerWorld1055250 — click path and target checks

The general labels below come from the author's published UI screenshots/description. Current authenticated fields were not exercised; v2 may lay them out differently. The observed unauthenticated path stops at login.

1. Open the model and sign into the engineer's MakerWorld account, then click **Customize**. Basia did not log in, create an account or bypass that gate.
2. In **General**, use **Display** to choose only the part being prepared, **Spec** forM2/M2.5/M3 and **Thread: Coarse**. Required metric pitches are respectively0.4/0.45/0.5; verify the generated labels rather than scaling a larger fastener.
3. In **Screw**, choose length, head and drive as below. In **Nut**, choose hex and the required thickness; check AF as well. In **Washer**, use the standard-size family, not the large washer.

| Required trial item | Generator selection | Mandatory output check before accepting a trial STL | Qty / jog |
|---|---|---|---:|
| M2x4 cap | SpecM2, Coarse; Screw Length4, Socket head, Hex/Allen drive | Under-head length4; headD3.8/H2; pitch0.4, drive1.5 | 2 |
| M2x10 cap | Same, Screw Length10 | Under-head length10; same head/drive | 2 |
| M2.5x6 cap | SpecM2.5, Coarse; Screw Length6, Socket head, Hex/Allen drive | Under-head6; headD4.5/H2.5; pitch0.45, drive2 | 3 |
| M2x4 countersunk | SpecM2, Coarse; Flat/countersunk head, Hex drive, nominal length4 | **Overall including head4**, headD4/K1.2/90deg; approved baseline drive1.27. A generic flat-head selection is not proof of these dimensions. | 6 |
| M2 nut | SpecM2, Coarse; Nut, Hex; custom thickness1.6 if needed | AF4/H1.6, pitch0.4; do not choose a nylon-insert/flanged or arbitrarily enlarged nut | 4 |
| M3 nut | SpecM3, Coarse; Nut, Hex; custom thickness2.4 if needed | AF5.5/H2.4, pitch0.5; H05 itself remains the existing printed part | 1 |
| M2 washer | SpecM2; Washer, Standard/ISO7089 | ID2.2/OD5/thickness0.3 nominal; accepted thickness range0.25..0.35 | 2 |

4. Inspect debug/dimension information. If a default head, AF or thickness differs, do **not** scale the whole part or silently alter the jog. The published v2 head-diameter control does not establish an independent head-height override. Unresolved dimensions block accepting that part.
5. Once the trial scope, output dimensions and any calibration/clearance choices are accepted, click **Generate**, then **Download** and select STL where offered. Import in Bambu Studio as millimetres at100% scale; check dimensions, measured stack and layer preview before printing. This export path is documented by the author, **not exercised end to end here**.
6. Use the engineer's confirmed machine/nozzle/material profile, not the author's example plate settings automatically. Final layers, orientation, thread compensation and fit calibration remain unconfirmed. Do not enlarge a captive nut's outer hex to make its thread fit.

The spring generator's equivalent documented path is Customize -> Spring dimensions -> Coil -> Generate -> Download. Known baseline inputs areL05/OD2.5/wire0.2/active coils4. **Dead coils/end geometry and a functional printable material/force design are not defined**; this is not a complete accepted spring-print recipe.

### Better or complementary generators

| Tool | Verified useful capability | Limit / recommendation |
|---|---|---|
| [MakerWorld1083205 — Bearing Generator, Koolm](https://makerworld.com/en/models/1083205-bearing-generator-parametric-ball-bearings) | Author documents custom bore, OD, width, flanges, rolling elements, chamfers and clearances, rather than a fixed608 model | Better starting point than34145 for30x42x7. Custom ranges/render/export for that size were not exercised; rolling geometry and print clearances are new choices, not SKF geometry. |
| [mrvarity — Print-in-Place Bearing Generator](https://mrvarity.com/apps/openscad/g/bearing/) and [public standalone SCAD](https://mrvarity.com/apps/openscad/g/bearing/bearing.scad) | Public source actually read: `standard_size=\"custom\"`, `outer_diameter=42`, `bore=30`, `width=7` independently specify the required main envelope. Source clamps bore toOD-8;30 is below34, so those inputs are not clamped. No external include dependency; source header statesMIT. | Strongest local-generation candidate for a **separately approved printed bearing trial**. Internal race/roller geometry, clearance and chamfer defaults are not approved project dimensions. Browser editor opened but default preview stayed pending and the attempted Customize interaction was not delivered; no successful browser render/export is claimed. |
| [LyraMaker Screw Generator](https://lyramaker.com/products/screw/) | Actual browser showsM2/M2.5/M3, Coarse/Fine/None, length4..120, Socket/Flat heads, Hex drive, hex nuts withDIN thickness, standardISO7089 washers, STL/3MF buttons and a visible default screw preview without login | Useful no-login alternative. Independent custom headD/K and AF/H were not established; imported dimensions still need checking. Its own advice calls for0.2-mm nozzle forM3 and smaller, unlike our known0.4 setup. No custom STL export or physical print tested. |
| [LyraMaker Spacer Generator](https://lyramaker.com/products/spacer/) | Actual fields independently set OD, hole diameter and thickness | **Not suitable for our0.3-mm washer through its current UI:** thickness slider minimum is0.6, step0.2. Do not follow the generic “any size” description or bypass that control. |
| [FreeCAD Fasteners Workbench](https://github.com/shaise/FreeCAD_FastenersWB) / [BOSL2 screw API](https://github.com/BelfrySCAD/BOSL2/wiki/screws.scad) | Editable local alternatives; BOSL2 documents custom screw/nut specification structures | Not the smallest next step: dependencies/workbench availability are not confirmed and nothing was installed. StandardISO10642 remains distinct from an accepted thin DIN7991 head. |

For mrvarity the documented path is **Open generator -> Customize -> Size: Custom -> outer_diameter42 / bore30 / width7 -> review rolling/fit/chamfer choices -> Render -> Export STL**. Its landing page and SCAD agree on independent dimensions. This is a candidate workflow, not a verified STL or permission to choose its internal mechanical geometry. Do not copy the site's suggested0.4 clearance or0.5 chamfer into an approved purchased-bearing fit claim.

`openscad --version` actually returns **OpenSCAD2026.10.11** on this workstation. Together with the public standalone bearing source, this provides a technically available local route without installing a new library; the source has not been rendered/exported for a project substitute. BOSL2 installation was not established by the inspected usual library directories. A simple dimensioned washer also does not inherently require a third-party generator, but no new CAD geometry or trial export is made by this assessment.

Spring-winding jigs are not an immediate substitute: [Spring-Winder](https://github.com/chadkirby/Spring-Winder) describes small torsion springs using about1-mm wire and a steel mandrel, not the specified0.2-mm compression spring; [MakerWorld spring-making tools190439](https://makerworld.com/en/models/190439-spring-making-tools) does not establish the needed wire/coil process. Neither is an approved manufacturing route forD-111600070.

### Source licences and actual verification boundary

- MakerWorld1055250: visible **CC BY-NC-SA4.0**;118564:CC0;34145:CC BY4.0.
- MakerWorld1131125 and1083205: visible **Standard Digital File License**, including restrictions on redistribution and derivative files/prints. Do not automatically place those models/generated derivatives into a distributable repository or handoff; use the maker's allowed personal-use workflow or obtain permission. No downloaded generator/source/derivative from these models is copied into this repository.
- mrvarity's public SCAD header statesMIT. LyraMaker application-code licensing was not established; use of BOSL2 does not establish the whole site's code licence.
- Actual runtime evidence: four supplied MakerWorld pages opened; both supplied customizers tested up to their login gate; both static collections checked for controls/sizes; LyraMaker inputs and default screw preview inspected; spacer minimum thickness observed; mrvarity public source read and editor opening attempted. No authenticated customizer session, successful custom bearing render/export, new mesh validation, slicing or physical trial is claimed.
- No task-created temporary files are retained. Browser-managed screenshots are inspection evidence only, not Fusion-model review views or final manufacturing deliverables.

### Subsequent trial-STL request — resolved generator blocker and verified delivery

The engineer requests actual STL preparation using mrvarity bearings and LyraMaker screws/nuts/washers. Separate modelF12-TH01 is now explicitly approved and delivered: [eight verified STL files and quantities](../models/jog-wheel/F12-TH01/Jog_Hardware_Rev_TH01_STL_handoff.md),22 instances per jog /44 per two-jog controller, excluding springs and retaining H05 as the existing printed part. No approved F12-D05 jog STL was overwritten. All eight actual files import successfully in BambuStudio; no slicing or printer job was performed.

Actual LyraMaker browser exercise: SpecM2, Coarse, Flat head, Hex drive, Length4, then Generate. The website reports `ERROR: Assertion 'is_def(entry)' failed: Screw size M2 unsupported for head type "flat"` in its bundledBOSL2 `screws.scad`, line2884. Download is disabled; no STL was produced. Source inspection confirms the large/hex countersunk table starts atM3, while the small M2 countersunk table is a different head/drive family. This is not evidence that M2 DIN7991 itself is unavailable; it is a limitation of this generator. No alternate drive/head, scaling or library patch is silently substituted.

The same published bundle defines socket headsM2 asD3.8/H2 andM2.5 asD4.5/H2.5; DIN nutsM2 asAF4/H1.6 andM3 asAF5.5/H2.4. LyraMaker's standardM2 washer table isID2.2/OD5/t0.3. These source checks support selecting those nominal variants but are not mesh/print verification.

The engineer explicitly selects **Osobny model nominalny** and **Przyjac ustawienia autorow**: prepare the M2x4 countersunk nominal model outside the standard LyraMaker UI using the accepted DIN7991 envelope, and use the published trial settings for the rest. Accepted trial settings: LyraMaker nut `$slop=0.1`; mrvarity automatic double-cone rollers, clearance0.4 and chamfer0.5, keeping bore30/OD42/width7. This is explicit trial-geometry selection, not calibrated fit/strength or a change to the approved jog. Native Fusion documents and approved STLs remain untouched.

After the actual eight-model view/check review, the engineer explicitly selects **Zatwierdzam F12-TH01**, authorizing the named trial model and eight STL/mm writes at `models/jog-wheel/F12-TH01/`. [Approval and frozen review hashes](APPROVALS.md#engineer-approval-of-f12-th01-printed-trial-hardware-model-and-stl-destination). The delivered files are byte-identical to reviewed preview meshes; [actual export checks](../models/jog-wheel/F12-TH01/Jog_Hardware_Rev_TH01_STL_exports.json) and [all-eight BambuStudio imports](../models/jog-wheel/F12-TH01/Jog_Hardware_Rev_TH01_Bambu_info.json) are recorded. This supersedes earlier no-export capability-assessment labels only for this separately approved trial set; no physical/production qualification or whole-jog/controller approval is implied.

### Spring S01 — manual experimental parameter proposal, not a qualified replacement

The engineer separately asks for manual MakerWorld1131125 spring inputs. The author's published [Spring control screenshot](https://makerworld.bblmw.com/makerworld/model/USbe15ee1e6794ff/design/2025-02-20_481d92f802b22.png?x-oss-process=image/resize,w_1000/format,webp) labels Coils as the number of active coils. Proposed S01 inputs:

| Control | Value | Basis |
|---|---|---|
| Spring Length | 5 | Accepted steel spring free length |
| Spring Diameter | 2.5 | Accepted outside diameter |
| Spring Coils | 4 active | Accepted active-coil count; verify the generated debug label reports4 active |
| Dead_Coils top | 1 | Experimental proposal, not documented original end geometry |
| Dead_Coils bottom | 1 | Experimental proposal, not documented original end geometry |
| Spread | 0 | Proposed uniform pitch |
| Midpoint | 0.25 | Retained UI default; expected inactive with Spread0 |
| Wire diameter | 0.2 | Accepted steel-wire diameter, not a qualified FDM strand size |
| Grounded flat ends | Yes | Experimental seating proposal, not confirmed original ends |
| Octagonal coil shape | No | Retain circular coil path |

No S01 STL is produced by Basia. This proposal is not manufacturer reconstruction, approval of new end geometry, measured force or a steel-equivalent PLA/PETG design. Engineer must check4 active coils andOD2.5/L5 after Generate and continuous strands in the actual layer preview; no automatic wire thickening or seat changes. The known nozzle is0.4, so successful physical printing at wire0.2 is unproven. MakerWorld credentials, passwords,2FA codes and session tokens must not be sent; the current hardware generators need no login.

## Checks and remaining gates

- Compared all seven purchased-fastener rows with approved quantities and their published critical nominal dimensions; six are the requested screws/nuts and the seventh is the required washer.
- Recomputed13 screws/5 nuts/2 washers per jog,26/10/4 for two jogs; no spares silently added. Decimal arithmetic gives26.18/52.36PLN for screws+nuts and27.20/54.40PLN including washers.
- Recomputed four-spring forces using `4 * 0.335 * (5 - installed_length)`:2.01/3.484/4.02N. This is not a new native geometry, physical fit, spring-rate or return test.
- Final BOM quantities/prices/local source links are checked against the actual document and frozen source data before handoff. No task-created temporary file was required; browser-managed screenshots are not final deliverables.
- **APPROVED scope unchanged:** F12-D05 drawing/model, nominal prototype only. **CHANGES REQUIRED before treating this as an approved alternative-parts purchase list:** engineer acceptance of the offered hardware/materials and supplier confirmation of the springs. Actual assembled fit, thin-seat/pilot strength, H05 retention, moving-mass/friction/return and switch calibration remain physical tests. No CAD correction or approval is implied by a catalogue match.
