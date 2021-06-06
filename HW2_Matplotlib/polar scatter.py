import matplotlib.pyplot as plt
import numpy as np

file = open('scatter.txt', 'r')
dataX = np.array([float(x) for x in ((file.readline()).split())])
dataY = np.array([float(x) for x in ((file.readline()).split())])

plt.figure()
ax = plt.axes(polar = True)
ax.set_facecolor("lightgrey")
plt.scatter(dataX, dataY, c=dataY, cmap = plt.cm.hsv)
plt.show()
'''
How to graph this    plot in a Cartesian coordinate system?

to add Cartesian coordinate system we need to use Axex() function
axes = Axes(xlim=(...), ylim=(...), figsize=(...))
'''
