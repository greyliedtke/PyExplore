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
from Dimensions import tube, in_to_mm, dowel_d, screw_od
r = viewscad.Renderer()

support_length = 25
height = 5
thick = 3

def sphere_holder(fname, sphere_d):
    main_sphere = sphere(d=sphere_d)
    out_d = sphere_d+2*thick
    out_sphere = sphere(d=out_d)
    support_sphere = translate([0, 0, sphere_d/8])(out_sphere-main_sphere)

    support_section = cube([out_d, out_d, height])
    support_section = translate([-out_d/2, -out_d/2, 0])(support_section)

    # intersecting area...
    sphere_support = intersection()(support_sphere, support_section)

    # arm extension
    arm = cube([support_length, thick, height])
    arm = translate([sphere_d/2.5, 0, 0])(arm)

    # cylinder to hang on dowel
    support_cylinder = tube(dowel_d + 2*thick, dowel_d, height*2)
    support_cylinder = translate([sphere_d/2.5+support_length+dowel_d/2, 0, 0])(support_cylinder)

    s1 = arm+support_cylinder
    part = sphere_support + s1

    # screw to hold support peice in place
    screw = cylinder(d=screw_od, h=50)
    screw = rotate([90,0,0])(screw)
    screw = translate([sphere_d/2+support_length+dowel_d/2,0,height])(screw)
    part -= screw

    # removing arc for snap on
    x_sect = rotate_extrude(angle = 90)(square(18))
    x_sect = rotate([0,0,45])(x_sect)
    x_sect = translate([sphere_d/2+support_length+dowel_d/2,0,0])(x_sect)
    part -= x_sect

    stl_file = r.render(
        part,
        file_header="$fa=.01;\n $fs=0.01",
        outfile=f"OpenScad/DowelHolder/STL/{fname}.stl",
    )

sphere_holder('58mm_sphere', 58)