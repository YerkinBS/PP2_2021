n = int(input())
arr = list(map(int, input().strip().split()))[:n]
print(*arr[::-1])