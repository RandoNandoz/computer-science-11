"""
Car Loan Program
Randy Zhu
"""

# region Calculate summary for loan
# Define a tax constant. 12% here in BC.
# Subject to change due to democracy.
TAX = float(1.12)
# Get user input on their payments, APR, and loan duration.
loan_initial = float(
    input("How much is your vehicle?: ").strip("$ ").replace(",", ""))
# If the initial amount of the loan is lesser than zero, tell the user
# of the error in their ways, and exit the program to chastise them
if loan_initial <= 0:
    print("Your initial loan amount cannot be zero or less than zero.".strip(
        "$ ").replace(",", ""))
    exit()
# Ask the user for the apr of their loan.
apr = float(input(
    "What is the annual percentage rate of your loan?: ").strip("% ")) * float(10**-2)
yearly_payment_period = int(input("How many years is your payment period?: "))
# If the payment amount is longer then 10 years,
# tell them that it's too long, and then exit.
if yearly_payment_period > 10:
    print("Your payment period cannot be more than 10 years.")
    exit()

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
principles_annually: "list[float]" = []
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
print(f"Total payments: ${round(cum_interest + loan_amount, 2)}")
print(f"Total interest paid: ${round(cum_interest, 2)}")
# endregion

# region recommend a car

# # Open the car listing file, r mode because we don't need it read - write.
# car_list_file = open("car_listings.csv", "r")
# # Get rid of the first useless line.
# car_list_file.readline()

# # Create a raw list of car data.
# raw_car_strings = []
# # Create an empty list of soon to be processed car data.
# car_dataset = []

# # For each line in the file, add the line of the car data.
# print("Adding data to memory.")
# for line in car_list_file:
#     raw_car_strings.append(
#         line.strip("\n ").replace(" ", "").split(",")
#     )

# # Close the file cuz we're done.
# car_list_file.close()
# # We want to cast the first index of the list to an int, so we can
# # sort the data to execute a binary search to find a price.
# print("Processing data (part 1/2)")
# for car in raw_car_strings:
#     for _ in car:
#         car[0] = int(car[0])
#         car_dataset.append(car)

# # With sorted(), it takes in a list, and has a key value
# # the key is the return value of the function that is called with the key.
# # by using lambda, we can create a temporary function which just returns the
# # first indice as the key. I tried writing my own sorting thing, it was
# # too hard to be honest.
# print("Sorting data (part 2/2)")
# # Resources:
# # https://docs.python.org/3/howto/sorting.html
# car_dataset = sorted(
#     car_dataset, key=lambda v: v[0])

# # Ask the user about their desired car price.
# user_desired_car_price = int(
#     input(f"What is your desired car price? The lowest price in the list is ${car_dataset[0][0]}, and the highest is ${car_dataset[-1][0]}: ").strip("$"))
# # If the user's desired car price is less than the lowest number on the dataset, tell them that it's invalid.
# if user_desired_car_price < car_dataset[0][0]:
#     print("Your price is too low.")
#     exit()
# # If the user's desired car price is higher than the highest number on the dataset, tell them that it's invalid.
# elif user_desired_car_price > car_dataset[-1][0]:
#     print("Your price is too high.")
#     exit()
# # Set a search limit, as this file is around 800K lines long, which means without a limit, it will take a long
# # time to give the user an appropriate response.
# search_limit = int(environ.get("SEARCH_LIMIT", 20))
# # Alert the user that the default search limit is set, and tell them how to set it.
# if search_limit == 20:
#     print("Going with default for search limit - 20. You can set a custom search limit with the environment variable SEARCH_LIMIT.")
# # If the limit is invalid, tell them so, and quit.
# elif search_limit <= 0:
#     print("The search limit is lesser than or equal to zero. Invalid limit.")
#     exit()
# # Tell them about the custom search limit.
# else:
#     print("SEARCH_LIMIT set to: " + str(search_limit) + ".")
# # Execute binary search for right price.
# # Create a new list of matches to the price.
# # Resources:
# # https://en.wikipedia.org/wiki/Binary_search_algorithm
# # https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search
# # https://www.youtube.com/watch?v=P3YID7liBug
# matches = []
# # Create the leftmost column of the search.
# search_left = 0
# # Create the rightmost column of the search, which is for now the the last index of the list.
# search_right = len(car_dataset) - 1
# # While the leftmost search position is lesser than or equal to
# # the rightmost search point, calculate the middle of the search
# # by averaging the left and the right.
# while search_left <= search_right:
#     print("Searching for cars...")
#     search_middle = floor((search_left + search_right)/2)
#     # For every item in the dataset.
#     if len(matches) >= search_limit:
#         break
#     for item in car_dataset:
#         # Alas, if the search limit is reached, stop looping.
#         if len(matches) >= search_limit:
#             break
#         # if the item's price is
#         # lesser than the user's desired car price, make the leftmost
#         # search column the middle plus one.
#         if item[0] < user_desired_car_price:
#             search_left = search_middle + 1
#         # If the price is more than the desired car price, move the
#         # right column to the middle search point plus one.
#         elif item[0] > user_desired_car_price:
#             search_right = search_middle + 1
#         # Else a match is found, because the price is equal to the user's desired car price,
#         # add the item to the list of matches.
#         else:
#             matches.append(item)
#     # If the entire dataset is looped through, the search fails. Return the set of matches, but not to limit.
#     print(
#         f"Search to {search_limit} results failed due to it being bigger than the cars in the dataset.")
#     break

# # Ask the user how many matches they want displayed.
# user_wants_times_printed = int(input(
#     f"There are {len(matches)} matches. How many matches would you like to see?: "))
# # If the user's times printed request is greater than the number of matches, just print all the results.
# if user_wants_times_printed > len(matches):
#     print("You have selected to print more than there are cars available. Going to print all results.")
#     for i in range(len(matches) - 1):
#         print(
#             f"Car {i + 1} is a {matches[i][1]} {matches[i][6]} {matches[i][7]}, with {matches[i][2]} miles.")
# # If the user want's an invalid case, tell them that it's invalid, and exit.
# elif user_wants_times_printed <= 0:
#     print("You cannot print zero or less than zero matches.")
#     exit()
# # Else, print to the user's request the make, model, year, and milage.
# else:
#     for i in range(user_wants_times_printed):
#         print(
#             f"Car {i + 1} is a {matches[i][1]} {matches[i][6]} {matches[i][7]}, with {matches[i][2]} miles.")
# endregion
