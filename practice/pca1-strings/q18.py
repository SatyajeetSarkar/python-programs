'''  Write a program to generating random strings until a given string is generated '''

import random
import string

target = 'abc'

characters = string.ascii_letters + string.digits   # allowed characters

attempts = 0

while True:
    attempts += 1
    random_string = ''.join(random.choice(characters) for _ in range(len(target)))

    print(f"Attempt {attempts}: {random_string}")

    if random_string == target:
        print("\nMatched! The string was generated successfully.")
        break
