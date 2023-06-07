"""
script to create rectangle mounting on t-slot
"""

# ------------------- imports -----------------------------------------
import solid2 as ps

# ------------------- main dimensions ---------------------------------
d_b_od = 40
d_s_od = 13.5
d_thick = 2
d_off = (d_b_od+d_s_od)/2+d_thick

ball_od = ps.CustomizerSpinnerVariable("ball_od", d_b_od)
support_od = ps.CustomizerSpinnerVariable("support_od", d_s_od)
thick = ps.CustomizerSpinnerVariable("thick", d_thick)
off_length = ps.CustomizerSpinnerVariable("ofset_length", d_off)

support_odd = support_od+2*thick
ball_odd = ball_od+2*thick

# ------------------- helper functions ---------------------------------
def tube(od, id, height):
    return ps.cylinder(d=od, h=height) - ps.cylinder(d=id, h=2 * height).down(height/2)


# ------------------- Base rectangle ------------------------------------
center_h = thick*4
p_center = tube(support_odd, support_od, center_h)
center_hole = ps.cylinder(d=3.5, h=20).rotateX(90).up(center_h/2).forward(10)
p_center -= center_hole

connect_length = off_length-support_od/2-ball_od/2
p_ball_connect = ps.cube([connect_length, thick, thick], center=True).right(
    support_od/2+connect_length/2).up(thick/2)

p_ball = tube(ball_odd, ball_od, thick).right(off_length)
p_ball_hold = p_ball+p_ball_connect
p_balls = p_ball_hold

rotates = 3
for r in range(rotates):
    p_balls += p_ball_hold.rotateZ(r*(360/rotates))
part = p_center+p_balls

part.save_as_scad(f"OpenScad/SP2/BallMount/BallMount.scad")

# rect_mount("Pico", 48, 11.4, 2, 10)
# rect_mount("v_conv", 25, 35)
# rect_mount("Zero", 23, 58)
# rect_mount("RelayBoard", 45, 20, 3, 10)