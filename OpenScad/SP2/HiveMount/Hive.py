"""
Create hive hex bins
"""

import solid2 as sp

thick = 10
side_l = 60
side_w = 3.5

h1 = sp.cube([side_l, side_w, thick], center=True).up(thick / 2).back(side_w / 2)
h2 = h1.back(side_w)
tr = {"b": 10, "h": 5}


def p_triangle(b, h):
    v1 = [0, 0, 0]
    v2 = [b, 0, 0]
    v3 = [b / 2, h, 0]
    triangle = sp.polygon([v1, v2, v3])
    triangle = sp.linear_extrude(height=thick)(triangle)
    triangle = triangle.left(b / 2).back(h / 2)
    return triangle


clearance = 3
ofs = 3
cc = sp.cube([ofs, ofs, thick], center=True).up(thick / 2)
tri_p = p_triangle(tr["b"], tr["h"]) + cc.forward(tr["h"] / 2)

tri_h = p_triangle(tr["b"] + clearance, tr["h"] + clearance)
tri_h = tri_h.back((tr["h"] + clearance) / 2 - ofs)

concave = h1 + h2 - tri_h
concave.save_as_stl("OpenScad/SP2/HiveMount/Files/Concave.stl")

convex = h1 + tri_p.rotateZ(180).forward(side_w / 2)
# convex.save_as_stl("OpenScad/SP2/HiveMount/Files/Convex.stl")

# assemb = concave+convex.rotateZ(180).forward(side_w+clearance/4)
# assemb.save_as_stl("OpenScad/SP2/HiveMount/Files/assemb.stl")

# ------------------- piece -----------------------------------
box_d = side_l
conc_1 = concave.forward(box_d / 2)
conc_2 = conc_1.rotateZ(180)
conv_1 = convex.rotateZ(90).left(box_d / 2)
conv_2 = conv_1.rotateZ(180)
box = conc_1 + conc_2 + conv_1 + conv_2
box.save_as_stl("OpenScad/SP2/HiveMount/Files/box.stl")

boxes = box + box.rotateZ(90).left(box_d + 1)
boxes.save_as_stl("OpenScad/SP2/HiveMount/Files/boxes.stl")
