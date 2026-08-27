"""
-------------------------------------------------------
Lab 10, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-20"
-------------------------------------------------------
"""
# Imports
from test_Sorts_List_linked import test_sort
from Sorts_List_linked import Sorts

print(f"n:    100      |      Comparisons       | |         Swaps          |")
print(f"Algorithm      In Order Reversed   Random In Order Reversed   Random")
print(f"-------------- -------- -------- -------- -------- -------- --------")

test_sort('Bubble Sort', Sorts.bubble_sort)
