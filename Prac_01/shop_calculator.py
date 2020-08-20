# Task 4
"""Gauvan Santiago Prac 01 Task 04"""
# asks for the number of items
total_cost = 0
items = int(input("Number of items: "))
# checks if there is correct amount of items
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
# adds the total price of items
for i in range(items):
    price = float(input("Price of item: "))
    total_cost += price
# applies 10% discount if total cost is over $100
# applies 10% discount if total cost is over $100
if total_cost > 100:
    total_cost *= 0.9  # apply 10% discount

print(items, " items comes to a total cost of $", total_cost)

print("Total price for {} items is ${:.2f}".format(items, total_cost))
