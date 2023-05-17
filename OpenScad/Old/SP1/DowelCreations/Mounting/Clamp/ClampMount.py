from solid import circle, cylinder, translate, cube, rotate, rotate_extrude, square, polygon
import viewscad

r = viewscad.Renderer()
from Dimensions import dowel_d, thick, tube, in_to_mm, screw_od

# base cylinder
base_height = 35
base = tube(dowel_d+2*thick, dowel_d, base_height) 

# screw holes
dowel_screw = cylinder(d=screw_od, h=20)
dowel_screw = rotate([90,0,0])(dowel_screw)
dowel_screw = translate([0, 0, 10])(dowel_screw)
dowel_screw2 = translate([0, 0, 15])(dowel_screw)


# clamp arm to 10-32 hole
clamp_arm = 25
clamp_piece = cube([clamp_arm, thick, base_height/2])
clamp_piece = translate([0, dowel_d/2, 0])(clamp_piece)

clamp_hole = cylinder(d=5, h=20)
clamp_hole = rotate([90,0,0])(clamp_hole)
clamp_hole = translate([clamp_arm/2, dowel_d, base_height/4])(clamp_hole)

# fixture on clamp to hold in place
clamp_fix = cube([thick, thick*4, base_height/2])
clamp_fix_1 = translate([clamp_arm, dowel_d/2, 0])(clamp_fix)
clamp_fix_2 = translate([-thick, dowel_d/2, 0])(clamp_fix)


part = base+clamp_piece+clamp_fix_1+clamp_fix_2
part = part - dowel_screw-dowel_screw2-clamp_hole

stl_file = r.render(part, file_header="$fa=.01;\n $fs=0.01", outfile="OpenScad/DowelHolder/STL/ClampMount.stl")

