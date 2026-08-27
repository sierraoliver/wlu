"""
-------------------------------------------------------
Assignment 7, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""
# Imports
from functions import get_indexes

numbers = [-90, 2, 1, -90, -90, 2, 1]
target_number = -90

index_list = get_indexes(numbers, target_number)

print(f"""List: {numbers}, Target Number: {target_number}
{index_list}
""")
