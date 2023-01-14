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
from Dimensions import tube, in_to_mm
r = viewscad.Renderer()

support_length = 25
height = 5
thick = 3

def sphere_holder(fname, sphere_d):
    main_sphere = sphere(d=sphere_d)
    out_d = sphere_d+thick
    out_sphere = sphere(d=out_d)
    support_sphere = translate([0, 0, sphere_d/3])(out_sphere-main_sphere)

    support_section = cube([out_d, out_d, height])
    support_section = translate([-out_d/2, -out_d/2, 0])(support_section)

    # intersecting area...
    sphere_support = intersection()(support_sphere, support_section)

    claw = cube([out_d, thick, out_d*1/2])
    claw_1 = intersection()(support_sphere, claw)

    bp = sphere_support+claw_1

    # arm extension
    # arm = cube([support_length, thick, height])
    # arm = translate([main_circle/2, 0, 0])(arm)

    # support_cylinder = tube(support_circle + 2*thick, support_circle, height)
    # support_cylinder = translate([main_circle/2+support_length+support_circle/2, 0, 0])(support_cylinder)

    # s1 = arm+support_cylinder
    # part = main_cylinder + s1

    # screw = cylinder(d=.14*in_to_mm, h=50)
    # screw = rotate([90,0,0])(screw)
    # screw = translate([main_circle/2+support_length+support_circle/2,0,height/2])(screw)
    # part -= screw

    # x_sect = rotate_extrude(angle = 90)(square(18))
    # x_sect = rotate([0,0,45])(x_sect)
    # x_sect = translate([main_circle/2+support_length+support_circle/2,0,0])(x_sect)
    # part -= x_sect

    stl_file = r.render(
        bp,
        file_header="$fa=.01;\n $fs=0.01",
        outfile=f"OpenScad/DowelHolder/STL/{fname}.stl",
    )

sphere_holder('58mm_sphere', 58)