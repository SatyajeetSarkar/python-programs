''' Write a program to swap commas and dots in a String '''

# str = input('Enter string: ')

# str = str.replace('.','#')
# str = str.replace(',','.')
# str = str.replace('#',',')

# print(str)

str = 'p,o.p'
index = 0

for ch in str:
    if ch == ',':
        str = str[:index] + '.' + str[index+1:]
    if ch == '.':
        str = str[:index] + ',' + str[index+1:]
    index+= 1

print(str)
