import sys
s = input()
inp = set(map(str, sys.stdin.read().split()))

for i in sorted(inp):
    if sorted(s) != sorted(i):
        print(i, end=' ')