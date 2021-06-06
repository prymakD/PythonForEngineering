import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

file = open('pie.txt', 'r')
X = [float(x) for x in ((file.readline()).split())]

Z = np.ones(5) * 0.03

plt.pie(X, colors=cm.terrain(np.arange(0.0, 1.0, 0.2)), explode=Z)
# explode - specifies the fraction of the radius with which to offset each wedge.

plt.show()