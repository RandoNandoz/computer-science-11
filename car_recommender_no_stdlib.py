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

cars = ""

for line in car_file:
    if car_price == int(line.strip("\n ").split(",")[0]):
        cars = cars + line.strip("\n ") + "|"

cars = cars.split("|")
if len(cars) == 1:
    print("There are no cars at this price range.")
    exit()

for i in range(3):
    car = choice(cars).split(",")
    print(f"Car {i + 1} is a: {car[-2]} {car[-1]} with {car[2]} miles.")
