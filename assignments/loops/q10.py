'''
3. Alternating Sequence Filter
● Problem statement: Write a program to read a sequence of integers until the end (or
given length). Then produce a new list by selecting numbers according to this rule: you
begin expecting an even number; when you encounter an even number you accept it,
then switch expectation to odd; when you next encounter an odd number you accept it,
switch expectation to even, and so on. If a number does not meet the current
expectation you skip it and keep going. At the end print the accepted list.
● Input: A list of integers.
● Output: A list of integers (the accepted ones) printed in their original order.
'''

# Taking input list
n = int(input("Enter numbers of terms: "))

# Even or Odd flag
expect_even= True
# New empty list
result = ""

for i in range(1, n+1):
    if expect_even and i%2 == 0:
        result = result + " " + str(i)
        expect_even = False

    elif not expect_even and i%2!=0:
        result = result + " " + str(i)
        expect_even = True

print(result)