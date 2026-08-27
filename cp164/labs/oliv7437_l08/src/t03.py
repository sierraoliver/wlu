"""
-------------------------------------------------------
Lab 8, Task 3
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-08"
-------------------------------------------------------
"""
# Imports
from morse import fill_letter_bst
from BST_linked import BST
from functions import node

s = BST()

values = (('M', '--'),)
print(f"Values: {values}")

print(f"fill_letter_bst with values")
fill_letter_bst(s, values)

print(s._root._value)
node(s._root)
