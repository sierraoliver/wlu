"""
-------------------------------------------------------
Lab 5, Task 13
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports
from functions import loan

qualified = loan()

if qualified:
    print(f"This employee is qualified for a loan")

else:
    print(f"This employee is not qualified for a loan")
