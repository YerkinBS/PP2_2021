file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
pnt_9, pnt_10, pnt_11, ans = [], [], [], ''
for i in lines:
    v = i.split()
    if v[2] == '9': pnt_9.append(int(v[3]))
    if v[2] == '10': pnt_10.append(int(v[3]))
    if v[2] == '11': pnt_11.append(int(v[3]))
pnt_9.sort(key=int) 
pnt_10.sort(key=int)
pnt_11.sort(key=int)
ans += str(pnt_9.count(pnt_9[-1])) + ' '
ans += str(pnt_10.count(pnt_10[-1])) + ' '
ans += str(pnt_11.count(pnt_11[-1]))
output_file.write(ans)