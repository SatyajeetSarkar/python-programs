'''  Write a program to frequency of numbers in String '''

str = 'yr66799'

count = {i: 0 for i in range(10)}

for s in str:
    if 48 <= ord(s) <= 57:
        count[s] = count.get(s, 0) + 1

print(count)