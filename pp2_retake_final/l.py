v = list(map(int, input().split()))
d = {}

for i in v:
    d[i] = d.get(i, 0) + 1

ans = 0
for key, value in d.items():
    if value == 1:
        ans += key 
print(ans)