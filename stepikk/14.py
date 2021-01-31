v = [int(i) for i in input().split()]
v.sort()
for i in range(len(v)):
    if i + 1 == len(v):
        break
    if i == 0:
        if v[i] == v[i+1]:
            print(v[i], end = ' ')
    elif v[i] == v[i+1] and v[i] != v[i-1]:
        print(v[i], end = ' ')