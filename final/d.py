v = set(list(map(str, input().split())))
for i in sorted(v):
    if i != i[::-1]:
        print(i)