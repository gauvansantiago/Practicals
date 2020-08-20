# Gauvan Santiago Prac_02 Task_04 exceptions_demo

try:
    # asks to input numerator and denominator
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # while loop will prevent ZeroDivisionError and ask for a valid denominator
    while denominator == 0:
        print(print("Cannot divide by zero!"))
        denominator = int(input("Enter the denominator: "))
    # calculates the fraction and changes it to a number
    fraction = numerator / denominator
    print(fraction)
# Valid numbers meaning whole numbers without decimal points
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# When will a ValueError occur?
# A ValueError will occur if you put in a number with a decimal as an input
# When will a ZeroDivisionError occur?
# ZeroDivisionError occurs when you input 0 in either denominator and numerator as well as on both
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes
