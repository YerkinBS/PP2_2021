f = open('output.txt', 'w')
with open('input.txt') as s:
    for i in s:
        i = i.rstrip()
        f.write(i[::-1])
f.close()