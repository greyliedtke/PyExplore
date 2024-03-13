"""
script for creating rotating servo holder of sand art
"""
import solid2 as sp

d_od = 7.5
screw_od = 3.5
thick = 3

# creating base for servo mounting
base = sp.cylinder(d=35, h=thick)

d_rect = sp.cube([15, 15, 20], center=True)
d_hole = sp.cylinder(d=d_od, h=40).translateZ(-20)
dowel_mount = d_rect-d_hole
dowel_mount = dowel_mount.rotateY(90)
dowel_mount -= sp.cylinder(d=screw_od, h=10).translateX(-4)
dowel_mount -= sp.cylinder(d=screw_od, h=10).translateX(4)
dowel_mount = dowel_mount.translateX(25).translateZ(15/2)
d2m = dowel_mount.rotateZ(120)
d3m = dowel_mount.rotateZ(240)
dms = dowel_mount+d2m+d3m

part = base+dms
part.save_as_stl('OpenScad/SP2/SandMan/base.stl')

d_length = 6*25.4
dowel = sp.cylinder(d=d_od, h=d_length).color("brown")
p_d1 = dowel.rotateY(90).up(thick+d_od/2)
p_ass = part+p_d1
p_ass.save_as_stl('OpenScad/SP2/SandMan/ass.stl')

sand_od = 12*25.4
height = 25

arc = sp.square([10, height], center=True).right(
    sand_od/2).rotate_extrude(30).up(height/2).right(-sand_od/2)
arc += sp.square([10, thick], center=True).right(sand_od/2 -
                                              10).rotate_extrude(30).up(height/2).right(-sand_od/2)

d_rect = sp.cube([15, 15, 20], center=True)
d_hole = sp.cylinder(d=d_od, h=40).translateZ(-20)
dowel_mount = d_rect-d_hole
dowel_mount = dowel_mount.rotateY(90)
dowel_mount -= sp.cylinder(d=screw_od, h=10).translateX(-4)
dowel_mount -= sp.cylinder(d=screw_od, h=10).translateX(4)
dowel_mount = dowel_mount.translateX(-25).translateZ(15/2)

part = arc+dowel_mount
part.save_as_stl('OpenScad/SP2/SandMan/sandm.stl')
