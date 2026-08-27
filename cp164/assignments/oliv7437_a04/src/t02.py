"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from utilities import array_to_queue

source = Queue()
target = Queue()

source_list = []
target_list = []

numbers = [2, 3]
values = []

print(f"Source: {numbers}")
print(f"Target: {values}")

array_to_queue(source, numbers)
array_to_queue(target, values)

equals = source == target
print(f"Equals: {equals}")
