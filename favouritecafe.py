"""
Date: 10-02-2020
Name: Randy Zhu
Purpose: Find the most popular cafe @SFU
"""
# var init
starbucks = 0
tim_hortons = 0
renaissance = 0
cafe_prefs = []

# Get input from five users.
for index in range(5):
    cafe_prefs.append(
        input(
            f"Person {index + 1}, can you please tell me your favorite cafe in SFU?: "
        )
    )

pref: str
for pref in cafe_prefs:
    if pref.lower().strip("?!. ") == "starbucks":
        starbucks += 1
    elif pref.lower().strip("?!. ") == "tim hortons":
        tim_hortons += 1
    elif (pref.lower().strip("?!. ") == "renaissance" or
          pref.lower().strip("?!. ") == "renaissance cafe"):
        renaissance += 1

print(
    f"""
    The most popular cafes are:
    \nStarbucks with {starbucks} votes,
    \nTim Hortons with {tim_hortons} votes,
    \nRenaissance Cafe with {renaissance} votes.
    """
)
