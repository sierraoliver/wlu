"""
-------------------------------------------------------
Assignment 8, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports
from functions import valid_isbn

isbn = input("ISBN: ")

is_valid = valid_isbn(isbn)

print(f"{is_valid}")
