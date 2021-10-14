import numpy as np, random as rd
v = []
for i in range(7):
    l = []
    for j in range(7):
        if i == 0 or i + 1 == 7:
            l.append(1)
        elif j == 0 or j + 1 == 7:
            l.append(1)
        else:
            l.append(0)
    v.append(l)

a = np.array(v)
print(a)