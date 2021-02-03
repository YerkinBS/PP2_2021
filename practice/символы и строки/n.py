s = input()
ans = ''
for i in range(len(s)):
    if i + 1 < len(s) and s[i] == ' ' and s[i+1] != ' ':
        ans += s[i]
    elif 'a' <= s[i] <= 'z':
        ans += s[i]
print(ans)