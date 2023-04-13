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
r = viewscad.Renderer()

thick = 2
dowel_d = 13.5  # 1/2 in dowel best fit. 13 snug
screw_od = 3.5
height = 10

def tube(od, id, height): return cylinder(d=od, h=height) - cylinder(d=id, h=height)


# Main dowel snap on arc ---------------------------------------------------
d1_od = dowel_d + 2*thick
c1 = tube(d1_od, dowel_d, height)

# screw to hold support peice in place
screw = cylinder(d=screw_od, h=50)
screw = rotate([90,0,0])(screw)
screw = translate([0,0,height/2])(screw)
c1 -= screw

# removing arc for snap on
x_sect = rotate_extrude(angle = 90)(square(100))
x_sect = rotate([0,0,45])(x_sect)
c1 -= x_sect

# extension arms
arm1 = translate([dowel_d/2, -thick*2, 0])(cube([20, thick, height]))
arm2 = translate([0, 6, 0])(arm1)
screw = cylinder(d=screw_od, h=50)
screw = rotate([90,0,0])(screw)
screw = translate([dowel_d/2 + 15,20,height/2])(screw)

part = c1 + arm1 + arm2 - screw


r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile=f"OpenScad/DowelHolder/Shelf/Vert.stl",
)