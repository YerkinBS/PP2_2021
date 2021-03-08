def file_read(file_name):
    with open(file_name, 'r') as myfile:
        data = myfile.readlines()
        print(data)

file_read('test.txt')