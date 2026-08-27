"""
-------------------------------------------------------
Lab 11, Task 6
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats

smallest, largest, total, average = matrix_stats(
    [[2, 0, -1, 1], [10, 4, -5, 9], [-6, 3, 6, 0]])

print(f"{smallest}, {largest}, {total}, {average}")
