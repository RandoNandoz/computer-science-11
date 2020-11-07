"""
Randy Zhu
2020-10-29
Guess secret number.
"""
# Import random number library.
from random import randint

# Assign secret number value.
secret_number = randint(a=1, b=10)

# Set user number to their input, casted to an int.
user_number = int(input("Take a guess: "))

# While the user's number is not equal to the secret number, get them to guess again.
while user_number != secret_number:
    user_number = int(input("Incorrect, guess again: "))

# On user success, alert them of so.
print("Success, you have guessed the number! The number was " +
      str(secret_number) + "!")
