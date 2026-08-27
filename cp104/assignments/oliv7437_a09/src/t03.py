"""
-------------------------------------------------------
Assignment 8, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import file_statistics

file_handle = open("addresses.txt", "r", encoding="utf-8")

upper, lower, digits, space, remaining = file_statistics(file_handle)

print(f"{upper}, {lower}, {digits}, {space}, {remaining}")

file_handle.close()
