import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plot the points.
rw = RandomWalk(5000)
rw.fill_walk()

# Set the size of the plotting window.
plt.figure(figsize=(12, 9))

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, linewidth=0.5, c='blue')

# Emphasize the first and last points.
plt.scatter(0, 0, c='black')
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='black')

# Remove the axes
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()