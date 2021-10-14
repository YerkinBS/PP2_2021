def power_of_two(sum_of_char):
    pwr = 1
    while sum_of_char != pwr:
        if pwr >= 1000:
            return False
        pwr *= 2

    else: return True


n = int(input())
text = []
while n > 0:
    text.append(input())
    n -= 1

cnt = 0
for line in text:
    for c in enumerate(line):
        if 'a' <= c[1] <= 'z' or 'A' <= c[1] <= 'Z': cnt += 1
        if c[1] == ' ' or c[1] == '\n' or c[0] + 1 == len(line):
            if power_of_two(cnt): print('H', end=' ')
            else: print('C', end=' ')
            cnt = 0
    print()