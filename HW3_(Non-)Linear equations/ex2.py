import numpy as np

matrix = np.random.uniform(-100, 100, (9, 9))
matrix_int = matrix.astype(np.int32)
even = matrix_int[matrix_int % 2 == 0]
print (np.sort(even))
