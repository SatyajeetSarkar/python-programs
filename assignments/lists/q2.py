''' “List-of-Lists Aggregation: Sales Data” '''

sales = [
    [5, 3, 0, 2],
    [7, 0, 2, 1],
    [0, 1, 4, 0]
]

products = len(sales[0])

totals = [0] * products

for i in sales:
    for j in range(products):
        totals[j] += i[j]

max_sales = totals[0]
max_prod_no = 1
min_sales = totals[0]   
min_prod_no = 1

for i in range(len(totals)):
    if totals[i] > max_sales:
        max_sales = totals[i]
        max_prod_no = i+1
    
    if totals[i] < max_sales:
        min_sales = totals[i]
        min_prod_no = i+1

for i in range(len(totals)):
    print(f'Product{i+1}: {totals[i]}')

print(f'Maximum Total Sales: Product {max_prod_no}, sales: {max_sales}')            
print(f'Minimum Total Sales: Product {min_prod_no}, sales: {min_sales}')            
