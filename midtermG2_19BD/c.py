n = int(input())
num = list(map(int, input().split()))
print('YES' if len(set(num)) == len(num) else 'NO') 

