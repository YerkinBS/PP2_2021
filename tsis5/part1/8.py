def longest_word(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
    words.sort(key=len)
    print([word for word in words if len(word) == len(words[-1])])

longest_word('test.txt')