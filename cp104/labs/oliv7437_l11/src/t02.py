"""
-------------------------------------------------------
Lab 11, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import generate_matrix_char

rows = int(input("Rows: "))
cols = int(input("Columns: "))

matrix = generate_matrix_char(rows, cols)

print(f"{matrix}")
