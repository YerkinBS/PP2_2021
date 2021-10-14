v = list(map(int, input().split()))

cnt = 0
for i in range(len(v)):
    for j in range(i+1, len(v)):
        if v[i] == v[j]: cnt += 1

print(cnt)