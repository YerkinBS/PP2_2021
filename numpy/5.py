import numpy as np, random as rd
a = np.array([rd.randint(10, 99) for i in range(20)])
print(a)
print()
print(a.reshape(2, 10))