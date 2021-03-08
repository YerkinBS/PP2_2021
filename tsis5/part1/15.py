import random
def random_line(file_name):
    lines = open(file_name).read().splitlines()
    return random.choice(lines)

print(random_line('lol.txt'))