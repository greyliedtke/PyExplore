"""
script to create rectangle mounting on t-slot
"""

# ------------------- imports -----------------------------------------
import solid2 as ps

# ------------------- main dimensions ---------------------------------
d_b_od = 7.5
d_s_l = 10
d_thick = 2

d_od = ps.CustomizerSpinnerVariable("d_od", d_b_od)
support_l = ps.CustomizerSpinnerVariable("support_l", d_s_l)
thick = ps.CustomizerSpinnerVariable("thick", d_thick)
ang = ps.CustomizerSpinnerVariable("angle", 90)
d_odd = d_od+2*thick


# ------------------- helper functions ---------------------------------
def tube(od, id, height):
    return ps.cube([od, od, height], center=True).up(height/2) - ps.cylinder(d=id, h=2 * height).down(height/2)


# ------------------- Base ------------------------------------
p_center = tube(d_odd, d_od, support_l)
center_hole = ps.cylinder(d=3.5, h=20).rotateX(90).up(support_l/2).forward(10)
p_center -= center_hole
p = p_center

# connection
p_cnxn = p_center.rotateY(ang).right(d_odd/2).up(support_l/2)

p+=p_cnxn

p.save_as_scad(f"OpenScad/SP2/Dowel/Dowel.scad")
