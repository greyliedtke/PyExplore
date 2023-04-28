"""
base with arc for coils
"""

# imports
from solid import *
from solid import translate
import viewscad
import solid
from dimensions import tube, screw_od, thick, mag_od

r = viewscad.Renderer()


# magnet rotor
mag_d = mag_od-thick
mag_h = 20

# rotor base
rotor_base = cylinder(d=mag_d+thick*2, h=thick)
rotor_tube = tube(mag_d, mag_d-thick, mag_h)
rotor_tube = translate([0, 0, thick])((rotor_tube))
rotor_hole = cylinder(d=screw_od, h=10)

# lip to serve as key
rl = cube([thick, 1, mag_h])
rl = translate([mag_d/2, 0, thick])((rl))
rl += translate([-(mag_d+thick), 0, 0])((rl))


rotor = rotor_tube+rotor_base-rotor_hole+rl

r.render(
    rotor,
    file_header="$fn = 120;",
    outfile="OpenScad/Coil/STL/rotor_house.stl",
    include_orig_code=True,
)
