check, ans = 0, 0
while True:
    n = int(input())
    ans += n ** 2
    check += n
    if check == 0:
        break
print(ans)