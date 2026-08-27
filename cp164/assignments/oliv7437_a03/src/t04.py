"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_stack
from Stack_array import Stack

numbers = [10, 2]

s = Stack()

array_to_stack(s, numbers)

print("Original Stack")
length = len(s._values)
for x in range(length):
    data = s._values[x]
    print(data)

s.reverse()

print("Reversed Stack")
for y in range(length):
    data = s._values[y]
    print(data)
