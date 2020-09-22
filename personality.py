# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:38:58 2020
Personality Bot.
@author: Randy Zhu
"""

# idk what this even is lmaooo
from random import choice, randint

user_colour = input("What's your favourite colour?: ")
user_snack = input("What's your favourite snack?: ")
user_state = input("How are you?: ").capitalize()
user_name = input("What's your name?: ")
user_age = int(input("How old are you?: "))
BASIC_COLOURS = [
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Violet"
    ]
POSITIVE_RESPONSES = [
    "Alright " + user_name + f"{user_colour} nice colour preference.",
    "Me too " + user_name + f"I love {user_snack} as well!"
    "Tasty!",
    ]
NEGATIVE_RESPONSES = [
    "You are not a good human, " + user_name + ", your favourite colour: " +
    user_colour + " is not a good colour in my opinion. Your snack: "
    + user_snack + " is also not a good snack.",
    "Your colour choices are bad.",
    f"{user_name}, I think we can agree to disagree about {user_snack}",
    f"{user_name}, I think we can agree to disagree about {user_colour}",
    ]
NEUTRAL_RESPONSES = [
    f"Interesting choice {user_name}, as a machine, I have never had {user_snack}.",
    f"Honesty, {user_name}, as a machine, I do not see colours. I only see ones and zeros.",
    f"Decent choice of colour {user_name}."
    ]

# If the user is not under the age of ten, give them any response
if 1user_state == "Good" or user_state == "Great" or user_state == "Excellent" and user_age > 10):
    three_sided_die = randint(0, 2)
    if three_sided_die == 0:
        print(choice(POSITIVE_RESPONSES))
    elif three_sided_die == 1:
        print(choice(NEUTRAL_RESPONSES))
    elif three_sided_die == 2:
        print(choice(NEGATIVE_RESPONSES))
# If they're choice of colour doesn't match the bot's, give them a non-positive reply.
elif (user_state == "Good" or user_state == "Great" 
      or user_state == "Excellent" and user_colour 
      not in BASIC_COLOURS and user_age > 10):
    two_sided_evil_die = randint(1, 2)
    if two_sided_evil_die == 1:
        print(choice(NEUTRAL_RESPONSES))
    elif two_sided_evil_die == 2:
        print(choice(NEGATIVE_RESPONSES))

# If they're doing alright, give them a positive, or neutral message.
elif user_state == "Alright" or user_state == "Decent" and user_age > 10:
    print(choice(NEUTRAL_RESPONSES))

# If they're doing bad, only give them a positive response.
elif user_state == "Bad" or user_state == "Awful" or user_state == "Not Good" and user_age > 10:
    print(choice(POSITIVE_RESPONSES))
    
# Alas, if they're a child, give them a positive response. Don't bully children.
elif user_age < 10:
    print(choice(POSITIVE_RESPONSES))
    