s = list(map(str, input().split()))
s.sort(key=len)
print(s[-1] + '\n' + str(len(s[-1])))

