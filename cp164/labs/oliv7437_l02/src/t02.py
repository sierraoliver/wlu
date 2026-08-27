"""
-------------------------------------------------------
Lab 2, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-16"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack

s = Stack()
values = [99]
print(f"List: {values}")

array_to_stack(s, values)

print(f"From Stack:")
for value in s:
    print(value)
