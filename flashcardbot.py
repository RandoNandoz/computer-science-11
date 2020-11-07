"""
A flash card bot.
# Author:  Randy Zhu
# Date:  28-09-2020
"""

from os import system

# Create question list.
questions = []
answers = []
SCORE = 0
questions.append(
    [input("Input your first question for the flash card: "), 0])
answers.append(
    [input("Input the answer to the first question: "), 0])
questions.append(
    [input("Input your second question for the flash card: "), 1])
answers.append(
    [input("Input the answer to the second question: "), 1])
questions.append(
    [input("Input your third question for the flash card: "), 2])
answers.append(
    [input("Input the answer to the third question: "), 2])

system("clear")

# Make a loop that asks the questions
for question in questions:
    print(question[0])
    answer = input(
        "What is the answer to the question above?: ").lower().strip(".!?")
    if answer == answers[question[1]][0].lower().strip(".!?"):
        print("Correct!")
        SCORE += 1
    else:
        print("Wrong, the correct answer was " + answers[question[1]][0] + ".")
print(f"Your score was {SCORE}/3, or {(SCORE / 3) * 100}%.")
