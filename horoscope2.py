# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:44:38 2020
Bot which asks the user what year they were born, and tells them their horoscope.
@author: Randy Zhu
"""

# Data of the horoscopes.
# I wonder how much RAM this uses.
rat = [
    1996,
    1984,
    1972,
    1960,
    1948
]
ox = [
    1997,
    1985,
    1973,
    1961,
    1949
]
tiger = [
    1998,
    1986,
    1974,
    1962,
    1950
]
rabbit = [
    1999,
    1987,
    1975,
    1963,
    1951
]
dragon = [
    2000,
    1988,
    1976,
    1964,
    1952
]
snake = [
    2001,
    1989,
    1977,
    1965,
    1953
]
horse = [
    2002,
    1990,
    1978,
    1966,
    1954
]
goated = [
    2003,
    1991,
    1979,
    1967,
    1955
]
monkey = [
    2004,
    1992,
    1980,
    1968,
    1956
]
rooster = [
    2005,
    1993,
    1981,
    1969,
    1957
]
dog = [
    2006,
    1994,
    1982,
    1970,
    1958
]
pig = [
    2007,
    1995,
    1983,
    1971,
    1959
]

# Asks the user what year they were born in.
user_year = input("In what year were you born?: ").strip(" ,!.?")
# Because input() returns string, we need to cast the user_year variable
# to an int.
user_year = int(user_year)
# Checks if the user's year are in the arrays.
if user_year in rat:
    # Print a response according to their year.
    print("You were born in the year of the rat.")
elif user_year in ox:
    print("You were born in the year of the ox.")
elif user_year in tiger:
    print("You were born in the year of the tiger.")
elif user_year in rabbit:
    print("You were born in the year of the rabbit")
elif user_year in dragon:
    print("You were born in the year of the dragon")
elif user_year in snake:
    print("You were born in the year of the snake")
elif user_year in horse:
    print("You were born in the year of the horse")
elif user_year in goated:
    print("You are goated")
elif user_year in monkey:
    print("You were born in the year of le monke")
elif user_year in rooster:
    print("You were born in the year of the rooster")
elif user_year in dog:
    print("You were born in the year of the dog")
elif user_year in pig:
    print("You were born in the year of the pig.")
