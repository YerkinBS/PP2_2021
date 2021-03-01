n = int(input())
arr = list(map(int, input().split()))[:n]
sorted_arr = sorted(arr)
for i in range(n):
    if arr[i] != sorted_arr[i]:
        print('Not interesting')
        exit()
print('Interesting')