"""
file to create ring of ball holding lol
"""

import solid2 as ps


def tube(od, id, height): return ps.cylinder(d=od, h=height) - \
    ps.cylinder(d=id, h=2*height).down(height)

thick = 3.5
off_length = 58

support = {
    "id": 13.5,
    "odd": 13.5+2*thick
}

ball = {
    "id": 54,
    "odd": 54+2*thick
}

center_h = thick*4
p_center = tube(support["odd"], support["id"], center_h)
center_hole = ps.cylinder(d=3.5, h=20).rotateX(90).up(center_h/2).forward(10)
p_center -= center_hole

connect_length = off_length-support["id"]/2-ball["id"]/2
p_ball_connect = ps.cube([connect_length, thick, thick], center=True).right(
    support["id"]/2+connect_length/2).up(thick/2)

p_ball = tube(ball["odd"], ball["id"], thick).right(off_length)
p_ball_hold = p_ball+p_ball_connect
p_balls = p_ball_hold
rotates = 6
for r in range(rotates):
    p_balls += p_ball_hold.rotateZ(r*(360/rotates))

part = p_center+p_balls

part.save_as_stl("OpenScad/SP2/Ballmount/ball_circle.stl")
