import matplotlib.pyplot as plt
import numpy as np

file = open('data3.dat.txt', 'r')
sample1 = [np.double(x) for x in ((file.readline()).split(','))]
sample2 = [np.double(x) for x in ((file.readline()).split(','))]
sample3 = [np.double(x) for x in ((file.readline()).split(','))]

plt.boxplot((sample1, sample2, sample3))
plt.show()
