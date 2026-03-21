''' Write a program to find words that are greater than the given length k '''

str = "hello world go to"
k = 3

splitted_list = []
w = ''
for i in str:
    if i == ' ':
        splitted_list.append(w)
        w = ''
    else:
        w += i

for s in splitted_list:
    len = 0
    for _ in s:
        len += 1

    if len > k:
        print(s)

