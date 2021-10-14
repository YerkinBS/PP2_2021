a, b, c, d = int(input()), int(input()), int(input()), int(input())
print('\n'.join([str(i) for i in range(a, b + 1) if i % d == c]))



