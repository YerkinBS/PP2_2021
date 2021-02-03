n, m = map(int, input().split())
if m / n > 1:
    print((m + n - 1) // n)
else:
    print(1)