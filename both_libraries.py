import pygal

from random_walk import RandomWalk

# Make a random walk, and plot the points.
rw = RandomWalk(5000)
rw.fill_walk()

# Analyze the results.
frequencies = []
results = []
max_result = rw.x_values + rw.y_values
for x_value in rw.x_values:
    frequency = results.count(x_value)
    frequencies.append(frequency)
    results.append(x_value)


# Visualize the results.
hist = pygal.Bar()

hist.title = "IDK"
hist.x_labels = results
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('???', frequencies)
hist.render_to_file('both_libraries.svg')