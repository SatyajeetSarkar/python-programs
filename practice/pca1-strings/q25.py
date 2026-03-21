''' Write a program to print permutation of a given string using inbuilt function '''

from itertools import permutations

s = input("Enter string: ")

perms = permutations(s)

for p in perms:
    print("".join(p))
