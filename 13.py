v = [int(i) for i in input().split()]
x = []
if len(v) == 1:
    print(v[0])
    exit(0)
for i in range(len(v)):
    if i == 0:
        x += [v[1] + v[-1]]
    elif i == len(v) - 1:
        x += [v[0] + v[-2]]
    else:
        x += [v[i-1] + v[i+1]]
for i in x:
    print(i, end = ' ')