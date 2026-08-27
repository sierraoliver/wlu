"""
-------------------------------------------------------
Lab 2, Task 6
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-09-10"
-------------------------------------------------------
"""
# Imports

# Constants
MONTHS = 12

# getting input from user
mortgage_principal = float(input("Mortgage principal ($): "))

years = int(input("Number of years: "))

interest_rate = int(input("Yearly interest rate (%): "))

# getting monthly
years *= MONTHS

interest_rate /= 100

interest_rate /= MONTHS


# calculating monthly payments
numerator = ((1 + interest_rate)**years) * interest_rate

denominator = ((1+interest_rate)**years)-1

monthly_payment = mortgage_principal * (numerator/denominator)

print("The monthly payments are: $ ", monthly_payment)
