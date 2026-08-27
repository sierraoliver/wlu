"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_reverse
from utilities import array_to_stack
from Stack_array import Stack

numbers = [3, 4]

s = Stack()

array_to_stack(s, numbers)

print("Original Stack")
length = len(s._values)
for x in range(length):
    data = s._values[x]
    print(data)

stack_reverse(s)

print("Reversed Stack")
for y in range(length):
    data = s._values[y]
    print(data)
