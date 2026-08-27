"""
-------------------------------------------------------
Lab 8, Task 12
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""
# Imports
from functions import list_sums

list1 = [-91, 5, 40, 3, -2, 50, 7]
list2 = [1, 5, 72, 30, 87, 6, 0]
print(f"""List 1: {list1}
List 2: {list2}
""")

target = list_sums(list1, list2)

print(f"{target}")
