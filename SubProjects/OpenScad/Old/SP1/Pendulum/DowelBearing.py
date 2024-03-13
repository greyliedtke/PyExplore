"""
Dowel Bearing piece
"""

# imports
from solid import *
from solid import translate
import viewscad
import solid
from dimensions import tube, bearing_od, bearing_odr, bearing_height, dowel_d, screw_od

r = viewscad.Renderer()

thick = 2

part_height = max(dowel_d, bearing_height+2*thick)

# outer circle for dowels...
outer_od = bearing_od*2
outer_id = outer_od-2*thick
outer_cylinder_tube = tube(outer_od, outer_id, part_height) # outer cylinder 

# inner cylinder for bearing
inner_od = bearing_od+2*thick
inner_cylinder_tube = tube(inner_od, bearing_od, part_height) # outer cylinder part diameter

# rim to keep bearing in place
bearing_rim = tube(bearing_od, bearing_odr, thick) # outer cylinder part diameter

# Solid body
dowel_bearing = outer_cylinder_tube + inner_cylinder_tube + bearing_rim 

# support holes
support_d = (outer_od - bearing_od)/2    # place in middle of two tubes
sup_tube = tube(support_d, screw_od, part_height) # outer cylinder part diameter
mid_tube = bearing_od/2 + support_d/2
sup_tube_1 = translate([0, mid_tube, 0])((sup_tube))
sup_tube_2 = translate([0, -mid_tube, 0])((sup_tube))
# print(mid_tube)

bearing_half = outer_cylinder_tube + inner_cylinder_tube + bearing_rim + sup_tube_1 + sup_tube_2

# hole cutouts...
dowel_hole = cylinder(d=dowel_d, h=outer_od, center=True)
dowel_hole = rotate([90,0,0])(dowel_hole)
dowel_hole_1 = translate([mid_tube, 0, part_height/2])((dowel_hole))
dowel_hole_2 = translate([-mid_tube, 0, part_height/2])((dowel_hole))
dowel_holes = dowel_hole_1 + dowel_hole_2
db = bearing_half - dowel_holes

screw_hole = cylinder(d=screw_od, h=100, center=True)

screw_hole = rotate([0,90,0])(screw_hole)
screw_hole = translate([0, 0, part_height/2])((screw_hole))

db = db - screw_hole
# screw_hole_1 = translate([-screw_x, 0, 0])((screw_hole))

r.render(db, file_header = '$fn = 120;', outfile='OpenScad/Pendulum/STL/dowel_bearing.stl', include_orig_code=True)
# file_header = '$fa = 0.1;\n$fs = 0.1;',