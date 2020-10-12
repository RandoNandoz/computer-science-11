# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 09:23:24 2020
Evaluate whether something is a good idea.
@author: Randy Zhu
"""

# Ask for the user's idea.
idea = input("Give me your idea: ")

# Make a list of ideas.
# ikea brand hashmap
# nested lists > dictionary lol
idea_questions = [
    # Make an array of arrays, and the arrays inside this array are like key -
    # value pairs, with index 0 being the questions, and index 1 being the
    # weight.
    ["Out of 100, how much is this idea worth to you?: ", 5],
    ["Out of 100, how much will this idea matter in 2 days?: ", 1],
    ["Out of 100, how much will this idea matter in 2 weeks?: ", 2],
    ["Out of 100, how much will this idea matter in 2 years?: ", 4],
    ["Out of 100, how much will this idea matter in 20 years?: ", 5],
    ["How large will the impact of your idea be (big/medium/small)?: ", 5]
]

# Initialize the goodness score.
idea_goodness_score = 0
# Ask the question of how much it's worth.
worth = input(idea_questions[0][0])
# The goodness score is the worth, multiplied by the weight of the worth.
idea_goodness_score += int(worth) * idea_questions[0][1]

# For each question in the slice of indexes one to four,
# ask it, and then calculate with its average.
# We take the slice 1 - 4, as there are questions
# which must be evaluated differently.
for question in idea_questions[1:4]:
    idea_goodness_score += int(input(question[0])) * question[1]

# Get the impact of the questions, by taking the 5th index, and asking it, then,
# if it's a big impact, give it 100, medium, 50, and small, 25.
impact = input(idea_questions[5][0])
if impact.lower().strip("!?. ") == "big":
    impact = 100
elif impact.lower().strip("!?. ") == "medium":
    impact = 50
elif impact.lower().strip("!?. ") == "small":
    impact = 25
# Add the impact to the score.
idea_goodness_score += impact

# If the user answers all 100s, and they think it is a big impact, tell them to
# go for it.
if idea_goodness_score == 1300:
    print("Go for it, it's the best idea every: ")
# If the user answers mostly good, then tell them it is good.
elif idea_goodness_score >= 650:
    print(idea + " is good, go for it!")
# If the user gives a short - term, medium low impact, low value idea, tell
# them to reevaluate.
elif idea_goodness_score >= 300:
    print(idea + " is decent, but you may want to reevaluate some parts")
# If the goodness score is low, then unfortunately, it is not a good idea.
elif idea_goodness_score < 300:
    print("Hate to say it, but " + idea + " does not seem good to me.")
# Invalid case.
else:
    print("I dunno about " + idea + ".")
