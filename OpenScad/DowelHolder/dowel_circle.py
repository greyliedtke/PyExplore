"""
circular dowel hook ...
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
    sphere, 
    intersection
)
import viewscad
from Dimensions import tube, dowel_d, screw_od
r = viewscad.Renderer()

height = 10
thick = 3

# function to create hook of two circles with holes for attaching
def cc_holder(d1, d2, ext=0):


    # Main dowel snap on arc ---------------------------------------------------
    d1_od = d1 + 2*thick
    c1 = tube(d1_od, d1, height)

    # screw to hold support peice in place
    screw = cylinder(d=screw_od, h=50)
    screw = rotate([90,0,0])(screw)
    screw = translate([0,0,height/2])(screw)
    c1 -= screw

    # removing arc for snap on
    x_sect = rotate_extrude(angle = 90)(square(100))
    x_sect = rotate([0,0,45])(x_sect)
    c1 -= x_sect

    # extension arm if necessary
    if ext > 0:
        c1 += translate([d1/2, -thick, 0])(cube([ext, thick*2, height]))

    c2 = tube(d2 + 2*thick, d2, height)
    c2 -= screw

    # removing arc for snap on
    c2 -= x_sect
    c2 = rotate([0,0,180])(c2)

    c2 = translate([d2/2+d1/2+ext,0,0])(c2)
    return c1+c2



part = cc_holder(dowel_d, 50.2, 20)
r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile=f"OpenScad/DowelHolder/STL/c2.stl",
)