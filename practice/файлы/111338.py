file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines = file.readlines()
d, ans = {}, ''
cnt_9, cnt_10, cnt_11 = 0, 0, 0
cl_9_sum, cl_10_sum, cl_11_sum = 0, 0, 0
for i in lines:
    v = i.split()
    if v[2] == '9':
        cnt_9 += 1
        cl_9_sum += int(v[3])
    if v[2] == '10':
        cnt_10 += 1
        cl_10_sum += int(v[3])
    if v[2] == '11':
        cnt_11 += 1
        cl_11_sum += int(v[3])
d[9] = cl_9_sum / cnt_9
d[10] = cl_10_sum / cnt_10
d[11] = cl_11_sum / cnt_11
for i in sorted(d.keys(), key=int):
    ans += (str(d[i]) + ' ')
output_file.write(ans)
print(ans)