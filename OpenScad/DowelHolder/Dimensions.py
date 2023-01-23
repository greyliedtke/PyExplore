import os

from solid import (
    cylinder
)

import viewscad
r = viewscad.Renderer()

def tube(od, id, height):
    # function to create tube from two diameters and height
    outer_cylinder = cylinder(d=od, h=height)
    innter_cylinder = cylinder(d=id, h=height)
    tube_cyl = outer_cylinder - innter_cylinder
    return tube_cyl

# dimensions
thick = 2  # standard wall thickness
dowel_d = 13.5  # 1/2 in dowel best fit. 13 snug
in_to_mm = 25.4  # in to mm conversion
screw_od = 3.5


# plantpot_d = 2.75
def f_creator(part, file_name):
    fp = os.getcwd()
    create_f = f"{fp}/{file_name}.stl"
    print(create_f)

    r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile=create_f,
)


