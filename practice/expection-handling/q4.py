''' calculate average of 4 sem'''

sum = 0
count = 0

try:
    for i in range(1, 5):
        value = int(input(f"Enter marks for sem {i}: "))
    
        if value == "":
            raise Exception('All 4 marks are required')
    
        if value < 0 or value > 100:
            raise Exception('value cannot be negative or greater than 100')
        
        sum += value
        count += 1
        
    avg = sum/count
    print(avg)
        
except ValueError:
    print("Invalid input")