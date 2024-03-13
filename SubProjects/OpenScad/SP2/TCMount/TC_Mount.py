"""
script to create holder for Thermocouples
"""

# imports
import solid2 as ps

stl_dir = "OpenScad/SP2/TCMount"

# main dimensions
tc = {
    "w": 18,
}

through_hole = 3.5
thick = 1.5

base = {
    "w": tc["w"]+3*(through_hole+thick),
    "l": 10
}


base_p = ps.cube([base['w'], base['l'], thick], center=True).up(thick/2)
base_h = ps.cylinder(d=through_hole, h=10).down(thick)
side_h = base_h.right(tc["w"]/2+2*thick) + base_h.left(tc["w"]/2+2*thick)
p_base = base_p-base_h-side_h

# creating sides to hold tc in place
side_holder = ps.cube([thick, base["l"], thick*2], center=True).up(thick)
p_sides = side_holder.right(tc["w"]/2) + side_holder.left(tc["w"]/2)


p = p_base+p_sides


p.save_as_stl(f"{stl_dir}/TC_M.stl")
print('created')
