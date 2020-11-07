# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 09:44:26 2020
How is it going bot?
@author: Randy Zhu
"""

# == equality comparison
# < less than
# > greater than
# <= less than or equal to
# >= greater or equal to
# != not equal
# Description: This bot asks how is it going, and analyzes your response,
# and make a comment depending on your response and its analysis

# Ask user how it's going & store the reply
userState = input("How's it going?: ")

# If statement format
#   if bool_expr:
# execute
# previous bool_expr has to be false
#   elif bool_expr:
# execute
# If the user's state is Good/good/great, then reply with "Good!".
if userState == "Good" or userState == "good" or userState == "great":
    good_thing = input("Good! Why, what went well?: ")
    print(good_thing.strip(".!? ") + "? That's great!")

# If the user says bad, then reply with "Oh, no!"
elif userState.capitalize() == "Bad":
    print("Oh, no!")
# If the user says decent, then reply with "Alright."
elif userState.capitalize() == "Decent":
    print("Alright.")
# If the user says awful, then reply with "Sorry."
elif userState.capitalize() == "Awful":
    print("Sorry for asking.")
# Incases of invalid input, it will print a generic response.
else:
    print("I see...")
