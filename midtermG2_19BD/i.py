n = int(input()) 
A = list(map(int, input().strip().split()))[:n]
k = int(input())
x, y = A[0:k], A[k:n]

X, Y = '', ''
for i in x:
    X += str(i)
for i in y:
    Y += str(i)
if len(X) != 0 and len(Y) != 0:
    print(int(X) * int(Y))
else:
    print(0)