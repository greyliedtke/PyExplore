"""
script to create pi zero mounting
"""

# ------------------- imports -----------------------------------------
import solid2 as ps

# ------------------- main dimensions ---------------------------------
f_name = input("FileName:")
thick = 2
screw_od = 3
mount_od = 6
hh = 20
mount_l = 20
mount_w = 20
hh_w, hh_l = 25, 35
# voltage-4/20 conversion board - 25, 35
# Pico -- 11.4, 48
# zero -- 23, 58


# ------------------- functions -----------------------------------------
def tube(od, id, height):
    return ps.cylinder(d=od, h=height) - ps.cylinder(d=id, h=2 * height).down(height)


# ------------------- Base rectangle ------------------------------------
base_l = ps.cube([hh_l + thick / 2, screw_od * 1.5, thick], center=True).up(thick / 2)
base_w = (
    ps.cube([hh_w + thick / 2, screw_od * 1.5, thick], center=True)
    .up(thick / 2)
    .rotateZ(90)
)

# ------------------- Screw Tubes -----------------------------------------
screw_tube = tube(screw_od + thick * 2, screw_od, 10)

# ------------------- Moving Everything ------------------------------------
base_l = base_l + screw_tube.right(hh_l / 2) + screw_tube.left(hh_l / 2)

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
