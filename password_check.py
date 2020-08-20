""" Gauvan Santiago Prac 03 Task 01"""

MINIMUM_LENGTH = 4


def main():
    """ Get password using functions and print """
    password = get_password(MINIMUM_LENGTH)
    asterisk(password)


def get_password(MINIMUM_LENGTH):
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short")
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    return password


def asterisk(password):
    print('*' * len(password))


main()
