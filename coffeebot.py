"""
Author: Randy Zhu
Date: 09-22-20
Purpose: Coffee bot which responds to what you want.
"""

user_wants_cream = input(
    "I'm CoffeeBot. Would you like cream with your coffee? (Yes/No/Y/N): ")
if user_wants_cream.lower() == "yes" or user_wants_cream.lower() == "y":
    print("Here's your coffee with cream.")
elif user_wants_cream.lower() == "no" or user_wants_cream.lower() == "n":
    print("Here's your coffee, no cream.")
else:
    print(f"Sorry, I don't know what {user_wants_cream} means.")
