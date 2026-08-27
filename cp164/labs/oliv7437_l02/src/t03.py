"""
-------------------------------------------------------
Lab 2, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-16"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array

numbers = [1, 2, 3]
s = Stack()

array_to_stack(s, numbers)

length = len(s._values)
stack_num = []

for x in range(length):
    value = s._values[x]
    stack_num.append(value)

print(f"Stack:{stack_num}")

target = []
stack_to_array(s, target)

print(f"Array: {target}")
