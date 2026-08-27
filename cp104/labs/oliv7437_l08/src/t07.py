"""
-------------------------------------------------------
Lab 8, Task 7
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""
# Imports
from functions import list_categorize

list = [1, 2, 3, 4, 5, 6, 7, 0, 0, -12, -90, 90, 31]
print(f"List: {list}")

positives, negatives, zeroes, evens, odds = list_categorize(list)

print(f"{positives},{negatives},{zeroes},{evens},{odds}")
