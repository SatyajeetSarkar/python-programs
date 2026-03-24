'''10. Write a Python program to get the top three items in terms of cost in a shop.
d1={'dress':23,'pant':45,'shoe':12,'bungle':55,'book':8}
output:
bungle 55
pant 45
dress 23'''

d1 = {'dress':23,'pant':45,'shoe':12,'bungle':55,'book':8}

# Convert dictionary to list of tuples manually
items = []
for key in d1:
    items.append((key, d1[key]))

# Manual sorting (Descending) using Bubble Sort
n = len(items)

for i in range(n):
    for j in range(0, n - i - 1):
        if items[j][1] < items[j + 1][1]:
            # Swap
            temp = items[j]
            items[j] = items[j + 1]
            items[j + 1] = temp

# Print top 3 items
for i in range(3):
    print(items[i][0], items[i][1])