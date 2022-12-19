"""
Script to create double pendule rectangle version parts
"""

from solid import circle, cylinder, translate, cube, rotate, rotate_extrude, square
import viewscad

r = viewscad.Renderer()

# Creating bearing dowel holder... all dimensions in mm
bearing_height = 7  # mm
bearing_od = 23
thick = 2
dowel_d = 7  # 1/2 in dowel
screw_offset = 5  # how far screw is from end of dowel
screw_d = 2
part_gap = 1


def tube(od, id, height):
    # function to create tube from two diameters and height
    outer_cylinder = cylinder(d=od, h=height)
    innter_cylinder = cylinder(d=id, h=height)
    tube_cyl = outer_cylinder - innter_cylinder
    return tube_cyl


# rectangle outline
base_length = bearing_od + 2 * dowel_d + 2 * thick + 2 * screw_offset
base_width = bearing_od + 2 * thick
base_height = (dowel_d / 2) + thick

outline = cube([base_length, base_width, base_height], center=True)  # outer rectangle

bearing_odr = 21  # bearing outer diameter race CHECK THIS!!!
bearing_hole = cylinder(d=bearing_od, h=bearing_height / 2 - part_gap)
bearing_hole = translate([0, 0, 2])(bearing_hole)
through_hole = cylinder(d=bearing_odr, h=base_height)
through_hole = translate([0, 0, -base_height / 2])(through_hole)


bearing_half = outline - bearing_hole - through_hole

# hole cutouts...
dowel_hole = cylinder(d=dowel_d, h=base_width, center=True)
dowel_hole = rotate([90, 0, 0])(dowel_hole)
dowel_x = (bearing_od + dowel_d) / 2 + thick
dowel_z = -base_height / 2 + thick + dowel_d / 2
dowel_hole_1 = translate([dowel_x, 0, dowel_z])((dowel_hole))
dowel_hole_2 = translate([-dowel_x, 0, dowel_z])((dowel_hole))
dowel_holes = dowel_hole_1 + dowel_hole_2


screw_x = base_length / 2 - screw_offset / 2
screw_hole = cylinder(d=screw_d, h=base_height, center=True)
screw_hole_1 = translate([-screw_x, 0, 0])((screw_hole))
screw_hole_2 = translate([screw_x, 0, 0])((screw_hole))
screw_hole_3 = translate([dowel_x, 0, 0])((screw_hole))
screw_hole_4 = translate([-dowel_x, 0, 0])((screw_hole))
screw_holes = screw_hole_1 + screw_hole_2 + screw_hole_3 + screw_hole_4

bearing_half = bearing_half - dowel_holes - screw_holes

r.render(bearing_half, file_header="$fa=1;\n $fs=0.5", outfile="rect_dp.stl")
