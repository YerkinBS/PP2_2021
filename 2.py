f = input()
if f == 'треугольник':
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
elif f == 'прямоугольник':
    a, b = float(input()), float(input())
    S = a * b
    print(S)
elif f == 'круг':
    r = float(input())
    S = 3.14 * (r ** 2)
    print(S)