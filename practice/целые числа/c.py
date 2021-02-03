sec = int(input())
hours = sec // 3600
minutes = (sec % 3600) // 60
print('It is', hours, 'hours', minutes, 'minutes.')