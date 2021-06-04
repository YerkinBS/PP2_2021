def is_power(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2      
    return True

v = set(list(map(int, input().split())))
for i in sorted(v, key=int):
    if not is_power(i):
        print(i, end=' ')