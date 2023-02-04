"""
create right angle bracket
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

screw_od = 3.8
arm_len_1 = 7
arm_len_2 = 10+screw_od*1.5
width = 12
thick = 3

# first arm...
b_1 = cube([arm_len_1, width, thick])
screw = translate([arm_len_1-screw_od*1,width/2,0])(cylinder(d=screw_od, h=50))
arm_1 = b_1-screw

b_2 = cube([arm_len_2, width, thick])
screw = translate([arm_len_2-screw_od*1.5,width/2,0])(cylinder(d=screw_od, h=50))
arm_2 = b_2-screw
arm_2 = rotate([0, -90, 0])(arm_2)

part = arm_1+arm_2

stl_file = r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile=f"OpenScad/simple/bracket.stl",
)

