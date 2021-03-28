file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
d, ans, pts = {}, '', []
for i in lines:
    v = i.split()
    d[int(v[3])] = v[0] + ' ' + v[1]
    pts.append(int(v[3]))
pts.sort(key=int)
if pts.count(pts[-1]) != 1:
    ans += str(pts.count(pts[-1]))
else:
    ans += d[pts[-1]]
output_file.write(ans)