word = input()
k = int(input())
ans = ''
for i in word:
    if ord(i) - k >= 65:
        ans += chr(ord(i) - k)
    else:
        ans += chr(ord(i) + 26 - k)
print(ans)