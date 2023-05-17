import solid2 as sp


# standard lib
import sys

sys.path.append("OpenScad/SP2/Glib")
import gal

fdir = "OpenScad/SP2/Rshelf/Files"

# assembly level dimensions
screw_od = 3
thick = 2

# -------------------1. bottom support below bearing -----------------------------------------
p_bch = 10
p1 = gal.bearing_inner_support(10, gal.dowel_14["od"])
p1 -= sp.cylinder(d=screw_od, h=30).rotateX(90).up(10 / 2)
p1.save_as_scad(f"{fdir}/1_bottom_cylinder.scad")


# ------------------- 2. top support piece -----------------------------------------
# sit on top of bearing and have arms extend down for screw mounting beneath
p2_bt = gal.BearingContainer(2, screw_od)

p2_ms = gal.tube(45, p2_bt.odd, thick)

p2 = p2_bt.p + p2_ms
p2.save_as_scad(f"{fdir}/2_top_support.scad")


# 3. The real deal...
p3_bt = gal.BearingContainer(3, screw_od)

ball_rim = 30
ball_od = 50
ball_thick = 5

p3_bs = gal.tube(ball_rim, p2_bt.odd, ball_thick)

ball_circ_0 = gal.tube(ball_od+2*thick, ball_od, ball_thick).forward(ball_od/2+ball_rim/2)
ball_circs = ball_circ_0
for b in range(3):
    ball_circs+=ball_circ_0.rotateZ(360/3*b)

p3 = p3_bt.p + p3_bs + ball_circs
p3.save_as_scad(f"{fdir}/3_balls.scad")
