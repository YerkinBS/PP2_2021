def prime_check(num):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False

a, b = map(int, input().split())
for i in range(b, a-1, -1):
    if prime_check(i):
        print(i, end=' ')