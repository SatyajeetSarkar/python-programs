#Input
grad = input("Graduate? (y/n): ")
marks = float(input("Graduation %: "))
math_grad = input("Math in graduation? (y/n): ")
if math_grad=='n': math_hs = input("Math in HS? (y/n): ")
cat = input("Category (G/SC/ST): ")

min_marks = 45 if cat.lower() in ['sc', 'st'] else 50

#Checking
if grad == 'y' and marks >= min_marks and (math_grad == 'y' or math_hs == 'y'):
    print("Eligible for MCA admission")
else:
    print("Not eligible")