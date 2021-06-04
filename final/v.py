a, b, k = map(int, input().split())
ans, div = [], 1
while True:
    if div > a or div > b: break
    if a % div == 0 and b % div == 0:
        ans.append(div)
    div += 1

ans.sort()
print(ans[-k])