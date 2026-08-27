"""
-------------------------------------------------------
Lab 6, Task 4
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

values = [11, 22, 33, 44]

for x in range(len(values)):
    s.prepend(values[x])

value = s.find(11)
print(f"Find: {value}")

index = s.index(44)
print(f"Index: {index}")

contain = 33 in s
print(f"Contains: {contain}")
