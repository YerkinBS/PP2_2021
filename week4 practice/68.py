n, cnt = int(input()), 0
arr = list(map(int, input().strip().split()))[:n]
for i in range(1, len(arr)-1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        cnt += 1
print(cnt)