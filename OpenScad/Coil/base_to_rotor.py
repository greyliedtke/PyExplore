"""
base with arc for coils
"""

# imports
from solid import *
from solid import translate
import viewscad
import solid
from dimensions import tube, thick, bearing_height, bearing_idr, bearing_id, screw_od


# center base resting on inner bearing
inner_b = tube(bearing_id, screw_od, bearing_height/2)
inner_b_lip = tube(bearing_idr, screw_od, thick)
inner_b_lip = translate([0, 0, bearing_height/2])((inner_b_lip))

# final part
btp = inner_b+inner_b_lip

# creating stl file
r = viewscad.Renderer()
r.render(
    btp,
    file_header="$fn = 120;",
    outfile="OpenScad/Coil/STL/b_to_r.stl",
    include_orig_code=True,
)
