import glob
char_list = []
files_list = glob.glob('*.txt')
for file_el in files_list:
    with open(file_el, 'r') as file:
        char_list.append(file.read())
print(char_list)