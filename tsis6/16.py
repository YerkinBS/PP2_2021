def Squares_list(v):
    new_v = [x * x for x in v]
    print(new_v)

v = [x for x in range(1, 31)]
Squares_list(v)