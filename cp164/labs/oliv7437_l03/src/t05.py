"""
-------------------------------------------------------
Lab 3, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

number = int(input(f"Number: "))
while number != -1:
    pq.insert(number)
    print(f"""Inserted: {number}""")

    number = int(input(f"Number: "))

while not pq.is_empty():
    remove = pq.remove()
    print(f"Removed: {remove}")
