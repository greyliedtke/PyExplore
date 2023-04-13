"""
create thermocouple mount
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



tc_post_d, tc_post_h = 2, 6
tc_w, tc_l, tc_h = 15, 25, 10
screw_od = 3.8
thick = 3

# first tc half...
tc_half = cube([tc_l*2, tc_w+2*thick, thick])
tc_post = translate([tc_l/2,tc_w/2+thick,0])(cylinder(d=tc_post_d, h=tc_post_h+thick))

tc_wall_1 = cube([tc_l*2, thick, thick+tc_h])
tc_wall_2 = translate([0,tc_w+thick,0])(tc_wall_1)

part = tc_half+tc_wall_1+tc_wall_2+tc_post

stl_file = r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile=f"OpenScad/simple/TC_holder.stl",
)

