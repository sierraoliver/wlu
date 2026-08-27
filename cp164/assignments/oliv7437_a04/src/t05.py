"""
-------------------------------------------------------
Assignment 4, Task 5
-------------------------------------------------------
Author:  Sierra Oliver
ID:      169067437
Email:   oliv7437@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq
from functions import pq_split_key

source = Priority_Queue()

values = [30, 76, 12, 6000, -4, 45]
key = -2

print(f"Source: {values}")
print(f"Key: {key}")

array_to_pq(source, values)

target1, target2 = pq_split_key(source, key)

print(f"Target 1")
for x in range(len(target1._values)):
    print(target1._values[x])

print(f"Target 2")
for y in range(len(target2._values)):
    print(target2._values[y])
