lepeshki = [
    'Erkin', 'Akezhan', 'Nurtay', 'Mansur', 'Erlan', 'Ernar Ambal', 'Ernar Noob',
    'Olzhik', 'Dimash', 'Bauyrzhan', 'Zhassulan', 'Rayimkek', 'Alan', 'Sanzhar',
    'Bagdat', 'Aknazar', 'Liya', 'Ademi', 'Almira', 'Amina', 'Binazir', 'Dayana',
    'Aruzhan', 'Aidan' ]

with open('lol.txt', 'w') as file:
    for chel in lepeshki:
        file.write("%s\n" % chel)

content = open('lol.txt')
print(content.read())