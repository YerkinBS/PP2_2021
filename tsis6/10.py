def Even_Check(x):
    if x % 2 == 0: return True
    else: return False

v = list(map(int, input().split()))
print(list(filter(Even_Check, v)))