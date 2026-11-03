# beatbreaker — Product Design

This document describes the current design and its boundaries, not an assembly certification or work log. Open work belongs in [TODO.md](TODO.md); scoped release decisions and files are recorded in [approvals](docs/APPROVALS.md) and the [artifact register](docs/ARTIFACTS.md). Dimensions are in millimetres unless stated otherwise. Selected components, nominal CAD checks and physical qualification are different things.

## 1. Product and scope

beatbreaker is a DIY two-deck DJ/MIDI controller intended to run Mixxx on a Raspberry Pi 4, with an ESP32-S3 reading controls and driving indicators. The Pi is intended as USB host and the ESP as USB MIDI device; a separate USB-to-UART connection is intended for development. Complete firmware, mapping and integrated electronics are not yet available.

**REV_B is the sole current release, approved for an unpowered mechanical trial only.** It consolidates the accepted B26-LAP-build123d11 geometry, including integral controller holders. Use the [complete drawing](schematics/REV_B/beatbreaker_REV_B_drawing.pdf), [standalone build123d source](models/REV_B/beatbreaker_REV_B.py), [validation/BOM/environment/handoff JSON](models/REV_B/beatbreaker_REV_B_validation.json), [STLs](models/REV_B/STL/) and [assembly STEP](models/REV_B/beatbreaker_REV_B_assembly.step). The [engineer's acceptance](docs/APPROVALS.md#engineer-accepts-all-controller-holders-and-authorizes-updating-rev_b) and [release register](docs/ARTIFACTS.md) define their scope. REV_A and earlier releases are history, not current authorities; earlier approvals remain valid only within their own recorded scope.

The 43-file package contains 37 STL definitions for 169 printed occurrences. The recorded source replay and PDF reconstruction match 565 represented occurrences; mesh and STEP checks have the coverage and limits in the JSON. Nine inherited cap definitions are exact meshes without recovered analytic histories. Purchased equipment representations are incomplete. None of these results qualifies actual fit, print process, strength, electrical or thermal safety, or production.

Enclosure parts are selected as PETG; jog and cap materials remain TBD. A Bambu Lab P2S with 0.4 mm nozzle and a reported 256 × 256 mm XY bed is available. The 250 × 250 × 250 mm screen is a conservative nominal part-bound screen, **not automatic printer-fit or print approval**. The [variant B recipe](docs/PRINT_SETTINGS.md) is selected for the 4 mm PETG floor trial, with 0.20 mm layers assumed; applied settings, orientation, supports, calibration and physical results remain open. Variants A and C are optional comparisons, not a change to the selection.

## 2. Functions and controls

Counts are for the whole controller. These are design targets, not a working integration.

| Function | Definition and limits |
|---|---|
| Decks and jogs | Two non-pressing B26 jog assemblies with AS5048A magnetic sensors. F.11 is withdrawn and F12 is not pursued; their press switches and springs are not B26 requirements. |
| Mode | An additional NUDGE/SCRATCH button is requested; its location, component, behavior, mapping and input allocation are **TBD**. It is not included in the 30 existing buttons. |
| Buttons | 30 panel buttons: B01–B24 and T01–T06. B3F-family input is a reference; exact electrical variant, stroke, return and cap engagement remain unverified. |
| Browse | One incremental rotary encoder, A/B rotation only. Its push contacts are unused and left unconnected; no push MIDI action. |
| Analog | 13 10 kΩ rotary potentiometers and five faders. Taper, electrical variants and pinouts are not all confirmed. |
| Indicators | 20 SK6812 RGBW LEDs in two 10-LED chains for stereo master VU only, not deck meters. Optical mechanics and diffuser are deferred. |
| Audio | Raspberry Pi DAC Pro, selected dual RCA panel and headphone interface; wiring, signal and detect behavior remain TBD. |

The resulting demand is 18 analog controls, 30 existing button inputs plus the unspecified mode control, three rotary channels and two LED data outputs. Two PCF8575 modules are planned; their final allocation must be reconciled with the mode decision. The earlier E01 allocation predates the non-pressing jog and is not a wiring release.

## 3. Mechanical assembly and trial boundaries

The release drawing and JSON govern represented geometry, locations and quantities. The nominal panel is 600 × 300; table coordinates use rear-left origin, X right and Y toward the front, with CAD Y = −table Y. The lower shell has a 4 mm floor, 2 mm walls, overlapping joints, 14 bridges and 18 removable feet; use the release for the detailed geometry and hardware. The engineer reported flexing when lifting the empty enclosure. The earlier 1 kg lifting case was a provisional assumption, not a measured assembled mass or strength rating. Establish actual mass, agreed deflection limits and loaded joint performance physically.

### Proposed lower-shell joint redesign

The redesign intent is to address the reported flex using the released lap/bridge and foot arrangement, not a verified improvement. The floor occupies nominal Z −2 to 2, retaining the former interior floor surface at Z 2; the underside is flat apart from removable feet. Feet use trial tapered pegs and adhesive pads; the nominal interference zone is only 0.3 mm along the taper. Fit, repeated insertion/removal, retention, creep, pad adhesion and friction, leveling, load sharing, seam and wall-lap fit, hardware and tool access remain physical checks. The trial pad is 3M Bumpon SJ5012, a self-adhesive polyurethane elastomer; the manufacturer's typical 12.7 diameter × 3.5 height dimensions are not purchase or fit verification. Do not infer safe lifting from the CAD.

The removable-foot study was inspired by [MandicLab's feet.stl](https://github.com/mandiclab/djc-diy/blob/main/3D%20models/feet.stl); that project identifies CERN-OHL-S-2.0. REV_B contains 18 FT03 feet. The reference does not prove the original pegs latch or the trial feet retain; review attribution and licensing implications before any adaptation of protected source. This reference does not determine this repository's license.

### Jog and sensor mounting

The selected AS5048A PCB seat is integral to C04/C06 and remains with the shell when the jog is removed; the PCB is removable. Alignment depends on jog-to-floor mounting, and a damaged integral seat can require shell repair or reprint. Remove upper panels for installation/service; do not assume the whole jog passes through the panel opening. The supplied sensor reference is 15 × 17, with two Ø2.2 holes on 12 pitch and a confirmed 2 mm bare laminate; actual component heights, lands and breakout implementation are unverified. Each jog uses a selected Ø8 × 4 N35/Ni diametric magnet. Verify actual clearance, magnetic readings, rotation, fasteners and service fit.

The original screen recorded **24 failed upper sharp-bearing-reference pair-poses**. A separate source-bound check passes the **selected SKF 61806-2RS1 nominal upper shaft-abutment interface** (modeled R0.2 fillet and Ø32.2 shoulder versus SKF limits); it does not erase those failures, reconstruct the actual bearing corner, certify the whole assembly or transfer to substitutes. Actual bearing identity, seating, free rotation, endplay/preload and non-SKF compatibility require real trials. See the [release validation](models/REV_B/beatbreaker_REV_B_validation.json) and [SKF sheet](elements/SKF_61806-2RS1_product_sheet_2020-09-30.pdf).

### Controller holders

C04 contains U1 ESP and U2 PCF8575 holders; C06 contains U3 PCF8575 and U4 CD74HC4067 holders. Install boards in open lower shells before controls, jogs, other equipment and upper panels. ESP slides into its edge holder from smaller toward larger table Y; the opposite approach was obstructed in the sampled reference. The trial uses nominal 0.1 mm per-side interference, not measured insertion force or retention.

Both identical PCF boards and the mux have **2 mm laminates, flat finished undersides, no headers and top-only soldered wires**. Underside solder or protrusions invalidate that selected bearing configuration. ESP uses its unchanged reversed headers, projecting 8 mm below the PCB; the upper connected envelope budget is 3 mm. Board insertion, damage, support removal, retention under plug loads, insulation, fatigue and PETG creep are not physically qualified. The rejected B25-MOUNT-01 holder geometry and its goldpin conflict must not be reused. DAC retention is **TBD**: plain modeled pads do not establish screw retention, and temporary hot glue is not structural or electrical approval.

### Appearance

The selected Pine Cherry palette is dark beige top-panel segments, pine green lower shell and raised display housing, red HOT CUE/CUE/PLAY-PAUSE and five fader caps, and dark brown rotary knobs and remaining small button caps. Each printed part is single-color. Jog platters and internal parts have no new color assignment; actual filament shade and finish are unverified. This is an appearance decision, not a material, geometry or print qualification.

## 4. Confirmed inputs and interfaces

### Controls and retained interfaces

- **Faders:** two tempo and two volume controls have 41 mm travel; the crossfader has 28 mm. The supplied body is 60 × 9 × 6 excluding terminals, blade 4 × 1, exposed lever 15, without mounting holes. Retain end cups, central supports and selected cap interfaces. Actual terminal/solder clearance, full travel and cap grip remain unverified. The historical tempo source mesh had duplicate/nonmanifold shoulder facets; do not silently infer a repaired editable feature history from it.
- **Pots:** 13 × 10 kΩ, with stated shaft length 23 mm, retained asymmetric corner cradles and removable retainers. The electrical taper and precise shaft datum remain TBD; do not subtract cap depth from shaft length across unmatched datums. Verify actual bearing, collar, terminals and knob fit; no threaded clamp or side-adjustment mechanism is assumed.
- **Buttons and caps:** retain the selected B3F-family interface and approved cap meshes. The 1.8 mm source callout is not established switch travel. The engineer reported good button/fader/pot seat fit for tested B18 hardware; that does not establish fit or strength of the complete REV_B assembly.
- **BROWSE:** supplied [encoder drawing](elements/encoder_browse.png) specifies A = 7, L = 15, M7 × 0.75 bushing and nominal Ø6 D-shaft. Actual rotary contacts, cap grip and electrical assignment remain open; push is unused.

### Display installation contract

The engineer supplied an external **276 × 76** outline and confirmed **2 mm overlap on each edge**, retaining the **272 × 72** opening centred at table (300, 46.25). Rear insertion is selected: the display front bears on the **panel underside**. The confirmed **17 mm** depth is from that front bearing surface to the indicated rear frame land, not total display thickness and not an additional 17 mm. The right short-side rear-frame bearing band A is 2 mm; left-side mirrored contacts are a nominal selection, not a measured matching band. The release includes rear toes, columns, guides and reverse M3 × 8 access. Actual rear body, image visibility, frame lands, toe sweep, plug clearance, service access and retention strength remain unverified. The supplied [display image](elements/EP-0189-05.webp) is a reference; actual display identity remains TBD and catalogue dimensions do not override the confirmed opening/datum.

### Pi and DAC

Pi 4 Model B reference PCB is 85 × 56 × 1.6 with four Ø2.7 mounting holes on 58 × 49 pitch; see the [supplied drawing](elements/RP-008343-DS-1-raspberry-pi-4-mechanical-drawing.pdf). Raspberry Pi DAC Pro is selected. The low-profile successor separates Pi and DAC using a 40-pin cable; actual cable, installed board envelopes, fastening and service fit remain unverified. DAC pads in REV_B do not establish retention.

For the earlier B19 **direct-stack** configuration only, the engineer confirmed 36 mm from the Pi PCB underside to the highest DAC element, M2.5 × 10+6 spacers and measured 4 mm thread projection below the Pi. These are retained measurements of that assembly, not a claim that REV_B uses the direct stack or that its separated-board installation has that envelope. The DAC source documents have a 65 × 58 versus 65 × 57 outline discrepancy; reconcile the actual board before relying on a complete envelope.

### Selected panel RCA

The selected dual RCA panel is **Goobay/Wentronic 11310 (CP02)**: face 51.7 × 19.9, mounting pitch 43.9 and two Ø3.6 holes. The mounting row is 9.9 from the lower face edge, not the 9.95 face midpoint. The engineer confirmed 24 inward from the inner shell face. The delegated printed trial window is 34.9 × 15.9, not a supplier cutout specification; face centre is table (265, 0, 18). Actual rear body, terminals, retention, connected fit and audio wiring remain unverified. See the [supplier drawing](https://www.electrokit.com/upload/product/41003/41003608/41003608.pdf).

The headphone reference is the supplied [3.5 mm jack](elements/pol_pl_Gniazdo-jack-sluchawkowe-3-5mm-przykrecane-pozlacane-PJ-392-x2-szt-20242_6.webp), filename PJ-392, drawing title PJD-035-77D; M6 × 0.5 thread and maximum Ø8.15 bare body. One jack and nut are needed, not necessarily the two-piece pack. Earlier top-panel position (14,14) belongs to the historical R12 layout; use REV_B for the current represented position. Actual variant, fit, plug/solder clearance and DAC headphone connection/detect remain open. Do not substitute RCA line outputs for headphone signals.

### Selected mains inlet

The engineer identified the purchased inlet/switch/fuse-holder assembly using [this supplied drawing](elements/gniazdo_zasilania_nowe.png). Its source calls out nominal 47.5 × 28 cutout with +0.1 on height, 50 × 30.5 face, 3 mm flange and sectional depths 30.5/29.4. The declared 25.5 inward proxy is 30.5 − 3 flange − 2 wall, not measured complete terminal geometry. The older inlet image and its different cutout are not the selected source. Actual model/ratings, clip capture at the wall, corner/registration, terminals, printed fit and protection are not established.

### Rear ventilation and scope

Two matching rear honeycomb grilles are represented at X20–90 and X510–580, Z10–38, 24 hexagonal cuts each, nominal 6 across flats and 1.2 web in a 2 mm wall. They are not evidence of adequate airflow or a mains touch barrier. Actual thermal behavior, terminal protection and unobstructed air paths remain open. Cables/plugs and mains protection are engineer-owned under a geometry-neutral assumption, **not** a connected-fit or safety approval. Program the ESP with the enclosure open; no external programming aperture is selected. The Keple USB/AUX module and Behringer U-PHONO UFO202 are deferred; UFO202 has no current mount or reserved geometry.

## 5. Electronics, power and safety

The selected supply is **Mean Well RS-25-5**, rated 5 V / 5 A / 25 W; its [datasheet](elements/05839_datasheet.pdf) covers multiple output variants. It is an open-terminal mains component, with AC/L, AC/N and FG, 88–264 VAC input, free-air convection and derating. The selected supply rating is not a complete power budget or an identified display rail. Define and approve inlet ratings, fusing/protection, PE continuity, terminal guarding, strain relief, separation, wiring, thermal installation and the complete power tree before energizing. Do not invent ratings or assume that component certification qualifies a printed enclosure. An independently certified enclosed adapter is the safer bench route until the internal installation is released.

Native ESP USB is intended for MIDI to the Pi; USB-to-UART is for programming/logging. Native D−/D+ are GPIO19/20. Neither port should be assumed data-only or isolated from another host VBUS. External supply, Pi and development USB combinations require an explicitly verified power path, ground, VBUS sensing, attach/detach and back-feed protection; a cut cable or D+/D−/GND alone is not a complete design. Never apply 5 V to 3V3 or ADC pins.

The following are **proposals**, not approved wiring or a frozen GPIO map:

- Power pots, CD74HC4067 and PCF8575 at 3.3 V subject to regulator budget. Route 13 pot wipers via mux channels 0–12, leaving 13–15 spare; use five direct ADC inputs for faders, preferably ADC1. Settle, filter and calibrate actual endpoints.
- PCF buttons switch to ground using quasi-bidirectional inputs; individual external 10 kΩ pull-ups are not initially proposed. Distinct addresses and a suitable I²C SDA/SCL pull-up pair to 3.3 V are still required, accounting for breakout resistors. Shared INT is conditional on verified open-drain outputs and pull-up; verify clearing and debounce.
- Earlier candidate assignments were faders GPIO1/2/4/5/6, mux SIG 7 and select 8–11, I²C 12/13, conditional INT 14, jog SPI 15/16/17 with CS 18/21, BROWSE 39/40 and LED data 41/42. Confirm actual board exposure, sensor breakout and mode allocation before use. GPIO34 is not an ESP32-S3 ADC; GPIO35–37 may be used by flash/PSRAM, GPIO38 may share onboard RGB, and GPIO0/3/45/46 have boot/strapping concerns. Board memory/module variant is not confirmed.

The electrical draft E01 is not approved for complete wiring or energizing and is not yet published as a release. Breadboard work, integrated point-to-point wiring and any later PCB each require their own appropriate validation.

## 6. LED subsystem

The selected [SK6812 RGBW strip](https://botland.com.pl/paski-led-adresowane/12486-pasek-led-rgbw-sk6812-cyfrowy-adresowany-ip65-144-ledm-432wm-5v-1m-5904422319373.html) is 5 V, 144 LEDs/m, 12 mm wide, silicone-covered IP65 as supplied, cuttable after each LED. MAIN_L is L01–L10 and MAIN_R L11–L20; existing panel apertures are retained. Cutting and soldering do not automatically preserve IP65. Strip, diffuser, optical performance and mechanical mounting are deferred.

Two channels of one 5 V 74AHCT125 are planned for data level shifting. Proposed initial series resistors are 330 Ω per active chain (220–470 Ω adjustment range), with 100 nF local decoupling and 470–1000 µF bulk capacitance at the full LED entry; unused-channel handling remains to be defined. These are prototype values, not measured optima or a wiring release. Supplier current scaled to 20/144 m is approximately 1.25 A / 6.25 W at 5 V for LEDs alone, not a measured maximum or system budget. Verify brightness, current, voltage drop and temperature; do not route full LED current through the breadboard or DevKit traces.

## 7. Firmware and host

The intended architecture separates hardware drivers, input processing, logical events, MIDI mapping and LED feedback. Pots/faders are intended to send CC; buttons use Note or CC, BROWSE sends relative rotation only, and Mixxx supplies master meter feedback. NUDGE/SCRATCH behavior, message IDs, relative encoding, release semantics, feedback mapping, Mixxx version and USB stack remain TBD. Wi-Fi/BLE are outside the current implementation.

The existing [bench diagnostic](firmware/bench_inputs/README.md) reports one fader, pot, button and AS5048A over serial; it is not complete MIDI or mode firmware. Confirm the actual board, sensor pinout, supply and terminals before wiring/upload. Use its isolated USB-only bench configuration, without unverified mains/Pi/LED power combinations. Raw ADC counts are not calibrated travel and may saturate near 3.3 V.

## 8. Bill of materials boundary

The [REV_B JSON](models/REV_B/beatbreaker_REV_B_validation.json) `printed_parts` is the source for printed STL filenames, quantities and checksums, including jog and caps. It is **not** a complete purchased-part, hardware or order-ready BOM. Confirm actual variants, stock, electrical compatibility, fit and fasteners before ordering or installation.

| Quantity | Item | Boundary |
|---:|---|---|
| 1 each | Raspberry Pi 4, DAC Pro, display | DAC selected; actual display identity, installed interfaces and DAC retention open |
| 1 each | Mean Well RS-25-5 and selected mains inlet/switch/fuse-holder | Supply selected; inlet ratings, protection, power budget and safe installation open |
| 1 each | Goobay 11310 dual RCA panel and 3.5 mm headphone jack | Source references selected; actual fit and audio wiring open |
| 1 | ESP32-S3-DevKitC-1 | v1.1 mechanical reference, exact module/memory variant TBD; reversed headers |
| 2 | PCF8575 modules | Identical 32 × 21 × 2 PCBs, components 2 above; flat underside/no headers/top-only wires |
| 1 | CD74HC4067 module | Body 41 × 18 × 3.6 excluding pins; PCB 2, components 1.6 above; same flat/no-header wiring configuration |
| 13 | 10 kΩ potentiometers | Taper and exact electrical variant TBD |
| 5 | Faders | Four 41 mm travel, one 28 mm; electrical variant and pinout TBD |
| 30 | Panel switches | 24 B and six T; exact switch variant TBD; mode button additional and TBD |
| 1 | BROWSE encoder | Rotary only; push unused |
| 2 | AS5048A modules | Actual breakout and sensing interface TBD |
| 4 | Jog bearings | SKF 61806-2RS1 reference; actual bearing fit and substitutes unverified |
| 2 | Ø8 × 4 N35 diametric magnets | Magnetic fit/operation unverified |
| 20 | SK6812 RGBW LEDs | Two 10-LED master VU chains; optics and power validation open |
| 1 | 74AHCT125 | Two planned active data channels; circuit details TBD |
| TBD | Fasteners, pads, connectors, wiring, protection, decoupling and USB power-path parts | Quantities, ratings and installation require actual-interface and safety work |

Engineering changes require an affected revision and named approval. Physical trial results, open questions and acceptance gates are tracked in [TODO.md](TODO.md#prototype-gates); no release claim here substitutes for them.
