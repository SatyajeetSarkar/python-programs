''' Write a program to string slicing in Python to check if a string can become empty by recursive deletion '''

s = input("Enter main string: ")
part = input("Enter substring to delete: ")

while part in s:
    index = s.find(part)
    s = s[:index] + s[index+len(part):]

if s == "":
    print("String becomes empty after recursive deletion.")
else:
    print("String does NOT become empty. Remaining string:", s)
