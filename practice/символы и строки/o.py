ip = input()
if ip.count('.') != 3:
    print(0)
    exit()
for i in range(len(ip)):
    if ip[i] == '.' and i == len(ip) - 1 or ip[i] == '.' and i == 0:
        print(0)
        exit()
    if i + 1 < len(ip) and ip[i] == '.' and not ip[i+1].isdigit():
        print(0)
        exit()
print(1)