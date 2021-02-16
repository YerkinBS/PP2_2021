n = int(input())
arr = list(map(int, input().strip().split()))[:n]
x = int(input())
if x > 0:
    x = abs(x)
    while x > len(arr):
        x -= len(arr)
    print(*arr[-x:], end = ' ')
    print(*arr[0:-x])
else:
    x = abs(x)
    while x > len(arr):
        x -= len(arr)
    print(*arr[x:], end = ' ')
    print(*arr[0:x])