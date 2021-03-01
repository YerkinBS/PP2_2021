n, dict_data = int(input()), {} 
while n > 0:
    line = list(map(str, input().split()))
    for i in range(2, 2 + int(line[1])):
        dict_data[line[i]] = line[0]
    n -= 1
m = int(input())
while m > 0:
    city = input()
    print(dict_data[city] if city in dict_data else 'Unknown')
    m -= 1