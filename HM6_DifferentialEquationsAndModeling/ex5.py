import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('PCAdata.txt')
covmat = np.cov(data)
w, v = np.linalg.eig(covmat)
data = np.dot(v[::2], data)
plt.scatter(data[0], data[1])
plt.show()
