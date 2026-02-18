'''
file = open('text.txt', 'r')
txt1 = file.readline()
print(txt1) 
txt2 = file.readline()
print(txt2) 

file2 = open('output.txt', 'w')
file2.write(txt)

file.close()
# file2.close()
'''

import json

count = 0   
sum = 0
lst = []
dict = {}

with open('input.txt', 'r') as file:
    for t in file:
        lst.append(int(t))
        count += 1
        sum += int(t)

dict['count'] = count
dict['sum'] = sum

file2 = open('output.txt', 'w')
file2.write(f"{count} input items \nand sum {sum}")
json.dump(lst, file2)
json.dump(dict, file2)

print('Done')