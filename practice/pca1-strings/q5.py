'''WAP to print even length words in a string.'''

str = input('Enter string: ')

str = str.split(' ')

for s in str:
    if len(s)%2==0:
        print(s)

