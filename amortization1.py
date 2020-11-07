# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:01:13 2020
Produce an amortization chart for a mortage.
@author: Randy Zhu
"""

# Import higher precision math library to prevent weird rounding errors with floating points
from decimal import Decimal

# Ask the user for inputs on purchase price of the home, the payment period, interest rate as a percent,
# down payment, and payment amount per period.
purchase_price = Decimal(input("What is the purchase price of the home?: "))
payment_type = input(
    "What is the payment type of the mortgage?: ").lower().strip("!?. ")
interest_rate = Decimal(
    input("What is the interest rate of the mortgage as a percent?: ").strip("%")) * Decimal(10**-2)
down_payment = (Decimal(
    input("What is the down payment of the mortgage expressed as a percent?: ").strip("%")) * Decimal(10**-2)) * purchase_price
payment_amount = Decimal(
    input("What is the payment amount of the mortgage?: "))

# Define a payment_weekly variable, and set it to zero.
payment_weeks = 0
# Define another payment name variable, which we will set later.
payment_name = ""
# Set payment data accordingly with user input.
if payment_type == "monthly":
    payment_weeks = 12
    payment_name = "Month: "
elif payment_type == "semi-monthly":
    payment_weeks = 24
    payment_name = "Half month: "
elif payment_type == "bi-weekly":
    payment_weeks = 26
    payment_name = "Bi - week: "
elif payment_type == "weekly":
    payment_weeks = 52
    payment_name = "Week: "

# Set the intital loan amaount.
loan_amount = purchase_price - down_payment
# Set the initial interest rate.
interest_rate_for_payment = interest_rate / payment_weeks
# Set the initital price of interest on a payment
interest_rate_per_payment = loan_amount * interest_rate_for_payment

# Print first column on table.
print(
    """
        | Period | Starting Balance | Payment | Interest | Principle | Ending Balance |
    """, end=""
)

# First set the balance to be the loan amount.
balance = loan_amount
# We need a counter for the loop to indicate which month.
months = 0
# The principle is the subtractive result of the payment and the interest rate for each payment
principle = 0
# The annual interest and principle.
pperannum = 0
iperannum = 0
# The totals of the payment.
pcum = 0
icum = 0
# While the balance is not paid:
while balance - principle > 0:
    # Subtract the balance per principle as payment,
    balance -= principle
    # Set the interest rate as the remaining balance, which was previously subtracted multiplied by th  t
    # e
    # interest rate for the payment overall.
    interest_rate_per_payment = balance * interest_rate_for_payment
    # Alas, set the principle to the payment amount minus the interest rate per payment.
    principle = payment_amount - interest_rate_per_payment
    # If the balance without the principle is lesser than 0, declare that it is paid.
    if balance - principle < 0:
        print(
            # Print the month, and the cumulative principle and interest.
            f"| Month {months + 1} | Paid! | Final interest paid ${round(icum,2)} | Final principle paid ${round(pcum, 2)}")
        # Stop looping.
        # break
    # Print the stats
    print(
        f"""
        | {payment_name + str(months + 1)} | {"$" + str(round(balance, 2))} | {"$" + str(payment_amount)} | {"$" + str(round(interest_rate_per_payment, 2))} | {"$" + str(round(principle, 2))} | {"$" + str(round(balance - principle, 2))} |
        """, end=""
    )
    # After displaying the payment, and performing the calculations,
    # add the principle to the cumulative payments.
    pcum += principle
    icum += interest_rate_per_payment
    # Add the same thing to the payment per annum.
    # Why do we do this? Because this is the per annum
    # payment for the program, and below, we clear the value
    # if a month has passed.
    pperannum += principle
    iperannum += interest_rate_per_payment

    # Check whether a month has passed per payment type, and report accordingly.
    if payment_type == "monthly":
        if (months + 1) % 12 == 0:
            print(f"iperannum: {round(iperannum, 2)}")
            print(f"pperannum: {round(pperannum, 2)}")
            iperannum = 0
            pperannum = 0
    if payment_type == "semi-monthly":
        if (months + 1) % 24 == 0:
            print(f"iperannum: {round(iperannum, 2)}")
            print(f"pperannum: {round(pperannum, 2)}")
            iperannum = 0
            pperannum = 0
    if payment_type == "bi-weekly":
        if (months + 1) % 26 == 0:
            print(f"iperannum: {round(iperannum, 2)}")
            print(f"pperannum: {round(pperannum, 2)}")
            iperannum = 0
            pperannum = 0
    if payment_type == "weekly":
        if (months + 1) % 52 == 0:
            print(f"iperannum: {round(iperannum, 2)}")
            print(f"pperannum: {round(pperannum, 2)}")
            iperannum = 0
            pperannum = 0
    # Add one to the months.
    months += 1
