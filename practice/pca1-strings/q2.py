''' Write a program to take binary input numbers and convert it to an integer without
using int() function.'''

binary = '1010'

decimal = 0
power = 0

rev_bin = binary[::-1]

# Traverse from right to left
for digit in rev_bin:
    if digit == '1':
        decimal += 2 ** power
    power += 1

print("Decimal value:", decimal)
