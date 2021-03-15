def Range_Check(a, b, x):
    if a <= x <= b: return True
    else: return False

a, b = map(int, input().split())
x = int(input())
print('{} is in the range'.format(x) if Range_Check(a, b, x) else '{} is not in the range'.format(x))