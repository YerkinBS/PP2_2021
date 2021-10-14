n, k = map(int, input().split())
v = []
for i in range(n):
    a, b = map(int, input().split())
    v.append((a, b))
m = []
l = []
for i in v:
    if i == v[0]:
        m.append(i)
        continue
    if i[0] >= m[-1][0] and i[1] >= m[-1][1]:
        m.append(i)
    else:
        l.append(i)

m2 = []
l2 = []
if len(l) > 1:
    for i in l:
        if i == l[0]:
            m2.append(i)
            continue
        if i[0] >= m[-1][0] and i[1] >= m[-1][1]:
            m2.append(i)
        else:
            l2.append(i)

if k == 1:
    print(len(m))
else:
    print(len(m) + len(m2) + len(l[:k-1]) + len(l2[:k-1]))