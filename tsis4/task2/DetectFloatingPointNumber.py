import re
n = int(input())
for i in range(n):
    fl_num = input()
    print(bool(re.search(r'^[-+]?[0-9]*\.[0-9]+$', fl_num)))