# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 08:59:16 2020

@author: Randy Zhu
"""
# Importing the choice function from the random library.
from random import choice
# Interrogates the user for their favourite book.
favourite_book = input("What is your favourite book? ")
# List of strings which are potential choices for the reply to the user.
comments = [
    f"Oh, nice! {favourite_book} is a good choice.",
    f"{favourite_book} is a good one.",
    f"Hmm, {favourite_book} is a strange taste",
    f"Blah blah blah, {favourite_book}",
    f"Whoa there. {favourite_book} is an odd choice",
    f"Hahahaa!"
    ]
# Using the python random library, we use the choice function imported above
# to pick a random indice of the array.
random_comment = choice(comments)

# crash and burn!
# prints(")
       
# Using the random string from the array of comments, 
# we print it as a reply to the user, along with the user's favourite book.
print(random_comment)