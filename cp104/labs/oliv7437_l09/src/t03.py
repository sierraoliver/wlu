"""
-------------------------------------------------------
Lab 9, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""
# Imports
from functions import parse_code

product_code = input("Enter code: ")

pc, pi, pq = parse_code(product_code)

print(f"{pc} {pi} {pq}")
