"""
-------------------------------------------------------
Assignment 1, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from functions import list_subtraction

minuend = [1, 2, 65, 90, 10, 1, 2, 4, 5, 6]
subtrahend = [1]

print(f"""Original: {minuend}
Subtract: {subtrahend}""")

list_subtraction(minuend, subtrahend)

print(f"Updated: {minuend}")
