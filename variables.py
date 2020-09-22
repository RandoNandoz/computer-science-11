# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:04:37 2020

@author: Randy Zhu
"""

name = "Bob"
age = 15
average = (12 + age + 13) / 3
isHappy = True

print(name, type(name)) # expected output: <class 'str'>
print(age, type(age))
print(average, type(average))
print(isHappy, type(isHappy))

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
