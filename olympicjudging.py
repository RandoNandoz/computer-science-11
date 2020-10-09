# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:23:16 2020
An olympic judging program.
@author: Randy Zhu
"""

scores = []
score = 0
for i in range(5):
    scores.append(float(input("Enter your score, Judge " + str(i + 1) + ": ")))

for i in scores:
    score += i

print("Your olympic score is " + str(score / 5) + ".")
