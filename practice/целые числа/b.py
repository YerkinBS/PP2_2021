n = int(input())
if n > 0:
    print(((1 + n) * n) // 2)
elif n < 0:
    n *= -1
    print(((((1 + n) * n) // 2) - 1) * - 1)
else:
    print(1)