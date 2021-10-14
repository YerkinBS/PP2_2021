n = int(input())

d = {}
while n > 0:
    v = tuple(sorted(list(map(int, input().split())), key=int))
    if v in d.keys():
        d[v] += 1
        print(d[v])
    else:
        d[v] = 0
        print(d[v])
    n -= 1