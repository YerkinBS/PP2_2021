n, k = map(int, input().split())
a = [[0]*3 for _ in range(n)]
for i in range(n):
    a[i] = [int(j) for j in input().strip().split(" ")]
for i in range(0, n):
    suum = 0
    for j in range(0, 3):
        suum += a[i][j]
    if suum / 3 >= float(k):
        print('YES')
        exit()
print('NO')