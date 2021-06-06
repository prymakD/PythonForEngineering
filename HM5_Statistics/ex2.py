import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

X = np.load('daneX.npy')
Y = np.load('daneY.npy')

H, xedges, yedges = np.histogram2d(X, Y, bins=100)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(0, 100, 1)
X, Y = np.meshgrid(x, y) #Return coordinate matrices from coordinate vectors.

ax.plot_surface(X, Y, H, cmap='jet')

plt.show()
