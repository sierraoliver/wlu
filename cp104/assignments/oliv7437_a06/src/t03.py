"""
-------------------------------------------------------
Assignment 6, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-10"
-------------------------------------------------------
"""
# Imports
from functions import interest_table

principal_amount = float(input("Enter principal amount: "))
interest_rate = float(input("Enter interest rate (%): "))
payment = float(input("Enter monthly payment: "))

interest_table(principal_amount, interest_rate, payment)
