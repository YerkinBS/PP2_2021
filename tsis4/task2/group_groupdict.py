import re
s = input()
ans = re.search(r'([a-zA-Z0-9])\1+', s)
if ans:
    print(ans.group(1))
else:
    print(-1)