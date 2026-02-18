''' Count words "to" and "the" present in a text file '''
''' 
dict = {'to': 0, 'the': 0}

with open('text1.txt', 'r') as file:
    for line in file:
        for word in line.split():
            if word == 'to':
                dict['to'] += 1
            if word == 'the':
                dict['the'] += 1

print(dict)
'''

''' Display all lines in a file with line/record number '''

with open('text1.txt', 'w') as file:
    for line in file:
        file.write()