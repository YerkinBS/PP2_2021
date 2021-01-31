v = [int(i) for i in input().split()]
x = int(input())
ans = []
for i in range(len(v)):
    if x == v[i]:
        ans += [i]
if len(ans) == 0:
    print('Отсутствует')
else:
    for i in ans:
        print(i, end = ' ')