s = input()
t = s.upper()
cnt = t.count('G') + t.count('C')
perc = (cnt / len(t)) * 100
print(perc)