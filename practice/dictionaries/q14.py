'''14. Write a Python program to convert more than one list to a nested dictionary.
Original strings:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]
Nested dictionary:
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim
Richards': 92}}]'''

ids = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
marks = [85, 98, 89, 92]

result = []

# Loop through index
for i in range(len(ids)):
    inner_dict = {}
    name_mark = {}

    name_mark[names[i]] = marks[i]
    inner_dict[ids[i]] = name_mark

    result.append(inner_dict)

print(result)