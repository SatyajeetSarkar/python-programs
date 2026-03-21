''' Write a program to check if a string contains any special character '''

str = '%jjjd'

schar_flag = False

for s in str:
    if not 48<=ord(s)<=57 or 65<=ord(s)<=90 or 97<=ord(s)<=122:
        schar_flag = True
        break

if schar_flag:
    print('String contains special character')
else:
    print('String dont contains special character')