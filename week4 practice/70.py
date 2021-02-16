n = int(input())
arr = list(map(int, input().strip().split()))[:n]
if n % 2 != 0: n -= 1
for i in range(0, n, 2):
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp
print(*arr)
