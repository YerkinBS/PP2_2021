import re

def mail_check(tar):
    return re.search(r"^[a-z]+@[a-z]+.[a-z]+", tar)


email=input()
print('Yes' if mail_check(email) else 'No')