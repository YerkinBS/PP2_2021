v = [s for s in input().split()]
ans = ''
for i in v:
    if len(i) > len(ans):
        ans = i
print(ans)
print(len(ans))