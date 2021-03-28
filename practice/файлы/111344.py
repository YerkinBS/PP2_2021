file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
d, ans = {}, ''
for i in lines:
    v = i.split()
    if v[2] in d.keys():
        d[v[2]] += 1
    else:
        d[v[2]] = 1
for i in sorted(d.keys(), key=int):
    if d[i] == list(sorted(d.values(), key=int))[-1]:
        ans += str(i) + ' '
output_file.write(ans)