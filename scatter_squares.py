import matplotlib.pyplot as plt

x_cube_values = list(range(1, 5001))
y_cube_values = [x**3 for x in x_cube_values]

x_square_values = list(range(1, 5001))
y_square_values = [x**2 for x in x_square_values]

plt.scatter(x_cube_values, y_cube_values, c=(0, 0, 1), edgecolor='none', s=40)
plt.scatter(x_square_values, y_square_values, c=(1, 0, 0), edgecolor='none', s=40)

# Set chart title and label axes.
plt.title("Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Numbers of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, 5000, 0, 12500000])

plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')