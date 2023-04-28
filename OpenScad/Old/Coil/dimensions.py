"""
File to organize master dimensions and common functions
"""

from solid import cylinder
from solid import translate
import viewscad
import solid

# Creating bearing dowel holder... all dimensions in mm
bearing_height = 7  # mm
bearing_od = 23
bearing_odr = 18.5
bearing_id = 7.75
bearing_idr = 11.5
thick = 2
dowel_d = 7.5 # 1/4 in dowel
mag_d = 3.5
screw_od = 3.5
mount_ext = 25

mag_od = 30

def tube(od, id, height):
    outer_cylinder = cylinder(d=od, h=height)
    innter_cylinder = cylinder(d=id, h=height)
    tube_cyl = outer_cylinder-innter_cylinder
    return tube_cyl

