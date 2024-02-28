"""
tools for plotting data
"""
import math
import matplotlib.pyplot as plt


def p_to_p(p1, p2):
    # create line that connects two points
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        return [x1, y1]
    m = dy/dx
    b = y1 - m*x1
    return [m, b, dx]


def bound_box(data):
    bb_points = []
    for d in data:
        x,y = d[0], d[1]
        x1 = math.floor(x)
        x2 = math.ceil(x)
        if x1 == x2:
            x2 += 1
        y1 = math.floor(y)
        y2 = math.ceil(y)
        if y1 == y2:
            y2 += 1
        bb_points += [[x1,y1], [x1, y2], [x2, y1], [x2, y2]]
        # remove duplicates
        bb_points = list(set([tuple(point) for point in bb_points]))
    return bb_points

def plotter(data, data2=None, matrix=False):
    # Create a figure and axis object
    fig, ax = plt.subplots()

    rd = ax.scatter(0, 8, color='red')
    rd.set_offsets(data)

    if data2:
        rd2 = ax.scatter(0, 8, color='blue')
        rd2.set_offsets(data2)

    if matrix:
        ax.set_xlim(0, 15)
        ax.set_ylim(0, 15)
    else:
        ax.set_xlim(-8, 8)
        ax.set_ylim(-8, 8)
    # Set the aspect ratio to equal
    ax.set_aspect('equal')
    return fig