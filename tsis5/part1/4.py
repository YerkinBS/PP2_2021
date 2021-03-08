import os, sys

def file_read_from_end(file_name, n):
    bufsize = 2 ** 13
    file_sz = os.stat(file_name).st_size
    iter = 0
    with open(file_name) as f:
        if bufsize > file_sz:
            bufsize = file_sz - 1
            data = []
            while True:
                iter += 1
                f.seek(file_sz - bufsize*iter)
                data.extend(f.readlines())
                if len(data) >= n or f.tell() == 0:
                    print(''.join(data[-n:]))
                    break

file_read_from_end('test.txt', int(input()))