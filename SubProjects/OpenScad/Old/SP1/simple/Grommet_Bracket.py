"""
create right angle bracket
"""

from solid import (
    circle,
    cylinder,
    translate,
    cube,
    rotate,
    rotate_extrude,
    square,
    polygon,
)
import viewscad
r = viewscad.Renderer()


# dimensions
grommet_od = 9.5 # 3/8 (9.525)
thick = 2 # meant for 1/16" (1.588)
screw_od = 3.8  # 4-40 screw
spacing = 7 # padding around all holes

# base piece with 6 holes...
p_length = 2*(grommet_od/2+spacing) + 2*(grommet_od+spacing)
p_width = 2*(grommet_od/2+spacing) + 1*(grommet_od+spacing)
bc = cube([p_length, p_width, thick])

# grommet holes
gh_1 = translate([spacing+grommet_od/2,spacing+grommet_od/2,0])(cylinder(d=grommet_od, h=50))
gh_2 = translate([spacing+grommet_od,0,0])(gh_1)
gh_3 = translate([spacing+grommet_od,0,0])(gh_2)
ghs = gh_1+gh_2+gh_3
ghs += translate([0,spacing+grommet_od,0])(ghs)


# base for mounting
base_mount = cube([p_length, p_width/2, thick])
screw_1 = translate([spacing+grommet_od/2,spacing+grommet_od/2,0])(cylinder(d=screw_od, h=50))
screw_2 = translate([2*(spacing+grommet_od),0,0])(screw_1)
bm = rotate([90, 0, 0])(base_mount-(screw_1+screw_2))

part = bc-ghs + bm

fname = 'base'
stl_file = r.render(
    part,
    file_header="$fa=.01;\n $fs=0.01",
    outfile=f"OpenScad/simple/STL/grom_holder.stl",
)

