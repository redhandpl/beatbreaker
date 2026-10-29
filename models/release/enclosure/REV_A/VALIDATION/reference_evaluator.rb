require 'json'
require 'digest'

base='schematics/work/enclosure/B26-CONSOLIDATED-02'
ref=JSON.parse(File.read("#{base}/reference_geometry_DRAFT.json"))
shell=JSON.parse(File.read("#{base}/shell/shell_dataset_DRAFT.json"))
proof='models/release/enclosure/B26/B26-build123d03_RELEASE/STEP/assembly-evidence.json'
leaves=JSON.parse(File.read(proof))['leaves']
selected=leaves.select { |x| ['Controls - incomplete purchased references','Equipment - incomplete purchased references'].include?(x['group']) }
index=selected.to_h { |x| [x['key'],x] }
raise 'reference evidence keys are not unique' unless index.size==90
results=[]
def compare(index,results,key,points,volume=nil)
  actual=index[key] or raise "missing #{key}"
  bounds=[(0..2).map { |i| points.map { |p| p[i] }.min },(0..2).map { |i| points.map { |p| p[i] }.max }]
  err=bounds.flatten.zip(actual['step_bounds_mm'].flatten).map { |a,b| (a-b).abs }.max
  verr=volume && (volume-actual['step_volume_mm3']).abs
  results << {'key'=>key,'max_bound_difference_mm'=>err,'volume_difference_mm3'=>verr,'bounds_ok'=>err<=0.000002,'volume_ok'=>verr.nil? || verr<=0.00001}
end
def corners(min,max)
  min[0].then { |x| [x,max[0]] }.product([min[1],max[1]],[min[2],max[2]])
end
ref['equipment_boxes'].each do |r|
  x,y=r['centre_XY']; w,h=r['size_XY']; z0,z1=r['z']
  compare(index,results,r['id'],corners([x-w/2.0,-y-h/2.0,z0],[x+w/2.0,-y+h/2.0,z1]),w*h*(z1-z0))
end
compare(index,results,'J01-body',corners([96.925,-322.5,5.925],[105.075,-306.2,14.075]),Math::PI*(4.075**2*11.8+3**2*4.5))
compare(index,results,'J01-nut',corners([97,-321.8,6],[105,-320,14]),Math::PI*(4**2-3**2)*1.8)
a=49*Math::PI/180; c=Math.cos(a); s=Math.sin(a); cy=96-40*c; h=23+40*s
points=[[-138,-38],[-138,38],[138,38],[138,-38]].map { |u,v| [300+u,-cy-c*v,h-s*v] }
compare(index,results,'D01-front-plane',points)
compare(index,results,'RCA-front-plane',[[28.85,0,0.05],[80.55,0,19.95]])
groups=shell['schedules']['controls'].select { |r| r['id'].end_with?('-FIXED') || r['id']=='E01-fixed_cage' }
raise 'control group count' unless groups.length==49 && groups.map { |r| r['owner'] }.uniq.size==49
groups.each do |row|
  owner=row['owner']; m=row['CSG'][1]
  if owner.start_with?('B','T'); low=[-6,-6,0]; high=[6,6,4.3]; volume=12*12*4.3
  elsif owner.start_with?('P'); low=[-5.7,-5.5,0]; high=[5.7,7,6.8]; volume=11.4*12.5*6.8
  elsif owner.start_with?('F'); low=[-30,-4.5,0]; high=[30,4.5,21]; volume=60*9*6+4*1*15
  elsif owner=='E01'; low=[-5.9,-7,0]; high=[5.9,7.5,21.5]; volume=nil
  else; raise "unknown #{owner}"; end
  transform=lambda { |p| t=(0..2).map { |i| (0..2).sum { |j| m[i][j]*p[j] } + m[i][3] }; [t[0],-t[1],t[2]] }
  compare(index,results,owner+'-BODY-REF',corners(low,high).map(&transform),volume)
  if owner.start_with?('B','T')
    compare(index,results,owner+'-TIP-REF',corners([-1.9,-1.9,7.3],[1.9,1.9,7.3]).map(&transform))
  end
end
raise 'wrong coverage' unless results.length==90 && results.map { |r| r['key'] }.uniq.length==90
out={'scope'=>'Reference bounds and listed analytic reference-solid volumes only; no BRep symmetric difference or real purchased geometry check','coverage'=>results.length,'bound_tolerance_mm'=>0.000002,'volume_tolerance_mm3'=>0.00001,'reference_json_sha256'=>Digest::SHA256.file("#{base}/reference_geometry_DRAFT.json").hexdigest,'shell_json_sha256'=>Digest::SHA256.file("#{base}/shell/shell_dataset_DRAFT.json").hexdigest,'step_evidence_sha256'=>Digest::SHA256.file(proof).hexdigest,'results'=>results}
path='tmp/rev-a-reference/results-v2.json'; raise 'refusing overwrite' if File.exist?(path)
File.write(path,JSON.pretty_generate(out)+"\n")
failed=results.reject { |r| r['bounds_ok'] && r['volume_ok'] }
puts "Reference evidence: #{results.length} of 90 bounds, #{results.count { |r| !r['volume_difference_mm3'].nil? }} analytic volumes, failures #{failed.length}"
failed.each { |r| puts r.inspect }
exit(failed.empty? ? 0 : 1)
