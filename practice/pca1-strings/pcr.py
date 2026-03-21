li = "po ip op"

split_list = []
word = ''
new_li = ''

for ch in li:
    if ch == ' ':
        split_list.append(word)
        word = ''
    else:
        word += ch

split_list.append(word)

print(split_list)

# Join
for w in split_list[:-1]:
    new_li += w + ' '

new_li += split_list[-1]

print(new_li)