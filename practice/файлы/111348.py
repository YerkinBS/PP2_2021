file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
d, ans, pts = {}, '', []
for i in lines:
    v = i.split()
    if v[2] not in d.keys():
        d[v[2]] = v[3]
    else:
        if v[3] > d[v[2]]:
            d[v[2]] = v[3]
    pts.append(v[3])
pts = sorted(set(pts), key=int, reverse=True)
for i in sorted(d.keys(), key=int):
    if d[i] == pts[0]:
        ans += i + ' '
output_file.write(ans)