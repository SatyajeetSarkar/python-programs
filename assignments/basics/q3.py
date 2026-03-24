'''3. Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic
salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross
salary.'''


basic_salary = float(input("Enter salary = "))

#Gross salary

gross_salary = basic_salary + (basic_salary * 0.4) + (basic_salary * 0.2)
print("Gross Salary = ", gross_salary)