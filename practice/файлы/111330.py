file = open("input.txt")
output_file = open("output.txt","w")
newlist = file.read().split("\n")
for i in reversed(newlist):
    i = i.rstrip()
    output_file.write(i[::-1]+"\n")    