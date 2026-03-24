'''13. Write a Python program to filter a dictionary based on values.
Original Dictionary:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
Marks greater than 170:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}'''

d = {
    'Cierra Vega': 175,
    'Alden Cantrell': 180,
    'Kierra Gentry': 165,
    'Pierre Cox': 190
}

result = {}

for key in d:
    if d[key] > 170:
        result[key] = d[key]

print("Marks greater than 170:")
print(result)