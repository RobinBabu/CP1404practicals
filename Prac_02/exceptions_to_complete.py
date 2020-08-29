"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a valid integer: "))
        finished = True
        # TODO: this line
        # TODO: this line
    except ValueError:
        print("Invalid entry (not an integer)")
print("Valid result is:", result)