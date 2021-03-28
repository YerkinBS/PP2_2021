file = open("input.txt")
output_file = open("output.txt","w")
lines = file.readlines()
for line in lines:
    v = line.split()
    summ = 0
    for i in v:
        summ += int(i)
    output_file.write(str(summ) + '\n')