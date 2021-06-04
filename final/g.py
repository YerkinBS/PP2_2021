import sys, string

inp = map(str, sys.stdin.read().lower().split())
alph = list(string.ascii_lowercase)
d = {}
for i in alph:
    d[i] = 0

for i in inp:
    d[i[0]] = d.get(i[0], 0) + 1

for i in d.values():
    print(i)