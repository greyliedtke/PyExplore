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

t1, t2, t3 = tube(dd_o, dd_i, height), tube(dd_o, dd_i, height), tube(dd_o, dd_i, height)
t2 = translate([dd_o/2, 0, dd_o/2])(rotate([0, 90, 0])(t2))
t3 = rotate([0, 0, 90])(t2)


part = t1+t2+t3

stl_file = r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile="OpenScad/DowelHolder/CNXNS/RA.stl",
)
