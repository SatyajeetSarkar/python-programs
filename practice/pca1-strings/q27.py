''' Write a program to word location in String '''

str = input("Enter string: ")
word = input("Enter word: ")

pos = 1

for s in str.split(' '):
    if s == word:
        break

    pos += 1

print(pos)