import matplotlib.pyplot as plt

squares = [x ** x for x in range(5)]
print(squares)
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)
ax.set_xlabel("Value")
ax.set_ylabel("Square of Value")
ax.set_title("Graphical View")
plt.show()
