'''Write a program uppercase Half String.'''

str = input('Enter string: ')

half_index = len(str)//2

new_str = str[:half_index].upper() + str[half_index:]

print(new_str)
