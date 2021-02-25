import re
inp = input()
ans = re.findall(r"[^aeiou]([aeiouAEIOU]{2,})(?=[^aiueo])", inp)
if ans:
    for i in ans:
        print(i)
else:
    print(-1)