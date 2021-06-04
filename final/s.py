n = int(input())
v = list(map(int, input().split()))
t = sorted(v)[-1]
for i in v:
    if i != t:
        print(0, end=' ')
    else:
        print(1, end=' ')