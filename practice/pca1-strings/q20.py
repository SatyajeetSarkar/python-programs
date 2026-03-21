'''  Write a program for removing i-th character from a string '''

str = input('Enter string: ')

index = int(input('Enter character: '))

new_str =  str[:index] + str[index+1:]

print(f"New string is: {new_str}")
