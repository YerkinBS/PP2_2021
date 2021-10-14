def data(s):
    chars = [len(i) for i in sorted(s, key=len)]
    return(chars)

n = int(input())
d = {}
while n > 0:
    s = list(map(str, input().split()))
    total = ' total: ' + str(sum(data(s)))
    d[n] = ' '.join(map(str, data(s))) + total
    n -= 1

print('\n'.join([value for value in d.values()]))

