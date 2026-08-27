"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-24"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

s = BST()

values = [1, 2, 3]

for x in range(len(values)):
    s.insert(values[x])

print(f"Source: {s.levelorder()}")

zero, one, two = s.node_counts()
print(f"""Node Counts:
Zero: {zero}
One: {one}
Two: {two}""")

parent_value = 3
value = s.parent(parent_value)
print(f"Parent of {parent_value}: {value}")

value = s.parent_r(parent_value)
print(f"Parent of {parent_value}: {value}")
