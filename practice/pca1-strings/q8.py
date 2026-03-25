'''Python program to check if a string has at least one letter and one number'''

str = 'fh2edf'

letter_flag = 0
number_flag = 0

for ch in str:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        letter_flag = 1
    elif 0 <= ord(ch)-1 <= 9:
        number_flag = 1

if letter_flag and number_flag:
    print("The string consist of one letter and one number.")
else:
    print("The string doesn't consist of one letter and one number.")

    
