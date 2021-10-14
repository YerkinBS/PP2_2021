v = list(map(int, input().split()))
d = {}
for i in v:
    d[i] = d.get(i, 0) + 1
print(*[key for key, value in d.items() if value == sorted(d.values())[-1]])