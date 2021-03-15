def Fact_Find(n):
    i, ans = 1, 1
    while i <= n:
        ans *= i
        i += 1
    return ans

print(Fact_Find(int(input())))