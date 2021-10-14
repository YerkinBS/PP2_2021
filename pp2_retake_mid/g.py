n = int(input())
while n*2 > 0:
    stud_list = list(map(str, input().split()))
    pract_list = list(map(str, input().split()))

    print('Absent: ', end='')
    for student in sorted(stud_list):
        if student not in pract_list:
            print(student, end=' ')
    print()

    print('Lost: ', end='')
    for student in sorted(pract_list):
        if student not in stud_list:
            print(student, end=' ')
    print()
    n -= 1

    ## продано 