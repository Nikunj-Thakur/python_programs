import matplotlib.pyplot as plt
import math

linear = [x for x in range(100)]
print(linear)
squares = [x ** 2 for x in range(100)]
print(squares)
cubic = [x ** 3 for x in range(100)]
print(cubic)
exponential = [math.exp(x) for x in range(100)]
print(exponential)
logarithmic = [math.log(x) for x in range(1, 100)]
print(logarithmic)

fig, ax = plt.subplots(1, 5)

ax[0].plot(linear, linewidth=3)
ax[0].set_title("Linear Function", fontsize=8)


ax[1].plot(squares, linewidth=3)
ax[1].set_title("Square Function", fontsize=8)

ax[2].plot(cubic, linewidth=3)
ax[2].set_title("Cubic Function", fontsize=8)

ax[3].plot(exponential, linewidth=3)
ax[3].set_title("Exponential Function", fontsize=8)

ax[4].plot(logarithmic, linewidth=3)
ax[4].set_title("Logarithmic Function", fontsize=8)

for axes in ax:
    axes.set_xlabel("X Axis")
    axes.set_ylabel("Y Axis")
    axes.tick_params(labelsize=5)

plt.show()
