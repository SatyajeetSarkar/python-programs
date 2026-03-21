'''Write a program to least Frequent Character in String'''

str = input("Enter string: ")

min_char = str[0]
min_count = str.count(str[0])

for s in str:
    if s == min_char or s == ' ':
        pass

    if str.count(s) < min_count:
        min_char = s
        min_count = str.count(s)


print(f"Min char: {min_char}, Min count: {min_count}")