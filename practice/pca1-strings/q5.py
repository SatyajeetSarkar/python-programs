'''WAP to print even length words in a string.'''

str = input('Enter string: ')

split_list = []
word = ""

for s in str:
    if s == " ":
        split_list.append(word)
        word = ""
    else:
        word += s

for s in split_list:
    if len(s)%2==0:
        print(s)

