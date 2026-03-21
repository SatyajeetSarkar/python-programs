'''Python program to check if a string has at least one letter and one number'''

str = 'fh2edf'

letter_flag = 0
number_flag = 0

for ch in str:
    if 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
        letter_flag = 1
    elif 48 <= ord(ch) <= 57:
        number_flag = 1

if letter_flag and number_flag:
    print("The string consist of one letter and one number.")
else:
    print("The string doesn't consist of one letter and one number.")

    
