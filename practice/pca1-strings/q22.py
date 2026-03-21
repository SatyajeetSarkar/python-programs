'''  Write a program to find all close matches of input string from a list '''

s = ["Lion", "Li", "Tiger", "Tig"]
a = "Lion"

# Iterate through each string in the list
''' for string in s:
    if string.startswith(a) or a.startswith(string):
        print(string, end=" ") '''

for i in s:
    if a in i or i in a:
        print(i)