"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_combine
from utilities import array_to_stack
from Stack_array import Stack

s = Stack()
s2 = Stack()

source1 = [1, 2, 3]
source2 = [6, 70]

print(f"""Source 1: {source1}
Source 2: {source2}""")

array_to_stack(s, source1)
array_to_stack(s2, source2)

target = stack_combine(s, s2)

while not target.is_empty():
    value = target.pop()
    print(value)
