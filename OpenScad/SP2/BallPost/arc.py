"""
script for building links on servo wall art
"""

import solid2 as ps

fdir = "OpenScad/SP2/BallPost/Files"

# ------------------- part specific dimensions -----------------------------------------
psq = ps.square([2.5,25]).right(90)
p = psq.rotate_extrude(15, _fn=180)

p.save_as_scad(f"{fdir}/arc.scad")
