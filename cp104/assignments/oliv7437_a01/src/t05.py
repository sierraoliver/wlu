"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""
# Constants
PERCENT = 100

principal = float(input("Principal: $ "))

interest = float(input("Interest (%): "))
interest_percent = interest/PERCENT

years = int(input("Number of years: "))

compounded_per_year = int(
    input("Number of times interest compounded per year: "))

# calculation
total = (1 + (interest_percent/compounded_per_year))
total = total**(years*compounded_per_year)
total *= principal

print("Balance: $", total)
