'''Write a program to count the Number of matching characters in a pair of string'''

str_1 = 'tyutyty'
str_2 = 'ytytytu'

count = 0
new_str = ""

for s in str_1:
    if s not in new_str and s in str_2:
        count += 1
        new_str += s

print(count)