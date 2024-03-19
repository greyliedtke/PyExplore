"""
standard library for creating common parts.. genius

# add path to standard library
import sys
sys.path.append("OpenScad/SP2/Glib")
import gal
from gal import bearing, tube, bearing_container, bearing_inner_support, dowel_tube

"""
import solid2 as ps

# Common used dimensions
bearing = {
        "od": 23,
        "odr": 18.5,
        "id": 7.75,
        "idr": 11.5,
        "h": 7
    }

dowel_14 = {
    "od":7.5,
    "h":305
    }


dowel_12 = {
    "od":13.5,
    "h":900
    }

# rect_mount("Pico", 48, 11.4, 2, 10)
# rect_mount("v_conv", 25, 35)
# rect_mount("Zero", 23, 58)
# rect_mount("RelayBoard", 45, 20, 3, 10)

# ------------------- helper functions -----------------------------------------
def tube(od, id, height):
    return ps.cylinder(d=od, h=height) - ps.cylinder(d=id, h=2 * height).down(
        height / 2
    )


# ------------------- bearings -----------------------------------------
class BearingContainer:
    def __init__(self, thick, screw_od):
        self.h = thick + bearing["h"]
        p_bearing_base_rim = tube(bearing["od"] + 2 * thick, bearing["odr"], thick)
        p_bearing_outer_tube = tube(bearing["od"] + 2 * thick, bearing["od"], self.h)
        b_side_hole = ps.cylinder(d=screw_od, h=30).rotateX(90).up(self.h / 2)
        self.p = p_bearing_base_rim + p_bearing_outer_tube - b_side_hole
        self.odd = bearing["od"]+2*thick
        

    
def bearing_container(thick, screw_od):
    # Create a standard bearing container with rim and set screw to hold onto bearing
    part_h = thick + bearing["h"]
    p_bearing_base_rim = tube(bearing["od"] + 2 * thick, bearing["odr"], thick)
    p_bearing_outer_tube = tube(bearing["od"] + 2 * thick, bearing["od"], part_h)
    b_side_hole = ps.cylinder(d=screw_od, h=30).rotateX(90).up(part_h / 2)
    p_bearing_container = p_bearing_base_rim + p_bearing_outer_tube - b_side_hole
    return p_bearing_container

def bearing_inner_support(height, screw_od):
    p_bearing_rim_ext = tube(bearing["idr"], screw_od, height)
    p_bearing_inner_support = tube(bearing["id"], screw_od, bearing["h"] / 2).up(height)
    return p_bearing_rim_ext+p_bearing_inner_support


# -------------------- Dowels --------------------------------------------------------
def dowel_tube(d_od, thick, screw_od, height):
    d_mount = tube(d_od + 2 * thick, d_od, height)
    d_mount -= ps.cylinder(d=screw_od, h=30).rotateX(90).up(height/2)
    return d_mount


# ------------------- hollow rectangle -----------------------------------------
# creating rect in rect instead...
def hollow_rect(rect_x, rect_y, thick, height):
    inside = ps.cube([rect_x, rect_y, height * 2], center=True)
    outside = ps.cube([rect_x + 2 * thick, rect_y + 2 * thick, height], center=True)
    rect = (outside - inside).up(height / 2)
    return rect

# ------------------- rectangle with hole -----------------------------------------
def c_rect(x_side, y_side, height, hole):
    hr = ps.cube([x_side, y_side, height], center=True).up(height / 2) - ps.cylinder(
        d=hole, h=height * 2
    ).down(height / 2)
    return hr

# Testing purposes
if __name__ == "__main__":
    print("ok")