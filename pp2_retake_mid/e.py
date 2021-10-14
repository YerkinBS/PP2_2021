n = int(input())
d = {
    'a': 0,
    'b': 0,
    'c': 0
}
while n > 0:
    line = list(map(str, input().split()))
    for i in line[0]:
        if 'A' <= i <= 'Z': d['a'] += 1
    for i in line[1]:
        if i in 'aeiou': d['b'] += 1
    for i in line[2]:
        if '0' <= i <= '9': d['c'] += 1
    n -= 1

print(d) 


## продано