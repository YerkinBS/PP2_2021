file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
d, ans, win_pt = {}, '', 0
for i in lines:
    v = i.split()
    if win_pt < int(v[3]): win_pt = int(v[3])
    if v[2] in d.keys():
        d[v[2]].append(int(v[3]))
    else:
        d[v[2]] = [int(v[3])]
win_cnt = []
for key in sorted(d.keys(), key=int):
    win_cnt.append(d[key].count(win_pt))
mx_winner = sorted(win_cnt, key=int)[-1]
for key in sorted(d.keys(), key=int):
    if d[key].count(win_pt) == mx_winner:
        ans += key + ' '
output_file.write(ans)