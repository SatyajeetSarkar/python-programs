''' Write a program to sort String list by K character frequency'''

strings = ["apple", "banana", "mango", "papaya"]
k = 1

# sorted_list = sorted(strings, key = lambda x: x.count(k))

# print("Sorted list:", sorted_list)

dict = {}

for w in strings:
    for ch in w:
        if w[k] == ch:
            dict[w] = dict.get(w,0)+1

new_list = []


min_str = dict[0]
min_freq = dict.get(dict[0])

print(min_str, min_freq)