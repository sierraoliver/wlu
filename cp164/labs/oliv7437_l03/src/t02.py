"""
-------------------------------------------------------
Lab 3, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from utilities import array_to_queue

q = Queue()

values = [50, 4]
print(values)

array_to_queue(q, values)

while not q.is_empty():

    peek = q.peek()
    print(f"Peek: {peek}")

    remove = q.remove()
    print(f"Removed: {remove}")
