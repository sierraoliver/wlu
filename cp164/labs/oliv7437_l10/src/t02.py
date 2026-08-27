"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-22"
-------------------------------------------------------
"""
# Imports
from Sorts_array import Sorts

values = [33, 55, 4, 1, 3, -10]
sort = ('Bubble Sort', Sorts.bubble_sort)

description = sort[0]
func = sort[1]
print(f"Sort with {description}")
print(f"Before: {values}")
func(values)
print(f"After: {values}")
