s = input()
d = {}
for i in range(len(s)):
    d[s[i]] = d.get(s[i], 0) + 1
print(len(d.keys()))
for key, value in sorted(d.items(), key=str):
    print(key, value)