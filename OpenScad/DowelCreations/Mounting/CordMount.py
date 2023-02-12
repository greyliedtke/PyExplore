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
    sphere, 
    intersection
)
import viewscad
r = viewscad.Renderer()

height = 12
dd_i = 13.5
thick = 2
dd_o = dd_i+2*thick
screw_od = 3.5

def tube(od, id, height): return cylinder(d=od, h=height) - cylinder(d=id, h=height)

# Main dowel snap on arc ---------------------------------------------------
support_cylinder = tube(dd_o, dd_i, height)
part = support_cylinder

# screw to hold support peice in place
screw = cylinder(d=screw_od, h=50)
screw = rotate([90,0,0])(screw)
screw = translate([0,0,height/2])(screw)
part -= screw

# removing arc for snap on
x_sect = rotate_extrude(angle = 90)(square(18))
x_sect = rotate([0,0,45])(x_sect)
part -= x_sect

# support for cord -------------------------------------------------------------------------
cord_w = dd_o*2
cc = cube([thick, cord_w, height])
b_screw = cylinder(d=5, h=50)
b_screw = rotate([0,90,0])(b_screw)
b_screw_1 = translate([0,4,height/2])(b_screw)
b_screw_1 = translate([0,4,height/2])(b_screw_1)
cc += b_screw


cord_cube = translate([dd_i/2,-cord_w/2,0])(cc)

part += cord_cube

stl_file = r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile=f"OpenScad/DowelHolder/Mounting/CordMount.stl",
)