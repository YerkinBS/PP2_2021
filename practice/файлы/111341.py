file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
pnt_9, pnt_10, pnt_11, ans = [], [], [], ''
for i in lines:
    v = i.split()
    if v[2] == '9': pnt_9.append(int(v[3]))
    if v[2] == '10': pnt_10.append(int(v[3]))
    if v[2] == '11': pnt_11.append(int(v[3]))
pnt_9 = sorted(set(pnt_9), key=int)
pnt_10 = sorted(set(pnt_10), key=int)
pnt_11 = sorted(set(pnt_11), key=int)
ans += str(pnt_9[-2]) + ' '
ans += str(pnt_10[-2]) + ' '
ans += str(pnt_11[-2])
output_file.write(ans)