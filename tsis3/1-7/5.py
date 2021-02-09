n = int(input())
mypairs = {}
while n > 0:
    first, second = input().split()
    mypairs[first] = second
    mypairs[second] = first
    n -= 1
tar = input()
print(mypairs[tar])