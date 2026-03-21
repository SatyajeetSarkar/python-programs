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
'''
line_no = 0
with open('input.txt', 'r') as file:
    for line in file:
        line_no += 1
        print(f"{line_no}:{line}")
'''

''' Count Unique capital letters in a file '''
uni_cap = set()
with open('text1.txt', 'r') as file:
    content = file.read()

    for ch in content:
        if ch.isupper():
            uni_cap.add(ch)

print(uni_cap)