import solid2 as sp
import os

dir_s = os.path.dirname(os.path.abspath(__file__))

# OPENSCAD Dimensions
hole_space = sp.CustomizerSpinnerVariable("hole_space", 50)
hole_d = sp.CustomizerSpinnerVariable("hole_diameter", 3.5)
z_h = sp.CustomizerSpinnerVariable("height", 5)
thick = sp.CustomizerSpinnerVariable("thick", 2)



# triangle function
def p_triangle(b, h, z):
    # creates triangle of base and height
    v1 = [0, 0, 0]
    v2 = [b, 0, 0]
    v3 = [b / 2, h, 0]
    triangle = sp.polygon([v1, v2, v3])
    triangle = sp.linear_extrude(height=z)(triangle)
    triangle = triangle.left(b / 2).back(h / 2)
    return triangle

# PART Creation
x_din = 35
y_din = 2

x_base = x_din+2*thick
y_base = y_din+3*thick

tri_y = x_din/2

y_thick = 4
y_ext = 7
thick = 3

# din connection
base = sp.cube([x_base, y_base, z_h], center = True).up(z_h/2).forward(y_base/2)
din_hole = sp.cube([x_din, y_din, z_h], center = True).up(z_h/2).forward(thick+y_din/2)
ret_tri = p_triangle(x_din, tri_y, z_h).forward(tri_y/2+thick+y_din)
din_top_hole = sp.cube([x_din-thick, thick, z_h], center = True).up(z_h/2).forward(2*thick+y_din)


handle_x = thick*3
din_handle = sp.cube([handle_x, thick, z_h], center=True).up(z_h/2).right(x_din/2+handle_x/2).forward(thick/2+y_base-thick)

# customizable base holes
hole_sup_l = hole_space+2*hole_d
attach_base = sp.cube([hole_sup_l, thick, z_h], center=True).up(z_h/2).forward(thick/2)
attach_hole = sp.cylinder(d=hole_d, h=thick).rotateX(90).up(z_h/2)
attach_holes = attach_hole.right(hole_space/2).forward(thick)
attach_holes += attach_holes.left(hole_space)
hole_2_attach = attach_base-attach_holes


part_1h = base-ret_tri-din_hole-din_top_hole+din_handle - attach_hole
part_2h = base-ret_tri-din_hole-din_top_hole+din_handle + hole_2_attach

# SAVING
# part.save_as_stl(f"{dir_s}/SCAD/part.stl")
part_1h.save_as_scad(f"{dir_s}/SCAD/part_1h.scad")
part_2h.save_as_scad(f"{dir_s}/SCAD/part_2h.scad")