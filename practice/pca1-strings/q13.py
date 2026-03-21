'''Write a program to maximum frequency character in String'''

str = input("Enter string: ")

max_char = str[0]
max_count = str.count(str[0])

for s in str:
    if s == max_char or s == ' ':
        pass

    if str.count(s) > max_count:
        max_char = s
        max_count = str.count(s)


print(f"Max char: {max_char}, Max count: {max_count}")