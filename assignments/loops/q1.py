'''
1. “Sum Even and Odd Separately”
● Problem statement: Given a list of integers, compute two sums: one for all even
numbers, and one for all odd numbers. Then print both sums.
● Input: First integer n, then n integers.
● Output: Two integers: sum_of_evens, sum_of_odds.
'''
#Taking Input
start = int(input("Enter the start: "))
n = int(input("Enter the end: "))

sum_of_odds = 0
sum_of_evens = 0

while(start<=n):
    if(start%2==0):
        sum_of_evens += start
    else:
        sum_of_odds += start

    start += 1

print(f"Odd sum: {sum_of_odds}, Even sum: {sum_of_evens}")