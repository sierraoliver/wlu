"""
-------------------------------------------------------
Lab 6, Task 5
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

values = [1, 2, 3, 4]

for x in range(len(values)):
    s.prepend(values[x])

peek = s.peek()
print(f"Peek: {peek}")

remove = s.remove(peek)
print(f"Remove:{remove}")
print(f"Peek: {s.peek()}")
