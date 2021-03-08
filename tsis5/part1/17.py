def nline_remove(file_name):
    file_list = open(file_name).readlines()
    return [l.rstrip('\n') for l in file_list]

print(nline_remove('lol.txt'))