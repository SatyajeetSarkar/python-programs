''' Write a program to take input a string of digits and convert it to an integer without
using int() function. '''

str = '1234'

result = 0

for s in str:
    result = result*10 + ord(s) - 48

print(f"result: {result}")