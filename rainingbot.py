"""
Author: Randy Zhu
Date: 09-22-20
Purpose: If it's raining, respond accordingly, if it's not, respond accordingly.
"""

# Creates a boolean variable storing whether it's raining or not
IS_RAINING = False

# If it is raining:
if IS_RAINING:
    # Tell the user that the bot is going to bring its umbrella.
    print("I'm going to bring my umbrella!")
# If it is not raining
elif not IS_RAINING:
    # Tell the user that the bot is going to bring its sunglasses.
    print("I'm going to bring my sunglasses.")
