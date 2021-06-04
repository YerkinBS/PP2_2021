import sys

def prime_check(num):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False

inp = map(int, sys.stdin.read().split())
d = {}
for i in inp:
    d[int(i)] = d.get(i, 0) + 1
ans = []
for i in d.items():
    if not prime_check(i[0]) and i[1] > 1:
        ans.append(i[0])
for i in sorted(ans, key=int):
    print(i, end=' ')