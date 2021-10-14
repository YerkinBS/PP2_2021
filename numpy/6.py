import numpy as np
a = np.array([i for i in range(1, 26)]).reshape(5, 5)
b = np.array([i for i in range(26, 51)]).reshape(5, 5)
print('First matrix:\n', a, '\n')
print('Second matrix:\n', b, '\n')
ab1 = np.concatenate((a, b), axis=0)
ab2 = np.concatenate((a, b), axis=1)
print('Vertical add:\n', ab1, '\n')
print('Horizontal add:\n',ab2, '\n')