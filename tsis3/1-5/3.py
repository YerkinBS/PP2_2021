mylist = list(map(int, input().split()))
for i in range(len(mylist) - 1, -1, -1):
    print(mylist[i], end = ' ')