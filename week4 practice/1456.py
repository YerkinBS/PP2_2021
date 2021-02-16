n = int(input())
arr = list(map(int, input().strip().split()))[:n]
h = int(input())
arr.append(h)
arr = sorted(arr)
arr = arr[::-1]
for i in range(len(arr)):
    if arr[i] == h:
        ind = i
print(ind+1)