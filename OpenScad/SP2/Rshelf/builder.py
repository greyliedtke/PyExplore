import solid2 as sp


# ------------------- initialze variables -----------------------------------------
import dim as d

fdir = "OpenScad/SP2/Rshelf/Files"


# ------------------- helper functions -----------------------------------------
def tube(od, id, h):
    return sp.cylinder(d=od, h=h) - sp.cylinder(d=id, h=2 * h).down(h / 2)


# ------------------- bottom support below bearing -----------------------------------------
p_bch = 10
p_bc = tube(d.d_od + d.a_thick * 2, d.d_od, p_bch)
p_bc -= sp.cylinder(d=d.s_od, h=d.s_h, center=True).rotateY(90).up(p_bch / 2)
p_bc += tube(d.b_id, d.d_od, h=d.b_h).up(p_bch)
# screw hole
# butt up to below bearing
p_bc.save_as_scad(f"{fdir}/bottom_cylinder.scad")


# ------------------- top support piece -----------------------------------------
p_ts = tube(d.b_od + d.a_thick, d.b_odr, 3)

ttl = 40
mate_d = d.b_od + d.a_thick
mate = 3.5
p_tt = tube(d.b_od + 2 * d.a_thick, d.b_od, ttl)  # top tube connect top to base
p_t_h = sp.cylinder(d=d.s_od, h=10).forward(mate_d / 2)
p_t_h = p_t_h + p_t_h.rotateZ(120) + p_t_h.rotateZ(240)

p_top = p_ts + p_tt - p_t_h.up(ttl - 10)
p_top.save_as_scad(f"{fdir}/top_support.scad")


# ------------------- piece to connect to top -----------------------------------------

p_t_b = tube(mate_d + 20, mate_d - 2*d.a_thick, d.a_thick)
p_t_b -= p_t_h

c_off = 22

c_o_od = 2 * (d.c_od + c_off)

coaster_tube = tube(d.c_od + d.a_thick, d.c_od - d.a_thick, h=d.a_thick)
coaster_tube += tube(d.c_od + d.a_thick, d.c_od, h=d.c_h).up(d.a_thick)
coaster_tube = coaster_tube.forward(d.c_od / 2 + c_off)
coaster_tube += (
    coaster_tube.rotateZ(90) + coaster_tube.rotateZ(180) + coaster_tube.rotateZ(270)
)

# p_t_b += tube(c_o_od + d.a_thick, c_o_od, d.a_thick)

p_t_b += coaster_tube
p_t_b.save_as_scad(f"{fdir}/bot_c.scad")

print("parts created!")
