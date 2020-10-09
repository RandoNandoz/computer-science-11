# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 09:02:50 2020
evaluates city bliss.
@author: Randy Zhu
"""

# Ask about which city to evaluate.
city = input("What city would you like to evaluate?: ")
# Tell the user which city they are evaluating.
print("Okay, we are evaluating " + city + ".\n")

# Make a list of questions.
questions = [
    "How would you rate the environment out of 5?: ",
    "How would you rate the safety out of 5?: ",
    "How would you rate the public transport system out of 5?: "
]

# Initialize score.
score = 0

# for each question in the list, make a rating variable, which is the user's
# input out of five, ask the user about how much that rating means to them,
# and add it to score, multiplying the rating by the weight.
for question in questions:
    rating = int(input(question))
    weight = int(input("How important is that to you, out of 5?: "))
    score += rating * weight
    # print a newline.
    print()

# Tell the user their weighted average score.
print("You have rated " + city + " as " + str(score / (25 * len(questions))))
