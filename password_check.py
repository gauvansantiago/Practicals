""" Gauvan Santiago Prac 03 Task 01"""

MINIMUM_LENGTH = 4


def valid_password():
    """ Get password that meets the minimum length """
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short")
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))

    print('*' * len(password))


valid_password()
