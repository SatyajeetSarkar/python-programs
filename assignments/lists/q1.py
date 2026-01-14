''' “Sub-list Removal Variants” '''
li = [1, 2, 3, 4, 5]

result = []

for i in range(len(li)):
    new_list = li[:i] + li[i+1:]

    if new_list not in result:
        result.append(new_list)

print(result)    