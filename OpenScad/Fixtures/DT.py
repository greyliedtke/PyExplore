from solid import cylinder, translate, cube, rotate
import viewscad

r = viewscad.Renderer()

screw_hole = 6

# base cylinder
side_support = cube([20, 5, 77]) 
base_support = cube([20, 40, 10]) 

piece = side_support+base_support


# screw holes
hole = cylinder(d=screw_hole, h=12)
dt_hole = rotate([90,0,0])(hole)
dt_hole = translate([10,10,0])(dt_hole)
h1 = translate([0,0,25])(dt_hole)
h2 = translate([0,0,50])(dt_hole)

mount_hole = cylinder(d=4, h=12)
mount_hole = rotate([0,0,90])(mount_hole)
mount_hole = translate([10,20,0])(mount_hole)


piece = piece-h1-h2-mount_hole

stl_file = r.render(piece, file_header="$fa=.01;\n $fs=0.01", outfile="OpenScad/DT_Mount/DT_Mount.stl")

