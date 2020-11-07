# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:16:26 2020
Calculate age in 2051.
@author: Randy Zhu
"""
CURRENT_YEAR = 2020
current_age = int(input("How old are you right now?: "))

print("You wil be " + str(2051 - CURRENT_YEAR +
                          current_age) + " years old in 2051!")
