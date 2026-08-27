"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_stack
from Stack_array import Stack

s = Stack()
s2 = Stack()
target = Stack()

source1 = [33, 11]
source2 = [44, 22]

print(f"""Source 1: {source1}
Source 2: {source2}""")

array_to_stack(s, source1)
array_to_stack(s2, source2)

target.combine(s, s2)

while not target.is_empty():
    value = target.pop()
    print(value)
