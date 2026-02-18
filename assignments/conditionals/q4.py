'''A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for 6-10
days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 30 days
your membership will be cancelled. Write a program to accept the number of days the member is
late to return the book and display the fine or the appropriate message'''

no_of_days = int(input("Enter the number of days= "))
fine = 0.0

# Checking how long the member is late
if(no_of_days>30):
    print("Your membership is cancelled")

elif(no_of_days>10 and no_of_days<=30):  
    fine += no_of_days*5.0

elif(no_of_days>5 and no_of_days<=10):  
    fine += no_of_days*1.0

else:
    fine += no_of_days*0.5

# Displaying fine
if(fine>0):
    print("Total fine: ",fine)
else:
    print("No fine")    