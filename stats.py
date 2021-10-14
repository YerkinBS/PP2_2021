import re

sub = re.findall(r'[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]([aeiouAEIOU]{2,})[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]', input())
print('\n'.join([sub[i] for i in range(len(sub))]) if sub else -1)