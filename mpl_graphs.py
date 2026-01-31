import matplotlib.pyplot as plt
import math

input_values = [x for x in range(1,100)]

linear = [x for x in range(1,100)]
print(linear)
squares = [x ** 2 for x in range(1,100)]
print(squares)
cubic = [x ** 3 for x in range(1,100)]
print(cubic)
exponential = [math.exp(x) for x in range(1,100)]
print(exponential)
logarithmic = [math.log(x) for x in range(1, 100)]
print(logarithmic)

plt.style.use('seaborn-v0_8-darkgrid') # Use before calling subplots() method

fig, ax = plt.subplots(1, 5)

ax[0].plot(input_values, linear, linewidth=3)
ax[0].set_title("Linear Function (y=x)", fontsize=8)


ax[1].plot(input_values, squares, linewidth=3)
ax[1].set_title("Square Function (y=x**2)", fontsize=8)

ax[2].plot(input_values, cubic, linewidth=3)
ax[2].set_title("Cubic Function (y=x**3)", fontsize=8)
ax[2].ticklabel_format(style='plain')

ax[3].plot(input_values, exponential, linewidth=3)
ax[3].set_title("Exponential Function (y=e**x)", fontsize=8)
#ax[3].ticklabel_format(style='plain')

ax[4].plot(input_values, logarithmic, linewidth=3)
ax[4].set_title("Logarithmic Function (y=ln(x))", fontsize=8)

for axes in ax:
    axes.set_xlabel("X Axis")
    axes.set_ylabel("Y Axis")
    axes.tick_params(labelsize=5)


plt.show()
