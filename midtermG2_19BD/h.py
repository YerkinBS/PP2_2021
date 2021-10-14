n = int(input())
stud_list = list(map(str, input().strip().split()))[:n]
m = int(input())
pract_list = list(map(str, input().strip().split()))[:m]

missed_stud = [stud for stud in stud_list if stud not in pract_list]
not_in_group = [stud for stud in pract_list if stud not in stud_list]

print('Missed students:')
print('\n'.join(['-' + stud for stud in missed_stud]))
print('Not in the group:')
print('\n'.join(['-' + stud for stud in not_in_group]))



