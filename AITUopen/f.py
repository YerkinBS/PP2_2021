def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

a, b = map(int, input().split())
arr1 = sorted(prime_factors(a), key=int)
arr2 = sorted(prime_factors(b), key=int)
if len(arr1) != len(arr2):
    print('NO')
    exit()
elif arr1 == arr2:
    print('YES')
    exit()
i = 0
arr1_1 = arr1
arr2_1 = arr2
while True:
    if i == len(arr1):
        break
    for j in range(len(arr1)):
        arr1_1[i], arr2_1[j] = arr2_1[j], arr1_1[i]
        if arr1_1 == arr2_1:
            print('YES')
            exit()
        else:
            arr2_1[j], arr1_1[i] = arr1_1[i], arr2_1[j]
            arr2_1[i], arr1_1[j] = arr1_1[j], arr2_1[i]
            if arr1_1 == arr2_1:
                print('YES')
                exit()
            else:
                arr1_1[j], arr2_1[i] = arr2_1[i], arr1_1[j]
    i += 1
print('NO')