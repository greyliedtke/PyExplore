"""
script for building links on servo wall art
"""

# add path to standard library
import sys

sys.path.append("OpenScad/SP2/Glib")
import gal

import solid2 as ps

fdir = "OpenScad/SP2/Sphero/Files"

# ------------------- part specific dimensions -----------------------------------------
thick = 4
od_b = 55
clear_h = 25
screw_od = 2


#   1. Bearing container with arm for support
p1_b = gal.tube(od_b + 2 * thick, od_b, thick)

s_arc_d = (od_b**2 + clear_h**2) ** 0.5
p2_arc_c = gal.tube(s_arc_d + 2 * thick, s_arc_d, thick)
p2_arc_c += gal.tube(10, 6, thick).forward((s_arc_d + thick) / 2 - 10 / 2)

p2_arc_c = p2_arc_c.rotateX(90).up(clear_h / 2).forward(thick / 2)
p2_arc_c -= ps.cube([1000, 1000, 1000], center=True).down(500)
# p2_arc_c = p2_arc_c.up(thick)

rim_h = 2
p2_fr = ps.cube([thick*2, thick, rim_h], center=True).up(thick+rim_h/2).right(od_b/2+thick)
p2_arc_c += p2_fr

s_h = ps.cylinder(d=screw_od, h=10).right((od_b+thick)/2)

p1 = p1_b + p2_arc_c - s_h

p1.save_as_scad(f"{fdir}/dmount.scad")
