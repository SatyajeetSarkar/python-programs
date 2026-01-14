'''Given the length and breadth of a rectangle, write a program to find whether the area of the
rectangle is greater than its perimeter. For example, the area of the rectangle with length = 5 and
breadth = 4 is greater than its perimeter.'''

length = int(input('Enter the length= '))
breadth = int(input('Enter the breadth= '))

# Calculate the area
area = length*breadth

# Calculate the perimeter
perimeter = 2*(length+breadth)

# Finding either area of the rectangle is grater than perimeter or not
if(area>perimeter):
    print("Area of the rectangle is greater than it's perimeter")
else: 
    print("Area of the rectangle is not greater than it's perimeter")