"""
Car Loan Program
Randy Zhu
"""
from decimal import Decimal
import sys

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
    print("Your initial loan amount cannot be zero or less than.".strip(
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
"""
Calculate the monthly payment amount by the formula
loan amount * (monthly interest * (1 + monthly interest)^months of loan duration)
---------------------------------------------------------------------------------
                (1 + monthly interest)^months of loan duration - 1
"""
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
