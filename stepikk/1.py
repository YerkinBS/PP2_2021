a, b = float(input()), float(input())
calc = input()
if calc == '+':
    print(a + b)
elif calc == '-':
    print(a - b)
elif calc == '/':
    if b == 0:
        print("Деление на 0!")
    else:
        print(a / b)
elif calc == '*':
    print(a * b)
elif calc == 'mod':
    if b == 0:
        print("Деление на 0!")
    else:
        print(a % b)
elif calc == 'pow':
    print(a ** b)
elif calc == 'div':
    if b == 0:
        print("Деление на 0!")
    else:
        print(a // b)