from solid import circle, cylinder, translate, cube, rotate, rotate_extrude, square, polygon
import viewscad

r = viewscad.Renderer()
from Dimensions import dowel_d, thick, tube, in_to_mm

screw_d = .14*in_to_mm


# base cylinder
base = tube(dowel_d+2*thick, dowel_d, 35) 

# arm extension
arm_length = 25
arm = cube([arm_length, 3, 5])
arm = translate([dowel_d/2, 0, 0])(arm)

mount_hole = tube(screw_d+2*thick, screw_d, 5) 
mount_hole = translate([dowel_d/2+arm_length+screw_d/2, 0, 0])(mount_hole)

h1 = mount_hole+arm
h2 = rotate([0, 0,120])(h1)
h3 = rotate([0, 0,240])(h1)
support_arms = h1+h2+h3

# screw holes
dowel_screw = cylinder(d=screw_d, h=20)
dowel_screw = rotate([90,0,0])(dowel_screw)
dowel_screw = translate([0, 0, 10])(dowel_screw)
dowel_screw2 = translate([0, 0, 15])(dowel_screw)


part = base+support_arms-dowel_screw-dowel_screw2

stl_file = r.render(part, file_header="$fa=.01;\n $fs=0.01", outfile="OpenScad/DowelHolder/STL/TableMount.stl")

