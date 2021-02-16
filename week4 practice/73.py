n = int(input())
arr = list(map(int, input().strip().split()))[:n]
st = set(arr)
print(len(st))