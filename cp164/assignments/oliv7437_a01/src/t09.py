"""
-------------------------------------------------------
Assignment 1, Task 9
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from functions import matrixes_add

a = [[1, 2, 3], [5, 5, 5], [10, 15, 20]]
b = [[4, 5, 6], [7, 6, 7], [-3, 6, 7]]

print(f"""a: {a}
b: {b}""")

c = matrixes_add(a, b)

print(f"c: {c}")
