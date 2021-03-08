def file_read(file_name):
    my_array = []
    with open(file_name) as file:
        for line in file:
            my_array.append(line)
        print(my_array)

file_read('test.txt')