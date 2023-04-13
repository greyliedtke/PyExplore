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

thick = 3
screw_od = 3.5

# Main dowel snap on arc ---------------------------------------------------
width, len = 6.5, 30
edge_d = 3.5
part = cube([len, width, thick])
screw = cylinder(d=screw_od, h=50)
s1 = translate([edge_d, width/2, 0])(screw)
s2 = translate([len-2*edge_d, 0, 0])(s1)


part = part-s1-s2

r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile=f"OpenScad/DowelHolder/Shelf/Connector.stl",
)