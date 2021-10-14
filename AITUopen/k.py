n = int(input())
v = list(map(int, input().split()))[:n]
i = 0
while i < len(v):
    if i == 0:
        arm = min(v[i], v[i+1])
        karm = max(v[i], v[i+1])
        i += 2
    elif i % 2 == 0:
        arm = max(arm, v[i])
        karm = min(karm, v[i])
        i += 1
    elif i % 2 == 1:
        arm = min(arm, v[i])
        karm = max(karm, v[i])
        i += 1
print(abs(arm - karm))