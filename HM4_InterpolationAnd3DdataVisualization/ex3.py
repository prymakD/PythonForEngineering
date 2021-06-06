import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0.9, 1.1, 100)
Y = []
for x in X:
    Y.append(np.linalg.cond([[1., np.sqrt(x)], [1., 1./np.sqrt(x)]]))

plt.plot(X, Y)
plt.show()

# The condition number of the matrix measures the ratio
# of the maximum relative stretching to the maximum relative shrinking that matrix
# does to any non zero vectors.