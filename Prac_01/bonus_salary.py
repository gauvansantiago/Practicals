# Task 1
"""Gauvan Santiago Prac 01 Task 01"""
# asks the user to input the sales and turns it into a float value
sales = float(input("Please input your sales"))
# if bonus salary less than 1000, 10% bonus is calculated, if bonus over 1000, 15% bonus is calculated
if sales < 1000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.15
print("The bonus of the salary is", bonus,)


