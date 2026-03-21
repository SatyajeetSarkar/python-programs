''' Write a program to accept the strings which contain all vowels'''

s = "The quick brown fox jumps over the lazy dog"

vowel = 'aeiou'
flag = True
for v in vowel:
    if v not in s:
        flag = False
        break

if flag:
    print('True')
else:
    print('False')