file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
d, ans = {}, ''
for i in lines:
    v = i.split()
    if v[2] in d.keys():
        d[v[2]].append(int(v[3]))
    else:
        d[v[2]] = [int(v[3])]
new_d = {}
for key in d.keys():
    ssum = 0
    for el in d[key]:
        ssum += el
    if ssum / len(d[key]) not in new_d.keys():
        new_d[ssum / len(d[key])] = [key]
    else:
        new_d[ssum / len(d[key])].append(key)
for key in sorted(new_d.keys(), key=float, reverse=True):
    for el in sorted(new_d[key], key=int):
        ans += str(el) + ' '
output_file.write(ans)