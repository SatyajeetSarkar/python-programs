''' Write a program to find minimum number of rotations to obtain actual string '''

str = input("Enter a string: ")

org = str
count = 0

while True:
    str = str[1:] + str[0]
    count += 1

    if str == org:
        break

print(f"Minimum count: {count}")