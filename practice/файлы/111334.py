file = open("input.txt")
output_file = open("output.txt","w")
lines = file.readlines()
s, summ = '', 0
for line in lines:
    for i in range(len(line)):
        if '0' <= line[i] <= '9':
            s += line[i]
            if i+1 < len(line) and '0' <= line[i+1] <= '9':
                continue
            else:
                summ += int(s)
                s = ''
output_file.write(str(summ))