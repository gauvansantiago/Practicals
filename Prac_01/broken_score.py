# Task 2
"""Gauvan Santiago Prac 01 Task 02"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score > 90:
    print("Excellent")
elif score > 50:
    print("Passable")
else:
    print("Bad")
