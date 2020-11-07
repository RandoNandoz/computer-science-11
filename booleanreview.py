"""
Date: 09-22-20
Purpose: Bootlean review.
Author: Randy Zhu
"""

USER_NAME = "Angelica"

if USER_NAME == "Angelica":
    print("Hi teach")

print(USER_NAME == "Angelica")  # True
print(USER_NAME == "Michael")  # False
print(USER_NAME == "angelica")  # False
print(USER_NAME == "angelica" or USER_NAME == "Micheal")  # False
print(USER_NAME == "Angelica" or USER_NAME == "Micheal")  # True
