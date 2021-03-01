s = list(map(str, input().split()))
t, cmp, ans = sorted(s, key = len), 0, []
for word in t:
    if len(word) > cmp:
        cmp = len(word)
        ans.append(word)
print(ans[-1])
print(cmp)