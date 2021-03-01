import re

s = input()
t = re.findall(r'\w', s)
print('Found a match!' if len(t) == len(s) else 'Not matched!')