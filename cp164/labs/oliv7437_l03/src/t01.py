"""
-------------------------------------------------------
Lab 3, Task 1
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

q = Queue()

value = int(input("Number: "))

q.insert(value)

peek = q.peek()

print(f"Peek: {peek}")
