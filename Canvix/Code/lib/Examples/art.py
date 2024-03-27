"""
pixel art created...
"""

from Examples.Art import a1 as image
from Tools.matrix import Matrix as m

# ------------------------------------------------------
# handling image imports
images = {
    "a1": image
}
# ------------------------------------------------------

# ------------------------------------------------------
# send matrix image
def send_image(img_name):
    image_matrix = images[img_name]
    for i in image_matrix:
        x = i[0][0]
        y = i[0][1]
        color = i[1][0]
        m.send_point(x, y, color)
# ------------------------------------------------------
