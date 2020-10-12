"""
Greetings Chatbot
Author: Randy Zhu
Date: 09-14-20
"""


# This "bot" takes in the value of the users name using input(),
# Then responds with "Nice to meet you, {name}"

# Print function
# print("Hi, what's your name?")
# name = input()
# print("Nice to meet you",name)

# Concatenation
# print("Hi, what's your name?")
# nameconcat = input()
# print("Nice to meet you" + nameconcat)

username = input("Hi, what is your name?: ")
print(f"Nice to meet you, {username}.")
favouritebook = input(f"What's your favourite book, {username}?: ")
print(f"Cool book {username}, I too like {favouritebook}.")
