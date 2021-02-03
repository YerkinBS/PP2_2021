s = input()
s = s.replace(' ', '')
t = s[::-1]
if s == t:
    print('yes')
else:
    print('no')