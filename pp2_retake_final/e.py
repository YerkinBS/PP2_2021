v = list(map(int, input().split()))
cnt = 0
for i in enumerate(sorted(v, key=int)):
    if i[1] != v[i[0]]: cnt += 1
print(cnt)