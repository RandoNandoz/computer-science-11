# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:21:19 2020
Comparing two people's favourite movies.
@author: Randy Zhu
"""

# Get favourite movies for each person.
angelica_favourite_movies = ["Big Hero 6", "Inside Out", "Wall-E"]
# baymax_favourite_movies = ["Big Hero 6", "Star Wars", "Wall-E"]
# baymax_favourite_movies = ["a", "b", "c"]
baymax_favourite_moviesbaymax_favourite_movies = angelica_favourite_movies
# Make a common interest counter.
common_interest_counter = 0

# For every movie in the list of movies that angelica likes,
# compare it to baymax's, and if they match, add one to the
# common interest counter.
for movie in angelica_favourite_movies:
    if movie in baymax_favourite_movies:
        common_interest_counter += 1
# Print counter above ^
print(common_interest_counter)
