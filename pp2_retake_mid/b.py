IDs = list(map(int, input().split()))
N = int(input())

seq = [i for i in range(1, sorted(IDs)[-1] + 1)]

print(list(set(seq) - set(IDs))[N-1])


## продано