s = input()
tar = input()
if s.find(tar) == -1:
    print('Not found')
else:
    print('First time', tar, 'occured in position:', s.find(tar))