import solid2 as sp


# standard lib
import sys

sys.path.append("OpenScad/SP2/Glib")
import gal

fdir = "OpenScad/SP2/BearingShelf/Files"

# ball sizes
# tennis ball = 67
# main juggling balls = 
# hacky sacks = 
# mug


# assembly level dimensions
ball_od = sp.CustomizerSpinnerVariable("ball_od", 50)
ball_offset = sp.CustomizerSpinnerVariable("ball_offset", 50)
screw_od = 3
thick = sp.CustomizerSpinnerVariable("thick", 3)
ball_height = sp.CustomizerSpinnerVariable("height", 10)
balls = 3
d_od = 7.2

def tube(od, id, height): return sp.cylinder(d=od, h=height) - sp.cylinder(d=id, h=2 * height).down(height/2)

# -------------------1. bottom support below bearing -----------------------------------------
p1 = gal.bearing_inner_support(10, d_od)
p1 -= sp.cylinder(d=screw_od, h=30).rotateX(90).up(10 / 2)
p1.save_as_scad(f"{fdir}/1_bottom_cylinder.scad")


# ------------------- 2. top piece bearing to balls -----------------------------------------
p3_bt = gal.BearingContainer(3, screw_od)   # container around bearing

# first ball location
arm_l = ball_offset - (ball_od/2 + p3_bt.odd/2)
ball_circ_arm = sp.cube([thick, arm_l, ball_height], center=True).up(ball_height/2).forward(arm_l/2+p3_bt.odd/2-thick/2)
ball_circ_0 = gal.tube(ball_od+2*thick, ball_od, ball_height).forward(ball_offset)
p_bcarm = ball_circ_arm+ball_circ_0

# loop through number of balls
ball_circs = p_bcarm
for b in range(balls):
    ball_circs+=p_bcarm.rotateZ(360/balls*b)


# combine and save
p3 = p3_bt.p + ball_circs
p3.save_as_scad(f"{fdir}/3_balls.scad")

# ------------------- base piece -----------------------------------------
p_tb = tube(d_od+2*thick, d_od, ball_height)

p_screwb = tube(screw_od+3*thick, screw_od, ball_height).forward(arm_l)
p_screwb_arm = sp.cube([thick, arm_l, ball_height], center=True).up(ball_height/2).forward(arm_l/2-thick/2)

p_bb = p_tb+p_screwb+p_screwb_arm
p_bb.save_as_scad(f"{fdir}/base_o.scad")