'''2. The Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program to
convert this temperature into Centigrade degrees.'''

temp = float(input("Enter the temperature= "))

#Farenheit to celcius conversion
far_to_cel = (5*(temp-32))/9
print("Celcius = ", far_to_cel)