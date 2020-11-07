# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:10:47 2020
SFU's favourite spots!
@author: 1257035
"""

# Read file containing survey info, and then find out which spots are the
# favourites, by counting how many times each one was mentioned.

# Open the file.

file = open("responses.csv")

JUNK = file.readline()

# Read first real dataline.

data = file.readline()

club_ilia_tally = 0
uncle_fatih_tally = 0

for data in file:
    datalist = data.strip("\n").split(",")
    # We want to find the best pizza, so 4th column it is!
    answer = datalist[4]

    if answer.lower() == "uncle fatih's":
        uncle_fatih_tally += 1
    if answer.lower() == "club ilia":
        club_ilia_tally += 1

print(
    "Uncle Fatih's: ",
    uncle_fatih_tally,
    "\n",
    "Club ilia:",
    club_ilia_tally)
# Make comments about data.
if club_ilia_tally < 0:
    print("Nobody likes club ilia :( ")
elif club_ilia_tally == 1 and club_ilia_tally < 5:
    print("Club ilia is not bad.")
else:
    print("Club ilia is the people's favourite.")

file.close()
