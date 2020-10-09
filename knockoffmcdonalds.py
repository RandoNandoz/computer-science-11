# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:36:15 2020
Calculates price of order.
@author: 1257035
"""

TAX = 1.14
# mom can we have hashmap
# hashmap at home:
menu = [["burger", 5], ["fries", 3]]
price = 0
for item in menu:
    wants_item = input("Would you like a " + str(item[0]) + " for $" + str(item[1]) + "? (Yes/No): ")
    if wants_item.lower().strip("!?. ") == "yes":
        price += item[1]
print("Your total is $" + str(price * TAX) + ".")
