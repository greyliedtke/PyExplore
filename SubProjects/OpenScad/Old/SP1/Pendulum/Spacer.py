"""
Dowel Bearing piece
"""

# imports
from solid import *
from solid import translate
import viewscad
import solid
from dimensions import tube, bearing_id, bearing_idr, screw_od, mount_ext

r = viewscad.Renderer()

spacer_tube = tube(bearing_idr, screw_od, mount_ext) # outer cylinder 

r.render(spacer_tube, outfile='OpenScad/Pendulum/STL/spacer.stl', include_orig_code=True)
# file_header = '$fa = 0.1;\n$fs = 0.1;',