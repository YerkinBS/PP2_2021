import re

txt = input()
t, s, f = input(), input(), input()

txt = re.sub(t, s, txt)
print(txt.count(f))