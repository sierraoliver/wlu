"""
-------------------------------------------------------
Lab 11, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import generate_matrix_num

rows = int(input("Rows: "))
cols = int(input("Columns: "))
low = float(input("Low: "))
high = float(input("High: "))
value_type = input("Value Type: ")

matrix = generate_matrix_num(rows, cols, low, high, value_type)

print(f"{matrix}")
