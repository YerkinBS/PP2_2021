
for i in f:
    if '@' in i:
        output_file.write('YES')
        exit()
output_file.write('NO')