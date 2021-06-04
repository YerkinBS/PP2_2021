h, a, b = map(int, input().split())
days, distance = 1, 0
while True:
    distance += a
    if distance >= h: break
    distance -= b
    days += 1
print(days)