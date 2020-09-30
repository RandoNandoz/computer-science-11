"""
Created: 28-09-2020
Author: Randy Zhu
Purpose: Mind reader bot.
"""

# Introduce the game.
print("Welcome to the Mind Reader!")

words = ["cat", "dog", "apple"]
score = 0

for word in words:
    print("Player 1, enter 3 words you think of when I say " + word + ".")

    first = input("First word: ").lower().strip("!.? ")
    second = input("Second word: ").lower().strip("!.? ")
    third = input("Third word: ").lower().strip("!.? ")
    print("\n" * 1000)

    guess = input(
        "Player 2, what is one word you think Player 1 associates with " +
        word +
        "?: ").lower().strip("!.? ")

    if guess in [first, second, third]:
        print("You've got it!")
        score += 1

print("You got: " + str(score) + " right.")
