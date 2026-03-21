'''Write a program to specific Characters Frequency in String List'''

# test list
a = ["geeksforgeeks is best for geeks"]

# char list
b = ['e', 'b', 'g']

# manually count the frequency of characters in the list
char_count = {}
for s in a:
    for c in s:
        if c in b:
            char_count[c] = char_count.get(c, 0) + 1
print(char_count)