'''
2. Print Multiples with Skip”
● Problem statement: Given n and an integer k, and then a list of n integers, print all the
integers that are multiples of k, but skip the first one you encounter (i.e., don’t print the
first multiple found, but print any subsequent multiples).
● Input: Integers n, k, then n integers.
● Output: The printed list of numbers (space separated) that are multiples of k, skipping
the first. If fewer than two multiples, you might print none or just the later ones.
'''
# Taking inputs
n = int(input("Enter numbers of terms: "))
k = int(input("Enter the divisor: "))

# Initializing empty list
result = ""
count = 1

while count<=n:
    num = int(input("Enter num: "))

    if count!=1 and num%2==0:
        result = result + " " + str(num)
    count+=1

print(f"New list: {result}")