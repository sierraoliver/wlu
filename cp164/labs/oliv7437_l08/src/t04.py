"""
-------------------------------------------------------
Assignment 8, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-03-08"
-------------------------------------------------------
"""
# Imports
from morse import fill_code_bst
from BST_linked import BST
from functions import node

s = BST()

values = (('A', '.-'), ('T', "-"))
print(f"Values: {values}")

print(f"fill_code_bst with values")
fill_code_bst(s, values)

print(s._root._value)
node(s._root)
