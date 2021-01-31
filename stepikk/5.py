ticket = int(input())
tic = ticket // 1000
ket = ticket % 1000
sum1 = (tic // 100) + ((tic // 10) % 10) + (tic % 10) 
sum2 = (ket // 100) + ((ket // 10) % 10) + (ket % 10)
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный') 