def Palindrome_Check(s):
    t = s[::-1]
    if t == s: return True
    else: return False

s = input()
print('{} is palindrome'.format(s) if Palindrome_Check(s) else '{} is not palindrome'.format(s))