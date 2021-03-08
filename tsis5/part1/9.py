def file_line_cnt(file_name):
    with open(file_name) as file:
        for i, l in enumerate(file, 1):
            pass
        return i

print('Number of lines in the file:', file_line_cnt('test.txt'))