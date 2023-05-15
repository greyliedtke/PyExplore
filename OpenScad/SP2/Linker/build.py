"""
script for building links on servo wall art
"""

import solid2 as ps

bearing = {
    "od": 23,
    "odr": 18.5,
    "id": 7.75,
    "idr": 11.5,
    "h":7
}

# functions
def tube(od, id, height):
    return ps.cylinder(d=od, h=height) - ps.cylinder(d=id, h=2 * height).down(height)

thick = 2
screw_od = 4
arm_len = 75
bear_offset = 25

# base thick
p_bb = tube(bearing["od"]+2*thick, bearing["odr"], thick)
p_bt = tube(bearing["od"]+2*thick, bearing["od"], bearing["h"]+thick)
b_hole = ps.cylinder(d=screw_od, h=30).rotateX(90).up((bearing["h"]+thick)/2)
p_bearing = p_bb+p_bt-b_hole

p_arm = ps.cube([arm_len, thick*4, thick], center = True).up(thick/2).left(arm_len/2+bearing["od"]/2)

p_bcb = tube(bearing["idr"], screw_od, bear_offset)
p_bcc = tube(bearing["id"], screw_od, bearing["h"]/2).up(bear_offset)
p_bc = (p_bcb+p_bcc).left(arm_len+bearing["od"]/2)


p_link = p_bearing+p_arm+p_bc
p_link.save_as_scad("OpenScad/SP2/Linker/link.scad")