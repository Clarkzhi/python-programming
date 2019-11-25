#Inside your order_manager.py file, write code to read the orders.py file using the json module.
import json

with open('orders.json', 'r') as order_file:
    order = json.load(order_file)

print(type(order))
print(json.dumps(order))

#Store your data into a list variable called customer_orders
customer_orders = ('orders.json')

print(customer_orders)
#How many customers are there in all?
total = 0
for customer in customer_orders:
    
    total += 1

print(total) 
#Print the name and email address of the customer with id 13
for customer in customer_orders:
    if customer['id'] = 13
    print(customer.values())

#Print all the items ordered by the customer with id 20.


for customer in customer_orders:
    if customer['id'] = 20:
        orders_20 = []
        for items in 


#How may customers bought wine
total = 0 
for items in customer_orders:
    if items = wine
    total += 1

#What is the total cost of the items ordered by Matti?
for 

#Which customer spent the most money on orders


