"""
-------------------------------------------------------
Lab 8, Task 9
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""
# Imports
from functions import many_search
values = [4, 80, 6, 43, 31, 9, 0, -1]
value = 75
print(f"""Values: {values}
Value: {value}
""")

indexes = many_search(values, value)

print(f"{indexes}")
