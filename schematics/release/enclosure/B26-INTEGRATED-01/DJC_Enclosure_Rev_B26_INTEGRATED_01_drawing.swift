import AppKit
import CoreGraphics
import CryptoKit
import Foundation
import PDFKit

let root=URL(fileURLWithPath:FileManager.default.currentDirectoryPath)
let destination=root.appendingPathComponent("schematics/enclosure/B26-INTEGRATED-01/DJC_Enclosure_Rev_B26_INTEGRATED_01_drawing.pdf")
precondition(!FileManager.default.fileExists(atPath:destination.path),"Refusing to overwrite drawing")
struct Source {let path:String;let pages:[Int]?;let role:String}
let sources:[Source]=[
 Source(path:"schematics/enclosure/B26-DETAIL-01/DJC_Enclosure_Rev_B26_DETAIL_01_drawing.pdf",pages:nil,role:"B26 layout and fader delta"),
 Source(path:"schematics/enclosure/B26-ROOF-01/DJC_Enclosure_Rev_B26_ROOF_01_drawing.pdf",pages:nil,role:"Roof, display and retention"),
 Source(path:"schematics/enclosure/B26-REAR-POST-03/DJC_Enclosure_Rev_B26_REAR_POST_03_drawing.pdf",pages:nil,role:"Four rear closure axes"),
 Source(path:"schematics/enclosure/B26-JOINTS-03/DJC_Enclosure_Rev_B26_JOINTS_03_drawing.pdf",pages:nil,role:"Fourteen shell bridges"),
 Source(path:"schematics/enclosure/B26-INTEGRATION-01/B26_roof_shell_drawing.pdf",pages:nil,role:"Roof, shell and two additional bridges"),
 Source(path:"schematics/enclosure/B26-PANELS-03/DJC_Enclosure_Rev_B26_PANELS_03_drawing.pdf",pages:nil,role:"Six flat panels and current jog seam"),
 Source(path:"schematics/enclosure/B17/DJC_T_cap_Rev_B17_drawing.pdf",pages:nil,role:"Triangle cap geometry"),
 Source(path:"schematics/frontpanel/K02/DJC_Keycaps_Rev_K02_drawing.pdf",pages:nil,role:"40 mm cap foundation geometry"),
 Source(path:"schematics/frontpanel/K03/DJC_Keycaps_Rev_K03_drawing.pdf",pages:nil,role:"40 mm CUE, PLAY and HOT CUE caps"),
 Source(path:"schematics/jog-wheel/F13-STATIC-01/Jog_Wheel_F13_STATIC_01_DRAFT.pdf",pages:nil,role:"Jog rotor, carrier, covers and collars"),
 Source(path:"schematics/jog-wheel/F13-STATIC-02/Jog_Wheel_F13_STATIC_02_drawing.pdf",pages:nil,role:"Static sensor and underside fixing amendment"),
 Source(path:"schematics/jog-wheel/F13-STATIC-04/Jog_Wheel_F13_STATIC_04_drawing.pdf",pages:nil,role:"Foot / web clearance amendment"),
 Source(path:"schematics/jog-wheel/F13-PANEL-06/F13_PANEL_06_drawing.pdf",pages:nil,role:"Y165 seam and candidate jog approach"),
 Source(path:"schematics/jog-wheel/F13-TOOLS-01/F13_collar_tools_drawing.pdf",pages:nil,role:"Trial collar-tool interfaces"),
 Source(path:"schematics/jog-wheel/F12-D05/Jog_Wheel_Rev_F12_D05_DRAFT.pdf",pages:[4,5,9,14],role:"Selected sensor peg, boss, toe and nut-entry sheets only")]
let dataSources=[
 "schematics/frontpanel/R12/DJC_frontpanel_R12_DRAFT_coordinates.csv",
 "schematics/frontpanel/K01/DJC_Keycaps_Rev_K01_definition.json",
 "schematics/frontpanel/K02/DJC_Keycaps_Rev_K02_definition.json",
 "schematics/frontpanel/K02/DJC_Keycaps_Rev_K02_logo_sources.json",
 "schematics/frontpanel/K03/DJC_Keycaps_Rev_K03_definition.json",
 "schematics/enclosure/B17/DJC_T_cap_Rev_B17_definition.json",
 "old_case/performance-pad.stl",
 "old_case/knob.stl",
 "old_case/tempo-fader.stl",
 "old_case/crossfader.stl",
 "schematics/enclosure/B09/DJC_Enclosure_Rev_B09_controls.json",
 "schematics/enclosure/B09/DJC_Enclosure_Rev_B09_equipment.json",
 "schematics/enclosure/B19/DJC_Enclosure_Rev_B19_definition.json",
 "schematics/enclosure/B22/DJC_Enclosure_Rev_B22_definition.json",
 "schematics/enclosure/B22/DJC_Enclosure_Rev_B22_validation.json",
 "schematics/enclosure/B24/DJC_Enclosure_Rev_B24_validation.json",
 "schematics/enclosure/B24-JOINTS-02/DJC_Enclosure_Rev_B24_JOINTS_02_definition.json",
 "schematics/enclosure/B24-AC01-LOW-01/DJC_Enclosure_Rev_B24_AC01_LOW_01_definition.json",
 "schematics/enclosure/B25-ELEC-02/DJC_Enclosure_Rev_B25_ELEC_02_definition.json",
 "schematics/jog-wheel/F12-D05/Jog_Wheel_Rev_F12_D05_definition.json",
 "models/enclosure/B15/DJC_Enclosure_Rev_B15_inputs.scad",
 "models/enclosure/B19/FUSION/DJC_Enclosure_Rev_B19_Fusion01_BOM_and_exports.json",
 "models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_BOM_and_exports.json",
 "models/enclosure/B24/FUSION/DJC_Enclosure_Rev_B24_Fusion05_validation.json",
 "models/enclosure/B16/FUSION/CAP_B_Rev_B16_Fusion01.stl",
 "models/enclosure/B17/FUSION/CAP_T_Rev_B17_Fusion01.stl",
 "models/enclosure/B16/FUSION/CAP_P_Rev_B16_Fusion01.stl",
 "models/enclosure/B16/FUSION/CAP_F_Rev_B16_Fusion01.stl",
 "models/enclosure/B16/FUSION/CAP_C_Rev_B16_Fusion01.stl",
 "models/enclosure/B16/FUSION/CAP_E_Rev_B16_Fusion01.stl",
 "models/enclosure/B24/FUSION/KEYCAPS_K03/CAP-CUE40_Rev_K03_Fusion03.stl",
 "models/enclosure/B24/FUSION/KEYCAPS_K03/CAP-PP40_Rev_K03_Fusion03.stl",
 "models/enclosure/B24/FUSION/KEYCAPS_K03/CAP-HC40_Rev_K03_Fusion03.stl",
 "models/enclosure/B24/BUILD123D/shell.py",
 "models/enclosure/B24/BUILD123D/panels.py",
 "models/enclosure/B24/BUILD123D/controls.py",
 "models/enclosure/B24/BUILD123D/caps.py",
 "models/enclosure/B24/BUILD123D/bridges.py",
 "models/enclosure/B24/BUILD123D/hardware.py",
 "models/enclosure/B24/BUILD123D/display_toes.py",
 "models/enclosure/B24/BUILD123D/reference_controls.py",
 "models/enclosure/B24/BUILD123D/reference_equipment.py"]
func digest(_ path:String)throws->String{let data=try Data(contentsOf:root.appendingPathComponent(path));return SHA256.hash(data:data).map{String(format:"%02x",$0)}.joined()}
let inputs=try (sources.map{$0.path}+dataSources).map{($0,try digest($0))}
precondition(Set(inputs.map{$0.0}).count==inputs.count)
let mm=72.0/25.4,H=297.0
var media=CGRect(x:0,y:0,width:420*mm,height:H*mm)
let data=NSMutableData()
guard let consumer=CGDataConsumer(data:data as CFMutableData),let context=CGContext(consumer:consumer,mediaBox:&media,nil) else {fatalError("Cannot create cover")}
func text(_ s:String,_ x:Double,_ y:Double,_ size:Double=8.5,_ color:NSColor = .black){let f=NSFont.systemFont(ofSize:size),w=(s as NSString).size(withAttributes:[.font:f]).width/mm;precondition(x>=8 && x+w<412 && y>=5 && y<288,"Text outside page: \(s)");(s as NSString).draw(at:NSPoint(x:x*mm,y:(H-y)*mm-f.ascender),withAttributes:[.font:f,.foregroundColor:color])}
func rows(_ a:[String],_ x:Double,_ y:Double,_ dy:Double=9,_ size:Double=8.5,_ c:NSColor = .black){for(i,s) in a.enumerated(){text(s,x,y+Double(i)*dy,size,c)}}
func line(_ x:Double,_ y:Double,_ u:Double,_ v:Double){context.setLineWidth(0.5);context.move(to:CGPoint(x:x*mm,y:(H-y)*mm));context.addLine(to:CGPoint(x:u*mm,y:(H-v)*mm));context.strokePath()}
func begin(_ title:String,_ n:Int){context.beginPDFPage(nil);NSGraphicsContext.saveGraphicsState();NSGraphicsContext.current=NSGraphicsContext(cgContext:context,flipped:false);text("B26-INTEGRATED-01 / REVIEW DRAFT / NOT APPROVED / NOT FOR MANUFACTURE",12,11,10,.systemRed);text(title,12,20,14);line(12,27,408,27);line(12,278,408,278);text("mm / rear-left floor underside / cover sheet \(n) / subsequent appended pages keep original labels",12,284,8)}
func end(){NSGraphicsContext.restoreGraphicsState();context.endPDFPage()}

begin("1 / Integrated drawing scope and source precedence",1)
rows([
"Coordinate contract: X right, Y toward operator, Z up; floor bottom Z0, floor top Z2.",
"Main case 600 x 320 x 20; six lower shells, six distinct flat panels and two additional roof halves.",
"Jogs fixed in Z at (110,165)/(490,165); D110 platter, no press action or shared-mode button yet.",
"Fader end assemblies translate outward 1.5 mm per side; retained axes and blade/caps do not move.",
"Roof is raised 5 mm relative to B24. Preserve 276 x 76 display reference and 272 x 72 opening.",
"U1/U2/U3/U4 mounting remains deliberately deferred under B25-ELEC-02; no guessed board holes.",
"Referenced PDFs are appended with historical labels; only selected F12 sensor pages are included.",
"This cover defines precedence only. Old DRAFT labels are historical and never confer new approval.",
"1. B26-PANELS-03 supersedes B26-PANELS-02's Y145 outlines; accepted F13-PANEL-06 sets Y165.",
"2. B26-REAR-POST-03 replaces four Y24 closure axes by Y8; five roof axes remain Y4.",
"3. B26-INTEGRATION-01 adds two rear C07s to B26-JOINTS-03: 16 bridges / 32 screws total.",
"4. F13-STATIC-02 modifies F13-STATIC-01: bottom-up fasteners, D50 sensor plate and ear pilots.",
"5. F13-STATIC-04 changes P02 feet top to local Z3.8 and extends webs down to Z3.8; cover stays Z4.",
"6. Only the listed F12-D05 sensor features apply: PCB pegs, toe bosses, nut entries, bores, wire trough",
"   and P08 toes. F12 spring reliefs, switch, push stroke, old housing and old platter do NOT apply.",
"7. F13-TOOLS-01 describes trial service tools only; no tool is part of the controller assembly.",
"8. K03 supersedes K02 only for CUE and PLAY/PAUSE logo size; K02/K01 retain other cap geometry."
],14,36,10,8.5)
end()

begin("2 / Assembly proposal, roles and outstanding checks",2)
rows([
"PRINTED: C01..C06 x1 each; six flat panels x1 each; D02L/D02R x1 each; C07 x16; 10 fader",
"bridges; 30 switch retainers; 13 pot retainers; one encoder retainer; four display toes; 49 caps.",
"Two jogs each: P01 rotor/platter, P02 carrier, P04/P07 collars, P05/P06 covers, D50 sensor plate",
"and two F12 P08 toes. These are proposed part quantities pending evaluated body/BOM verification.",
"PURCHASED/REFERENCE: bearings, fasteners, electronics, display, faders, potentiometers and switches.",
"Incomplete purchased bodies are labelled reference; they must not be exported as printed parts.",
"Legacy cap meshes are immutable display/reference assets, not editable feature history. Reconstruct or",
"otherwise provide revision-matched editable cap sources before claiming the final source deliverable.",
"Nominal assembly intent: join lower shells; install controls and rear panels; assemble each jog off-case;",
"approach from +Y with jog +6 Z as F13-PANEL-06; seat sensor/bosses and underside screws; fit front",
"panels with caps removed; fit roof before R03 due to its front wedges; verify actual paths before use.",
"F13-TOOLS-01 uses nominal separated-prong trial interfaces; 0.45/0.5 mm radial features and 0.18 mm",
"tool clearance are near FDM capability and NOT validated strength, calibrated fit or an operating tool.",
"There is no demonstrated complete 3D installed or moving assembly. All representations need BRep,",
"full-head/nut, part/solid count, motion, distance, print-volume and viewer checks after the drawing gate.",
"Real display rear, purchased terminal/contact geometry, real wires and solder remain incomplete/reference.",
"Cables/plugs and mains protection are engineer-owned geometry-neutral assumptions, not a safety pass.",
"PETG intended; nominal printer 250 x 250 x 250 and nozzle0.4. Usable margins, layer, supports/brim,",
"calibration, exact tolerance and physical acceptance thresholds remain open. Do not infer manufacturing readiness.",
"This candidate package is NOT an approved named complete drawing/model, STL, STEP or physical prototype."
],14,35,10,8.4)
end()

let pageItems=12
for start in stride(from:0,to:inputs.count,by:pageItems) {
 let n=3+start/pageItems
 begin("\(n) / Immutable source snapshots",n)
 let subset=inputs[start..<min(start+pageItems,inputs.count)]
 for (i,item) in subset.enumerated(){let y=36+Double(i)*19;text(item.0,14,y,7.7);text("SHA-256: "+item.1,14,y+6.5,7.5,.systemBlue)}
 end()
}
context.closePDF()
guard let cover=PDFDocument(data:data as Data) else {fatalError("Cannot reopen cover")}
let output=PDFDocument()
for i in 0..<cover.pageCount {guard let p=cover.page(at:i)?.copy() as? PDFPage else {fatalError("Invalid cover page")};output.insert(p,at:output.pageCount)}
for source in sources {
 guard let doc=PDFDocument(url:root.appendingPathComponent(source.path)) else {fatalError("Cannot open \(source.path)")}
 for i in source.pages ?? Array(0..<doc.pageCount) {
  guard i>=0 && i<doc.pageCount,let p=doc.page(at:i)?.copy() as? PDFPage else {fatalError("Missing appendix page in \(source.path)")}
  output.insert(p,at:output.pageCount)
 }
}
let expected=output.pageCount
guard let result=output.dataRepresentation() else {fatalError("Cannot serialize combined PDF")}
try result.write(to:destination,options:.withoutOverwriting)
guard let reopened=PDFDocument(url:destination),reopened.pageCount==expected,
      reopened.page(at:0)?.string?.contains("B26-INTEGRATED-01") == true,
      reopened.page(at:1)?.string?.contains("C07 x16") == true else {fatalError("Combined PDF reopen/content failed")}
for (path,hash) in inputs {let actual=try digest(path);precondition(actual==hash,"Input changed while collecting: \(path)")}
print("B26-INTEGRATED-01: \(reopened.pageCount) pages; \(inputs.count) fingerprinted sources; cover \(cover.pageCount) pages")
