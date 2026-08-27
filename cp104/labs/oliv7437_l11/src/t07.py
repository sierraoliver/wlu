"""
-------------------------------------------------------
Lab 11, Task 7
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import find_position

matrix = [[-6, 5, 7], [3, -6, -2], [9, -8, -7], [0, -7, -6]]

s_loc, l_loc = find_position(matrix)

print(f"{s_loc},{l_loc}")
