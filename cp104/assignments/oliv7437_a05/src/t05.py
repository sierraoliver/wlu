"""
-------------------------------------------------------
Assignment 5, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
from functions import range_addition

start = int(input("Enter starting number: "))
increment = int(input("Enter increment number: "))
count = int(input("Enter number of values: "))

total = range_addition(start, increment, count)

print(f"""
Total: {total}
""")
