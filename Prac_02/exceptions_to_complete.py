# Gauvan Santiago Prac_02 Task_04 exceptions_to_complete

finished = False
result = 0
# prevents program from ending until a valid integer is given
while not finished:
    try:
        #  asks for an input of an integer
        result = int(input("Enter integer: "))
        finish = True
    # if integer is invalid it asks for a valid integer
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
