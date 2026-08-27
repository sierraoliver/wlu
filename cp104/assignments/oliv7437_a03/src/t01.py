"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports
from functions import footage_to_acres

square_feet = float(input("Enter the square footage: "))

acres = footage_to_acres(square_feet)

print(f"The square footage in acres is {acres}")
