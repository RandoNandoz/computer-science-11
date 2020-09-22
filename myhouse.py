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
myWall = "|" + " " * 10   + " " * 5 + " " * 10 + "|" + "\n"

# The second type of wall, containing window
mySecondWall = "|" + " " * 10 + "\'"  + " " * 5 + "\'" + " " * 8 + "|" + "\n"

# Roof
print(" " * 7 + "\'" * 13)
# Roof
print(" " * 7 + "\'" + " " * (int(len(myWall)) - 17) + "\'")
# Roof
print(" " * 6 + "\'" + " " * (int(len(myWall)) - 15) + "\'")
print(" " * 5 + "\'" + " " * (int(len(myWall)) - 13) + "\'")
# Roof
print(" " * 4 + "\'" + " " * (int(len(myWall)) - 11) + "\'")
# Roof
print(" " * 3 + "\'" + " " * (int(len(myWall)) - 9) + "\'")
# Roof
print(" " * 2 + "\'" + " " * (int(len(myWall)) - 7) + "\'")
# Roof
print(" " + "\'" + " " * (int(len(myWall)) - 5) + "\'")
# Wall
print("\'" + " " * (int(len(myWall) - 3)) + "\'")
# Wall
print("\'" * ((int(len(myWall)) - 1)))
# Wall
print(myWall * 3, end="")
# Window
print("|" + " " * 10 + "\'" * 7 + " " * 5 + " " * 3 +"|")
# Window
print(mySecondWall * 3, end="")
# Window
print("|" + " " * 10 + "\'" * 7 + " " * 5 + " " * 3 +"|")
# Window
print(myWall, end="")
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
print("\'" * ((int(len(myWall)) - 1)))
