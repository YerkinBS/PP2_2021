import numpy as np, random as rd
a = np.array([rd.randint(1, 9) for i in range(15)]).reshape(5, 3)
b = np.array([rd.randint(1, 9) for i in range(6)]).reshape(3, 2)
print('First array:\n', a, '\n')
print('Second array:\n', b, '\n')
print('After multiplication:\n', np.matmul(a, b))