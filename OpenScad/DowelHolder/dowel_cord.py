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
thick = 3


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
cord_cube += translate([0,-2*thick,0])(cube([cord_len, thick*2, thick/2]))     # beef to prevent bending
screw = translate([cord_len-2*screw_od,thick,height/2])(rotate([90,0,0])(cylinder(d=screw_od, h=50)))   # screw hole at half height


cord_cube = translate([dowel_d/2,0,0])(cord_cube - screw)

part += cord_cube


stl_file = r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile=f"OpenScad/DowelHolder/STL/dowel_cord.stl",
)