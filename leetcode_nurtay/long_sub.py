def Uniq_Sub_Check(s, checker):
    for c in s:
        if c in checker: return False
        checker.append(c)
    return True

# s = input()
# subs = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

# uniq_subs = [i for i in subs if Uniq_Sub_Check(i, [])]

# uniq_subs.sort(key=len)

# print(len(uniq_subs[-1]))


s = input()
mx_len = 0
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        if Uniq_Sub_Check(s[i:j], []) and len(s[i:j]) > mx_len: mx_len = len(s[i:j])

print(mx_len)