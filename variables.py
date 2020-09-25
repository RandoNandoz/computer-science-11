# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:04:37 2020

@author: Randy Zhu
"""

NAME = "Bob"
AGE = 15
AVERAGE = (12 + AGE + 13) / 3
IS_HAPPY = True

print(NAME, type(NAME)) # expected output: <class 'str'>
print(AGE, type(AGE))
print(AVERAGE, type(AVERAGE))
print(IS_HAPPY, type(IS_HAPPY))

print("*" * 20)

# Ints
print(int(1))
print(int(2.8))
print(int("3"))

number = int(input("Enter a number: "))
print(number)

# Floats
print(float(1))
print(float(2.8))
print(float("3"))
print(float("4.2"))

# Strings
print(str("s1"))
print(str(2))
print(str(3.0))
