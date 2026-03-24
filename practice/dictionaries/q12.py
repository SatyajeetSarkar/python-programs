'''12. Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from
11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
{'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
15
25
35
x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]'''

d = {}

# Create lists manually
x_list = []
for i in range(11, 20):
    x_list.append(i)

y_list = []
for i in range(21, 30):
    y_list.append(i)

z_list = []
for i in range(31, 40):
    z_list.append(i)

# Assign to dictionary
d['x'] = x_list
d['y'] = y_list
d['z'] = z_list

# Access 5th element (index 4)
print(d['x'][4])
print(d['y'][4])
print(d['z'][4])

# Print full dictionary values
for key in d:
    print(key, "has value", d[key])