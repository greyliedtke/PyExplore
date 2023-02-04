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
r = viewscad.Renderer()


height = 12
arm_length = 25
dd_i = 13.5
thick = 2
dd_o = dd_i+2*thick
outer_arc = 15

def tube(od, id, height): return cylinder(d=od, h=height) - cylinder(d=id, h=height)

# two circle halves
h1 =  rotate_extrude(angle = 180)(square([outer_arc, 2]) - square([10, 2]))
sc = rotate([90, 0, 0])(translate([outer_arc, dd_o/2, 0])(tube(dd_o, dd_i, height)))

part = h1+sc

stl_file = r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile="OpenScad/DowelHolder/ArmHook/VHook.stl",
)
