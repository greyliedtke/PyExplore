"""
Dowel Bearing piece
"""

# imports
from solid import *
from solid import translate
import viewscad
import solid
from dimensions import (
    tube,
    bearing_od,
    bearing_odr,
    bearing_height,
    dowel_d,
    screw_od,
    thick,
)

r = viewscad.Renderer()

# two rings to hold bearing in place on part
outer_od = bearing_od + 3 * thick
outer_id = bearing_od - thick
base_tube = tube(outer_od, bearing_odr, thick)
bearing_tube = tube(outer_id, bearing_odr, thick*2)  # outer cylinder
bearing_tube = translate([0, 0, thick])((bearing_tube))

# support holes
sup_hole = tube(screw_od * 2, screw_od, thick)
sup_distance = 17.25
sup_hole_1 = translate([0, sup_distance, 0])((sup_hole))
sup_hole_2 = translate([0, -sup_distance, 0])((sup_hole))

cap = base_tube + bearing_tube + sup_hole_1 + sup_hole_2


r.render(
    cap,
    file_header="$fn = 120;",
    outfile="OpenScad/Pendulum/STL/dowel_bearing_cap.stl",
    include_orig_code=True,
)
