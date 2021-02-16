n, a, b, c, d = map(int, input().split())
arr = []
for i in range(1, n + 1):
    arr.append(i)
arr[a-1:b] = reversed(arr[a-1:b])
arr[c-1:d] = reversed(arr[c-1:d])
print(*arr)