"""
Dowel Bearing piece
"""

# imports
from solid import *
from solid import translate
import viewscad
import solid
from dimensions import tube, bearing_odr, bearing_od, bearing_height, thick, mag_od

r = viewscad.Renderer()


# center base of magnets
base_tube = tube(bearing_od+thick, bearing_od, bearing_height+thick)
base_b = tube(bearing_od, bearing_odr, thick)
base = base_tube + base_b

# arms for coils
gap = 5
arm_len = mag_od/2 + gap
coil_od = 30
coil_arm = cube([arm_len, 2*thick, 2*thick])
coil_arm = translate([bearing_od/2, 0, 0])((coil_arm))

coil_len = 20
coil_tube = tube(coil_od, coil_od-thick, coil_len)  # outer cylinder

# adding lips to keep wire in place
ll = thick
coil_tube_bl = tube(coil_od+ll, coil_od, ll)  # outer cylinder
coil_tube_tl = translate([0, 0, coil_len-ll])((coil_tube_bl))
coil_tube += coil_tube_bl+ coil_tube_tl

coil_tube = rotate([0, 90, 0])(coil_tube)
coil_tube = translate([arm_len, 0, coil_od/2+ll])((coil_tube))

arm1 = coil_arm+coil_tube
arm2 = rotate([0, 0, 120])(arm1)
arm3 = rotate([0, 0, 240])(arm1)
arms = arm1+arm2+arm3

coil_base = base + arms

r.render(
    coil_base,
    file_header="$fn = 120;",
    outfile="OpenScad/Coil/STL/base.stl",
    include_orig_code=True,
)
