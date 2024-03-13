# imports
from solid import *
from solid import translate
import viewscad
import solid
from dimensions import tube, bearing_id, bearing_idr, screw_od, bearing_height, thick

r = viewscad.Renderer()


bearing_top = tube(bearing_idr, screw_od, thick)
bearing_tube = tube(bearing_id, screw_od, thick+bearing_height/2)

bearing_cap = bearing_tube + bearing_top

r.render(bearing_cap, outfile='OpenScad/Pendulum/STL/bearing_cap.stl', include_orig_code=True)
