from collections import Counter

def word_cnt(file_name):
    with open(file_name) as file:
        return Counter(file.read().split())

print('Number of words in the file:', word_cnt('test.txt'))