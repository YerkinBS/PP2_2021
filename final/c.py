n = list(map(int, input().split()))
v, cnt = [], 0
for i in n:
    if i != 0:
        v.append(i)
    else: cnt += 1
print(*v, end=' ')
for i in range(cnt):
    print(0, end=' ')