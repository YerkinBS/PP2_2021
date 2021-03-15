import string
alph = string.ascii_lowercase

def Pan_Check(s):
    if len(set(s)) >= len(alph): return True
    else: return False

s = input()
print("String '{}' is pangram".format(s) if Pan_Check(s) else "String '{}' is not pangram".format(s))