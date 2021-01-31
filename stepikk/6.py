a, b = int(input()), int(input())
d = max(a, b)
while True:
    if (d % a == 0) and (d % b == 0):
        break
    d += 1
print(d)
