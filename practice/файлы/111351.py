def cmp(x):
    return (x[1], 100 - int(x[0]))

file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
d, ans = {}, ''
for i in lines:
    v = i.split()
    if v[2] not in d.keys():
        d[v[2]] = 1
    else:
        d[v[2]] += 1
for key, value in sorted(d.items(), key=cmp, reverse=True):
    ans += key + ' '
output_file.write(ans)