file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
d, ans, pts = {}, '', []
for i in lines:
    v = i.split()
    d[int(v[3])] = v[0] + ' ' + v[1]
    pts.append(int(v[3]))
uniq_pts = sorted(set(pts), key=int)
if pts.count(uniq_pts[-2]) != 1:
    ans += str(pts.count(uniq_pts[-2]))
else:
    ans += d[uniq_pts[-2]]
output_file.write(ans)