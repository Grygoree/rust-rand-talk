import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

import math


def main():
    iterations_per_figure = 200
    fig, ax = plt.subplots()
    circle = patches.Circle((0,0), radius=1, fill=False)
    ax.add_patch(circle)
    ax.set_xlim((-1,1))
    ax.set_ylim((-1,1))
    plt.gca().set_aspect('equal')

    ## Add points
    points = generate_points(iterations_per_figure)
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    colors = ["blue" for _ in points]

    plt.scatter(xs, ys, None, colors)
    plt.savefig("sad_circle_1.png")

    points.extend(generate_points(iterations_per_figure))
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    colors = ["blue" for _ in points]

    plt.scatter(xs, ys, None, colors)
    plt.savefig("sad_circle_2.png")

    points.extend(generate_points(iterations_per_figure))
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    colors = ["blue" for _ in points]

    plt.scatter(xs, ys, None, colors)
    plt.savefig("sad_circle_3.png")

def generate_points(num_points):
    points = []
    for _ in range(num_points):
        angle = (random.uniform(0,1)*2.0 - 1.0) * math.pi
        radius = (random.uniform(0,1))
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append((x,y))
    return points

if __name__ == "__main__":
    main()