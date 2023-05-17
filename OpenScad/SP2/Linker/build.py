"""
script for building links on servo wall art
"""

# add path to standard library
import sys
sys.path.append("OpenScad/SP2/Glib")
import gal
from gal import bearing, tube, bearing_container, bearing_inner_support, dowel_tube

import solid2 as ps

# ------------------- part specific dimensions -----------------------------------------
thick = 2
link_distance = 70
screw_od = 3.5
arm_len = link_distance - (bearing["od"] + 2 * thick) / 2 - bearing["idr"] / 2
bear_offset = 25

#   1. Bearing container with arm for support
#  ------------------- base -----------------------------------------
part_h = bearing["h"] + thick
p_bearing = bearing_container(thick, screw_od)

# ------------------- arm for part -----------------------------------------
p_arm = (
    ps.cube([arm_len, thick * 4, part_h], center=True)
    .up(part_h / 2)
    .left(arm_len / 2 + bearing["od"] / 2)
)

# ------------------- bearing carrier attachment -----------------------------------------
p_bc = bearing_inner_support(bear_offset, screw_od).left(
    arm_len + bearing["od"] / 2 + thick
)

# ------------------- combining -----------------------------------------
p_link = p_bearing + p_arm + p_bc
# ------------------- saving -----------------------------------------
p_link.save_as_scad("OpenScad/SP2/Linker/link.scad")
print("created part")


# 2 .........................................................
# ------------------- creating top mount to dowel ---------------------------
d_12 = gal.dowel_12["od"]
sup_mount_h = 12
sup_mount_offset = bear_offset * 2
sup_mount_x = sup_mount_offset - d_12 / 2

z_height = bearing["idr"]
d_mount = dowel_tube(d_12, thick, screw_od, z_height)

d_mount_br = bearing_inner_support(sup_mount_x, screw_od).up(bearing["h"] / 4)
d_mount_br = (
    d_mount_br.rotateY(270)
    .right(d_12 / 2 + thick)
    .forward(d_12 / 2 + bearing["idr"] / 2)
    .up(sup_mount_h / 2)
)

d_mount_cnxn = (
    ps.cube([thick, d_12 / 2 + bearing["idr"], bearing["idr"]], center=True)
    .up(bearing["idr"] / 2)
    .forward((d_12 / 2 + bearing["idr"]) / 2)
    .right(d_12 / 2 + thick / 2)
)

p_dmount = d_mount + d_mount_br + d_mount_cnxn
p_dmount.save_as_scad("OpenScad/SP2/Linker/dmount.scad")

