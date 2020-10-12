# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:36:16 2020
Find who I have the most in common with.
@author: Randy Zhu
"""

# Type hints
from typing import Union


# Create a new blank list called people.
people: "list[list[Union[str, int]]]" = []
# Create a new blank list called "Most in common",
# which is a list of the people who I have the most in common with..
most_in_common = []
# A list of my favourites @SFU
my_favourites: "list[str]" = [
    "Bubble World",
    "Chef Hung",
    "Pizza Hut",
    "Quesada(Cornerstone)",
    "Steve's Poke Bar"
]

# Open the file.
file = open("sfu_best_cmpt120.csv")

# Read the first useless line.
file.readline()

# Sanitize user input by removing all the newlines, and removing all the spaces.
counter = 0
# Make an empty list of new favourites
new_favourites: "list[str]" = []
# For every favorite there is, loop through each index of it.
for favorite in my_favourites:
    # Replace all the newlines, and remove spaces.
    new_favourites.append(my_favourites[counter].strip("\n ").replace(" ", ""))
    counter += 1
# Reassign the old favourites to the new - sanitized favourites.
my_favourites = new_favourites

# For every line in the file, remove newlines, remove spaces, and split by commas.
# If the input matches the data from the .csv, add one to the score, and then append
# the score into the empty list of people, creating nested lists, kind of like
# key value pairs, like this: ["Name", score]
for line in file:
    score = 0
    data = line.strip("\n").replace(" ", "").split(",")
    name = data[1]
    favorite_item: str
    for favorite_item in my_favourites:
        if favorite_item in data:
            score += 1
    people.append([name, score])
file.close()

# Now we need to create a list of original names, iterating through the file again,
# and making a list of names
new_file = open("sfu_best_cmpt120.csv")
new_file.readline()

names: "list[str]" = []
for old_line in new_file:
    data = old_line.strip("\n").split(",")
    name = data[1]
    names.append(name)
file.close()

# Now, with the list of people and their scores, loop through and:
person: "list[Union[str,int]]"
for person in people:
    # If the list of those who I am most in common with is empty,
    # Just append the first value which shows up.
    if most_in_common == []:
        most_in_common.append(person)
    # If it is not empty, compare whether the score of the last index in the list
    # is below the current score. If it is, clear the last,
    # and add the current person with their score,
    # as the score in the list is below the current person.
    # This will ensure that the list has a homogenus score.
    else:
        if most_in_common[-1][1] < person[1]:
            most_in_common.clear()
            most_in_common.append(person)
        # If the last item in the list is equal to the current, add the current
        # person to the list of those who are most in common.
        elif most_in_common[-1][1] == person[1]:
            most_in_common.append(person)
# Alas, print the list of people who have the most in common.
counter = 0
# For every name in the list of names, loop through the most in common list, and
# check whether their name is in the same position as the most_in_common, and if so,
# print their original name!
for name in names:
    for commoner in most_in_common:
        if commoner[0] == names[counter].strip("\n").replace(" ", ""):
            print(names[counter].strip(" "))
    counter += 1
