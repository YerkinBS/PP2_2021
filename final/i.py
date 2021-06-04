import sys

inp = map(str, sys.stdin.read().split())
d = {}

for i in inp:
    d[i] = d.get(i, 0) + 1

for i in sorted(d.items(), key=str):
    print(i[0], i[1])