'''5. An Insurance company follows following rules to calculate premium.
● If a person’s health is excellent and the person is between 25 and 35 years of age and lives in a
city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot exceed
Rs. 2 lakhs.
● If a person satisfies all the above conditions except that the sex is female then the premium is
Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh.
● If a person’s health is poor and the person is between 25 and 35 years of age and lives in a village
and is a male then the premium is Rs. 6 per thousand and his policy cannot exceed Rs. 10,000.
● In all other cases the person is not insured.
Write a program to output whether the person should be insured'''

health = input("Enter health= ").lower()
age = int(input("Enter age= "))
location = input("Enter location= ").lower()
sex = input("Enter sex= ").lower()

# Checking whether the person will be insured or not
if health == "excellent" and 25 <= age <= 35 and location == "city":
    if sex == "male":
        premium = 4
        policy_amount = 200000
        print("Insured premium is", premium, "per thounsand", "max policy amount", policy_amount)
    
    elif sex == "female":
        premium = 3
        policy_amount = 100000
        print("Insured premium is", premium, "per thounsand", "max policy amount", policy_amount)

    else:
        print("Not insured")

elif health == "poor" and 25 <= age <= 35 and location == "village" and sex == "male":
    premium = 6
    policy_amount = 10000
    print("Insured premium is", premium, "per thounsand", "max policy amount", policy_amount)

else:
    print("Not insured")