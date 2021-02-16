n, cnt = int(input()), 0
arr = list(map(int, input().strip().split()))[:n]
for i in range(n):
    if i == 0:
        continue
    if arr[i] > arr[i-1]:
        cnt += 1
print(cnt)