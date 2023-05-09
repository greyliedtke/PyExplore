"""
script to create pi zero mounting
"""

# ------------------- imports -----------------------------------------
import solid2 as ps

# ------------------- main dimensions ---------------------------------
mag_od = 9
mag_h = 4
bungie_od = 6
thick = 2
d_height = mag_h+bungie_od+2*thick
hh = 30

# ------------------- functions -----------------------------------------
def tube(od, id, height):
    return ps.cylinder(d=od, h=height) - ps.cylinder(d=id, h=2 * height).down(height)


# ------------------- Base magnet ------------------------------------
p_base = tube(mag_od, mag_od-2*thick, thick)
p_tube = tube(mag_od+2*thick, mag_od, d_height)
b_hole = ps.cylinder(d=bungie_od, h=hh).rotateX(90).forward(hh/2).up(d_height-bungie_od)

# ------------------- Build -----------------------------------------
p = p_base+p_tube-b_hole
p.save_as_stl(f"OpenScad/SP2/Magnet_Bungie/Files/MagnetBungie.stl")
