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
from Dimensions import tube, dowel_d, screw_od
r = viewscad.Renderer()

height = 12
thick = 2


# Main dowel snap on arc ---------------------------------------------------
support_cylinder = tube(dowel_d + 2*thick, dowel_d, height)
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
cord_len = 20
cord_cube = cube([cord_len, thick, height])
cord_cube = translate([0,-dowel_d/3,0])(cord_cube)
cord_cube += translate([0,dowel_d/2,0])(cord_cube)
# cord_cube += translate([0,-2*thick,0])(cube([cord_len, thick*2, thick/2]))     # beef to prevent bending
screw = translate([cord_len-2*screw_od,dowel_d,height/2])(rotate([90,0,0])(cylinder(d=screw_od, h=50)))   # screw hole at half height

cord_cube = translate([dowel_d/2,0,0])(cord_cube - screw)
part += cord_cube


# command strip base -------------------------------------------------------------------------
command_height, command_width = 50, 20
command_base = cube([thick, command_width, command_height])
command_base -= translate([0,command_width/2,command_height/2])(rotate([0,90,0])(cylinder(d=screw_od, h=50)))   # screw hole 1
command_base -= translate([0,command_width/2,command_height*3/4])(rotate([0,90,0])(cylinder(d=screw_od, h=50)))   # screw hole 2


command_base = translate([dowel_d/2+cord_len,-dowel_d/2,0])(command_base)

part += command_base

stl_file = r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile=f"OpenScad/DowelHolder/STL/DWC.stl",
)