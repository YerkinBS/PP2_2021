file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
d, ans = {}, ''
for i in lines:
    v = i.split()
    d[v[0] + ' ' + v[1]] = v[3]
for key in sorted(d.keys(), key=str):
    ans += key + ' ' + d[key] + '\n'
output_file.write(ans)