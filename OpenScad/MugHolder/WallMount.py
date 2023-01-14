"""
Script to create double pendule rectangle version parts
Creating bearing dowel holder... 
all dimensions in mm
1 in = 25.4 mm

"""

from solid import circle, cylinder, translate, cube, rotate, rotate_extrude, square, polygon
import viewscad

r = viewscad.Renderer()
from Dimensions import dowel_d, thick, tube, in_to_mm

screw_d = .14*in_to_mm
height = .5*in_to_mm
arm_length = 3*in_to_mm


# base cylinder
base = tube(dowel_d+2*thick, dowel_d, height) 

# arm extension
arm = cube([arm_length, thick, height])
arm = translate([0, dowel_d/2, 0])(arm)

# vertical hook 
wall_mount = cube([thick, dowel_d, height])
wall_mount = translate([arm_length, dowel_d/2, 0])(wall_mount)

# screw holes
screw = cylinder(d=screw_d, h=dowel_d+2*thick)
dowel_screw = rotate([90,0,0])(screw)
dowel_screw = translate([0, 0, height/2])(dowel_screw)
wall_screw = rotate([0,90,0])(screw)
wall_screw = translate([arm_length, dowel_d, height/2])(wall_screw)

part = base+arm+wall_mount-dowel_screw-wall_screw

stl_file = r.render(part, file_header="$fa=.01;\n $fs=0.01", outfile="OpenScad/DowelHolder/STL/WallMount.stl")

