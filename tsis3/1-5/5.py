mylist = list(map(int, input().split()))
n = int(input())
if n > 0:
    n = abs(n)
    while n > len(mylist):
        n -= len(mylist)
    print(*mylist[-n:], end = ' ')
    print(*mylist[0:-n])
else:
    n = abs(n)
    while n > len(mylist):
        n -= len(mylist)
    print(*mylist[n:], end = ' ')
    print(*mylist[0:n])