"""
-------------------------------------------------------
Lab 3, Task 4
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

number = int(input(f"Number: "))

pq.insert(number)

peek = pq.peek()

print(f"""Inserted: {number}
Peek: {peek}""")
