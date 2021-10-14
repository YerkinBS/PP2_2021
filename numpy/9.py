import numpy as np, random as rd
a = np.array([rd.randint(10, 99) for i in range(25)]).reshape(5, 5)
print('Original array:\n', a, '\n')
print('Reversed array:\n', np.flip(a))