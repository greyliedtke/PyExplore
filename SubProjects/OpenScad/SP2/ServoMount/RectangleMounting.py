"""
script to create pi zero mounting
"""

# ------------------- imports -----------------------------------------
import solid2 as ps

# ------------------- main dimensions ---------------------------------
thick = 2
screw_od = 2
mount_od = 6
hh = 20
mount_l = 40
mount_w = 40
servo = {
    "l": 23,
    "w": 13,
    "hd": 27
}

# ------------------- Base rectangle ------------------------------------
p_base = ps.cube([mount_l, mount_w, thick], center=True).up(thick / 2).forward(mount_w/2)
p_servo = ps.cube([servo["l"], servo["w"], thick], center=True).up(thick/2).forward(servo["w"]/2)

h_servo = ps.cylinder(d=screw_od, h=hh).forward(servo["w"]/2)
h_servos = h_servo.right(servo["hd"]/2) + h_servo.left(servo["hd"]/2)
h_mount = ps.cylinder(d=mount_od, h=hh).forward(mount_w-mount_od)


# ------------------- Screw Tubes -----------------------------------------
p = p_base-p_servo - h_servos - h_mount
p.save_as_scad("OpenScad/SP2/ServoMount/Files/servomount.scad")
