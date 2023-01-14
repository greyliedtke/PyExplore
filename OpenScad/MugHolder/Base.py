"""
Creating bearing dowel holder... 
all dimensions in mm
Create circular base with support for hanging wire...

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
from Dimensions import tube, dowel_d, screw_od, thick
r = viewscad.Renderer()



support_length = 25
height = 5

coaster_d =  60


coaster_support = tube(od=coaster_d, id=coaster_d-thick, height=height)
coaster_edge = tube(od=coaster_d+thick, id=coaster_d, height=height*2)

dowel_b = tube(od=dowel_d+thick, id=dowel_d, height=height*2)
screw = cylinder(d=screw_od, h=50)
screw = rotate([90,0,0])(screw)
screw = translate([0,0,height])(screw)
dowel_b -= screw

dowel_b = rotate([-45,0,0])(dowel_b)
barrel_offset = ((dowel_d+thick)/2)*2**.5
dowel_b = translate([0, coaster_d/2, barrel_offset])(dowel_b)



part = coaster_support+coaster_edge+dowel_b

fname = 'base'
stl_file = r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile=f"OpenScad/MugHolder/STL/{fname}.stl",
)
