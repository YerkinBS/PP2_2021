a = list(map(int, input().split())) 
b = list(map(int, input().split())) 
t = int(input())

ab = zip(a, b)
cnt = 0

for i in ab:
    if i[0] <= t <= i[1]:
        cnt += 1

print(cnt)

## продано