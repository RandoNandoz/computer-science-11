# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 09:29:48 2020
Chatbot which asks three questions with randomness
@author: Randy Zhu
"""

# We import the choice function to pick a random index in an array.
from random import choice

BASIC_COLOUR_LIST = [
    "Red",
    "Green",
    "Blue",
    "Yellow",
    "Orange",
    "Violet",
    "Pink"
    ]

# Captures the user's favourite food.
userFavouriteFood = input("What is your favourite food?: ")
# An array of potential comments about the user's favourite food.
listCommentsAboutFood = [
    f"I too am a big fan of {userFavouriteFood}",
    f"Wow, in my opinion, {userFavouriteFood} is an odd one, but you do you.",
    f"{userFavouriteFood} is an eccentric choice, but if you like it, I like it as well.",
    f"Delicious! {userFavouriteFood} is amazing!"
    ]
# Prints a random choice from the array.
print(choice(listCommentsAboutFood))

# Get's the user's favourite colour, then stores it in a variable
userFavouriteColour = input("What's your favourite color?: ")

# A list of comment's about their favourite colour.
listCommentsAboutColour = [
    f"""
    You're a {userFavouriteColour} person? No way,
    I thought you were a {choice(BASIC_COLOUR_LIST)} type of person
    as your favourite food is {userFavouriteFood}
    """,
    f"""
    Knew it. Considering your favourite food is {userFavouriteFood},
    you had to be a {userFavouriteColour} type of person.
    """,
    f"""
    We have a lot in common - human, not only do I like {userFavouriteFood},
    I also like {userFavouriteColour}!
    """,
    f"""
    My guess is... {choice(BASIC_COLOUR_LIST)}. Let me see your answer: {userFavouriteColour}.
    Tell me, am I right?
    """
    ]
# Prints a random selection of the array.
print(choice(listCommentsAboutColour))

# Get's the user's favourite word or phrase.
userFavouriteWord = input("What's your favourite word, or phrase?: ")

# Make a list of comments about the phrase.
listCommentsAboutPhrase = [
    f"""
    Wow! We have so much in common human! You like {userFavouriteFood}, 
    {userFavouriteColour}, and {userFavouriteWord}?! Me too.
    """,
    f"""
    {userFavouriteWord} seems a little degrading to me. Could just be my memory acting up though.
    """,
    f"""
    I knew it, {userFavouriteWord} is your favourite!
    """
    ]
# Print random index of the list of comments.
print(choice(listCommentsAboutPhrase))