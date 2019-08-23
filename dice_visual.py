import pygal

from die import Die

# Create two D8 dice.
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(500000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
x_labels = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    x_labels.append(value)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 500,000 times."
hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * 3', frequencies)
hist.render_to_file('dice_visual.svg')