"""
script for building links on servo wall art
"""

import solid2 as ps

# ------------------- loading dimensions -----------------------------------------
import json

with open("OpenScad/dimensions.json", "r") as file:
    # Load JSON data from file as a dictionary
    dim = json.load(file)
bearing = dim["bearing"]
dowel = dim["dowel"]


# ------------------- helper functions -----------------------------------------
def tube(od, id, height):
    return ps.cylinder(d=od, h=height) - ps.cylinder(d=id, h=2 * height).down(
        height / 2
    )


# ------------------- part specific dimensions -----------------------------------------
thick = 2
link_distance = 70
screw_od = dim["screw"]["od_440"]
arm_len = link_distance - (bearing["od"] + 2 * thick) / 2 - bearing["idr"] / 2
bear_offset = 25

# ------------------- base -----------------------------------------
part_h = bearing["h"] + thick
p_bb = tube(bearing["od"] + 2 * thick, bearing["odr"], thick)
p_bt = tube(bearing["od"] + 2 * thick, bearing["od"], part_h)
b_hole = ps.cylinder(d=screw_od, h=30).rotateX(90).up(part_h / 2)
p_bearing = p_bb + p_bt - b_hole

# ------------------- arm for part -----------------------------------------
p_arm = (
    ps.cube([arm_len, thick * 4, part_h], center=True)
    .up(part_h / 2)
    .left(arm_len / 2 + bearing["od"] / 2)
)

# ------------------- bearing carrier attachment -----------------------------------------
p_bcb = tube(bearing["idr"], screw_od, bear_offset)
p_bcc = tube(bearing["id"], screw_od, bearing["h"] / 2).up(bear_offset)
p_bc = (p_bcb + p_bcc).left(arm_len + bearing["od"] / 2 + thick)

# ------------------- combining -----------------------------------------
p_link = p_bearing + p_arm + p_bc


# ------------------- creating top mount to dowel ---------------------------
d_12 = dim["dowel_1/2"]["od"]
sup_mount_h = 12
sup_mount_offset = bear_offset * 2
sup_mount_x = sup_mount_offset - d_12 / 2
d_mount = tube(d_12 + 2 * thick, d_12, sup_mount_h)
d_mount -= ps.cylinder(d=screw_od, h=30).rotateX(90).up(sup_mount_h/2)

d_mount_br = (tube(bearing["idr"], screw_od, sup_mount_x)+ tube(bearing["id"], screw_od, bearing["h"] / 2).up(bearing["h"]/4) )# .up(thick)
d_mount_br = d_mount_br.rotateY(270).right(d_12/2+thick).forward(d_12/2+bearing["idr"]/2).up(sup_mount_h/2)

d_mount_cnxn = ps.cube([thick, d_12/2+bearing["idr"], bearing["idr"]], center=True).up(bearing["idr"]/2).forward((d_12/2+bearing["idr"])/2).right(d_12/2+thick/2)

p_dmount = d_mount + d_mount_br + d_mount_cnxn
p_dmount.save_as_scad("OpenScad/SP2/Linker/dmount.scad")

# ------------------- saving -----------------------------------------
p_link.save_as_scad("OpenScad/SP2/Linker/link.scad")
print("created part")
