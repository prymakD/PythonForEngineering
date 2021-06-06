import numpy as np
import matplotlib.pyplot as plt

x = np.load('solve.npz')

print(x.files)
A = x['A']
b = x['b']
A2 = x['A2']
b2 = x['b2']

x1 = np.linalg.solve(A,b)
c = np.linalg.lstsq(A.T, b, rcond=None)[0]
m2, c2 = np.linalg.lstsq(A2.T, b2, rcond=None)[0]

x_all = np.arange(-5, 100,5 )


#Subtask 2:
plt.subplot(212)
plt.plot(x_all, m2*(x_all)+c2, 'r', label='Approximated line')
plt.legend()
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
plt.show()