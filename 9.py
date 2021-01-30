a, b = int(input()), int(input())
cnt, sum = 0, 0
for i in range(a, b + 1):
    if i % 3 == 0: 
        cnt += 1
        sum += i
aver = sum / cnt
print(aver)