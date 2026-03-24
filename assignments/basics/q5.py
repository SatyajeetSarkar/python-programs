'''5. If a five-digit number is input through the keyboard, write a program to print a new number by
adding one to each of its digits. For example, if the number that is input is 12391 then the output
should be displayed as 23402.'''

amount = int(input("Enter the amount = "))


# For hundred notes
hundred = amount // 100
remainder = amount % 100

# For fifty notes
fifty = remainder // 50
remainder = remainder % 50

# For ten notes
ten = remainder // 10

print("100s: ", hundred, "50s: ", fifty, "10s: ", ten)