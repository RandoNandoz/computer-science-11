# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:49:38 2020

@author: 1257035
"""

treats = [["small", 1, 0], ["medium", 2, 1], ["large,", 3, 2]]
given_treats = []
dog_score = 0 
for _ in treats:
    given_treats.append(int(input()))

for i in enumerate(given_treats):
    if i == given_treats[0][3]:
        dog_score += i[1] * given_treats[i[0]][2]
                