def Prime_Check(n):
    if n == 2 or n == 3: return True
    if n == 1 or n == 0: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True

n = int(input())
print('{} is prime'.format(n) if Prime_Check(n) else '{} is not prime'.format(n))