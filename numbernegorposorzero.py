"""
Author: Randy Zhu
Date: 09-22-20
Purpose: Checks if the number is positive or negative.
"""

# Asks the user for a number.
number = int(input("Give me a number: "))

# If the number is below zero:
if number < 0:
    # Tell the user that it is below zero.
    print("Your number is negative.")
# If the number is zero:
elif number == 0:
    # Tell the user that it is zero.
    print("Your number is zero.")
# If the number is above zero:
elif number > 0:
    # Tell the user that it is above zero.
    print("Your number is above zero.")
