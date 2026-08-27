"""
-------------------------------------------------------
Lab 6, Task 6
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

values = [1, 2, 3, 4, 5]

for x in range(len(values)):
    s.prepend(values[x])

data = s[3]
print(f"Value: {data}")

s[3] = 10
item = s[3]
print(f"Item: {item}")
