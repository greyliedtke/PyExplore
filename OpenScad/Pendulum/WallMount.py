# imports
from solid import *
from solid import translate
import viewscad
import solid
from dimensions import tube, bearing_id, bearing_idr, screw_od, bearing_height, thick, mount_ext

r = viewscad.Renderer()

# hold bearing in place
bearing_top = tube(bearing_idr, screw_od, mount_ext+thick)
bearing_tube = tube(bearing_id, screw_od, mount_ext+bearing_height/2+thick)

# base support 
sup_c_d = 30
sup_circle = cylinder(d=sup_c_d, h=thick)

# support holes for screw
sup_hole = cylinder(d=screw_od, h=thick)
sup_hole_1 = translate([sup_c_d/2 - screw_od/2 - thick, 0, 0])(sup_hole)
sup_hole_2 = rotate([0,0,120])(sup_hole_1)
sup_hole_3 = rotate([0,0,120])(sup_hole_2)
sup_holes = sup_hole_1+sup_hole_2+sup_hole_3



# actual part
bearing_cap = bearing_tube + bearing_top + sup_circle - sup_holes

r.render(bearing_cap, outfile='OpenScad/Pendulum/STL/wall_mount.stl', include_orig_code=True)
