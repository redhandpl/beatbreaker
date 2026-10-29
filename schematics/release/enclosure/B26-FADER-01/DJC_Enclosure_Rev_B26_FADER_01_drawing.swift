import AppKit
import CoreGraphics
import Foundation

// Review draft only: the approved B26 source and exports are not modified.
let root = URL(fileURLWithPath: FileManager.default.currentDirectoryPath)
let out = root.appendingPathComponent("schematics/enclosure/B26-FADER-01/DJC_Enclosure_Rev_B26_FADER_01_drawing.pdf")
precondition(!FileManager.default.fileExists(atPath: out.path), "Refusing to overwrite PDF")
let mm = 72.0 / 25.4, W = 420.0, H = 297.0
var media = CGRect(x: 0, y: 0, width: W * mm, height: H * mm)
guard let pdf = CGContext(out as CFURL, mediaBox: &media, nil) else { fatalError("Cannot create PDF") }
func text(_ s: String, _ x: Double, _ y: Double, _ size: Double = 10, _ color: NSColor = .black) {
    let font = NSFont.systemFont(ofSize: size)
    (s as NSString).draw(at: NSPoint(x: x * mm, y: (H-y)*mm-font.ascender), withAttributes: [.font:font, .foregroundColor:color])
}
func line(_ x: Double, _ y: Double, _ X: Double, _ Y: Double, _ color: NSColor = .black, _ dashed: Bool = false) {
    pdf.saveGState(); pdf.setLineWidth(0.23*mm); pdf.setStrokeColor(color.cgColor)
    if dashed { pdf.setLineDash(phase: 0, lengths: [2*mm,mm]) }
    pdf.move(to: CGPoint(x:x*mm,y:(H-y)*mm)); pdf.addLine(to: CGPoint(x:X*mm,y:(H-Y)*mm)); pdf.strokePath(); pdf.restoreGState()
}
func rect(_ x: Double, _ y: Double, _ w: Double, _ h: Double, _ color: NSColor = .black) {
    line(x,y,x+w,y,color); line(x+w,y,x+w,y+h,color); line(x+w,y+h,x,y+h,color); line(x,y+h,x,y,color)
}
func circle(_ x: Double, _ y: Double, _ r: Double, _ color: NSColor = .black) {
    pdf.saveGState(); pdf.setLineWidth(0.23*mm); pdf.setStrokeColor(color.cgColor)
    pdf.strokeEllipse(in:CGRect(x:(x-r)*mm,y:(H-y-r)*mm,width:2*r*mm,height:2*r*mm)); pdf.restoreGState()
}
func dim(_ x1:Double,_ x2:Double,_ y:Double,_ s:String) {
    line(x1,y,x2,y); line(x1,y-1,x1,y+1); line(x2,y-1,x2,y+1); text(s,(x1+x2)/2-4,y-5,9)
}
func begin(_ name:String) {
    pdf.beginPDFPage(nil); NSGraphicsContext.saveGraphicsState(); NSGraphicsContext.current = NSGraphicsContext(cgContext:pdf,flipped:false)
    text("B26-FADER-01 / REVIEW DRAFT / NOT APPROVED / NOT FOR MANUFACTURE",12,11,11,.systemRed)
    text(name,12,20,15); line(12,27,408,27)
}
func end() { NSGraphicsContext.restoreGraphicsState(); pdf.endPDFPage() }

begin("1 / End-wall and screw-boss correction")
text("PLAN DETAIL / positive u end / F01-F04, 8:1 (local u right, v down)",15,37,11)
let x0=38.0, y0=53.0, scale=8.0
func X(_ u:Double)->Double { x0+(u-27.0)*scale }
func Y(_ v:Double)->Double { y0+(v+6.7)*scale }
// Existing positive-u cup: end wall and the two side wings.
rect(X(31.75),Y(-6.7),2*scale,13.4*scale)
rect(X(24.75),Y(-6.7),7*scale,2*scale)
rect(X(24.75),Y(4.7),7*scale,2*scale)
// Current B26 and proposed post outlines. Small diameter is the pilot.
circle(X(32.75),Y(0),2.2*scale,.systemRed)
circle(X(33.95),Y(0),2.2*scale,.systemBlue)
circle(X(33.95),Y(0),0.8*scale,.systemBlue)
line(X(31.75),Y(-6.7)-4,X(31.75),Y(6.7)+4,.gray,true)
line(X(33.95),Y(-6.7)-4,X(33.95),Y(6.7)+4,.systemBlue,true)
dim(X(31.75),X(33.95),Y(6.7)+10,"2.20")
text("RED = existing B26 boss; BLUE = proposed boss and pilot.",15,188,10)
text("Existing end wall and wings remain in B26 positions. Same positive/negative-u correction at each end.",15,195,10)
text("Wall inner face |u|=31.75 (F01-F04) / 31.60 (F05). Post radius 2.20, pilot radius 0.80.",15,202,10)
text("New axis = wall inner face + 2.20; new post inner face is flush with the wall inner face.",15,209,10)
text("Current post axis is wall inner face + 1.00; each post/pilot moves outward 1.20 from B26.",15,216,10)
text("No change to fader center, walls, wings, bottom rails, blade, cap or panel slot.",15,223,10)
text("Role: C04/C05/C06 lower shell integral bosses, printed PETG. Local coordinate origin is fader center.",15,230,10)
text("The grey line is a datum extension; colored outlines overlap and are not separate printable bodies.",15,237,10)
text("Projection convention: orthographic plan. mm throughout. Derived proposal; no physical fit approval.",15,244,10)
text("HOLD: check all boss/support/retainer neighbors, screw heads and driver envelopes before any release.",15,252,10,.systemRed)
text("Approval of this named drawing is required before modifying B26 CAD geometry.",15,259,10,.systemRed)
end()

begin("2 / Retainer definition, positions and assembly")
text("RETAINER PLAN / positive u end / all five faders / 8:1",15,37,11)
let px=30.0, py=53.0, sc=8.0
rect(px,py,8.4*sc,13.4*sc)
circle(px+5.2*sc,py+6.7*sc,1.1*sc)
circle(px+5.2*sc,py+6.7*sc,2.2*sc,.systemBlue)
line(px+5.2*sc,py-4,px+5.2*sc,py+13.4*sc+4,.gray,true)
dim(px,px+5.2*sc,py+13.4*sc+10,"5.20")
dim(px+5.2*sc,px+8.4*sc,py+13.4*sc+10,"3.20")
text("8.40 x 13.40 x 1.50; centered v=0. Through D2.20; 90-degree countersink D4.40 top.",15,185,10)
text("Top D4.40 meets bottom D2.20 at 1.10 below retainer top. Nominal outside material at outer end = 1.00.",15,192,10)
text("Inner edge remains |u|=28.75 / 28.60; outer edge |u|=37.15 / 37.00; axis |u|=33.95 / 33.80.",15,199,10)
text("First value F01-F04, second F05. Reverse u sign for the opposite end; z positions remain as B26.",15,206,10)
text("F01/F02/F03/F04: pilot axes +/-33.95, spacing 67.90; F05 +/-33.80, spacing 67.60.",15,213,10)
text("For F01-F04 (X,Y)=(X0+v,Y0+u); F05 (X,Y)=(X0+u,Y0-v); Z up; rear-left datum B26.",15,220,10)
text("Printed PETG: one integral end boss per end, two retainer bridges per fader; 5 faders / 10 bridges.",15,227,10)
text("Inherited trial fastener: M2x6 countersunk, max head D4.40; pilot D1.60, modeled depth 5.50.",15,234,10)
text("Nominal 60 mm body gives 1.75 mm (F01-F04) / 1.60 mm (F05) per end to boss at centered pose.",15,241,10)
text("Actual body/tabs, screw head, accessible driver, panel interaction, retention and PETG strength TBD.",15,248,10,.systemRed)
text("2D proposal only. No CAD, STL, STEP, physical fit or manufacturing release follows from this draft.",15,255,10,.systemRed)
text("Basis: approved B26-INTEGRATED-01 + B26-DETAIL-01 sheet 3; only described boss/bridge delta changes.",15,262,10)
end()
pdf.closePDF()
