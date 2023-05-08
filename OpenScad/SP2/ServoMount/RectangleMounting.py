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
mount_l = 20
mount_w = 20
hh_w, hh_l = 25, 35
servo = {
    "l": 20,
    "w": 10
}

# ------------------- Base rectangle ------------------------------------
p_base = ps.cube([hh_l, hh_w, thick], center=True).up(thick / 2)
p_servo = ps.cube([servo["l"], servo["w"], thick], center=True).up(thick/2)


# ------------------- Screw Tubes -----------------------------------------
screw_tube = ps.cylinder(d=screw_od, h=hh)

# ------------------- Moving Everything ------------------------------------
 = base_l + screw_tube.right(hh_l / 2) + screw_tube.left(hh_l / 2)

base_l = base_l.forward(hh_w / 2) + base_l.back(hh_w / 2)

base_w = base_w.right(hh_l / 2) + base_w.left(hh_l / 2)

base = base_l + base_w

# ------------------- Mounting to rail -------------------------------------
mount = ps.cube([mount_l, mount_w, thick], center=True).up(thick / 2)
mount = mount - ps.cylinder(d=mount_od, h=hh)
mounts = mount.forward(hh_w / 2 + mount_w / 2 - thick / 2) + mount.back(
    hh_w / 2 + mount_w / 2 - thick / 2
)

base = base + mounts
base.save_as_stl(f"OpenScad/SP2/Rect_Mount/Files/{f_name}.stl")
