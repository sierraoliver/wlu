"""
-------------------------------------------------------
Assignment 7, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""
# Imports
from functions import verify_sorted

numbers = [1, 2, 3, 4, -20]

in_order, index = verify_sorted(numbers)

print(f"""List: {numbers}
{in_order}, {index}""")
