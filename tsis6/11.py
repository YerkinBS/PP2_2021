def Perf_Num(n):
    summ = 0
    for i in range(1, n):
        if n % i == 0: summ += i
    if summ == n: return True
    else: return False

n = int(input())
print('{} is the perfect number'.format(n) if Perf_Num(n) else '{} is not the perfect number'.format(n))