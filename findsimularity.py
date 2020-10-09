# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:36:16 2020
Find who I have the most in common with.
@author: Randy Zhu
"""

from typing import Union


people = []
most_in_common = []
my_favourites: "list[str]" = [
    "Bubble World",
    "Chef Hung",
    "Pizza Hut",
    "Quesada(Cornerstone)",
    "Steve's Poke Bar"]
file = open("sfu_best_cmpt120.csv")

file.readline()

counter = 0
new_favourites: "list[str]" = []
for favourite in my_favourites:
    new_favourites.append(my_favourites[counter].strip("\n ").replace(" ", ""))
    counter += 1
my_favourites = new_favourites
print(my_favourites)

for line in file:
    score = 0
    data = line.strip("\n").replace(" ", "").split(",")
    name = data[1]
    favourite_item: str
    for favourite_item in my_favourites:
        if favourite_item in data:
            score += 1
    people.append([name, score])

person: "list[list[Union[str, int]]]"
for person in people:
    # print(person)
    if most_in_common == []:
        most_in_common.append(person)
    else:
        if most_in_common[-1][1] < person[1]:
            most_in_common.clear()
            most_in_common.append(person)
        # elif most_in_common[-1][1] == person[1]:
            # most_in_common.append(person)
        elif most_in_common[-1][1] == person[1]:
            most_in_common.append(person)
print(most_in_common)
file.close()
