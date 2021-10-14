a, d = map(int, input().split())
years = 0
while a <= d:
    a *= 3
    d *= 2
    years += 1
else: print(years)


