"""
Author: Randy Zhu
Date: 09-22-20
Purpose: Checks whether the user is of voting age.
"""
# Asks for the user's age.
age = int(input("How old are you?: "))
# Check if the user's age is negative.
if age < 0:
    # If it is, tell them that it cannot be negative, because that violates logic.
    print("Your age cannot be negative.")
# If the user's age is equal, or greater than 18:
elif age >= 18:
    # Tell them that they are of the legal age to vote.
    print("You are of legal age to vote.")
# In all other cases, where the user's age is not greater than or equal to 18:
else:
    # Tell the user that they cannot vote yet,
    # and how much longer they have to wait until they can vote.
    print(
        f"""
        You are not of legal age to vote yet.
        You will have to wait another {18 - age} years to vote.
        """
    )
