file = open('input.txt', 'r', encoding='utf-8')
output_file = open("output.txt","w")
lines, d, ans = file.readlines(), {}, ''
for i in lines:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
for key, value in d.items():
    if (value / len(lines)) * 100 > 50:
        print(key)
        exit()
for n, item in enumerate(sorted(d.items(), key=lambda x: x[1], reverse=True), 1):
    ans += item[0]
    if n == 2: break
output_file.write(ans)