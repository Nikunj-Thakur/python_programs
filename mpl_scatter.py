import matplotlib.pyplot as plt
import math
input = [x for x in range(1,50)]
square = [x*x for x in input]
cube = [x*x*x for x in input]
exponential=[math.exp(x) for x in input]
logarithmic=[math.log(x) for x in input]
print(input, square,cube,exponential,logarithmic)

plt.style.use('seaborn-v0_8-darkgrid') # Use before calling subplots() method

fig, ax = plt.subplots()

ax.set_title("Scatter plots for standard functions")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.scatter(input,input,color='red',s=5)
ax.scatter(input,square,color='blue',s=5)
ax.scatter(input,cube,color='green',s=5)
ax.scatter(input,exponential,color=(1,0.5,0),s=5) #color=orange
ax.scatter(input,logarithmic,color=(0,0,0),s=5) #color=black
ax.axis([0,50,0,900])
ax.ticklabel_format(style='plain')


plt.show()
