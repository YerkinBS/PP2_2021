file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
d, ans = {}, ''
for i in lines:
    v = i.split()
    if v[2] in d.keys():
        if v[3] >= d[v[2]]:
            d[v[2]] = v[3]
    else:
        d[v[2]] = v[3]
for i in sorted(d.keys(), key=int):
    ans += (str(d[i]) + ' ')
output_file.write(ans)