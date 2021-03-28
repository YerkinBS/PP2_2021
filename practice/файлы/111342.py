file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
ans, pts = '', []
for i in lines:
    v = i.split()
    pts.append(int(v[3]))
uniq_pts = sorted(set(pts), key=int)
ans += str(uniq_pts[-2]) + ' ' + str(pts.count(uniq_pts[-2]))
output_file.write(ans)