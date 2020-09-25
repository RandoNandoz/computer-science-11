# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:53:37 2020
Drawing a house with print statement.
AKA A NIGHTMARE
WHY DID I DO THIS?
Magic numbers in code hell™
@author: Randy Zhu
"""
# The walls of the house
MY_WALL = "|" + " " * 10   + " " * 5 + " " * 10 + "|" + "\n"

# The second type of wall, containing window
MY_SECOND_WALL = "|" + " " * 10 + "\'"  + " " * 5 + "\'" + " " * 8 + "|" + "\n"

# Roof
print(" " * 7 + "\'" * 13)
# Roof
print(" " * 7 + "\'" + " " * (int(len(MY_WALL)) - 17) + "\'")
# Roof
print(" " * 6 + "\'" + " " * (int(len(MY_WALL)) - 15) + "\'")
print(" " * 5 + "\'" + " " * (int(len(MY_WALL)) - 13) + "\'")
# Roof
print(" " * 4 + "\'" + " " * (int(len(MY_WALL)) - 11) + "\'")
# Roof
print(" " * 3 + "\'" + " " * (int(len(MY_WALL)) - 9) + "\'")
# Roof
print(" " * 2 + "\'" + " " * (int(len(MY_WALL)) - 7) + "\'")
# Roof
print(" " + "\'" + " " * (int(len(MY_WALL)) - 5) + "\'")
# Wall
print("\'" + " " * (int(len(MY_WALL) - 3)) + "\'")
# Wall
print("\'" * ((int(len(MY_WALL)) - 1)))
# Wall
print(MY_WALL * 3, end="")
# Window
print("|" + " " * 10 + "\'" * 7 + " " * 5 + " " * 3 +"|")
# Window
print(MY_SECOND_WALL * 3, end="")
# Window
print("|" + " " * 10 + "\'" * 7 + " " * 5 + " " * 3 +"|")
# Window
print(MY_WALL, end="")
# Door
print("|" + " " * 10 + "\'" * 7 + " " * 5 + " " * 3 +"|")
# Door
print("|" + " " * 10 + "\'" + " " * 5 + "\'" + " " * 8 + "|")
# Door
print("|" + " " * 10 + "\'" + " " * 5 + "\'" + " " * 8 + "|")
# Door
print("|" + " " * 10 + "\'" + " " * 3 + "\u1F91" + " " + "\'" + " " * 8 + "|")
# Door
print("|" + " " * 10 + "\'" + " " * 5 + "\'" + " " * 8 + "|")
# Floor
print("\'" * ((int(len(MY_WALL)) - 1)))
