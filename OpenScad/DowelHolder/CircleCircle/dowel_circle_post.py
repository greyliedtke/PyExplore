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

import sys
print(sys.path)
sys.path.append('C:Users/greyl/VScodeProjects/PyExplore/PyExplore/OpenScad/DowelHolder')

from ../.. import Dimensions
# tube, dowel_d, screw_od, f_creator


height = 10
thick = 2

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

    # adding vertical ledge
    c2 += rotate([0,0,45])(rotate_extrude(angle = 30)(square(100)))


    c2 = translate([d2/2+d1/2+ext,0,0])(c2)

    # vertical support on second circle
    return c1+c2


# dowel_d, 50.2, 20 - hacynth holder
part = cc_holder(dowel_d, 25, 3)

f_creator(part, 'yahmon')


