'''9. Write a Python program to print a dictionary in table format.'''

d = {'dress':23, 'shoe':12, 'book':8}

print("Key\tValue")
print("------------")

for key, value in d.items():
    print(f"{key}\t{value}")

