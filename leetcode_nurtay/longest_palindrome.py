s = input()
palindromes, i = [], 0
while i <= len(s):
    j = 0
    while j <= len(s):
        t = s[i:j]
        if t[::-1] == s[i:j] and len(t) != 0: palindromes.append(t)
        j += 1
    i += 1

palindromes.sort(key=len)
print(palindromes[-1])