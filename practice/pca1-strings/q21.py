'''  Write a program to split and join a string '''

str = input("Enter a string: ")
print(f"Before split: {str}")

str = str.split(' ')
print(f"After split: {str}")

str = ','.join(str)
print(f"After join: {str}")