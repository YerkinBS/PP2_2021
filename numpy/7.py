import numpy as np, random as rd
a = np.array([rd.randint(10, 99) for i in range(12)]).reshape(4, 3)
print('Original array:\n', a, '\n')
a[:, [2, 0]] = a[:, [0, 2]]
print('After swapping arrays the last column and first column:\n', a)