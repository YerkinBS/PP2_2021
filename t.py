def dop_cmp(x):
    surname = x.split()[1]
    name = x.split()[0]
    return (name, surname)

def cmp(x):
    error = 140 - x[0]
    return (dop_cmp(x[1]), error)

n = int(input())
d = {}

while n > 0:
    inp = input().split()
    d[int(inp[2])] = inp[0] + ' ' + inp[1]
    n -= 1

k = int(input())
cnt, ans = 0, []

for key, value in sorted(d.items(), key=cmp):
    if key >= k:
        cnt += 1
        ans.append(value + ' ' + str(key))

print(cnt)
print('\n'.join([i for i in ans]))