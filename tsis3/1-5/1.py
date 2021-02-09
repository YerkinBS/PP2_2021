mylist = list(map(int, input().split()))
for i in range(len(mylist)):
    if i % 2 == 0:
        print(mylist[i], end = ' ')