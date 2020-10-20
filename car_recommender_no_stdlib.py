"""
Recommends the car at a desired price.
Mon 19 Oct 2020 01:13:41 PM PDT
Randy Zhu
"""
from random import choice
# Open the car listing file.
car_file = open("car_listings.csv")
# Get rid of the first useless line.
car_file.readline()

# Ask the user about their desired car price.
car_price = int(input("What price do you want your car?: ").strip("$ "))

# Create a string of cars.
cars = ""

# For every line in the file
for line in car_file:
    # If the user's desired car price is equal to the first index of the line,
    # newlines removed, split by commas, add the line, stripped by newlines, along with
    # a pipe (this symbol => |) to the cars string.
    if car_price == int(line.strip("\n ").split(",")[0]):
        cars = cars + line.strip("\n ") + "|"

# The car list is the cars, split by the pipes above.
cars = cars.split("|")

# If the list is empty, tell them that there are no matches, and then exit.
if len(cars) == 1:
    print("There are no cars at this price range.")
    exit()

# Repeat 3 times
for i in range(3):
    # The car is equal to a random choice of the car list, then split by commas.
    car = choice(cars).split(",")
    # Print the car.
    print(f"Car {i + 1} is a: {car[-2]} {car[-1]} with {car[2]} miles.")
