"""
script for building links on servo wall art
"""

# add path to standard library
import sys
sys.path.append("OpenScad/SP2/Glib")
import gal
import solid2 as ps

fdir = "OpenScad/SP2/PWM_Mount/Files"

# ------------------- part specific dimensions -----------------------------------------
thick = ps.CustomizerSliderVariable("Thickness", 2)
rect_x = ps.CustomizerSliderVariable("rect_X", 75)
rect_y = ps.CustomizerSliderVariable("rect_Y", 40)
hole = ps.CustomizerSliderVariable("hole", 6)
height = ps.CustomizerSliderVariable("Height", 10)
mount_x = ps.CustomizerSliderVariable("Mount_SL", 12)

p_r = gal.hollow_rect(rect_x, rect_y, thick, height)
p_r -= ps.cylinder(d=hole, h=30).rotateX(90).up(height / 2)

# mounting piece
p_m = gal.c_rect(mount_x, mount_x, thick, hole).left(mount_x / 2 + rect_x / 2 + thick)
p_m += p_m.right(rect_x+2*thick+mount_x)

# combine and save
p = p_r + p_m
p.save_as_scad(f"{fdir}/mount.scad")
