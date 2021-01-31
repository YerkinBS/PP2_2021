s = input()
for x in range(len(s)):
    for i in range(len(s)):
        cnt = 1
        for j in range(i + 1, len(s)):
            if s[i] != s[j]:
                break
            else:
                cnt += 1
        print(s[i], end = '')
        print(cnt, end = '')
        break
    s = s[cnt :] 