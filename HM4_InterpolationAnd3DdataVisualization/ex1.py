from numpy import linalg as LA
import scipy.linalg
import numpy as np
import matplotlib.pyplot as plt

a = np.array([[2, 3], [5, 4]])
b = np.array([4, 23])

matrix_full = np.c_[a, b]

rank = np.linalg.matrix_rank(matrix_full)

solution = np.linalg.solve(a, b)

cond_num = LA.cond(matrix_full)

P, L, U = scipy.linalg.lu(matrix_full) #product of a lower triangular matrix and an upper triangular matrix

x1 = np.array(range(-2,5))
equation1 = eval('2*x1+3*x1-4')
print (equation1)
x2 = x1
equation2 = eval('5*x2+4*x2-23')
plt.plot(x1, equation1)
plt.plot(x2,equation2)
plt.show()

print (matrix_full)
print ('Rank: ' + str(rank) + '\n')
print ('Solution: ' + str(solution) + '\n')
print ('Conditional number: '+ str(cond_num) + '\n')
print ('lower ' + str(L))
print ('upper ' + str(U))
print('pivotal' + str(P))