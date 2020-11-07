"""
Author: Randy Zhu
Purpose: Determine whether the user is in the dark or light.
Date: 09-30-2020
"""
# Introduce yourself.
print("I will decide whether you can join the Dark Side.")
# Set variables.
IN_DARK = False

# Ask user for input.
user_likes_red_input = input("Is red your favorite color?: ")
user_likes_capes_input = input("Do you like capes?: ")

# If the user likes red or capes, set IN_DARK to True.
if (user_likes_red_input.lower().strip("?!. ") == "yes"
        or user_likes_capes_input.lower().strip("?!. ") == "yes"):
    IN_DARK = True

# If IN_DARK is True, tell them that they are in the dark side.
if IN_DARK:
    print("Dark side it is!")
# Otherwise, say that they're in the light side.
else:
    print("Light side, I see.")
