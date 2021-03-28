file = open("input.txt")
output_file = open("output.txt","a")
ans = ''
for n, line in enumerate(file.readlines(), 1):
    s = ''
    for i in line:
        if 'a' <= i.lower() <= 'z':
            s += chr(ord(i) + n)
    ans += s + '\n'
output_file.write(ans)