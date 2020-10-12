# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:44:38 2020
Bot which asks the user what year they were born, and tells them their horoscope.
@author: Randy Zhu
"""

# Asks the user what year they were born in.
user_year = input("In what year were you born?: ")
# Because input() returns string, we need to cast the user_year variable
# to an int.
user_year = int(user_year)

# Checks whether the user is born in a certain year of the zodiacs.
if user_year == 1996 or user_year == 1984 or user_year == 1972 or user_year == 1960 or user_year == 1948:
    print("You were born in the year of the rat.")
elif user_year == 1997 or user_year == 1985 or user_year == 1973 or user_year == 1961 or user_year == 1949:
    print("You were born in the year of the ox")
elif user_year == 1998 or user_year == 1986 or user_year == 1974 or user_year == 1962 or user_year == 1950:
    print("You were born in the year of the tiger.")
elif user_year == 1999 or user_year == 1987 or user_year == 1975 or user_year == 1963 or user_year == 1951:
    print("You were born in the year of the rabbit.")
elif user_year == 2000 or user_year == 1988 or user_year == 1976 or user_year == 1964 or user_year == 1952:
    print("You were born in the year of the dragon.")
elif user_year == 2001 or user_year == 1989 or user_year == 1977 or user_year == 1965 or user_year == 1953:
    print("You were born in the year of the snake.")
elif user_year == 2002 or user_year == 1990 or user_year == 1978 or user_year == 1966 or user_year == 1954:
    print("You were born in the year of the horse.")
elif user_year == 2003 or user_year == 1991 or user_year == 1979 or user_year == 1967 or user_year == 1955:
    print("You are goated.")
elif user_year == 2004 or user_year == 1992 or user_year == 1980 or user_year == 1968 or user_year == 1956:
    print("You were born in the year of le monke")
elif user_year == 2005 or user_year == 1993 or user_year == 1981 or user_year == 1969 or user_year == 1957:
    print("You were born in the year of the rooster")
elif user_year == 2006 or user_year == 1994 or user_year == 1982 or user_year == 1970 or user_year == 1958:
    print("You were born in the year of the dog")
elif user_year == 2007 or user_year == 1994 or user_year == 1982 or user_year == 1971 or user_year == 1959:
    print("You were born in the year of the pig")
# Cover the edge cases.
else:
    print("Your year is out of range for the zodiacs, human.")
