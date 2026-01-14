'''If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to determine
the youngest of the three.'''

age1 = int(input("Enter Ram age= "))
age2 = int(input("Enter Shyam age= "))
age3 = int(input("Enter Ajay age= "))

# Checking who is the youngest of the three

if age1 <= age2 and age1 <= age3:
    print('Youngest is Ram')

elif age2 <= age1 and age2 <= age3:
    print('Youngest is Shyam')

else:
    print('Youngest is Ajay') 