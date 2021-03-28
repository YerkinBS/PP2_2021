def dop_cmp(x):
    surname = x.split()[0]
    name = x.split()[1]
    return (surname, name)

def cmp(x):
    error = 100 - x[1]
    return (error, dop_cmp(x[0]))

file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
d, ans = {}, ''
for i in lines:
    v = i.split()
    d[v[0] + ' ' + v[1]] = int(v[3])
for key, value in sorted(d.items(), key=cmp):
    ans += key + ' ' + str(value) + '\n'
output_file.write(ans)