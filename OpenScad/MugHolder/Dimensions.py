
from solid import (
    cylinder
)

def tube(od, id, height):
    # function to create tube from two diameters and height
    outer_cylinder = cylinder(d=od, h=height)
    innter_cylinder = cylinder(d=id, h=height)
    tube_cyl = outer_cylinder - innter_cylinder
    return tube_cyl

# dimensions
thick = 2  # standard wall thickness
dowel_d = 13  # 1/2 in dowel best fit
in_to_mm = 25.4  # in to mm conversion
screw_od = 3.5
