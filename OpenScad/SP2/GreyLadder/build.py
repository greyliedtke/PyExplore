import solid2 as sp
import os

dir_s = os.path.dirname(os.path.abspath(__file__))

# OPENSCAD Dimensions

# ball_od = sp.CustomizerSpinnerVariable("ball_od", 50)
p_height = 10
post_d = 8
cord_hole = 6
screw_hole = 2.5
x_dist, y_dist = 11, 42
thick = 2
rim = 3

p_post = sp.cylinder(d=post_d, h = p_height)
post_h1 = sp.cylinder(d=screw_hole, h=5).up(p_height - 3)
post_h2 = sp.cylinder(d=cord_hole, h=10, center=True).rotateY(90).up(p_height/2)

post = p_post - post_h1 - post_h2
post = post.rotateZ(90)

posts = post + post.right(x_dist) + post.right(x_dist*2)
posts += posts.forward(y_dist)

base = sp.cube(2*x_dist+rim, y_dist+rim, thick) - sp.cube(2*x_dist-rim, y_dist-rim, thick).right(rim).forward(rim)
base = base.left(rim/2).back(rim/2)

part = posts + base
# PART Creation
# part = sp.cylinder(d=3, h=3)

# SAVING
part.save_as_scad(f"{dir_s}/SCAD/part.scad")