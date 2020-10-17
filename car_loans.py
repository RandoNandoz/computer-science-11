"""
Car Loan Program
Randy Zhu
"""
# region imports
# Import higher precision math lib to prevent rounding errors.
from decimal import Decimal
# Import the floor function for the binary search.
from math import floor
# For the exit function.
import sys
# Type hint, dw about this.
from typing import Any
# Import the environment variable library, and the path library to check whether there is a cache.
from os import environ, path
# endregion

# region Calculate summary for loan
# Define a tax constant. 12% here in BC.
# Subject to change due to democracy.
TAX = Decimal(1.12)
# Get user input on their payments, APR, and loan duration.
loan_initial = Decimal(
    input("How much is your vehicle?: ").strip("$ ").replace(",", ""))
# If the initial amount of the loan is lesser than zero, tell the user
# of the error in their ways, and exit the program to chastise them
if loan_initial <= 0:
    print("Your initial loan amount cannot be zero or less than zero.".strip(
        "$ ").replace(",", ""))
    sys.exit()
# Ask the user for the apr of their loan.
apr = Decimal(input(
    "What is the annual percentage rate of your loan?: ").strip("% ")) * Decimal(10**-2)
yearly_payment_period = int(input("How many years is your payment period?: "))
# If the payment amount is longer then 10 years,
# tell them that it's too long, and then exit.
if yearly_payment_period > 10:
    print("Your payment period cannot be more than 10 years.")
    sys.exit()

# The monthly interest is the annual interest rate divided by 12.
mpr = apr / 12

# The loan amount is equal to the initial user provided value
# of their car, multiplied by the tax amount.
loan_amount = loan_initial * TAX

# the monthly payment periods are the number of years times the 12 months in a month.
monthly_payment_periods = yearly_payment_period * 12

# Calculate the monthly payment amount by the formula
# loan amount * (monthly interest * (1 + monthly interest)^months of loan duration)
# ---------------------------------------------------------------------------------
#               (1 + monthly interest)^months of loan duration - 1

monthly_payment_amount = (
    loan_amount * (
        mpr * (1 + mpr) ** monthly_payment_periods
    )
) / (
    (1 + mpr)**monthly_payment_periods - 1
)

# Print a summary of the loan.
print(
    f"""
Summary:
Loan amount: ${round(loan_amount, 2)}
Duration (Months): {round(monthly_payment_periods, 2)} months
Duration (Years): {round(yearly_payment_period, 2)} years
Monthly payments: ${round(monthly_payment_amount, 2)}
""", end="", sep=""
)

# Make a loan balance variable, which is a copy of the loan amount.
# We need to make loan amount separate, as it will be used later.
loan_balance = loan_amount
# Initialize a monthly principle variable.
# pylint: disable=invalid-name
monthly_principle = 0
# Set an annual principle variable.
principle_per_annum = 0
# In lieu of a c-style for loop (e.g. for(int i; i >= 10; i++)), create
# a counter for the months elapsed.
months_elapsed = 1
# Make a list of principles per year.
principles_annually: "list[Decimal]" = []
# Set a cumulative interest variable.
cum_interest = 0
# We then simulate loan payments per month.
while loan_balance > 0:
    # First, subtract the principle from the loan balance.
    loan_balance -= monthly_principle
    # Then, set the interest rate per payment,
    # which is the loan's balance times the monthly interest rate.
    interest_rate_per_payment = loan_balance * mpr
    # Set the monthly principle to be the monthly payment amount,
    # minus the interest rate for year payment.
    monthly_principle = monthly_payment_amount - interest_rate_per_payment
    # Alas, start counting the principle per annum.
    principle_per_annum += monthly_principle
    # Start counting the cumulative interest.
    cum_interest += interest_rate_per_payment
    # If the months elapsed is divisible by 12 (a year would)
    # have passed, add the principle per annum counter
    # to the list of principles, and then set the value to zero.
    if (months_elapsed) % 12 == 0:
        principles_annually.append(principle_per_annum)
        principle_per_annum = 0
    # Once this cycle is complete, add one month to the month counter.
    months_elapsed += 1

# First, we set a year variable.
year = 1
loan_balance_yearly = loan_amount
# So principles annually is a list of principles,
# and for each principle in the list, we print the
# year that the principle is in, and the balance,
# which is the loan amount minus the principle.
for principle in principles_annually:
    loan_balance_yearly -= principle
    if loan_balance_yearly <= 0:
        print(f"Year {year} balance: $0.00", end="\n", sep="")
    else:
        print(
            f"Year {year} balance: ${round(loan_balance_yearly, 2)}", end="\n", sep="")
    year += 1
# Print the cumulative interest paid.
print(f"Total interest paid: ${round(cum_interest, 2)}")
# endregion

# region Reccommend a car

# Open the car listing file, because we don't need it read - write.
car_list_file = open("car_listings.csv", "r")
# If the cache is built, use the cache.
if path.exists('.car_cache.csv'):
    # Tell the user about it.
    print("Sorted cache built - this run will be fast.")
    # Close the car listing file.
    car_list_file.close()
    # Open up the cache file.
    car_list_file = open('.car_cache.csv')
    # Create a dataset list, and a list of strings, which is the imported data.
    car_dataset = []
    car_strings = []
    # Load the cache into memory.
    print("Loading cache into memory...")
    for line in car_list_file:
        car_strings.append(
            line.strip("\n ").replace(" ", "").split(",")
        )
    # Close the file because we are done with the file.
    car_list_file.close()
    # Cast the first number of the car strings to ints, as we need to perform comparisons. 
    for car in car_strings:
        car[0] = int(car[0])
        car_dataset.append(car)
else:
    # Alert to user that there is no cache, and that it will be slow.
    print("Cache is not built. This run will be slower, but subsequent runs will be faster.")
    # Get rid of the first useless line.
    car_list_file.readline()
    
    # Create a string list of car data.
    car_strings = []
    # Create an empty list of the car data.
    car_dataset = []

    # For each line in the file, add the line of the car data.
    print("Adding data to memory.")
    for line in car_list_file:
        car_strings.append(
            line.strip("\n ").replace(" ", "").split(",")
        )
    # Close the file cuz we're done.
    car_list_file.close()
    # We want to cast the first index of the list to an int, so we can
    # sort the data to execute a binary search to find a price.
    print("Processing data (part 1/2)")
    for car in car_strings:
        for _ in car:
            car[0] = int(car[0])
            car_dataset.append(car)
    # With sorted(), it takes in a list, and has a key value
    # the key is the return value of the function that is valled with the key.
    # by using lambda, we can create a temporary function which just returns the
    # first indice as the key. I tried writing my own sorting thing, it was
    # too hard to be honest.
    print("Sorting data (part 2/2)")
    car_dataset: "list[list[Any]]" = sorted(
        car_dataset, key=lambda v: v[0])
    # Warn the user about not killing the app.
    print("Created cache file .car_cache.csv, building cache... DO NOT Ctrl - C the program. Doing so wil corrupt the cache.")
    # Create a new file called the cache.
    cache = open(".car_cache.csv", "x")
    # Create a write counter, as we need not write a newline with the first write.
    writes = 0
    # Log the dataset into the file
    for items in car_dataset:
        # If there are zero writes, do not write a newline, and just increment one to the counter.
        if writes == 0:
            writes += 1
        # If it's anything other than 0, write a newline.
        else:
            cache.write("\n")
        counter = 0
        # For every bit in the dataset:
        for item in items:
            # If the counter is lesser than the length of the items, write a comma,
            # as it is not the last item in the line.
            if counter < len(items) - 1:
                cache.write(str(item) + ",")
            # Otherwise, just write the item to the file, and do not add a comma.
            else:
                cache.write(str(item))
            # Increment the counter per write of word.
            counter += 1
    # Tell the user that the cache build is finished.
    print("Cache built.")

# Ask the user about their desired car price.
user_desired_car_price = int(
    input("What is your desired car price?: ").strip("$"))
# Set a search limit, as this file is around 800K lines long, which means without a limit, it will take a long
# time to give the user an appropriate response.
search_limit = int(environ.get("SEARCH_LIMIT", 20))
# Alert the user that the default search limit is set, and tell them how to set it.
if search_limit == 20:
    print("Going with default for search limit - 20. You can set a custom search limit with the environment variable SEARCH_LIMIT.")
# If the limit is invalid, tell them so, and quit.
elif search_limit <= 0:
    print("The search limit is lesser than or equal to zero. Invalid limit.")
    sys.exit()
# Tell them about the custom search limit.
else:
    print("SEARCH_LIMIT set to: " + str(search_limit) + ".")
# Execute binary search for right price.
# Create a new list of matches to the price.
matches = []
# Create the leftmost column of the search.
search_left = 0
# Create the rightmost column of the search, which is for now the the last index of the list.
search_right = len(car_dataset) - 1
# While the leftmost search position is lesser than or equal to
# the rightmost search point, calculate the middle of the search
# by averaging the left and the right.
while search_left <= search_right:
    search_middle = floor((search_left + search_right)/2)
    # For every item in the dataset.
    if len(matches) >= search_limit:
        break
    for item in car_dataset:
        # Alas, if the search limit is reached, stop looping.
        if len(matches) >= search_limit:
            break
        # if the item's price is
        # lesser than the user's desired car price, make the leftmost
        # search column the middle plus one.
        if item[0] < user_desired_car_price:
            search_left = search_middle + 1
        # If the price is more than the desired car price, move the
        # right column to the middle search point plus one.
        elif item[0] > user_desired_car_price:
            search_right = search_middle + 1
        # Else a match is found, because the price is equal to the user's desired car price,
        # add the item to the list of matches.
        else:
            matches.append(item)

# Ask the user how many matches they want displayed.
user_wants_times_printed = int(input(
    f"There are {len(matches)} matches. How many matches would you like to see?: "))
# If the user's times printed request is greater than the number of matches, just print all the results.
if user_wants_times_printed > len(matches):
    print("You have selected to print more than there are cars available. Going to print all results.")
    for i in len(matches) - 1:
        print(
            f"Car {i + 1} is a {matches[i][1]} {matches[i][6]} {matches[i][7]}, with {matches[i][2]} miles.")
# If the user want's an invalid case, tell them that it's invalid, and exit.
elif user_wants_times_printed <= 0:
    print("You cannot print zero or less than zero matches.")
    sys.exit()
# Else, print to the user's request the make, model, year, and milage.
else:
    for i in range(user_wants_times_printed):
        print(
            f"Car {i + 1} is a {matches[i][1]} {matches[i][6]} {matches[i][7]}, with {matches[i][2]} miles.")
# endregion
