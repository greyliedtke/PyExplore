"""
Script to create double pendule rectangle version parts
Creating bearing dowel holder... 
all dimensions in mm
1 in = 25.4 mm

"""

from solid import (
    circle,
    cylinder,
    translate,
    cube,
    rotate,
    rotate_extrude,
    square,
    polygon,
)

import viewscad
from Dimensions import dowel_d, thick, tube, in_to_mm, screw_od
r = viewscad.Renderer()


height = 12
arm_length = 2 * in_to_mm

# base cylinder -----------------------------------------------------------------------------------------
base = tube(dowel_d + thick, dowel_d, height)

# arm extension -----------------------------------------------------------------------------------------
arm = cube([arm_length, thick, height/2])
arm = translate([dowel_d / 2, 0, 0])(arm)

# vertical hook -----------------------------------------------------------------------------------------
hook = cube([thick * 3, thick, height*2])
hook = translate([arm_length + dowel_d / 2 - 2 * thick, 0, 0])(hook)

hook = rotate_extrude(angle = 180)(square([15, 2]) - square([10, 2]))
hook = rotate([0,90,-90])(hook)
hook = translate([arm_length + dowel_d/2 ,thick,15])(hook)

# cut from base -----------------------------------------------------------------------------------------
x_sect = rotate_extrude(angle = 90)(square(18))
x_sect = rotate([0,0,45])(x_sect)

# screw to hold in place
screw = cylinder(d=screw_od, h=50)
screw = rotate([90,0,0])(screw)
screw = translate([0,0,height/2])(screw)

part = base + arm + hook - x_sect - screw

stl_file = r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile="OpenScad/DowelHolder/ArmHook/ArmHook.stl",
)
