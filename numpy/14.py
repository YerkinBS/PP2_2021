import numpy as np, random as rd
a = np.array([[3, -1], [2 + 9, 3 - 3]])
b = np.array([7, -10 + 21])
ans = np.linalg.solve(a, b)
print('x =', int(ans[0]), '\ny =', int(ans[1]))