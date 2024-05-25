import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
##import numpy as np


def main():
    fig, ax = plt.subplots()
    circle = patches.Circle((0,0), radius=1, fill=False)
    ax.add_patch(circle)
    ax.set_xlim((-1,1))
    ax.set_ylim((-1,1))
    plt.gca().set_aspect('equal')

    ## Add points
    points = generate_points(800)
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    ss = [3 for _ in points]
    colors = [point[2] for point in points]

    plt.scatter(xs, ys, ss, colors)
    plt.savefig("good_circle.png")

def generate_points(num_points):
    points = [(
        x := random.uniform(-1,1), 
        y := random.uniform(-1,1), 
        "red" if x**2 + y**2 > 1.0 else "blue") 
        for _ in range(num_points)]
    return points

if __name__ == "__main__":
    main()