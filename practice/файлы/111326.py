summ = 0
with open('input.txt', 'r') as f:
    for i in f.readlines():
        summ += int(i)
x = open('output.txt', 'w')
x.write(str(summ))