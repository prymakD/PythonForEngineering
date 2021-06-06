import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#The wireframe plot basically takes a grid of values and projects it onto the specified
# 3-dimensional surfaces, and it can help in making the resulting three-dimensional forms
# quite easy for visualization.
data = np.load('inter2D.npz')
X = data['x']
Y = data['y']
Z = data['z']

X, Y = np.meshgrid(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X, Y, Z)

plt.show()
