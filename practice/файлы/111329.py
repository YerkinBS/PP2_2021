file = open('input.txt')
out_file = open('output.txt', 'w')
lines = file.readlines()
for line in reversed(lines):
    line = line.rstrip()
    out_file.write(line + '\n')
out_file.close()