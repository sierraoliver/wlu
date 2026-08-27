"""
-------------------------------------------------------
Assignment 10, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-29"
-------------------------------------------------------
"""
# Imports
from Sorts_array import Sorts

values = [15, 23, 45, 12, 78, 61, 7, 180, 123, 10092]
print(f"Values: {values}")

Sorts.radix_sort(values)

print(f"Radix Sort: {values}")
