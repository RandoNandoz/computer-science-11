# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:36:16 2020
Find who I have the most in common with.
@author: Randy Zhu
"""

people = []
most_in_common = []
my_favourites =["Starbucks", "Chef Hung", "Uncle Fatih's", "Guadalupe (MBC)", "Steve's Poke Bar"]
file = open("sfu_best_cmpt120.csv")

file.readline()

for line in file:
    score = 0
    data = line.strip("\n").split(",")
    name = data[1]
    for item in my_favourites:
        if item in data:
            score += 1
    people.append([name, score])

for person in people:
    person_score = person[1]
    person_name = person[0]
    if person_score >= 5:
#        print(person_name)
#        print("hit1")
#        most_in_common.append(person_name)
        print(most_in_common)
    elif person_score == 4 and most_in_common == []:
        most_in_common.append(person_name)
    elif person_score == 3 and most_in_common == []:
        most_in_common.append(person_name)
    elif person_score == 2 and most_in_common == []:
        most_in_common.append(person_name)
    elif person_score == 1 and most_in_common == []:
#        print(most_in_common)
#        print(person_name)
#        print("hit5")
        most_in_common.append(person_name)
    elif person_score <= 0 and most_in_common == []:
        print("you have nobody in common")
if indexf
#print(most_in_common)
file.close()