"""
-------------------------------------------------------
Lab 9, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""
# Imports
from functions import validate_code

product_code = input("Enter code: ")

category, digits, qualifiers = validate_code(product_code)

print(f"{category}, {digits}, {qualifiers}")
