a, b, c = int(input()), int(input()), int(input())
if c <= b <= a:
    print(a) 
    print(c) 
    print(b) 
elif c <= a <= b:
    print(b) 
    print(c) 
    print(a) 
elif a <= b <= c:
    print(c) 
    print(a) 
    print(b) 
elif a <= c <= b:
    print(b) 
    print(a) 
    print(c) 
elif b <= c <= a:
    print(a) 
    print(b) 
    print(c) 
elif b <= a <= c:
    print(c) 
    print(b) 
    print(a) 