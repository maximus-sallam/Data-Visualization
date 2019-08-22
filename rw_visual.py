import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.viridis,
                edgecolors='none', s=15)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c=(0, 0, 0), edgecolors='none', s=30)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c=(0, 0, 0),
                edgecolors='none', s=30)

    # Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break