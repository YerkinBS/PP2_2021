n = int(input())
num = list(map(int, input().split()))
st = set(num)
if len(st) == len(num):
    print('YES')
else:
    print('NO')