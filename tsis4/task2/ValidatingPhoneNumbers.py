import re
n = int(input())
for i in range(n):
    number = input()
    if re.findall(r'^[7-9]\d{9}$', number):
        print('YES')
    else:
        print('NO')