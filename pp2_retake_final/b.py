v =list(map(str, input().split()))
d = dict()
for i in v:
    if i not in d.keys(): d[i] = 1
    else: d[i] += 1

for i in sorted(d.items()):
    print(i[0], '- ' + str(i[1]))

    # saled