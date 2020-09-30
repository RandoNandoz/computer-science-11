"""
Author: Randy Zhu
Purpose: Find vowels in one's first name.
Date: 24-09-2020
"""

# List of vowels.
VOWELS = [
    "a",
    "e",
    "i",
    "o",
    "u"
]
# Get the user's first name.
users_first_name = input("What's your first name?: ")
# A variable about whether there is a vowel in the user's name.
HAS_VOWEL_IN_NAME = False
# Iterate through the user's first name, looking for vowels. This should
# be O(n).
for i in enumerate(users_first_name):
    # For some reason, when you call enumerate() on a string,
    # it returns a tuple, so we access the 0th index of the tuple.
    if users_first_name[i[0]] in VOWELS:
        # Tell the user that they have a vowel in their name.
        print("You have the following vowels in your name.")
        # Set the variable of whether the user has a vowel true, if a vowel is
        # found in the search.
        HAS_VOWEL_IN_NAME = True
        # Stop iterating once a vowel is found.
        break

# If there is a vowel in the first name, print the positions
if HAS_VOWEL_IN_NAME:
    # which is the error return code for str.find(),
    # print the vowel's index.
    if (vowel_index := users_first_name.find("a")) != -1:
        print(f"The vowel \"a\", first found at position {vowel_index}")
    if (vowel_index := users_first_name.find("e")) != -1:
        print(f"The vowel \"e\", first found at position {vowel_index}")
    if (vowel_index := users_first_name.find("i")) != -1:
        print(f"The vowel \"i\", first found at position {vowel_index}")
    if (vowel_index := users_first_name.find("o")) != -1:
        print(f"The vowel \"o\", first found at position {vowel_index}")
    if (vowel_index := users_first_name.find("u")) != -1:
        print(f"The vowel \"u\", first found at position {vowel_index}")
# In all other cases, tell the user that they do not have a vowel in their
# name.
else:
    print("You do not have a vowel in your name.")
