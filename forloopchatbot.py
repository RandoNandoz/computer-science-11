"""
Author: Randy Zhu
Purpose: When text is inputted, check whether it is a palindrome or not.
Date: 24-09-2020
"""
# Get inputted text from the user.
print(
    "Give me a word, or a series of words, and I will tell your whether it is a palindrome or not."
)
# Get the user's input, make it lower case and remove any newlines.
user_input = input(
    "Input your word here: "
).lower().strip("\n")

# Create an empty string.
user_input_reverse = ""

# Reversely iterate on the user's input.
for i in reversed(range(len(user_input))):
    # When reversely iterating on the user's input, get the character at the index of the iteration,
    # and append it to the empty string, therefore reversing the string,
    user_input_reverse = user_input_reverse + user_input[i]

# If the user's input has a length of zero, or a negative length,
#  meaning that it is empty, tell them that it's empty.
if len(user_input) <= 0:
    print("You have inputted nothing.")
# If the user's input in reverse is equal to the user's original input,
# it is a palindrome. Tell them accordingly.
elif user_input_reverse == user_input:
    print(f"\"{user_input}\" is a palindrome.")
# If the user's input is not equal to the user's input in reverse,
# it is not a palindrome. Tell them accordingly.
else:
    print(
        f"As \"{user_input}\" in reverse is \"{user_input_reverse}\", it is not a palindrome."
    )
