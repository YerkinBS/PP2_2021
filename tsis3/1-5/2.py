mylist = list(map(int, input().split()))
ans = 1001
for i in range(len(mylist)):
    if mylist[i] <= ans and mylist[i] > 0:
        ans = mylist[i]
print(ans)