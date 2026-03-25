'''WAP to calculate the length of a string, avoid space.'''

str = 'Python Is Good'

# print(len(str.replace(' ', '')))

count = 0

for i in str:
    if i == ' ':
        continue
    else:
        count += 1

print(count)