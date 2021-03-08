def n_lines_read(file_name, n):
    from itertools import islice
    with open(file_name) as f:
        for line in islice(f, n):
            print(line)

n_lines_read('test.txt', int(input()))