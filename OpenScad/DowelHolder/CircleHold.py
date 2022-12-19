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

def circle_holder(fname, main_circle):

    # main cylinder to hold ball
    main_cylinder = tube(main_circle + 2*thick, main_circle, height)

    # arm extension
    arm = cube([support_length, thick, height])
    arm = translate([main_circle/2, 0, 0])(arm)

    # cylinder to hang on dowel
    support_cylinder = tube(dowel_d + 2*thick, dowel_d, height*2)
    support_cylinder = translate([main_circle/2+support_length+dowel_d/2, 0, 0])(support_cylinder)


    s1 = arm+support_cylinder
    part = main_cylinder + s1

    # screw to hold support peice in place
    screw = cylinder(d=screw_od, h=50)
    screw = rotate([90,0,0])(screw)
    screw = translate([main_circle/2+support_length+dowel_d/2,0,height])(screw)
    part -= screw

    # removing arc for snap on
    x_sect = rotate_extrude(angle = 90)(square(18))
    x_sect = rotate([0,0,45])(x_sect)
    x_sect = translate([main_circle/2+support_length+dowel_d/2,0,0])(x_sect)
    part -= x_sect

    stl_file = r.render(
        part,
        file_header="$fa=.01;\n $fs=0.01",
        outfile=f"OpenScad/DowelHolder/STL/{fname}.stl",
    )

circle_holder('55m', 55)