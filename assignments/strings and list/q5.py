''' "Anagram-Group Detection" '''

li = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

group = []

for w in li:
    flag = False
    for i in group:
        if sorted(w) == sorted(i[0]):
            i.append(w)
            flag = True
            break
    if not flag:
        group.append([w])

print(group)