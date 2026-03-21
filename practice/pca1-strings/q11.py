'''Write a program to remove all duplicates from a given string in Python, keeping the
first character only'''

str = input("Enter string: ")

new_str = "" 

for s in str:
    if s not in new_str:
        new_str += s

print(new_str)