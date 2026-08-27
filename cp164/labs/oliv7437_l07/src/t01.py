"""
-------------------------------------------------------
Lab 7, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List

s = List()

numbers = [1, 2, 3, 4]
print(f"Source: {numbers}")

for x in range(len(numbers)):
    s.append(numbers[x])

value = 1
result = s._linear_search_r(value)
index = result[2]
print(f"Index of {value}: {index}")
