file = open("input.txt")
output_file = open("output.txt","w")
l = file.readlines()
l.sort(key=len)
for i in l:
    if len(i) == len(l[-1]):
        output_file.write(i)