mylist = list(map(int, input().split()))
seclist = []
for i in mylist:
    if i != 0:
        print(i, end = ' ')
    else:
        seclist.append(i)
for i in seclist:
    print(i, end = ' ')