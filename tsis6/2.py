def Sum_Find(v):
    ans = 0
    for i in v:
        ans += i
    return ans

v = list(map(int, input().split()))
print(Sum_Find(v))