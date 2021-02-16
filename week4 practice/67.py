n = int(input())
arr = list(map(int, input().strip().split()))[:n]
for i in range(n):
    if i == 0:
        if (arr[i] > 0 and arr[i+1] > 0) or (arr[i] < 0 and arr[i+1] < 0):
            print('YES')
            exit()
        else:
            continue
    if (i + 1 < len(arr)) and ((arr[i] > 0 and arr[i+1] > 0) or (arr[i] < 0 and arr[i+1] < 0)):
            print('YES')
            exit()
    elif (i + 1 < len(arr)) and ((arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0)):
        print('YES')
        exit()
print('NO')