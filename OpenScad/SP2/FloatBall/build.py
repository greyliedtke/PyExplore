"""
script for building links on servo wall art
"""

# add path to standard library
import sys

sys.path.append("OpenScad/SP2/Glib")
import gal
import solid2 as ps

fdir = "OpenScad/SP2/FloatBall/Files"

# ------------------- part specific dimensions -----------------------------------------
thick = ps.CustomizerSliderVariable("Thickness", 2)
base_cube_l = ps.CustomizerSliderVariable("BaseLength", 50)
base_cube_h = ps.CustomizerSliderVariable("BaseHeight", 20)
sphere_d = ps.CustomizerSliderVariable("sphereD", 75)
sphere_offset = ps.CustomizerSliderVariable("SphereOffset", 25)
d_hole = 7

# bottom base
p_base = ps.cube([base_cube_l, base_cube_l, base_cube_h], center=True).up(
    base_cube_h / 2
)

# negative portion from sphere
n_sphere = ps.sphere(d=sphere_d).up(sphere_offset + base_cube_h)

# center hole through
hole_center = ps.cylinder(d=7, h=base_cube_h * 2).down(base_cube_h)

# dowel holes for mounting
d_od = 7.5
d_hole = ps.cylinder(d=d_od, h=base_cube_l * 2).rotateY(90).left(base_cube_l/2).forward(base_cube_l/4).up(d_od)
d_hole += d_hole.back(base_cube_l/2)

# combine and save
p = p_base - n_sphere - hole_center - d_hole
p.save_as_scad(f"{fdir}/base.scad")
