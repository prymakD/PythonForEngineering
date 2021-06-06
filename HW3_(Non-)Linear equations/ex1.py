import numpy as np

a = np.random.uniform(0, 100, 25)
max = np.where(a == np.amax(a))
a[a < 50] = 0
a[max] = 200
print (a)
