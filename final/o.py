import sys

inp = map(str, sys.stdin.read().split())
d = {}

for i in inp:
    d[i] = d.get(i, 0) + 1
v = list(d.values())
v.sort()

for i in d.items():
    if i[1] == v[-1]:
        print(i[0].upper())
        exit()