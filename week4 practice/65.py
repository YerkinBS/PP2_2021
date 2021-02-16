n, cnt = int(input()), 0
arr = list(map(int, input().strip().split()))[:n]
for i in arr:
    if i > 0:
        cnt += 1
print(cnt)