cnt = int(input())
if cnt % 10 == 1 and (cnt // 10) % 10 != 1:
    print(cnt, 'программист')
elif (cnt % 10 == 2 or cnt % 10 == 3 or cnt % 10 == 4) and (cnt // 10) % 10 != 1:
    print(cnt, 'программиста')
else:
    print(cnt, 'программистов')