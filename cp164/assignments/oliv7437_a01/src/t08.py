"""
-------------------------------------------------------
Assignment 1, Task 8
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats

values = [[1.9, -98.2], [43.0, 4.1], [32.6, -1.8]]
print(f"List: {values}")

small, large, total, average = matrix_stats(values)

print(f"""Small: {small}
Large: {large}
Total: {total}
Average: {average}
""")
