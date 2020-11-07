"""
Car Loan Program
Randy Zhu
"""
from decimal import Decimal
import sys
# Define a tax constant. 12% here in BC.
# Subject to change due to democracy.
TAX = Decimal(1.12)
# Get user input on their payments, APR, and loan duration.
LOAN_INIT = Decimal(input("How much is your vehicle?: "))
# If the initial amount of the loan is lesser than zero, tell the user
# of the error in their ways, and exit the program to chastise them
if LOAN_INIT < 0:
    print("Your initial loan amount cannot be zero.")
    sys.exit()
Y_PAYMENT_PERIOD = int(input("How many years is your payment period?: "))
# If the payment amount is longer then 10 years,
# tell them that it's too long, and then exit.
if Y_PAYMENT_PERIOD > 10:
    print("Your payment period cannot be more than 10 years.")
    sys.exit()
# Ask the user for the apr of their loan.
APR = Decimal(
    input("What is the annual percentage rate of your loan?: ").strip("% ")) * (10**-2)

# The loan amount is equal to the initial user provided value
# of their car, multiplied by the tax amount.
LOAN_AMT = LOAN_INIT * TAX
# The monthly interest is the annual interest rate divided by 12.
MPR = APR / 12
# The payment interest is the yearly loan amount times the apr.
M_PAYMENT_INTEREST = (LOAN_AMT / Y_PAYMENT_PERIOD) * APR
# The months of payment is the yearly payment period times 12.
PAYMENT_MONTHS = Y_PAYMENT_PERIOD * 12
# The monthly payment amount defined here is the loan amount divided by the months of payments
M_PAYMENT_AMT = LOAN_AMT / PAYMENT_MONTHS
# And the initial principle is the monthly payment amount minus the interest of the payment.
principle = M_PAYMENT_AMT - M_PAYMENT_INTEREST

loan_balance = LOAN_AMT
while loan_balance > 0:
    pass
