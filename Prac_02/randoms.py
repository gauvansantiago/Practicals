# Gauvan Santiago Prac_02 Task_02 randoms
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))
# What did you see on line 1?
# a random number was imported from the range of 5-20
# What was the smallest number you could have seen, what was the largest?
# the smallest number was 5 and the largest number was 20

# What did you see on line 2?
# an odd number was imported from the range 3-10
# What was the smallest number you could have seen, what was the largest?
# smallest number it produced was 3 largest number produced was 9
# Could line 2 have produced a 4?
# no it only imported random odd numbers

# What did you see on line 3?
# a random number was imported from the range of 2.5 - 5.5 which produced a number with 15 decimal places
# What was the smallest number you could have seen, what was the largest?
# 2.6 was the smallest number and the largest number 5.4


# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(0, 101))
