'''
4. Digit-Sum Recursion with Loop”
● Problem statement: Write a program that repeatedly asks the user for a positive integer.
For each integer, compute the “digit sum” (sum of its digits). If that digit sum is greater
than 9, take that result and again compute its digit sum, continue until the result is a 
single digit (≤ 9). Print the number of iterations it took and the final single-digit result.
Repeat this entire process for each integer entered until the user enters zero or a
negative number to stop. At the end, print how many integers were processed.
● Input: A sequence of integers. Terminate when input ≤ 0.
● Output: For each integer: print “Iterations: X, Final digit: Y”. After termination: print “Total
numbers processed: N”.
'''

count = 0

while True:
    num= int(input("Enter any postive integer to compute or 0 to exit: "))

    # Loop termination
    if(num<=0):
        break

    count += 1
    itr = 0

    while num>=9:
        sum = 0
        for i in str(num):
            sum += int(i)
        itr += 1
        num = sum

    print(f"Iterations: {itr}, Final digit: {num}")

print(f"Total numbers processed: {count}")     

