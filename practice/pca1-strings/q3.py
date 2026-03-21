'''WAP to remove i^th character of a string.'''

str = 'string'

index = 2

new_str =  str[:index] + str[index+1:]

print(f"New string is: {new_str}")