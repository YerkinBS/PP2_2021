n = int(input())
arr = sorted(set(list(map(int, input().strip().split()))[:n]))
for i, el in enumerate(arr, start=1):
    print(i, el)