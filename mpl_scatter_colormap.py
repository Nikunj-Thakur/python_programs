import matplotlib.pyplot as plt
import math

input = [x for x in range(1, 30)]
square = [x*x for x in input]
cube = [x*x*x for x in input]

print(input, square, cube)

plt.style.use('seaborn-v0_8-darkgrid')  # Use before calling subplots() method

fig, ax = plt.subplots()

ax.set_title("Scatter plots using colormap for linear, square and cubic functions")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.scatter(input, input, c=input, cmap=plt.cm.Blues, s=10)
ax.scatter(input, square, c=square, cmap=plt.cm.Reds, s=10)
ax.scatter(input, cube, c=cube, cmap=plt.cm.Greens, s=10)

plt.savefig("ScatterPlotWithColorMap.png",bbox_inches='tight') #bbox_inches='tight' trims extra whitespace from the plot

#plt.show()
