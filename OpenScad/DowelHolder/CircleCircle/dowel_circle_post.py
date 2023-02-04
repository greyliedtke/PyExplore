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
    square
)

import viewscad
r = viewscad.Renderer()


height = 12
arm_length = 25
dd_i = 13.5
thick = 2
dd_o = dd_i+2*thick
outer_arc = 15
screw_od = 3.5

def tube(od, id, height): return cylinder(d=od, h=height) - cylinder(d=id, h=height)

height = 10
thick = 2

# function to create hook of two circles with holes for attaching
def cc_holder(d1, d2, ext=0, post=0):

    # Main dowel snap on arc ---------------------------------------------------
    d1_od = d1 + 2*thick
    c1 = tube(d1_od, d1, height)

    # screw to hold support peice in place
    screw = translate([0,0,height/2])(rotate([90,0,0])(cylinder(d=screw_od, h=50)))
    c1 -= screw

    # removing arc for snap on
    x_sect = rotate_extrude(angle = 90)(square(100))
    x_sect = rotate([0,0,45])(x_sect)
    c1 -= x_sect

    # extension arm if necessary
    if ext > 0:
        c1 += translate([d1/2, -thick, 0])(cube([ext, thick*2, height]))

    # second circle
    c2 = tube(d2 + 2*thick, d2, height)
    c2 -= screw

    # arc section
    c2_angle = 30
    c2 -= rotate([0,0,15])(rotate_extrude(angle = c2_angle)(square(100)))
    c2 = rotate([0,0,180])(c2)

    # vertical post
    if post > 0 :
        post = tube(d2 + 2*thick, d2, height*2) - rotate_extrude(angle = 360-c2_angle)(square(100))
        c2 += rotate([0,0,180+2.5*c2_angle])(post)
    
    # moving circle relative to other one
    c2 = translate([d2/2+d1/2+ext,0,0])(c2)

    return c1+c2


# dowel_d, 50.2, 20 - hacynth holder
part = cc_holder(13.6, 25, 3, 2)


stl_file = r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile="OpenScad/DowelHolder/CircleCircle/dcp.stl",
)

