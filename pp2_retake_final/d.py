f, l = list(map(int, input().split()))
cab = list(map(int, input().split()))

print(*[i for i in range(f, l + 1) if i not in cab])