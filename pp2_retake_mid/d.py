n = int(input())

while n > 0:
    x = list(map(str, input().split()))
    ok = True
    if len(x) % 2 == 0 and 'A' <= x[0][0] <= 'Z' and x[-1].count('3') == 2:
        for i in enumerate(x):
            if not (i[0] % 2 == 1 and len(i[1]) % 2 == 0):
                ok = False
            if not (i[0] % 2 == 0 and len(i[1]) % 2 == 1):
                ok = False
    else: ok = False
    print('Wow! That is perfect.' if ok else 'Seriously?')
    n -= 1