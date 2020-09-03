"""
CP1404/CP5632 Practical - Suggested Solution
State names in a dictionary
File has been reformatted and state inputs can be any case
"""

states = {"QLD": "Queensland", "NSW": "New South Wales",
          "NT": "Northern Territory", "WA": "Western Australia",
          "ACT": "Australian Capital Territory", "VIC": "Victoria",
          "TAS": "Tasmania"}
# Displays States
print(states)

# Asks user for state and validates 
state = input("Enter short state: ").upper()
while state != "":
    if state in states:
        print(state, "is", states[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
