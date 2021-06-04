s = input()
t = input()
if s == t:
    print('YES')
    exit() 
else:
    if sorted(s) == sorted(t):
        print('YES')
    else:
        print('NO')