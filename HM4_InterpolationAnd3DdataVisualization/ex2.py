import scipy.linalg
import numpy as np
import matplotlib.pyplot as plt

a = np.array([[2., 3., 0], [5, 4, 0],[0, 5, 0]])
b = np.array([4, 23, 18])

matrix_full = np.c_[a, b]

x1 = np.array(range(-2,5))
equation1 = eval('2*x1+3*x1-4')
x2 = x1
equation2 = eval('5*x2+4*x2-23')
x3 = x1
equation3 = eval('5*x3-18')
plt.plot(x1, equation1, label='eq1')
plt.plot(x2,equation2, label='eq2')
plt.plot(x3,equation3, label='eq3')
plt.legend()

solution = np.linalg.lstsq(a, b, rcond=-1) ##Return the least-squares solution to a linear matrix equation
print("Solution: " + str(solution))
"""
Cut-off ratio for small singular values of a. For the purposes of rank determination, 
singular values are treated as zero if 
they are smaller than rcond times the largest singular value of a.
"""

plt.show()

