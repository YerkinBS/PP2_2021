n = int(input())
cnt = 0
for i in range(1, n + 1):
    for j in range(i):
        print(i, end = ' ')
        cnt += 1
        if cnt == n:
            exit(0)