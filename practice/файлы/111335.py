# file = open("input.txt")
output_file = open("output.txt","a")
output_file.write('Input file contains:\n')
lett_cnt, word_cnt, line_cnt = 0, 0, 0
with open('input.txt') as file:
    for i in file.read():
        if 'a' <= i.lower() <= 'z': lett_cnt += 1
        if i == ' ' or i == '.': word_cnt += 1
        if i == '\n': line_cnt += 1
output_file.write(str(lett_cnt) + ' letters\n' + str(word_cnt) + ' words\n' + str(line_cnt+1) + ' lines')