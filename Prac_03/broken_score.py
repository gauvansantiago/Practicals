""" Gauvan Santiago Prac 03 Task 03"""


def main():
    """Get score and display status."""
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    """Determine score status"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

