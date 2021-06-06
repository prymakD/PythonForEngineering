import numpy as np
import matplotlib.pyplot as plt

X = np.load('daneX.npy')
Y = np.load('daneY.npy')
plt.hist2d(X,Y, bins =[100, 110], cmap = 'jet') #If [int, int], the number of bins in each dimension (nx, ny = bins).

plt.colorbar()
plt.show()