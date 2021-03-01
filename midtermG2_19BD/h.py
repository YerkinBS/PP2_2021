n = int(input())
stud_list = list(map(str, input().strip().split()))[:n]
m = int(input())
pract_list = list(map(str, input().strip().split()))[:m]
missed_stud, not_in_group = [], []

for stud in stud_list:
    if not stud in pract_list:
        missed_stud.append(stud)
    
for stud in pract_list:
    if stud not in stud_list:
        not_in_group.append(stud)

print('Missed students:')
for stud in missed_stud:
    print('-', stud)
print('Not in the group:')
for stud in not_in_group:
    print('-', stud)