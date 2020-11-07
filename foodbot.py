"""
Purpose: Food suggestion bot.
Author: Randy Zhu
Date: 09-22-20
"""
# Desc:
# Ask the user for their favorite dish, e.g. tempura, sashimi, etc.
# Get dish name, then check if the food is in a certain category,
# then recommend a restaurant of that type.

japanese = [
    "sushi",
    "tempura",
    "sashimi",
    "nigiri",
]
korean = [
    "bibimbap",
    "kalbi"
]

dish = input("What's your favourite dish?: ").lower().strip(", .!?")

if dish in japanese:
    print("You should try Sushi Garden in Metrotown.")
if dish in korean:
    print("You should try Ma Dang Goul on Denman.")
