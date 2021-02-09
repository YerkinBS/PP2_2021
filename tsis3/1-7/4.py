def print_ans(myset):
    print(len(myset))
    print(*[str(i) for i in sorted(myset)])

n, m = map(int, input().split())
set1, set2 = set(), set()
while n > 0:
    set1.add(int(input()))
    n -= 1
while m > 0:
    set2.add(int(input()))
    m -= 1
print_ans(set1 & set2)
print_ans(set1 - set2)
print_ans(set2 - set1)