"""
-------------------------------------------------------
Lab 6, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-16"
-------------------------------------------------------
"""
# Imports
from List_linked import List

s = List()

values = [11, 22, 33, 44, 11, 22, 11]
print(f"Values: {values}")

for x in range(len(values)):
    s.prepend(values[x])

count = s.count(11)
print(f"Count of 11: {count}")

max_num = s.max()
print(f"Max: {max_num}")

min_num = s.min()
print(f"Min: {min_num}")
