import sys

inp = map(str, sys.stdin.read().split('\n'))
d = {}
for i in inp:
    v = i.split()
    if len(v) != 0:
        if v[0] in d.keys():
            if v[1] >= d[v[0]]:
                d[v[0]] = v[1]
        else:
            d[v[0]] = v[1]

for i in sorted(d.items(), key=str):
    print(i[0], i[1])