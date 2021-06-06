import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

#Cubic spline interpolation is a special case for Spline interpolation that is used very often to avoid the
# problem of Runge's phenomenon. This method gives an interpolating polynomial that is smoother and has
# smaller error than some other interpolating polynomials such as Lagrange polynomial and Newton polynomial
data = np.load('inter1D.npz')
X = data['x']
Y = data['y']

r = np.linspace(-1, 1, 10)
plt.plot(r, np.interp(r, X, Y), '--o')

f = interpolate.interp1d(X, Y, kind='cubic')

a = np.linspace(-1, 1, 100)
n = f(a)

plt.plot(a, n, '-', color='green')

plt.show()
