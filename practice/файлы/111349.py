file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
d, ans, pts_sum = {}, '', 0
for i in lines:
    v = i.split()
    pts_sum += int(v[3])
    if v[2] in d.keys():
        d[v[2]].append(int(v[3]))
    else:
        d[v[2]] = [int(v[3])]
aver_pts = pts_sum / len(lines)
new_d = {}
for key in sorted(d.keys(), key=int):
    ssum = 0
    for n, i in enumerate(d[key], 1):
        ssum += i
        if n == len(d[key]):
            new_d[key] = ssum / n
for key in sorted(new_d.keys(), key=int):
    if new_d[key] > aver_pts:
        ans += key + ' '
output_file.write(ans)