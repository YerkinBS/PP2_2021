a, d = map(int, input().split())
years = 0
while True:
    a *= 3
    d *= 2
    years += 1
    if a > d:
        print(years)
        exit()