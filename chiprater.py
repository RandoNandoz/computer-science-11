# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 08:53:28 2020
Rates potato chips
@author: Randy Zhu
"""

# introduce the bot itself.
print("Welcome to Chip Rater. I'd like you to answer a few questions.")

# make a list of questions
questions = [
    "How crispy is the chip out of 5?: ",
    "How would you rate the taste out of 5?: ",
    "Out of 5, how would you rate the packaging?: "
    ]

# make a variable tracking score
final_score = 0

# for every question in the questions list, ask it.
for question in questions:
    # the rating is the user's input casted to an int.
    rating = int(input(question))
    # the final score is the all the ratings added together
    final_score += rating
    
# Alas, get the average score by dividing by the number of questions.
print("You've rated this chip " + str(final_score / len(questions)))