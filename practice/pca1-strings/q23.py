''' Write a program to find uncommon words from two Strings '''

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

for s in str1.split(' '):
    if s not in str2:
        print(s)

for s in str2.split(' '):
    if s not in str1:
        print(s)


