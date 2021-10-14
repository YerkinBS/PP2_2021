f, l = map(int, input().split())
v = list(map(int, input().split()))
print(*[i for i in range(f, l + 1) if i not in v])