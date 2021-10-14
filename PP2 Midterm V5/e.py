n = int(input())
d = {}
while n > 0:
    v = list(map(str, input().split()))
    if v[0] not in d.keys():
        d[v[0]] = [i[1] for i in enumerate(v) if i[0] != 0]
    else:
        d[v[0]] += [i[1] for i in enumerate(v) if i[0] != 0]
    n -= 1

for i in d.items():
    print(str(i[0]) + ':', ', '.join([k for k in i[1]]))