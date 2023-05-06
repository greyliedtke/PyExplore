"""
Create hive hex bins
"""

import solid2 as sp

thick = 2
side_l = 25
side_w = 5

h1 = sp.cube([side_l, side_w, thick], center=True).up(thick / 2)
h2 = h1.back(side_w)
tr = {"b": 12, "h": 7}


def p_triangle(b,h):
    v1 = [0, 0, 0]
    v2 = [b, 0, 0]
    v3 = [b / 2, h, 0]
    triangle = sp.polygon([v1, v2, v3])
    triangle = sp.linear_extrude(height=thick)(triangle)
    triangle = triangle.left(b/2).back(h/2)
    return triangle

clearance = 2
tri_p = p_triangle(tr["b"], tr["h"])
tri_h = p_triangle(tr["b"]+clearance, tr["h"]+clearance)


concave = h1+h2-tri_h
concave.save_as_stl("OpenScad/SP2/HiveMount/Files/Concave.stl")

convex = h1+tri_p.rotateZ(180).forward(side_w)
convex.save_as_stl("OpenScad/SP2/HiveMount/Files/Convex.stl")

assemb = concave+convex.rotateZ(180).forward(side_w+clearance/4)
assemb.save_as_stl("OpenScad/SP2/HiveMount/Files/assemb.stl")
