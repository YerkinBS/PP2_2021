import string

def letters_file(n):
    with open('21.txt', 'w') as file:
        alph = string.ascii_uppercase
        letters = [alph[i:i + n] + '\n' for i in range(0, len(alph), n)]
        file.writelines(letters)

letters_file(int(input()))