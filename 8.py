a, b, c, d = int(input()), int(input()), int(input()), int(input())
print('\t', end = '')
for i in range(c, d + 1):
    print(i, '\t', end ='')
print()
for i in range(a, b + 1): 
    print(i, '\t', end = '')
    for j in range(c, d + 1):
        print(i * j, '\t', end = '')
    print()