"""
generic holder of circle with ledge
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

thick = 3
dowel_d = 13.5  # 1/2 in dowel best fit. 13 snug
screw_od = 3.5

def tube(od, id, height): return cylinder(d=od, h=height) - cylinder(d=id, h=height)



def circle_holder(fname, main_circle, ledge, extension, height):

    # main cylinder and ledge
    main_cylinder = tube(main_circle + 2*thick, main_circle, height)
    base_cylinder = tube(main_circle, ledge, thick)
    part = base_cylinder+main_cylinder

    # arm extension
    arm = cube([extension, thick, height])
    arm = translate([main_circle/2, 0, 0])(arm)

    # cylinder to hang on dowel
    support_cylinder = tube(dowel_d + 2*thick, dowel_d, height)
    support_cylinder = translate([main_circle/2+extension+dowel_d/2, 0, 0])(support_cylinder)

    s1 = arm+support_cylinder
    part += s1

    # screw to hold support peice in place
    screw = cylinder(d=screw_od, h=50)
    screw = rotate([90,0,0])(screw)
    screw = translate([main_circle/2+extension+dowel_d/2,0,height/2])(screw)
    part -= screw

    # removing arc for snap on
    x_sect = rotate_extrude(angle = 90)(square(18))
    x_sect = rotate([0,0,45])(x_sect)
    x_sect = translate([main_circle/2+extension+dowel_d/2,0,0])(x_sect)
    part -= x_sect

    # creating part
    r.render(
        part,
        file_header="$fa=.01;\n $fs=0.01",
        outfile=f"OpenScad/DowelHolder/CircleLedge/{fname}.stl",
    )

# circle_holder('Coaster', 104, 20, 15) 
# circle_holder('Candle', 65, 20, 15) # TJ mini candle
circle_holder('BB_Juggle', 55, 50, 20, 10)