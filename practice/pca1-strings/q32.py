''' Write a program to sort String list by K character frequency'''

# Function to count frequency of character k in a string
def count_k(s, k):
    count = 0
    for ch in s:
        if ch == k:
            count += 1
    return count

# Bubble sort based on frequency of k
def sort_by_k_frequency(str_list, k):
    n = len(str_list)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if count_k(str_list[j], k) > count_k(str_list[j + 1], k):
                # swap
                str_list[j], str_list[j+1] = str_list[j + 1], str_list[j]

# Input
strings = ["apple", "banana", "grape", "kiwi", "avocado"]
k = 'a'

# Sort
sort_by_k_frequency(strings, k)

# Output
print("Sorted list based on frequency of", k, ":")
for s in strings:
    print(s)