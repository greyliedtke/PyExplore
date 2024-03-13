"""
script to create holder for hoses and mount to slot-hardware
"""


# imports
import solid2 as ps

stl_dir = "OpenScad/SP2/HoseMount"

# main dimensions
hose = {
    "od": 20,
    "clamp_od": 24
}

base = {
    "w": 20,
    "l": 40
}
mount_h = 7
thick = 2
offset = 15


# function to create a tube that is arc with hole through it
def tube(od, id, h):
    tube_portion = ps.cylinder(d=od, h=h)-ps.cylinder(d=id, h=2*h).down(h/2)
    arc = ps.square([od, 2*h]).down(h/2).rotate_extrude(120)
    hole = ps.cylinder(d=4, h=25).rotateX(90).up(h/2)
    return tube_portion-arc-hole


# create rectangle with tubes at 4 corners
base_p = ps.cube([base['l'], base['w'], thick], center=True).up(thick/2)
base_h = ps.cylinder(d=mount_h, h=10).down(thick).left((base["l"]/2)-mount_h)
p_base = base_p-base_h

# creating hose clamp
p_hose_tube = tube(hose["clamp_od"], hose["od"],
                   base["w"]).rotateZ(120).rotateX(90).right(base['l']/2).up(hose["od"]/2).forward(base["w"]/2)

# creating an offset for hose
p_offset = ps.cube([thick, base["w"], offset], center=True).up(
    offset/2).right(base["l"]/2)
p_base += p_offset
p_hose_tube = p_hose_tube.up(offset)

p_base += p_hose_tube


p_base.save_as_stl(f"{stl_dir}/HoseMount.stl")
print('created')
