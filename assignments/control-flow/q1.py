'''If cost price and selling price of an item is input through the keyboard, write a program to
determine whether the seller has made profit or incurred loss. Also determine how much profit he
made or loss he incurred'''

cost = float(input('Enter the cost= '))
sell = float(input('Enter the sell price= '))

# Checking whether the seller has made profit or loss
if(sell>cost):
    print('Seller has made profit')
else:
    print('Seller has made loss') 

# Finding total profit or loss
value = sell - cost

if(sell>cost):
    print('Total profit: ',value)
else:
    print('Total loss: ',abs(value)) 