a = open('input.txt', 'r')
v = a.readlines()
print('Good\n' + str(len(v)) if v else 'No')