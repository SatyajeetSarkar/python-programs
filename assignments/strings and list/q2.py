''' “Digit-Extractor and Digit-Stats from Mixed String” '''

str = "abcc23cdd"

sum = 0
count = 0
max_digit = 0
min_digit = 10

for s in str:
    if 48 <= ord(s) <= 57:
        num = ord(s)-48

        sum += num

        if num > max_digit:
            max_digit = num

        if num < min_digit:
            min_digit = num

        count += 1

avg = sum/count

print(f"Sum: {sum} \nAverage: {avg} \nMaximum Digit: {max_digit} \nMinimum Digit: {min_digit}")