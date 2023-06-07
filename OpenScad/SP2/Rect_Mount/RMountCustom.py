"""
script to create rectangle mounting on t-slot
"""

# ------------------- imports -----------------------------------------
import solid2 as ps

# ------------------- main dimensions ---------------------------------
thick = 2
mount_od = 6
hh = 20
mount_w, mount_l = 20, 15
base_x = ps.CustomizerSliderVariable("base_x", 30, '5', '100')
base_y = ps.CustomizerSliderVariable("base_y", 30, '5', '100')
screw_od = ps.CustomizerSpinnerVariable("screw_od", 3.5, '.5')
offset = ps.CustomizerSpinnerVariable("offset", 5, '.5')


# ------------------- helper functions ---------------------------------
def tube(od, id, height):
    return ps.cylinder(d=od, h=height) - ps.cylinder(d=id, h=2 * height).down(height/2)


# ------------------- Base rectangle ------------------------------------
base_l = ps.cube([base_x + thick / 2, screw_od * 1.5, thick], center=True).up(thick / 2)
base_w = (
    ps.cube([base_y + thick / 2, screw_od * 1.5, thick], center=True)
    .up(thick / 2)
    .rotateZ(90)
)

# ------------------- Screw Tubes -----------------------------------------
screw_tube = tube(screw_od + thick * 2, screw_od, offset)

# ------------------- Moving Everything ------------------------------------
base_l = base_l + screw_tube.right(base_x / 2) + screw_tube.left(base_x / 2)
base_l = base_l.forward(base_y / 2) + base_l.back(base_y / 2)
base_w = base_w.right(base_x / 2) + base_w.left(base_x / 2)

base = base_l + base_w

# ------------------- Mounting to rail -------------------------------------
mount = ps.cube([mount_l, mount_w, thick], center=True).up(thick / 2)
mount = mount - ps.cylinder(d=mount_od, h=hh).forward(mount_w/2-mount_od)
mounts = mount.forward(base_y / 2 + mount_w / 2 - thick / 2) + mount.rotateZ(180).back(base_y / 2 + mount_w / 2 - thick / 2)

base = base + mounts
base = base.disable()
base.save_as_scad(f"OpenScad/SP2/Rect_Mount/Files/CustomRectMount.scad")

# rect_mount("Pico", 48, 11.4, 2, 10)
# rect_mount("v_conv", 25, 35)
# rect_mount("Zero", 23, 58)
# rect_mount("RelayBoard", 45, 20, 3, 10)