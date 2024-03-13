"""
script for ball bouncing around screen
"""

from Strip import s


class BallWall:
    def __init__(self):
        self.pos = [0,0]    # xy
        self.vel = [1,1]    # xy
        self.perim = [self.pos[0], self.pos[1], self.pos[0]+1, self.pos[1]+1]

    def init(self):
        # create border
        # reset pos
        s1.border([2, 0,0])
        

    def loop(self):
        x = self.pos[0] + self.vel[0]
        y = self.pos[1] + self.vel[1]

        # if hitting walls.. reverse velocity and move back
        if x == 16:
            self.pos[0] -= 2
            self.vel[0] = -self.vel[0]
        elif x == 0: 
            self.pos[0] +=2
            self.vel[0] = -self.vel[0]
        
        if y >= 16:
            self.pos[1] -= 2
            self.vel[1] = -self.vel[1]
        elif y == 0:
            self.pos[1] +=2
            self.vel[1] = -self.vel[1]

        return self.pos
    
bw = BallWall()

        

