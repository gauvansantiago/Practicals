# Task 3
"""Gauvan Santiago Prac 01 Task 03"""
# A counts from 0 to 100 in 10s
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# B counts down from 20 to 1 in 1s
for i in range(20, 0, -1):
    print(i, end=' ')
print()


# C asks the user for a number which prints stars as many as the number given
stars = int(input("Number of stars: "))
for i in range(stars):
    print('*', end=' ')
print()


# D asks the user for a number which prints the amount of stars from 1 to the given number
stars = int(input("Number of stars: "))
for i in range(1, stars + 1):
    print('*' * i)
print()
