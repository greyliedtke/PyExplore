"""
script for building links on servo wall art
"""

# add path to standard library
import sys

sys.path.append("OpenScad/SP2/Glib")
import gal

import solid2 as ps

fdir = "OpenScad/SP2/BallPost/Files"

# ------------------- part specific dimensions -----------------------------------------
thick = ps.CustomizerSliderVariable("Thickness", 2)
ball_od = ps.CustomizerSliderVariable("Ball_od", 50)
ball_odd = ball_od+2*thick
support_od = ps.CustomizerSliderVariable("SupportCirc", 15)
support_odd = support_od+2*thick
height = ps.CustomizerSliderVariable("Height", 10)
offset = ps.CustomizerSliderVariable("Circle_Offset", 10)
screw_od = 2

#   1. Bearing container with arm for support
bp = gal.dowel_tube(support_od, thick, 3, height)
bsp = gal.tube(ball_odd, ball_od, height).right((ball_odd+support_odd)/2+offset)


# arm connecting
arm_l = offset# -(ball_od+support_od)/2
p_a = ps.cube([arm_l, thick, height]).right(support_od/2).back(thick/2)

p1 = bp + bsp + p_a

p1.save_as_scad(f"{fdir}/dmount.scad")
