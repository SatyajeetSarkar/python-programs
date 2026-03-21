''' Write a program to find consecutive characters frequency '''

str = input("Enter the string: ")

count = 1

for i in range(1, len(str)):
    if str[i] == str[i-1]:
        count += 1
    else:
        print(f"{str[i-1]} : {count}")
        count = 1

print(f"{str[-1]} : {count}")