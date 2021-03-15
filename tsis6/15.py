def Alph_Sort(word):
    sorted_list = sorted(word, key=str)
    for i, x in enumerate(sorted_list):
        if i == len(sorted_list) - 1:
            print(x)
        else:
            print(x, end='-')

word = list(map(str, input().split('-')))
Alph_Sort(word)