import solid2 as sp
import os

dir_s = os.path.dirname(os.path.abspath(__file__))

# OPENSCAD Dimensions
screw_hole = 4  # 3.5 is threaded
x_dist = 60
y_width = 4
cyl_d = 7

ladder_space = 10

thick = 3
arc_d = 13

# ------------------- global func/var -----------------------------------------
def tube(od, id, height): return sp.cylinder(d=od, h=height) - sp.cylinder(d=id, h=height*2).down(height/2)

def d_hole():
    outer_cyl = sp.cylinder(d=10, h=thick)
    inner_cyl = sp.cylinder(d=7, h= thick)
    arc_remove = sp.square([2.5,25]).right(90)
    arc = arc_remove.rotate_extrude(15, _fn=180)
    d_snap = outer_cyl - inner_cyl - arc
    return d_snap

# 1. Base
# ------------------- base -----------------------------------------
base_cube = sp.cube([x_dist / 2, y_width, thick]).back(y_width / 2)
base_cyl = tube(cyl_d, screw_hole, thick).right(x_dist / 2)
base_hole = sp.cylinder(d=screw_hole, h=thick).right(x_dist / 2)

# 2. Ladder attachment
# ------------------- creating ladder layouts -----------------------------------------
sq_x = (x_dist+ladder_space)/2
arc_x = sq_x-ladder_space
base_cube_sq = sp.cube([sq_x, y_width, thick]).back(y_width / 2)
base_cyl_sq = d_hole().right(sq_x)
base_hole_sq = sp.cylinder(d=screw_hole, h=thick).right(sq_x)

# ------------------- arc hole -----------------------------------------
arc_rim = sp.cylinder(d=arc_d, h=thick).right(arc_x)

arc_hole = sp.cylinder(d=9, h=thick).right(arc_x)
arc_cut = sp.cube([arc_d / 2 + arc_x, arc_d, thick]).back(arc_d + y_width / 2)

part = base_cube_sq + base_cyl_sq + arc_rim - arc_hole - arc_cut - base_hole_sq

part = part + part.rotateZ(180)

# ------------------- base -----------------------------------------
base_part = base_cube+base_cyl-base_hole
base_part = base_part + base_part.rotateZ(180)
ass = base_part+part.back(20)



# SAVING
part.save_as_scad(f"{dir_s}/SCAD/part.scad")
base_part.save_as_scad(f"{dir_s}/SCAD/base_part.scad")
ass.save_as_scad(f"{dir_s}/SCAD/ass.scad")

