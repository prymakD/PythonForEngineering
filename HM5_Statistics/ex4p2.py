import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate

data = np.load('inter2D.npz')
X = data['x']
Y = data['y']
Z = data['z']


f = interpolate.interp2d(X, Y, Z, kind='cubic')
X1 = np.linspace(0, 10, 60)
Y1 = np.linspace(0, 10, 60)
Z1 = f(X1, Y1)
X1, Y1 = np.meshgrid(X1, Y1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X1, Y1, Z1, cmap='jet')

plt.show()
