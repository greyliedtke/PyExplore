"""
creating flowers that sprout and water

3 flowers that sprout and grow

"""

pix = 16
flowers = [2, 8, 13]    # x locations of flowers
earth = [[0 for i in range(pix)], list(range(pix))]
grass = [[0 for i in range(pix)], list(range(pix))]
sun = [[14, 15],[14,15]]

# create class for flower
class Flower:
    def __init__(self, x_loc, color):
        self.x_loc = x_loc
        self.stem = 0
        self.rate = 1
        self.flowers = color
        self.stem_mat = [[],[]]
        self.flower_mat = [[],[]]
    
    def grow(self):
        self.stem += 1




f1 = Flower(2, [255, 200, 0]) 


class Scene:
    def __init__(self):
        self.rate = .25

    def rain(self):
        # dropping rain 