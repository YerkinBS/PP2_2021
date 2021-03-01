moves = input()
X, Y = map(int, input().split())
x, y = 0, 0
for i in range(len(moves)):
    if moves[i] == 'R': x += 1
    if moves[i] == 'L': x -= 1
    if moves[i] == 'U': y += 1
    if moves[i] == 'D': y -= 1
    
    if x > X and y >= Y:
        print('Passed')
        exit()
    elif y > Y and x >= x:
        print('Passed')
        exit()
        
print('Missed')